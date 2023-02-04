from modulos.app import Gerenciador, GerenciadorError

def main():
    try:
        app = Gerenciador()
    except GerenciadorError as _:
        return
    
main()