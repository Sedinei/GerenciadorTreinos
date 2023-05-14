from typing import Optional, List, Tuple
from dataclasses import dataclass, field
from collections import namedtuple
from datetime import date
import logging
from .dao import DAODados, DAOError
from .entities import Athlete, Domain, Coach
from .utils import raise_log, fix_register_values


class EntitiesError(Exception): pass

@dataclass
class Athletes:
    pasta: str
    _dao: DAODados = field(init=False)
    
    def __post_init__(self) -> None:
        self._dao = DAODados(self.pasta)
        
    def get_all_athletes(self) -> List[Athlete]:
        return self._dao.get_all_registers('athlete')
    
    def get_groups(self) -> List[str]:
        return self._dao.get_groups()
    
    def insert_athlete(self, atlhlete: Athlete) -> None:
        self._dao.insert_athlete(atlhlete.name,
                                 atlhlete.dt_born,
                                 atlhlete.group,
                                 atlhlete.dt_start)

    def remove_athlete(self, athlete: Athlete) -> None:
        try:
            self._dao.remove_register('athlete', int(athlete.id))
        except DAOError as e:
            raise_log(EntitiesError, e.args[0])
            
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
        
    def remove_coach(self, coach: Coach) -> None:
        try:
            self._dao.remove_register('coach', int(coach.id))
        except DAOError as e:
            raise_log(EntitiesError, e.args[0])
        
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
        return self._dao.get_all_registers(type_domain)
    
    def remove_domain(self, type_domain: str, id_domain: str) -> None:
        infos_domain = SETS_DOMAINS[type_domain]
        try:
            self._dao.remove_register(type_domain, int(id_domain), infos_domain.table)
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