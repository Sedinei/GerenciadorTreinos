import json
from dataclasses import dataclass

@dataclass
class Config:
    pasta: str = ''
    
    def __post_init__(self) -> None:
        with open('config', 'r') as f:
            config = json.loads(f.read())
        self.pasta = config['pasta_dados']
        
    def salvar(self) -> None:
        config = {'pasta_dados': self.pasta}
        with open('config', 'w') as f:
            f.write(json.dumps(config))