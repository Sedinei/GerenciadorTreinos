import json
from dataclasses import dataclass

@dataclass
class Config:
    path: str = ''
    
    def __post_init__(self) -> None:
        with open('config', 'r') as f:
            config = json.loads(f.read())
        self.path = config['data_path']
        
    def save(self) -> None:
        config = {'data_path': self.path}
        with open('config', 'w') as f:
            f.write(json.dumps(config))