from modulos.app import Manager
from modulos.utils import raise_log

class ControlsError(Exception): pass

def main():
    Manager()
    
if __name__ == '__main__':
    main()