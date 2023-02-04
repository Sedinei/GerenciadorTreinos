from typing import Tuple
from dataclasses import dataclass, field
import os
import bcrypt
from .utils import ConexaoDB

#class DAOError(Exception): pass

@dataclass
class DAOControles:
    pasta: str
    arq: str = field(init=False)
    con: ConexaoDB = field(init=False)
    
    def __post_init__(self) -> None:
        ok = True
        if not os.path.isdir(self.pasta):
            os.mkdir(self.pasta)
            ok = False
        self.arq = os.path.join(self.pasta, 'control')
        if not os.path.isfile(self.arq): ok = False
        self.con = ConexaoDB(self.arq)
        if not ok: self._criar_tabelas()
    
    def get_usuario(self, id_user: int) -> Tuple[int, str, str]:
        with self.con as c:
            t = (id_user,)
            c.execute('''SELECT t1.nome_usuario, t2.tp_usuario
                         FROM usuarios as t1
                         LEFT JOIN tiposUsuario as t2
                         ON t1.id_tp_usuario=t2.id_tp_usuario
                         WHERE id_usuario=?''', t)
            nome, tipo = c.fetchone()
            return id_user, nome, tipo
    
    def verificar_senha(self, usuario: str, senha: str) -> Tuple[int, bool]:
        with self.con as c:
            t = (usuario,)
            c.execute('''SELECT id_usuario, senha_usuario FROM usuarios
                         WHERE nome_usuario=?''', t)
            id, hash_stored = c.fetchone()
        return id, self._verificar_senha(senha, hash_stored)
        
    def _criar_tabelas(self) -> None:
        pwd = self._criptografar_senha('admin')
        sqls = ['''CREATE TABLE bds_treino (
                    id_bd_treino INTEGER PRIMARY KEY,
                    nome_bd_treino TEXT UNIQUE)''',
                '''CREATE TABLE tiposUsuario (
                    id_tp_usuario INTEGER PRIMARY KEY,
                    tp_usuario TEXT UNIQUE)''',
                '''CREATE TABLE usuarios (
                    id_usuario INTEGER PRIMARY KEY,
                    nome_usuario TEXT UNIQUE,
                    id_tp_usuario INTEGER,
                    senha_usuario TEXT,
                    FOREIGN KEY(id_tp_usuario)
                    REFERENCES tiposUsuario(id_tp_usuario))''',
                '''INSERT INTO tiposUsuario VALUES
                   (1, "Gerenciador"),
                   (2, "Cadastrador"),
                   (3, "Leitor")''',
                f'''INSERT INTO usuarios VALUES(
                    NULL, "admin", 1, "{pwd}")''']
        with self.con as c:
            for sql in sqls:
                c.execute(sql)
                
    def _criptografar_senha(self, pwd: str) -> str:
        byte = pwd.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(byte, salt)
        return hashed.decode('utf-8')
    
    def _verificar_senha(self, pwd_inputed: str, hash_stored: str) -> bool:
        byte_inputed = pwd_inputed.encode('utf-8')
        byte_stored = hash_stored.encode('utf-8')
        return bcrypt.checkpw(byte_inputed, byte_stored)