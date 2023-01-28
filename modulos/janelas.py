import sys
from PySide6.QtWidgets import QApplication
from guis.guis_control import GetPasta

class Janelas:
    def get_pasta_dados(self):
        app = QApplication(sys.argv)
        window = GetPasta()
        window.show()
        app.exec()
        return window.resposta.text()