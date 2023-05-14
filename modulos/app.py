from typing import Optional
import sys
import os
import logging
from dataclasses import dataclass, field
from typing import List, Tuple, Union
from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QCursor, QIcon
from PySide6.QtWidgets import (QApplication, QMessageBox, QMainWindow, QLabel,
                               QDialog, QTreeWidgetItem, QAbstractItemView, QTreeWidget)
from guis.get_path_gui import Ui_get_path
from guis.get_information_gui import Ui_get_information
from guis.login_gui import Ui_Login
from guis.main_gui import Ui_MainWindow
from .config import Config
from .utils import raise_log
from .controls import Controls, User, ControlsError
from .entities import Athlete, Coach, Domain, DomainInfo, User, SETS_DOMAINS
from .entities_ctrl import Athletes, EntitiesError, Coaches, Domains

APP = QApplication(sys.argv)
MW = QMainWindow()
ICON = QIcon()
ICON.addFile(u":/images/cronometro.ico", QtCore.QSize(), QIcon.Normal, QIcon.Off)    

class ManagerError(Exception): pass


@dataclass
class Manager:
    cfg: Config = field(init=False, default=Config())
    ctrls: Controls = field(init=False)
    atlts: Athletes = field(init=False)
    chs: Coaches = field(init=False)
    dmns: Domains = field(init=False)
    
    def __post_init__(self) -> None:
        self._fit_log()
        if not self.cfg.path:
            self._just_log('Solicitando a pasta com os dados.')
            self.cfg.path = self.get_data_path()
            if not self.cfg.path:
                msg = 'Não foi informado nenhuma pasta com os dados.'
                self.box_warning(msg)
                raise_log(ManagerError, msg)
            self.cfg.save()
        self.ctrls = Controls(self.cfg.path)
        self.atlts = Athletes(self.cfg.path)
        self.dmns = Domains(self.cfg.path)
        self.chs = Coaches(self.cfg.path)
        MW.setWindowIcon(ICON)
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
    
    def get_all_values(self, type_data: str) -> List[Union[Athlete, Coach, Domain, User]]:
        if type_data in SETS_DOMAINS:
            registers = self.dmns.get_all_domain(type_data)
        elif type_data == 'atletas':
            registers = self.atlts.get_all_athletes()
        elif type_data == 'usuarios':
            registers = self.ctrls.get_all_users()
        elif type_data == 'treinadores':
            registers = self.chs.get_all_coaches()
        return registers
   
    def get_types_user(self) -> List[str]:
        return self.ctrls.get_types_user()
       
    def get_athletes_groups(self) -> List[str]:
        return self.atlts.get_groups()
    
    def get_data_path(self) -> str:
        window = GetPath()
        window.show()
        APP.exec()
        return window.resposta.text()
    
    def get_information(self, ask: str, text: str='') -> str:
        window = GetInformation()
        window.set_label(ask)
        window.set_text(text)
        window.show()
        APP.exec()
        return window.resposta.text()
    
    def is_at_least_one_selected(self, num_registers: int) -> bool:
        if num_registers == 0:
            msg = 'Você precisa selecionar ao menos um registro!'
            self.box_error(msg)
            return False
        return True  
    
    def is_just_one_selected(self, num_registers: int) -> bool:
        if self.is_at_least_one_selected(num_registers):
            if num_registers > 1:
                msg = 'Você só pode alterar um registro por vez!'
                self.box_error(msg)
                return False
        return True  
      
    def login(self, user: str, password: str) -> bool:
        try:
            self.ctrls.login(user, password)
        except ControlsError as e:
            msg = 'Não foi possível realizar o login'
            self.box_error(msg, e.args[0])
            return False
        return True
    
    def remove_register(self, type_register: str, register: Union[Athlete, Domain, User]) -> None:
        try:
            if type_register in SETS_DOMAINS:
                self.dmns.remove_domain(type_register, register.id)
            elif type_register == 'athlete':
                self.atlts.remove_athlete(register.id)
            elif type_register == 'coach':
                self.coach.remove_coach(register.id)
            elif type_register == 'user':
                self.ctrls.remove_user(register.id)
        except (ControlsError, EntitiesError) as e:
            msg = f'Não foi possível excluir o registro "{register.name}"'
            self.box_error(msg, e.args[0])
    
    def save_domain(self, type_domain: str, domain: Domain, insert: bool) -> bool:
        if insert and not self.dmns.is_unique(type_domain, domain.name):
            self.box_error(f'O nome "{domain.name}" já está sendo usado.')
            return False
        try:
            if insert: self.dmns.save_domain(type_domain, domain)
            else: self.dmns.change_domain(type_domain, domain)
        except EntitiesError as e:
            self.box_error('Houve um erro ao tentar salvar a informação.')
            return False
        return True
     
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
        
    def set_standard_window(self, window: Union[QDialog, QMainWindow]) -> None:
        style_btns = '''QPushButton {
                        	background-color: rgb(0, 0, 0);
                        	color: rgb(255, 255, 255);
                        	border-radius:10px;
                        	font: 10pt "Segoe UI";
                        	min-width: 100px;
                        	min-height: 30px;
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

    def style_title(self, label: QLabel, title: str) -> None:
        label.setTextFormat(QtCore.Qt.TextFormat.RichText)
        text = f'''<html><head/><body><p align="center">
                   <span style=" font-size:20pt; font-weight:700;">
                   {title}</span></p></body></html>'''
        label.setText(text)
        
        
        
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
        APP.exec()
        if self.ctrls.logged:
            self._init_main()
        
    def _init_main(self) -> None:
        window = MainWindow(self)
        window.show()
        APP.exec()
    
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
        box = QMessageBox(MW)
        box.setWindowTitle(titulo)
        box.setIcon(ico)
        box.setText(message)
        box.exec_()


class GetPath(QDialog, Ui_get_path):
    def __init__(self) -> None:
        super(GetPath, self).__init__()
        self.setupUi(self)
        self.resposta.setHidden(True)
        self.dir_base = 'D:\\' if os.path.isdir('d:/') else 'C:\\'
        self.pasta.setText(f'{self.dir_base}GerenciadorTreinos\\')
        self.setWindowIcon(ICON)
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
        

class GetInformation(QDialog, Ui_get_information):
    def __init__(self) -> None:
        super(GetInformation, self).__init__()
        self.setupUi(self)
        self.resposta.setHidden(True)
        self.setWindowIcon(ICON)
        self.btn_OK.clicked.connect(self._return_information)
        self.btn_cancelar.clicked.connect(self._cancel)
        
    def set_label(self, text_label: str) -> None:
        self.label.setTextFormat(QtCore.Qt.TextFormat.RichText)
        text = f'''<html><head/><body><p>
                   <span style=" font-size:10pt; font-weight:700;">
                   {text_label}: </span></p></body></html>'''
        self.label.setText(text)
        
    def set_text(self, text: str) -> None:
        self.texto.setText(text)
    
    def _cancel(self) -> None:
        self.resposta.setText('')
        self.close()
        
    def _return_information(self) -> None:
        self.resposta.setText(self.texto.text())
        self.close()
  
class Login(QDialog, Ui_Login):
    def __init__(self, app: Manager) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.app = app
        self.setWindowIcon(ICON)
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
        self.setWindowIcon(ICON)
        self.users = UsersView(self)
        self.athletes = AthletesView(self)
        self.domains = DomainsView(self)
        self._CLEAN_BUTTONS = ['btn_home',
                               'btn_cadastro',
                               'btn_registro',
                               'btn_relatorios',
                               'btn_conta']
        self.app.set_standard_window(self)
        self._set_connections()
        self.first_time_cadastro = True
        self.pages.setCurrentWidget(self.pg_home)

    def remove_selected_items(self, type_register: str) -> Optional[List[List[str]]]:
        registers = eval(f'self.mw.tbl_{type_register}.selectedItems()')
        if not self.app.is_at_least_one_selected(len(registers)):
            return
        registers = self._get_data_table(registers)
        nm_registers = [register[1] for register in registers]
        title = f'Exclusão de Registros'
        msg = f'Você deseja excluir o seguintes registros?\n'
        msg += '\n'.join(nm_registers)
        if not self.app.box_question(title, msg): return
        if type_register in SETS_DOMAINS:
            register_cls = Domain
            tab_ind = SETS_DOMAINS[type_register].ind_tab
        elif type_register == 'athlete':
            register_cls = Athlete
            tab_ind = 0
        elif type_register == 'coach':
            register_cls = Coach
            tab_ind = 4
        elif type_register == 'user':
            register_cls = User
            tab_ind = 5
        for register in registers:
            self.app.remove_register(type_register, register_cls(*register))
        self._set_pg_cadastro_tab(tab_ind)

    def _get_data_table(self, registers: List[QTreeWidgetItem]) -> List[List[str]]:
        result = []
        for register in registers:
            result.append([register.text(i) for i in range(register.columnCount())])
        return result

    def _return(self) -> None:
        cls_name = self.sender().objectName().split('_')[-1]
        if eval(f'self.{cls_name}.selected is not None'):
            exec(f'self.{cls_name}.selected = None')
        if cls_name == 'domains':
            if self.domains.page_return.startswith('cad_'):
                self._set_pg_cadastro_tab(self.domains.domain_info.ind_tab)
                self.qtab_cadastro.setCurrentIndex(self.domains.domain_info.ind_tab)
                self.pages.setCurrentWidget(self.pg_cadastro)
            else:
                items = eval(f'self.app.get_all_{self.domains.type_domain}s()')
                exec(f'self.box_{self.domains.type_domain}.clear()')
                exec(f'self.box_{self.domains.type_domain}.addItems(items)')
                exec(f'self.pages.setCurrentWidget(self.{self.domains.page_return})')
        elif cls_name == 'users':
            pass
        elif cls_name == 'athletes':
            pass
    
    def _save(self) -> None:
        splited_name = self.sender().objectName().split('_')
        cls_name = splited_name[-1]
        acction = splited_name[2]
        if eval(f'self.{cls_name}.save()'):
            if acction == 'fechar': self._return()
            elif acction == 'manter': exec(f'self.{cls_name}.set_pg_include()')

    def _set_connections(self) -> None:
        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_home))
        self.btn_cadastro.clicked.connect(self._set_pg_cadastro)
        self.btn_registro.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_registro))
        self.btn_relatorios.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_relatorios))
        self.btn_conta.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_conta))
        self.btn_salvar_fechar_athletes.clicked.connect(self._save)
        self.btn_salvar_fechar_domains.clicked.connect(self._save)
        self.btn_salvar_fechar_users.clicked.connect(self._save)
        self.btn_salvar_manter_athletes.clicked.connect(self._save)
        self.btn_salvar_manter_domains.clicked.connect(self._save)
        self.btn_salvar_manter_users.clicked.connect(self._save)
        self.btn_voltar_athletes.clicked.connect(self._return)
        self.btn_voltar_domains.clicked.connect(self._return)
        self.btn_voltar_users.clicked.connect(self._return)
        self.qtab_cadastro.tabBarClicked.connect(self._set_pg_cadastro_tab)
        for widget in self.__dict__:
            if not widget.startswith('btn_'): continue
            if widget.startswith('btn_voltar_'): exec(f'self.{widget}.clicked.connect(self._return)')
            elif (widget.startswith('btn_salvar_fechar_') or
                  widget.startswith('btn_salvar_manter_')): exec(f'self.{widget}.clicked.connect(self._save)')
            else:
                splited_name = widget.split('_')
                if '_'.join(splited_name[-2:]) in SETS_DOMAINS:
                    exec(f'self.{widget}.clicked.connect(self._start_domain)')
        
    def _set_pg_cadastro(self) -> None:
        if self.first_time_cadastro:
            self.first_time_cadastro = False
            self._set_pg_cadastro_tab(0)
            self.qtab_cadastro.setCurrentIndex(0)
        self.pages.setCurrentWidget(self.pg_cadastro)
    
    def _set_pg_cadastro_tab(self, index_tab: int) -> None:
        widget_name = self.qtab_cadastro.widget(index_tab).objectName()
        type_data = widget_name.replace('cad_', '')
        registers = self.app.get_all_values(type_data)
        widget = eval(f'self.tbl_{type_data}')
        widget.clear()
        for register in registers:
            QTreeWidgetItem(widget, register)
    
    def _start_domain(self) -> None:
        splited_btn_name = self.sender().objectName().split('_')
        acction = splited_btn_name[-3]
        type_domain = '_'.join(splited_btn_name[-2:])
        page_return = f'cad_{type_domain}'
        self.domains.start_domain_view(type_domain, acction, page_return)

        
@dataclass
class UsersView:
    mw: MainWindow
    selected: User = field(init=False)
    
    def __post_init__(self) -> None:
        self.types_user = self.mw.app.get_types_user()
        self.mw.box_tp_usuario.addItems(self.types_user)
        self.default_type_user = self.types_user[0]
        self.mw.btn_incluir_usuario.clicked.connect(self._set_pg_cad_usuario)
        self.mw.btn_alterar_usuario.clicked.connect(self._select_user_change)
        self.mw.btn_excluir_usuarios.clicked.connect(self._remove_user)
        self.mw.btn_trocar_senha_usuario.clicked.connect(self._select_user_password_change)
        self.mw.btn_salvar_nova_senha_users.clicked.connect(self._save_new_password)
    
    def _change_user(self) -> None:
        id_user = int(self.mw.hd_id_user.text())
        field_values = {'name_user':{
                              'old': self.mw.hd_txt_old_name_user.text(),
                              'new': self.mw.txt_nome_usuario.text()
                            },
                        'email_user':{
                              'old': self.mw.hd_txt_old_email_user.text(),
                              'new': self.mw.txt_email_usuario.text()
                            },
                        'type_user':{
                              'old': self.mw.hd_txt_old_type_user.text(),
                              'new': self.mw.box_tp_usuario.currentText()
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
        self.mw.pages.setCurrentWidget(self.mw.pg_cadastro)
    
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
        self.mw.pages.setCurrentWidget(self.mw.pg_cadastro)
        
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
        self.mw.pages.setCurrentWidget(self.mw.pg_cadastro)
        
    def _select_user_change(self) -> None:
        register = self.mw.tbl_usuarios.selectedItems()
        if not self.mw.app.is_just_one_selected(len(register)):
            return
        self._user = User(*register)
        self._set_pg_alt_usuario(*user)
     
    def _select_user_password_change(self) -> None:
        registers = self.mw.tbl_usuarios.selectedItems()
        if not self.mw.app.is_just_one_selected(len(registers)):
            return
        id_user = registers[0].text(0)
        name_user = registers[0].text(1)
        self._set_pg_alt_senha_usuario(id_user, name_user)
           
    def _set_pg_cad_usuario(self) -> None:
        self.mw.app.style_title(self.mw.lbl_titulo_pg_cad_alt_usuario, 'Cadastro de Usuário')
        self.mw.btn_salvar_fechar_users.clicked.connect(self._save_user)
        self.mw.txt_nome_usuario.setText('')
        self.mw.txt_email_usuario.setText('')
        self.mw.box_tp_usuario.setCurrentText(self.default_type_user)
        self._clean_password()
        self.mw.txt_nome_usuario.setFocus()
        self.mw.pages.setCurrentWidget(self.mw.pg_cad_alt_usuario)
        
    def _set_pg_alt_senha_usuario(self, id_user: str, name_user: str) -> None:
        self.mw.hd_id_user_new_pass.setText(id_user)
        self.mw.txt_nome_usuario_nova_senha.setText(name_user)
        self._clean_password(new=True)
        self.mw.txt_nova_senha_usuario.setFocus()
        self.mw.pages.setCurrentWidget(self.mw.pg_alt_senha_usuario)
             
    def _set_pg_alt_usuario(self, id_user: str, name_user: str,
                                                 email_user: str, type_user: str) -> None:
        self.mw.app.style_title(self.mw.lbl_titulo_pg_cad_alt_usuario, 'Alteração de Usuário')
        self.mw.btn_salvar_fechar_users.clicked.connect(self._change_user)
        self.mw.txt_nome_usuario.setText(name_user)
        self.mw.txt_email_usuario.setText(email_user)
        self.mw.box_tp_usuario.setCurrentText(type_user)
        self.mw.txt_nome_usuario.setFocus()
        self.mw.pages.setCurrentWidget(self.mw.pg_cad_alt_usuario)

@dataclass
class AthletesView:
    mw: MainWindow
    selected: Optional[Athlete] = field(init=False)
    
    def __post_init__(self) -> None:
        self.mw.btn_incluir_atleta.clicked.connect(self._set_pg_cad_atleta)
        self.mw.btn_alterar_atleta.clicked.connect(self._select_athlete_change)
        self.mw.btn_excluir_atletas.clicked.connect(self._remove_athlete)
        self.mw.btn_cad_alt_atleta_incluir_grupo.clicked.connect(self._new_group)
     
    def _new_group(self) -> None:
        self.mw.domains.start_domain_view(type_domain='posicoes',
                                          acction='incluir',
                                          page_retun='pg_cad_alt_atleta')
      
    def _remove_athlete(self) -> None:
        self.mw.remove_selected_items('athlete')
    
    def _save_athlete(self) -> None:
        self.mw.pages.setCurrentWidget(self.mw.pg_cadastro)
        
    def _select_athlete_change(self) -> None:
        pass
    
    #TODO Implementar morfologia da página de cadastro/alteração
    def _set_pg_cad_atleta(self) -> None:
        self.mw.txt_nome_atleta.setText('')
        self.mw.dt_nascimento.setDate(QtCore.QDate())
        self.mw.box_gp_atleta.clear()
        self.mw.box_gp_atleta.addItems(self.mw.app.get_athletes_groups())
        self.mw.dt_inicio.setDate(QtCore.QDate())
        self.mw.app.style_title(self.mw.lbl_titulo_pg_cad_alt_atleta, 'Cadastro de Atleta')
        self.mw.btn_salvar_fechar_athletes.clicked.connect(self._save_athlete)
        self.mw.lbl_fim_vinculo.setHidden(True)
        self.mw.dt_fim.setHidden(True)
        self.mw.txt_nome_atleta.setFocus()
        self.mw.pages.setCurrentWidget(self.mw.pg_cad_alt_atleta)
        

@dataclass
class DomainsView:
    mw: MainWindow
    domain_info: DomainInfo = field(init=False)
    page_return: str = field(init=False)
    selected: Optional[Domain] = field(init=False)
    type_domain: str = field(init=False)
    
    def save(self) -> bool:
        domain = Domain(id=None,
                        name=self.mw.txt_nome_dominio.text(),
                        description=self.mw.txt_descricao_dominio.toPlainText())
        if not any(domain):
            self.mw.app.box_error(f'Nenhum campo do formulário pode ficar em branco.')
            return False
        insert = True
        if self.selected:
            insert = False
            changes = [self.selected.id]
            for i in range(1, len(domain)):
                changes.append(None if domain[i] == self.selected[i] else domain[i])
            if not any(changes[1:]):
                self.mw.app.box_error(f'Nenhum campo do formulário foi alterado.')
                return False
            domain = Domain(*changes)
        return self.mw.app.save_domain(self.type_domain, domain, insert)
    
    def set_pg_include(self) -> None:
        self.selected = None
        self.mw.txt_nome_dominio.setText('')
        self.mw.txt_descricao_dominio.setText('')
        title = f'Cadastro de {self.domain_info.title}'
        self.mw.app.style_title(self.mw.lbl_titulo_pg_cad_alt_dominio, title)
        self.mw.btn_salvar_manter_domains.setHidden(False)
        self.mw.txt_nome_dominio.setFocus()
        self.mw.pages.setCurrentWidget(self.mw.pg_dominio)
            
    def start_domain_view(self, type_domain: str, acction: str, page_retun: str) -> None:
        self.type_domain = type_domain
        self.page_return = page_retun
        self.selected = None
        self.domain_info = SETS_DOMAINS[self.type_domain]
        if acction == 'incluir': self.set_pg_include()
        elif acction == 'alterar': self._select_domain_change()
        elif acction == 'excluir': self._remove_domain()
        
    def _remove_domain(self) -> None:
        self.mw.remove_selected_items(self.type_domain)
    
    def _select_domain_change(self) -> None:
        register = eval(f'self.mw.tbl_{self.type_domain}.selectedItems()')
        if not self.mw.app.is_just_one_selected(len(register)):
            return
        register = self.mw._get_data_table(register)[0]
        self.selected = Domain(*register)
        self._set_pg_change()
    
    def _set_pg_change(self) -> None:
        self.mw.txt_nome_dominio.setText(self.selected.name)
        self.mw.txt_descricao_dominio.setText(self.selected.description)
        title = f'Alteração de {self.domain_info.title}'
        self.mw.app.style_title(self.mw.lbl_titulo_pg_cad_alt_dominio, title)
        self.mw.btn_salvar_manter_domains.setHidden(True)
        self.mw.txt_nome_dominio.setFocus()
        self.mw.pages.setCurrentWidget(self.mw.pg_dominio)
    