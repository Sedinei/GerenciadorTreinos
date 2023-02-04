from typing import Optional
from dataclasses import dataclass, field
from collections import namedtuple
from .dao import DAOControles

Usuario = namedtuple('Usuario', ['id', 'nome', 'tipo'])

@dataclass
class Controles:
    pasta: str
    logado: bool = field(init=False, default= False)
    usuario_logado: Optional[Usuario] = field(init=False)
    _dao: DAOControles = field(init=False)
    
    def __post_init__(self) -> None:
        self._dao = DAOControles(self.pasta)
        
    def logar(self, usuario: str, senha: str) -> bool:
        if self.logado:
            self.usuario_logado = None
            self.logado = False
        id_user, self.logado = self._dao.verificar_senha(usuario, senha)
        if self.logado:
            self.usuario_logado = Usuario(*self._dao.get_usuario(id_user))
        return self.logado