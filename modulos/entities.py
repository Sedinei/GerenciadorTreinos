from collections import namedtuple

Athlete = namedtuple('Athlete', ['id', 'name', 'dt_born', 'group', 'dt_start', 'dt_end'])
Domain = namedtuple('Domain', ['id', 'name', 'description'])
DomainInfo = namedtuple('DomainInfo', ['title', 'placeholder', 'table', 'ind_tab'])
Coach = namedtuple('Coach', ['id', 'name', 'dt_start', 'dt_end'])
User = namedtuple('User', ['id', 'name', 'type', 'email'])

TYPES_USER = ['Gerenciador', 'Registrador', 'Leitor']

SETS_DOMAINS = {'posicoes': DomainInfo(title='Posição',
                                        placeholder='posição',
                                        table='posicao',
                                        ind_tab=1),
                'tp_dispensa': DomainInfo(title='Tipo de Dispensa',
                                          placeholder='tipo de dispensa',
                                          table='tipo_dispensa',
                                          ind_tab=2),
                'tp_treino': DomainInfo(title='Tipo de Treino',
                                        placeholder='tipo de treino',
                                        table='tipo_treino',
                                        ind_tab=3)}