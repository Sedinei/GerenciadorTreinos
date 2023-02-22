from typing import Optional, List, Tuple
from dataclasses import dataclass, field
from collections import namedtuple
import logging
from .dao import DAOControls, DAOError

User = namedtuple('User', ['id', 'name', 'email', 'type'])

class ControlsError(Exception): pass

@dataclass
class Controls:
    pasta: str
    logged: bool = field(init=False, default= False)
    user_logged: Optional[User] = field(init=False)
    _dao: DAOControls = field(init=False)
    
    def __post_init__(self) -> None:
        self._dao = DAOControls(self.pasta)
        
    def get_all_users(self) -> List[Tuple[int, str, str, str]]:
        return self._dao.get_all_users()
        
    def login(self, user: str, password: str) -> None:
        if self.logged:
            self.user_logged = None
            self.logged = False
        id_user, self.logged = self._dao.check_password(user, password)
        if self.logged:
            self.user_logged = User(*self._dao.get_user(id_user))
        else:
            raise ControlsError('Senha ou usuário inválido!')
    
    def save_password_user(self, id_user: int, password: str) -> None:
        try:
            self._dao.save_password_user(id_user, password)
        except DAOError as e:
            msg = f'Não foi possível alterar a senha para o usuário de id "{id_user}" ' \
                  f'em razão do seguinte erro: {e.args[0]}'
            logging.error(msg)
            raise ControlsError('Erro na aplicação.')
    
    def change_user(self, id_user: int, name_user: str, email_user: str, type_user: str) -> None:
        if name_user and not self._dao.check_unique_name_user(name_user):
            msg = f'Já existe um usuário com o nome "{name_user}".'
            raise ControlsError(msg)
        try:
            self._dao.change_user(id_user, name_user, email_user, type_user)
        except DAOError as e:
            msg = 'Houve o seguinte erro ao tentar alterar o usuário com os seguintes dados:\n'
            msg += f'id_user: {id_user}\n'
            msg += f'name_user: {name_user}\n'
            msg += f'email_user: {email_user}\n'
            msg += f'type_user: {type_user}\n'
            msg += f'Em razão do seguinte erro: {e.args[0]}'
            logging.error(msg)
            raise ControlsError('Erro no programa.')
    
    def remove_user(self, id_user: int) -> None:
        try:
            self._dao.remove_user(id_user)
        except DAOError as e:
            raise ControlsError(e.args[0])
    
    def save_user(self, name_user: str, email_user: str, type_user: str, password: str):
        try:
            self._dao.save_user(name_user, email_user, type_user, password)
        except DAOError as e:
            raise ControlsError(e.args[0])