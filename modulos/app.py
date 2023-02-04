import sys
import os
import logging
from dataclasses import dataclass, field
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow, QDialog
from guis.get_pasta_gui import Ui_get_pasta
from guis.login_gui import Ui_Login
from .config import Config
from .controles import Controles

class GerenciadorError(Exception): pass

@dataclass
class Gerenciador:
    cfg: Config = field(init=False, default=Config())
    ctrls: Controles = field(init=False)
    _app: QApplication = QApplication(sys.argv)
    _main_wdw: QMainWindow = QMainWindow()
    
    def __post_init__(self) -> None:
        self._ajustar_log()
        if not self.cfg.pasta:
            logging.debug('Solicitando a pasta com os dados.')
            self.cfg.pasta = self.get_pasta_dados()
            if not self.cfg.pasta:
                msg = 'Não foi informado nenhuma pasta com os dados.'
                self.alerta(msg)
                raise GerenciadorError
            self.cfg.salvar()
        self.ctrls = Controles(self.cfg.pasta)
        self.logar()
        
    def abrir_app(self) -> None:
        pass
        
    def alerta(self, mensagem: str) -> None:
        logging.warning(mensagem)
        self._aviso(mensagem, 'alerta')
        
    def erro(self, mensagem: str) -> None:
        logging.error(mensagem)
        self._aviso(mensagem, 'erro')
        
    def get_pasta_dados(self) -> str:
        window = GetPasta()
        window.show()
        self._app.exec()
        return window.resposta.text()
    
    def logar(self) -> None:
        window = Login(self)
        window.show()
        self._app.exec()
        if self.ctrls.logado:
            nome = self.ctrls.usuario_logado.nome
            tipo = self.ctrls.usuario_logado.tipo
            msg = f'Usuário "{nome}" do tipo "{tipo}" logado!'
            self.mensagem(msg)
            self.abrir_app()
            
    def mensagem(self, mensagem: str) -> None:
        logging.debug(mensagem)
        self._aviso(mensagem, 'mensagem')
    
    def _ajustar_log(self):
        if os.path.isfile('stdout.log'):
            if os.path.isfile('stdprev.log'):
                os.remove('stdprev.log')
            os.rename('stdout.log', 'stdprev.log')
        logging.basicConfig(filename='stdout.log',
                            format='%(asctime)s %(levelname)s: %(message)s',
                            datefmt='%d/%m/%Y %H:%M:%S',
                            encoding='utf-8',
                            filemode='w',
                            level=logging.INFO)
    
    def _aviso(self, mensagem: str, tipo: str) -> None:
        if tipo == 'alerta':
            ico = QMessageBox.Warning
            titulo = 'ATENÇÃO!'
        elif tipo == 'erro':
            ico = QMessageBox.Critical
            titulo = 'ERRO!'
        elif tipo == 'mensagem':
            ico = QMessageBox.Information
            titulo = 'Aviso'
        else:
            ico = QMessageBox.NoIcon
            titulo = ''
        dlg = QMessageBox(self._main_wdw)
        dlg.setWindowTitle(titulo)
        dlg.setIcon(ico)
        dlg.setText(mensagem)
        dlg.exec_()
    
class GetPasta(QDialog, Ui_get_pasta):
    def __init__(self) -> None:
        super(GetPasta, self).__init__()
        self.setupUi(self)
        self.resposta.setHidden(True)
        self.dir_base = 'D:\\' if os.path.isdir('d:/') else 'C:\\'
        self.pasta.setText(f'{self.dir_base}GerenciadorTreinos\\')
        self.btn_procurar.clicked.connect(self._find_pasta)
        self.btn_OK.clicked.connect(self._retorna_pasta)
        self.btn_cancelar.clicked.connect(self._cancelar)
    
    def _cancelar(self) -> None:
        self.resposta.setText('')
        self.close()
    
    def _retorna_pasta(self) -> None:
        self.resposta.setText(self.pasta.text())
        self.close()
        
    def _find_pasta(self) -> None:
        dialog = QtWidgets.QFileDialog()
        pasta = dialog.getExistingDirectory(None,
                                            "Selecione a pasta",
                                            dir=self.dir_base)
        self.pasta.setText(pasta)
        
class Login(QDialog, Ui_Login):
    def __init__(self, app: Gerenciador) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.app = app
        self.btn_login.clicked.connect(self._verificar_login)
        
    def _verificar_login(self) -> None:
        user = self.usuario.text()
        pwd = self.senha.text()
        if not self.app.ctrls.logar(user, pwd):
            msg = 'Usuário ou senha inválidos!'
            self.app.erro(msg)
        self.close()