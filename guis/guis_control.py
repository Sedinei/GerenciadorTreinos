import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog
from .get_pasta_gui import Ui_get_pasta

class GetPasta(QDialog, Ui_get_pasta):
    def __init__(self):
        super(GetPasta, self).__init__()
        self.setupUi(self)
        self.resposta.setHidden(True)
        self.btn_procurar.clicked.connect(self._find_pasta)
        self.btn_OK.clicked.connect(self._retorna_pasta)
        self.btn_cancelar.clicked.connect(self._cancelar)
    
    def _cancelar(self):
        self.resposta.setText('')
        self.close()
    
    def _retorna_pasta(self) -> None:
        self.resposta.setText(self.pasta.text())
        self.close()
        
    def _find_pasta(self) -> None:
        dialog = QtWidgets.QFileDialog()
        pasta = str(dialog.getExistingDirectory(None, "Selecione a pasta"))
        self.pasta.setText(pasta)