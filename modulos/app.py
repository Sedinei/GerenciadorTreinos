import sys
import os
import logging
from dataclasses import dataclass, field
from typing import List, Tuple, Union
from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QCursor, QIcon
from PySide6.QtWidgets import (QApplication, QMessageBox, QMainWindow,
                               QDialog, QTreeWidgetItem, QAbstractItemView)
from guis.get_pasta_gui import Ui_get_pasta
from guis.login_gui import Ui_Login
from guis.main_gui import Ui_MainWindow
from .config import Config
from .controls import Controls, ControlsError

def set_standard_window(window: Union[QDialog, QMainWindow]) -> None:
    style_btns = '''QPushButton {
                    	background-color: rgb(0, 0, 0);
                    	color: rgb(255, 255, 255);
                    	border-radius:10px;
                    	font: 10pt "Segoe UI";
                    	min-width: 75px;
                    	min-height: 25px;
                    }
                    QPushButton:hover {
                    	background-color: rgb(255, 255, 255);
                    	color: rgb(0, 0, 0);
                    }'''
    style_tbls = '''alternate-background-color: #bfffbf;
                    background-color: #deffde;
                    selection-color: #deffde;'''
    size_tbl_cols = {'tbl_usuarios': [200, 100]}
    for widget in window.__dict__:
        if widget.startswith('btn_'):
            exec(f'window.{widget}.setStyleSheet(style_btns)')
            exec(f'window.{widget}.setCursor(QCursor(QtCore.Qt.PointingHandCursor))')
        elif widget.startswith('hd_'):
            exec(f'window.{widget}.setHidden(True)')
        elif widget.startswith('tbl_'):
            exec(f'window.{widget}.setAlternatingRowColors(True)')
            exec(f'window.{widget}.setSortingEnabled(True)')
            exec(f'window.{widget}.setSelectionMode(QAbstractItemView.ExtendedSelection)')
            exec(f'window.{widget}.setColumnHidden(0, True)')
            exec(f'window.{widget}.setStyleSheet(style_tbls)')
            sizes_cols = size_tbl_cols.get(widget)
            if sizes_cols:
                for i, size in enumerate(sizes_cols):
                    col = i + 1
                    exec(f'window.{widget}.setColumnWidth(col, size)')


class ManagerError(Exception): pass

@dataclass
class Manager:
    cfg: Config = field(init=False, default=Config())
    ctrls: Controls = field(init=False)
    _app: QApplication = QApplication(sys.argv)
    _main_wdw: QMainWindow = QMainWindow()
    
    def __post_init__(self) -> None:
        self._fit_log()
        if not self.cfg.path:
            self._just_log('Solicitando a pasta com os dados.')
            self.cfg.path = self.get_data_path()
            if not self.cfg.path:
                msg = 'Não foi informado nenhuma pasta com os dados.'
                self.box_warning(msg)
                raise ManagerError
            self.cfg.save()
        self.ctrls = Controls(self.cfg.path)
        icon = QIcon()
        icon.addFile(u":/images/cronometro.ico", QtCore.QSize(), QIcon.Normal, QIcon.Off)
        self._main_wdw.setWindowIcon(icon)
        self._init_login()
               
    def box_error(self, message_user: str, message_error: str='') -> None:
        if message_error:
            message_user = f'{message_user} em razão do seguinte erro: {message_error}'
        logging.error(f'Manager: {message_user}')
        self._message_box(message_user, 'error')
         
    def box_message(self, message_user: str) -> None:
        logging.debug(f'Manager: {message_user}')
        self._message_box(message_user, 'message')
        
    def box_question(self, title: str, message: str) -> bool:
        box = QMessageBox()
        box.setIcon(QMessageBox.Question)
        box.setWindowTitle(title)
        box.setText(message)
        box.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        buttonY = box.button(QMessageBox.Yes)
        buttonY.setText('Sim')
        buttonN = box.button(QMessageBox.No)
        buttonN.setText('Não')
        box.exec_()
        if box.clickedButton() == buttonY:
            return True
        else: return False
        
    def box_warning(self, message_user: str) -> None:
        logging.warning(f'Manager: {message_user}')
        self._message_box(message_user, 'warning')
 
    def change_user(self, id_user: int, name_user: str='',
                    email_user: str='', type_user: str='') -> None:
        try:
            self.ctrls.change_user(id_user, name_user, email_user, type_user)
        except ControlsError as e:
            msg = f'Não foi possível alterar os dados do usuário "{name_user}"'
            self.box_error(msg, e.args[0])
   
    def get_all_users(self) -> List[Tuple[int, str, str, str]]:
        return self.ctrls.get_all_users()
    
    def get_data_path(self) -> str:
        window = GetPasta()
        window.show()
        self._app.exec()
        return window.resposta.text()
    
    def login(self, user: str, password: str) -> bool:
        try:
            self.ctrls.login(user, password)
        except ControlsError as e:
            msg = 'Não foi possível realizar o login'
            self.box_error(msg, e.args[0])
            return False
        return True
           
    def remove_user(self, id_user: int, name_user: str) -> None:
        try:
            self.ctrls.remove_user(id_user)
        except ControlsError as e:
            msg = f'Não foi possível excluir o usuário "{name_user}"'
            self.box_error(msg, e.args[0])
     
    def save_password_user(self, id_user: int, password: str, name_user: str) -> None:
        try:
            self.ctrls.save_password_user(id_user, password)
        except ControlsError as e:
            msg = f'Não foi possível alterar a senha do usuário "{name_user}"'
            self.box_error(msg, e.args[0])
             
    def save_user(self, user: str, email: str, type_user: str, password: str):
        try:
            self.ctrls.save_user(user, email, type_user, password)
        except ControlsError as e:
            msg = f'Não foi possível incluir o usuário "{user}"'
            self.box_error(msg, e.args[0])
        self._just_log(f'Novo usuário "{user}" salvo.')
        
    def _fit_log(self):
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
       
    def _init_login(self) -> None:
        window = Login(self)
        window.show()
        self._app.exec()
        if self.ctrls.logged:
            self._init_main()
        
    def _init_main(self) -> None:
        window = MainWindow(self)
        window.show()
        self._app.exec()
    
    def _just_log(self, message: str) -> None:
        logging.debug(f'Manager: {message}')
    
    def _message_box(self, message: str, tipo: str) -> None:
        if tipo == 'warning':
            ico = QMessageBox.Warning
            titulo = 'ATENÇÃO!'
        elif tipo == 'error':
            ico = QMessageBox.Critical
            titulo = 'ERRO!'
        elif tipo == 'message':
            ico = QMessageBox.Information
            titulo = 'Aviso'
        else:
            ico = QMessageBox.NoIcon
            titulo = ''
        box = QMessageBox(self._main_wdw)
        box.setWindowTitle(titulo)
        box.setIcon(ico)
        box.setText(message)
        box.exec_()


class GetPasta(QDialog, Ui_get_pasta):
    def __init__(self) -> None:
        super(GetPasta, self).__init__()
        self.setupUi(self)
        self.resposta.setHidden(True)
        self.dir_base = 'D:\\' if os.path.isdir('d:/') else 'C:\\'
        self.pasta.setText(f'{self.dir_base}GerenciadorTreinos\\')
        self.btn_procurar.clicked.connect(self._find_path)
        self.btn_OK.clicked.connect(self._return_path)
        self.btn_cancelar.clicked.connect(self._cancelar)
    
    def _cancelar(self) -> None:
        self.resposta.setText('')
        self.close()
    
    def _find_path(self) -> None:
        dialog = QtWidgets.QFileDialog()
        path = dialog.getExistingDirectory(None,
                                            "Selecione a pasta",
                                            dir=self.dir_base)
        self.pasta.setText(path)
        
    def _return_path(self) -> None:
        self.resposta.setText(self.pasta.text())
        self.close()
        
class Login(QDialog, Ui_Login):
    def __init__(self, app: Manager) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.app = app
        self.btn_login.clicked.connect(self._verificar_login)
        
    def _verificar_login(self) -> None:
        user = self.usuario.text()
        pwd = self.senha.text()
        if not self.app.login(user, pwd):
            self.usuario.setText('')
            self.senha.setText('')
            self.usuario.setFocus()
            return
        self.close()

class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, app: Manager) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.app = app
        self.users = UsersView(self)
        self._CLEAN_BUTTONS = ['btn_home',
                               'btn_cadastro',
                               'btn_registro',
                               'btn_relatorios',
                               'btn_conta']
        set_standard_window(self)
        self._set_buttons_main()
        self.pages.setCurrentWidget(self.pg_home)

    def _set_buttons_main(self) -> None:
        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_home))
        self.btn_cadastro.clicked.connect(self._set_pg_cadastro)
        self.btn_registro.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_registro))
        self.btn_relatorios.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_relatorios))
        self.btn_conta.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_conta))
        
    def _set_pg_cadastro(self) -> None:
        self.qtab_cadastro.tabBarClicked.connect(self._set_pg_cadastro_tab)
        self._set_pg_cadastro_tab_cad_atletas()
        self.pages.setCurrentWidget(self.cad_atletas)
    
    def _set_pg_cadastro_tab(self, index_tab: int) -> None:
        widget = self.qtab_cadastro.widget(index_tab)
        exec(f'self._set_pg_cadastro_tab_{widget.objectName()}()')
        
    def _set_pg_cadastro_tab_cad_atletas(self) -> None:
        pass
    
    def _set_pg_cadastro_tab_cad_gp_atletas(self) -> None:
        pass
        
    def _set_pg_cadastro_tab_cad_tp_dispensa(self) -> None:
        pass
    
    def _set_pg_cadastro_tab_cad_tp_treino(self) -> None:
        pass
        
    def _set_pg_cadastro_tab_cad_treinadores(self) -> None:
        pass
        
    def _set_pg_cadastro_tab_cad_usuarios(self) -> None:
        self.tbl_usuarios.clear()
        users = self.app.get_all_users()
        for user in users:
            user = list(user)
            user[0] = str(user[0])
            QTreeWidgetItem(self.tbl_usuarios, user)
        self.pages.setCurrentWidget(self.cad_usuarios)
            
        
@dataclass
class UsersView:
    mw: MainWindow
    
    def __post_init__(self) -> None:
        self.mw.btn_incluir_usuario.clicked.connect(self._set_pg_cad_usuario)
        self.mw.btn_alterar_usuario.clicked.connect(self._select_user_change)
        self.mw.btn_excluir_usuarios.clicked.connect(self._remove_user)
        self.mw.btn_trocar_senha_usuario.clicked.connect(self._select_user_password_change)
        self.mw.btn_salvar_usuario.clicked.connect(self._save_user)
        self.mw.btn_salvar_alterar_usuario.clicked.connect(self._change_user)
        self.mw.btn_salvar_nova_senha_usuario.clicked.connect(self._save_new_password)
    
    def _change_user(self) -> None:
        id_user = int(self.mw.hd_id_user.text())
        field_values = {'name_user':{
                              'old': self.mw.hd_txt_old_name_user.text(),
                              'new': self.mw.txt_novo_nome_usuario.text()
                            },
                        'email_user':{
                              'old': self.mw.hd_txt_old_email_user.text(),
                              'new': self.mw.txt_novo_email_usuario.text()
                            },
                        'type_user':{
                              'old': self.mw.hd_txt_old_type_user.text(),
                              'new': self.mw.box_novo_tp_usuario.currentText()
                            }
                        }
        if any([v['new']=='' for v in field_values.values()]):
            msg = 'Você não pode deixar nenhum campo em branco!'
            self.mw.app.box_error(msg)
            self.mw._set_pg_cadastro_tab_cad_usuarios()
            return
        parameters = {'id_user': id_user}
        for k, v in field_values.items():
            if v['old'] != v['new']:
                parameters[k] = v['new']
        if len(parameters) != 1:
            self.mw.app.change_user(**parameters)
        self.mw._set_pg_cadastro_tab_cad_usuarios()
    
    def _clean_password(self, new: bool=False) -> None:
        if new:
            self.mw.txt_nova_senha_usuario.setText('')
            self.mw.txt_confirma_nova_senha_usuario.setText('')
        else:
            self.mw.txt_senha_usuario.setText('')
            self.mw.txt_confirma_senha_usuario.setText('')
    
    def _is_same_password(self, password: str, confirme_password: str, new: bool=False) -> bool:
        if password != confirme_password:
            self._clean_password(new)
            msg = 'Senha e confirmação de senha são diferentes!'
            self.mw.app.box_error(msg)
            return False
        return True
        
    def _is_valid_change_selection(self, num_registers: int) -> bool:
        if num_registers > 1:
            msg = 'Você só pode alterar um usuário por vez!'
            self.mw.app.box_error(msg)
            return False
        elif num_registers == 0:
            msg = 'Você precisa selecionar um usuário!'
            self.mw.app.box_error(msg)
            return False
        return True  
  
    def _remove_user(self) -> None:
        registers = self.mw.tbl_usuarios.selectedItems()
        if len(registers) == 0:
            msg = 'Você precisa selecionar um usuário!'
            self.mw.app.box_error(msg)
            return            
        nm_users = [register.text(1) for register in registers]
        if self.mw.app.ctrls.user_logged.name in nm_users:
            msg = 'Você não pode excluir o usuário logado!'
            self.mw.app.box_error(msg)
            return
        title = 'Exclusão de usuários'
        msg = 'Você deseja excluir os seguintes usuários?\n'
        msg += '\n'.join(nm_users)
        if not self.mw.app.box_question(title, msg): return
        for register in registers:
            id_user = int(register.text(0))
            name_user = register.text(1)
            self.mw.app.remove_user(id_user, name_user)
        self.mw._set_pg_cadastro_tab_cad_usuarios()
            
    def _save_new_password(self) -> None:
        new_pass = self.mw.txt_nova_senha_usuario.text()
        cf_new_pass = self.mw.txt_confirma_nova_senha_usuario.text()
        if not self._is_same_password(new_pass, cf_new_pass, new=True):
            return
        id_user = int(self.mw.hd_id_user_new_pass.text())
        name_user = self.mw.txt_nome_usuario_nova_senha.text()
        self.mw.app.save_password_user(id_user, new_pass, name_user)
        self.mw._set_pg_cadastro_tab_cad_usuarios()
        
    def _save_user(self) -> None:
        user = self.mw.txt_nome_usuario.text()
        email = self.mw.txt_email_usuario.text()
        tp_user = self.mw.box_tp_usuario.currentText()
        pass_user = self.mw.txt_senha_usuario.text()
        cf_pass_user = self.mw.txt_confirma_senha_usuario.text()
        if not self._is_same_password(pass_user, cf_pass_user):
            return
        self.mw.app.save_user(user, email, tp_user, pass_user)
        self.mw._set_pg_cadastro_tab_cad_usuarios()
        
    def _select_user_change(self) -> None:
        registers = self.mw.tbl_usuarios.selectedItems()
        if not self._is_valid_change_selection(len(registers)):
            return
        user = [registers[0].text(i) for i in range(registers[0].columnCount())]
        self._set_pg_alt_usuario(*user)
     
    def _select_user_password_change(self) -> None:
        registers = self.mw.tbl_usuarios.selectedItems()
        if not self._is_valid_change_selection(len(registers)):
            return
        id_user = registers[0].text(0)
        name_user = registers[0].text(1)
        self._set_pg_alt_senha_usuario(id_user, name_user)
           
    def _set_pg_cad_usuario(self) -> None:
        self.mw.txt_nome_usuario.setText('')
        self.mw.txt_email_usuario.setText('')
        self.mw.box_tp_usuario.setCurrentText('Gerenciador')
        self._clean_password()
        self.mw.txt_nome_usuario.setFocus()
        self.mw.pages.setCurrentWidget(self.mw.pg_cad_usuario)
        
    def _set_pg_alt_senha_usuario(self, id_user: str, name_user: str) -> None:
        self.mw.hd_id_user_new_pass.setText(id_user)
        self.mw.txt_nome_usuario_nova_senha.setText(name_user)
        self._clean_password(new=True)
        self.mw.txt_nova_senha_usuario.setFocus()
        self.mw.pages.setCurrentWidget(self.mw.pg_alt_senha_usuario)
             
    def _set_pg_alt_usuario(self, id_user: str, name_user: str,
                                                 email_user: str, type_user: str) -> None:
        self.mw.hd_id_user.setText(id_user)
        self.mw.hd_txt_old_name_user.setText(name_user)
        self.mw.hd_txt_old_email_user.setText(email_user)
        self.mw.hd_txt_old_type_user.setText(type_user)
        self.mw.txt_novo_nome_usuario.setText(name_user)
        self.mw.txt_novo_email_usuario.setText(email_user)
        self.mw.box_novo_tp_usuario.setCurrentText(type_user)
        self.mw.txt_nome_usuario.setFocus()
        self.mw.pages.setCurrentWidget(self.mw.pg_alt_usuario)
           