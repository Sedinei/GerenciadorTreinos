from typing import Tuple, List
from dataclasses import dataclass, field
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
    
    def check_unique_name_user(self, name_user: str) -> bool:
        sql = '''SELECT count(*)
                 FROM usuarios
                 WHERE nome_usuario=?'''
        t = (name_user, )
        with self.con as c:
            c.execute(sql, t)
            num_names = c.fetchone()[0]
        return num_names==0         
    
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
                raise DAOError(e.args[0])
            
    def save_password_user(self, id_user: int, password: str) -> None:
        hassed_pass = self._get_crypto_password(password)
        sql = 'UPDATE usuarios SET senha_usuario=? WHERE id_usuario=?'
        t = (hassed_pass, id_user)
        with self.con as c:
            try:
                c.execute(sql, t)
            except DBError as e:
                raise DAOError(e.args[0])
    
    def check_password(self, user: str, password: str) -> Tuple[int, bool]:
        with self.con as c:
            t = (user,)
            c.execute('''SELECT id_usuario, senha_usuario FROM usuarios
                         WHERE nome_usuario=?''', t)
            id, hash_stored = c.fetchone()
        return id, self._check_password(password, hash_stored)
    
    def remove_user(self, id_user: int) -> None:
        sql = '''DELETE FROM usuarios WHERE id_usuario=?'''
        t = (id_user,)
        with self.con as c:
            try:
                c.execute(sql, t)
            except DBError as e:
                raise DAOError(e.args[0])
    
    def save_user(self, user: str, email: str, type_user: str, password: str) -> None:
        id_tp_user = self._get_id_type_user(type_user)
        hash_pwd = self._get_crypto_password(password)
        t = (user, email, id_tp_user, hash_pwd)
        sql = 'INSERT INTO usuarios VALUES (NULL, ?, ?, ?, ?)'
        with self.con as c:
            try:
                c.execute(sql, t)
            except DBError as e:
                raise DAOError(e.args[0])
        
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
                    REFERENCES tiposUsuario(id_tp_usuario))''',
                '''INSERT INTO tipos_usuario VALUES
                   (1, "Gerenciador"),
                   (2, "Registrador"),
                   (3, "Leitor")''',
                f'''INSERT INTO usuarios VALUES(
                    NULL,
                    "{user_adm_default}",
                    "sem_email",
                    1,
                    "{pwd_adm_default}")''']
        with self.con as c:
            for sql in sqls:
                c.execute(sql)
                
    def _get_crypto_password(self, pwd: str) -> str:
        byte = pwd.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(byte, salt)
        return hashed.decode('utf-8')
    
    def _check_password(self, pwd_inputed: str, hash_stored: str) -> bool:
        byte_inputed = pwd_inputed.encode('utf-8')
        byte_stored = hash_stored.encode('utf-8')
        return bcrypt.checkpw(byte_inputed, byte_stored)
    
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
            raise DAOError(msg)
        return id_type_user[0]
    
@dataclass
class DAODados:
    file: str
    con: ConnetionDB = field(init=False)
    
    def __post_init__(self) -> None:
        self.con = ConnetionDB(self.file)
        
    def start_db(self) -> None:
        sqls = ['''CREATE TABLE tipo_treino (
                    id_tp_treino INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome_tp_treino TEXT UNIQUE NOT NULL,
                    arquivado_tp_treino BOOLEAN)''',
                '''CREATE TABLE treinador (
                    id_treinador INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome_treinador TEXT UNIQUE NOT NULL,
                    arquivado_treindor BOOLEAN)''',
                '''CREATE TABLE grupo_atleta (
                    id_gp_atleta INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome_gp_atleta TEXT UNIQUE NOT NULL,
                    arquivado_gp_atleta BOOLEAN)''',
                '''CREATE TABLE tipo_dispensa (
                    id_tp_dispensa INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome_tp_dispensa TEXT UNIQUE NOT NULL,
                    arquivado_tp_dispensa BOOLEAN)''',
                '''CREATE TABLE atleta (
                    id_atleta INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome_atleta TEXT UNIQUE NOT NULL,
                    dt_nasc_atleta DATE NOT NULL,
                    id_gp_atleta INTEGER NOT NULL,
                    FOREING KEY(id_gp_atleta)
                    REFERENCES grupo_atleta(id_gp_atleta))''',
                '''CREATE TABLE dispensa (
                    id_tp_dispensa INTEGER NOT NULL,
                    id_atleta INTEGER NOT NULL,
                    dt_dispensa DATE NOT NULL,
                    tempo FLOAT NOT NULL,
                    PRIMARY KEY (id_tp_dispensa,
                                 id_atleta,
                                 dt_dispensa),
                    FOREING KEY(id_tp_dispensa)
                    REFERENCES tipo_dispensa(id_tp_dispensa),
                    FOREING KEY(id_atleta)
                    REFERENCES atleta(id_atleta))''',
                '''CREATE TABLE treino (
                    id_treino INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    id_treinador INTEGER NOT NULL,
                    id_tp_treino INTEGER NOT NULL,
                    tempo FLOAT NOT NULL,
                    FOREING KEY(id_treinador)
                    REFERENCES treinador(id_treinador),
                    FOREING KEY(id_tp_treino)
                    REFERENCES tipo_treino(id_tp_treino))''',
                '''CREATE TABLE treino_atleta (
                    id_treino INTEGER NOT NULL,
                    id_atleta INTEGER NOT NULL,
                    tempo FLOAT NOT NULL,
                    PRIMARY KEY (id_treino,
                                 id_atleta),
                    FOREING KEY(id_treino)
                    REFERENCES treino(id_treino),
                    FOREING KEY(id_atleta)
                    REFERENCES atleta(id_atleta))''']
        with self.con as c:
            for sql in sqls:
                c.execute(sql)