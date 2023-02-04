import os
import sqlite3
from dataclasses import dataclass, field

def singleton(the_class):
    instances = {}
    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]
    return get_class

@dataclass
class ConexaoDB:
    '''
    Abstrai a conexão a um banco de dados SQlite3 que é usado para armazenar as informações do corpus e das configurações
    dos objetos. Essa classe é para ser usada em uma estrutura com with, lançando um cursor para a conexão ao DB do arquivo
    e fazendo o commit e close ao final do bloco.
    '''
    arq_db: str
    conn: sqlite3.Connection = field(init=False)

    def __enter__(self):
        self.conn = sqlite3.connect(self.arq_db)
        return self.conn.cursor()

    def __exit__(self, tipo_excecao, valor_excecao, traceback):
        self.conn.commit()
        self.conn.close()

    def existe(self) -> bool:
        '''
        Verifica se o arquivo de DB já foi criado.
        Retorno:
            True --> Se existe o arquivo de DB
            False --> Se não existe o arquivo de DB
        '''
        return os.path.isfile(self.arq_db)