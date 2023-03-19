from typing import Optional, List, Tuple
from dataclasses import dataclass, field
from collections import namedtuple
from datetime import date
import logging
from .dao import DAODados, DAOError
from .utils import raise_log, fix_register_values


class EntitiesError(Exception): pass

Athlete = namedtuple('Athlete', ['id', 'name', 'dt_born', 'group', 'dt_start', 'dt_end'])
Domain = namedtuple('Domain', ['id', 'name', 'description'])
DomainInfo = namedtuple('DomainInfo', ['title', 'placeholder', 'table', 'ind_tab'])
Coach = namedtuple('Coach', ['id', 'name', 'dt_start', 'dt_end'])

SETS_DOMAINS = {'gp_atletas': DomainInfo(title='Grupo de Atletas',
                                        placeholder='grupo de atletas',
                                        table='grupo_atletas',
                                        ind_tab=1),
                'tp_dispensa': DomainInfo(title='Tipo de Dispensa',
                                          placeholder='tipo de dispensa',
                                          table='tipo_dispensa',
                                          ind_tab=2),
                'tp_treino': DomainInfo(title='Tipo de Treino',
                                        placeholder='tipo de treino',
                                        table='tipo_treino',
                                        ind_tab=3)}

@dataclass
class Athletes:
    pasta: str
    _dao: DAODados = field(init=False)
    
    def __post_init__(self) -> None:
        self._dao = DAODados(self.pasta)
        
    def get_all_athletes(self) -> List[Athlete]:
        dao_athletes = self._dao.get_all_athletes()
        return [Athlete(*fix_register_values(dao_athlete))
                for dao_athlete in dao_athletes]
    
    def get_groups(self) -> List[str]:
        return self._dao.get_groups()
    
    def insert_athlete(self, atlhlete: Athlete) -> None:
        self._dao.insert_athlete(atlhlete.name,
                                 atlhlete.dt_born,
                                 atlhlete.group,
                                 atlhlete.dt_start)

@dataclass
class Coaches:
    pasta: str
    _dao: DAODados = field(init=False)
        
    def __post_init__(self) -> None:
        self._dao = DAODados(self.pasta)
        
    def get_all_coaches(self) -> List[Coach]:
        dao_coaches = self._dao.get_all_coaches()
        return [Coach(*fix_register_values(dao_coache))
                for dao_coache in dao_coaches]
        
@dataclass
class Domains:
    pasta: str
    _dao: DAODados = field(init=False)
    
    def __post_init__(self) -> None:
        self._dao = DAODados(self.pasta)
    
    def change_domain(self, type_domain: str, domain: Domain) -> None:
        infos_domain = SETS_DOMAINS[type_domain]
        try:
            self._dao.change_domain(infos_domain.table, type_domain, domain.id,
                                    domain.name, domain.description)
        except DAOError as e:
            raise_log(EntitiesError, e.args[0])
    
    def get_all_domain(self, type_domain: str) -> List[Domain]:
        infos_domain = SETS_DOMAINS[type_domain]
        dao_domains = self._dao.get_all_domain(infos_domain.table, type_domain)
        return [Domain(*fix_register_values(dao_domain))
                for dao_domain in dao_domains]
    
    def remove_domain(self, type_domain: str, id_domain: str) -> None:
        infos_domain = SETS_DOMAINS[type_domain]
        try:
            self._dao.remove_domain(infos_domain.table, type_domain, int(id_domain))
        except DAOError as e:
            raise_log(EntitiesError, e.args[0])
    
    def save_domain(self, type_domain: str, domain: Domain) -> None:
        infos_domain = SETS_DOMAINS[type_domain]
        try:
            self._dao.save_domain(infos_domain.table, domain.name, domain.description)
        except DAOError as e:
            raise_log(EntitiesError, e.args[0])
            
    def is_unique(self, type_domain: str, name_domain: str) -> bool:
        infos_domain = SETS_DOMAINS[type_domain]
        return self._dao.is_unique(infos_domain.table, type_domain, name_domain)