from typing import Tuple, List
import logging
from dataclasses import dataclass, field
from .utils import singleton, raise_log
import os
import bcrypt
import sqlite3
from sqlite3 import Error as DBError

class DAOError(Exception): pass

@dataclass
class ConnetionDB:
    arq_db: str
    conn: sqlite3.Connection = field(init=False)

    def __enter__(self):
        self.conn = sqlite3.connect(self.arq_db)
        return self.conn.cursor()

    def __exit__(self, tipo_excecao, valor_excecao, traceback):
        self.conn.commit()
        self.conn.close()

    def exist(self) -> bool:
        return os.path.isfile(self.arq_db)

@dataclass
class DAOControls:
    path: str
    types_user: List[str]
    con: ConnetionDB = field(init=False)
    file: str = field(init=False)
    
    def __post_init__(self) -> None:
        ok = True
        if not os.path.isdir(self.path):
            os.mkdir(self.path)
            ok = False
        self.file = os.path.join(self.path, 'control')
        if not os.path.isfile(self.file): ok = False
        self.con = ConnetionDB(self.file)
        if not ok: self._create_tables()
    
    def change_user(self, id_user: int, name_user: str, email_user: str, type_user: str) -> None:
        id_tp_user = self._get_id_type_user(type_user) if type_user else None
        fields = []
        t = []
        if name_user:
            fields.append('nome_usuario=?')
            t.append(name_user)
        if email_user:
            fields.append('email_usuario=?')
            t.append(email_user)
        if type_user:
            fields.append('id_tp_usuario=?')
            t.append(id_tp_user)
        sql = f'UPDATE usuarios SET {",".join(fields)} WHERE id_usuario=?;'
        t.append(id_user)
        with self.con as c:
            try:
                c.execute(sql, t)
            except DBError as e:
                raise_log(DAOError, e.args[0])
     
    def check_password(self, user: str, password: str) -> Tuple[int, bool]:
        with self.con as c:
            t = (user,)
            c.execute('''SELECT id_usuario, senha_usuario FROM usuarios
                         WHERE nome_usuario=?''', t)
            id, hash_stored = c.fetchone()
        return id, self._check_password(password, hash_stored)
    
    def check_unique_name_user(self, name_user: str) -> bool:
        sql = '''SELECT count(*)
                 FROM usuarios
                 WHERE nome_usuario=?'''
        t = (name_user, )
        with self.con as c:
            c.execute(sql, t)
            num_names = c.fetchone()[0]
        return num_names==0         
    
    def get_all_users(self) -> List[Tuple[int, str, str, str]]:
        with self.con as c:
            c.execute('''SELECT
                             t1.id_usuario
                            ,t1.nome_usuario
                            ,t2.tp_usuario
                            ,t1.email_usuario
                        FROM usuarios AS t1
                        LEFT JOIN tipos_usuario AS t2
                        ON t1.id_tp_usuario=t2.id_tp_usuario''')
            users = c.fetchall()
        return users
    
    def get_user(self, id_user: int) -> Tuple[int, str, str, str]:
        with self.con as c:
            t = (id_user,)
            c.execute('''SELECT t1.nome_usuario, t1.email_usuario, t2.tp_usuario
                         FROM usuarios as t1
                         LEFT JOIN tipos_usuario as t2
                         ON t1.id_tp_usuario=t2.id_tp_usuario
                         WHERE id_usuario=?''', t)
            name_user, email_user, type_user = c.fetchone()
            return id_user, name_user, email_user, type_user
            
    def remove_user(self, id_user: int) -> None:
        sql = '''DELETE FROM usuarios WHERE id_usuario=?'''
        t = (id_user,)
        with self.con as c:
            try:
                c.execute(sql, t)
            except DBError as e:
                raise_log(DAOError, e.args[0])
    
    def save_password_user(self, id_user: int, password: str) -> None:
        hassed_pass = self._get_crypto_password(password)
        sql = 'UPDATE usuarios SET senha_usuario=? WHERE id_usuario=?'
        t = (hassed_pass, id_user)
        with self.con as c:
            try:
                c.execute(sql, t)
            except DBError as e:
                raise_log(DAOError, e.args[0])
   
    def save_user(self, user: str, email: str, type_user: str, password: str) -> None:
        id_tp_user = self._get_id_type_user(type_user)
        hash_pwd = self._get_crypto_password(password)
        t = (user, email, id_tp_user, hash_pwd)
        sql = 'INSERT INTO usuarios VALUES (NULL, ?, ?, ?, ?)'
        with self.con as c:
            try:
                c.execute(sql, t)
            except DBError as e:
                raise_log(DAOError, e.args[0])
                  
    def _check_password(self, pwd_inputed: str, hash_stored: str) -> bool:
        byte_inputed = pwd_inputed.encode('utf-8')
        byte_stored = hash_stored.encode('utf-8')
        return bcrypt.checkpw(byte_inputed, byte_stored)
    
    def _create_tables(self) -> None:
        user_adm_default = 'admin'
        pwd_adm_default = self._get_crypto_password('admin')
        sqls = ['''CREATE TABLE bds_dados (
                    id_bd_dados INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome_bd_dados TEXT NOT NULL UNIQUE)''',
                '''CREATE TABLE tipos_usuario (
                    id_tp_usuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    tp_usuario TEXT NOT NULL UNIQUE)''',
                '''CREATE TABLE usuarios (
                    id_usuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome_usuario TEXT NOT NULL UNIQUE,
                    email_usuario TEXT NOT NULL UNIQUE,
                    id_tp_usuario INTEGER NOT NULL,
                    senha_usuario TEXT NOT NULL,
                    FOREIGN KEY(id_tp_usuario)
                    REFERENCES tipos_usuario(id_tp_usuario))''']
        with self.con as c:
            for sql in sqls:
                c.execute(sql)
            c.execute(f'''INSERT INTO usuarios VALUES(
                          NULL,
                          "{user_adm_default}",
                          "sem_email",
                          1,
                          "{pwd_adm_default}")''')
            for i, type_user in enumerate(self.types_user):
                c.execute(f'''INSERT INTO tipos_usuario
                              VALUES ({i+1}, "{type_user}")''')
      
    def _get_crypto_password(self, pwd: str) -> str:
        byte = pwd.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(byte, salt)
        return hashed.decode('utf-8')
    
    def _get_id_type_user(self, type_user: str) -> int:
        with self.con as c:
            sql = '''SELECT id_tp_usuario
                     FROM tipos_usuario
                     WHERE tp_usuario=?'''
            t = (type_user,)
            c.execute(sql, t)
            id_type_user = c.fetchone()
        if id_type_user is None:
            msg = f'Não existe tipo de usuário "{type_user}".'
            raise_log(DAOError, msg)
        return id_type_user[0]
    

@singleton
@dataclass
class DAODados:
    path: str
    con: ConnetionDB = field(init=False)
    file: str = field(init=False)
    
    def __post_init__(self) -> None:
        ok = True
        self.file = os.path.join(self.path, 'data')
        if not os.path.isfile(self.file): ok = False
        self.con = ConnetionDB(self.file)
        if not ok: self._create_tables()

    def change_domain(self, table: str, suffix: str, id_domain: int,
                       name_domain: str, description_domain: str) -> None:
        fields = []
        t = []
        if name_domain:
            fields.append(f'nome_{suffix}=?')
            t.append(name_domain)
        if description_domain:
            fields.append(f'descricao_{suffix}=?')
            t.append(description_domain)
        sql = f'UPDATE {table} SET {",".join(fields)} WHERE id_{suffix}=?;'
        t.append(id_domain)
        with self.con as c:
            try:
                c.execute(sql, t)
            except DBError as e:
                raise_log(DAOError, e.args[0])
    
    def get_all_athletes(self) -> List[Tuple[int, str, str, str, str, str]]:
        with self.con as c:
            c.execute('''SELECT
                             t1.id_atleta
                            ,t1.nome_atleta
                            ,t1.dt_nasc_atleta
                            ,t2.nome_gp_atletas
                            ,t1.dt_inicio_atleta
                            ,t1.dt_fim_atleta
                        FROM atleta AS t1
                        LEFT JOIN grupo_atletas AS t2
                        ON t1.id_gp_atletas=t2.id_gp_atletas''')
            athletes = c.fetchall()
            return athletes
    
    def get_all_coaches(self) -> List[Tuple[int, str]]:
        with self.con as c:
            c.execute('''SELECT
                             id_treinador
                            ,nome_treinador
                            ,dt_inicio_treinador
                            ,dt_fim_treinador
                        FROM treinador''')
            return c.fetchall()
                
    def get_all_domain(self, table: str, suffix: str) -> List[Tuple[int, str, str]]:
        with self.con as c:
            c.execute(f'''SELECT
                            id_{suffix},
                            nome_{suffix},
                            descricao_{suffix}
                        FROM {table}
                        WHERE arquivado_{suffix}=FALSE''')
            return c.fetchall()
    
    def get_groups(self) -> List[str]:
        with self.con as c:
            c.execute('''SELECT nome_gp_atletas
                         FROM grupo_atletas
                         WHERE arquivado_gp_atletas=TRUE''')
            groups = c.fetchall()
            return [group[0] for group in groups]
        
    def insert_athlete(self, name: str, dt_born: str, group: str, dt_start: str) -> None:
        with self.con as c:
            t = (group, )
            sql = '''SELECT id_gp_atletas
                     FROM grupo_atletas
                     WHERE nome_gp_atletas=?'''
            c.execute(sql, t)
            id_group = c.fetchone()[0]
            t = (name, dt_born, id_group, dt_start)
            sql = '''INSERT INTO atleta
                     VALUES (NULL, ?, ?, ?, ?, NULL)'''
            c.execute(sql, t)
    
    def is_unique(self, table: str, suffix: str, name_domain: str) -> bool:
        sql = f'SELECT COUNT(*) FROM {table} WHERE nome_{suffix}=?'
        t = (name_domain,)
        with self.con as c:
            c.execute(sql, t)
            return c.fetchone()[0] == 0
    
    def remove_domain(self, table: str, suffix: str, id_domain: int) -> None:
        t = (id_domain,)
        sql = f'DELETE FROM {table} WHERE id_{suffix}=?'
        with self.con as c:
            try:
                c.execute(sql, t)
            except DBError as e:
                raise_log(DAOError, e.args[0])
    
    def save_domain(self, table: str, name: str, description: str) -> None:
        t = (name, description)
        sql = f'INSERT INTO {table} VALUES (NULL, ?, ?, FALSE)'
        with self.con as c:
            try:
                c.execute(sql, t)
            except DBError as e:
                raise_log(DAOError, e.args[0])
     
    def _create_tables(self) -> None:
        sqls = ['''CREATE TABLE tipo_treino (
                    id_tp_treino INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome_tp_treino TEXT UNIQUE NOT NULL,
                    descricao_tp_treino TEXT NOT NULL,
                    arquivado_tp_treino BOOLEAN)''',
                '''CREATE TABLE treinador (
                    id_treinador INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome_treinador TEXT UNIQUE NOT NULL,
                    dt_inicio_treinador TEXT NOT NULL,
                    dt_fim_treinador TEXT,
                    arquivado_treinador BOOLEAN)''',
                '''CREATE TABLE grupo_atletas (
                    id_gp_atletas INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome_gp_atletas TEXT UNIQUE NOT NULL,
                    descricao_gp_atletas TEXT NOT NULL,
                    arquivado_gp_atletas BOOLEAN)''',
                '''CREATE TABLE tipo_dispensa (
                    id_tp_dispensa INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome_tp_dispensa TEXT UNIQUE NOT NULL,
                    descricao_tp_dispensa TEXT NOT NULL,
                    arquivado_tp_dispensa BOOLEAN)''',
                '''CREATE TABLE atleta (
                    id_atleta INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome_atleta TEXT UNIQUE NOT NULL,
                    dt_nasc_atleta TEXT NOT NULL,
                    id_gp_atletas INTEGER NOT NULL,
                    dt_inicio_atleta TEXT NOT NULL,
                    dt_fim_atleta TEXT,
                    FOREIGN KEY(id_gp_atletas)
                    REFERENCES grupo_atletas(id_gp_atletas))''',
                '''CREATE TABLE dispensa (
                    id_tp_dispensa INTEGER NOT NULL,
                    id_atleta INTEGER NOT NULL,
                    dt_dispensa TEXT NOT NULL,
                    minutos INTEGER NOT NULL,
                    PRIMARY KEY (id_tp_dispensa,
                                 id_atleta,
                                 dt_dispensa),
                    FOREIGN KEY(id_tp_dispensa)
                    REFERENCES tipo_dispensa(id_tp_dispensa),
                    FOREIGN KEY(id_atleta)
                    REFERENCES atleta(id_atleta))''',
                '''CREATE TABLE treino (
                    id_treino INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    id_treinador INTEGER NOT NULL,
                    id_tp_treino INTEGER NOT NULL,
                    minutos INTEGER NOT NULL,
                    FOREIGN KEY(id_treinador)
                    REFERENCES treinador(id_treinador),
                    FOREIGN KEY(id_tp_treino)
                    REFERENCES tipo_treino(id_tp_treino))''',
                '''CREATE TABLE treino_atleta (
                    id_treino INTEGER NOT NULL,
                    id_atleta INTEGER NOT NULL,
                    minutos INTEGER NOT NULL,
                    PRIMARY KEY (id_treino,
                                 id_atleta),
                    FOREIGN KEY(id_treino)
                    REFERENCES treino(id_treino),
                    FOREIGN KEY(id_atleta)
                    REFERENCES atleta(id_atleta))''']
        with self.con as c:
            for sql in sqls:
                c.execute(sql)