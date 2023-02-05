# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)
from  . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(863, 533)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 203, 70);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.btn_home.setFont(font)

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_cadastro = QPushButton(self.frame)
        self.btn_cadastro.setObjectName(u"btn_cadastro")
        self.btn_cadastro.setFont(font)

        self.horizontalLayout.addWidget(self.btn_cadastro)

        self.btn_registro = QPushButton(self.frame)
        self.btn_registro.setObjectName(u"btn_registro")
        self.btn_registro.setFont(font)

        self.horizontalLayout.addWidget(self.btn_registro)

        self.btn_relatorios = QPushButton(self.frame)
        self.btn_relatorios.setObjectName(u"btn_relatorios")
        self.btn_relatorios.setFont(font)

        self.horizontalLayout.addWidget(self.btn_relatorios)

        self.btn_conta = QPushButton(self.frame)
        self.btn_conta.setObjectName(u"btn_conta")
        self.btn_conta.setFont(font)

        self.horizontalLayout.addWidget(self.btn_conta)


        self.verticalLayout_2.addWidget(self.frame)

        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.horizontalLayout_2 = QHBoxLayout(self.pg_home)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.pg_home)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.1);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(291, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/images/cronometro.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(290, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.pages.addWidget(self.pg_home)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_5 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabWidget = QTabWidget(self.pg_cadastro)
        self.tabWidget.setObjectName(u"tabWidget")
        self.cad_atletas = QWidget()
        self.cad_atletas.setObjectName(u"cad_atletas")
        self.verticalLayout_16 = QVBoxLayout(self.cad_atletas)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tbl_atletas = QTreeWidget(self.cad_atletas)
        self.tbl_atletas.setObjectName(u"tbl_atletas")

        self.horizontalLayout_9.addWidget(self.tbl_atletas)

        self.frame_11 = QFrame(self.cad_atletas)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_11)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.btn_incluir_atletas = QPushButton(self.frame_11)
        self.btn_incluir_atletas.setObjectName(u"btn_incluir_atletas")

        self.verticalLayout_15.addWidget(self.btn_incluir_atletas)

        self.btn_alterar_atletas = QPushButton(self.frame_11)
        self.btn_alterar_atletas.setObjectName(u"btn_alterar_atletas")

        self.verticalLayout_15.addWidget(self.btn_alterar_atletas)

        self.btn_excluir_atletas = QPushButton(self.frame_11)
        self.btn_excluir_atletas.setObjectName(u"btn_excluir_atletas")

        self.verticalLayout_15.addWidget(self.btn_excluir_atletas)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_11)


        self.horizontalLayout_9.addWidget(self.frame_11)


        self.verticalLayout_16.addLayout(self.horizontalLayout_9)

        self.tabWidget.addTab(self.cad_atletas, "")
        self.cad_gp_atletas = QWidget()
        self.cad_gp_atletas.setObjectName(u"cad_gp_atletas")
        self.verticalLayout_8 = QVBoxLayout(self.cad_gp_atletas)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tbl_gp_atletas = QTreeWidget(self.cad_gp_atletas)
        self.tbl_gp_atletas.setObjectName(u"tbl_gp_atletas")

        self.horizontalLayout_6.addWidget(self.tbl_gp_atletas)

        self.frame_7 = QFrame(self.cad_gp_atletas)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_incluir_gp_atletas = QPushButton(self.frame_7)
        self.btn_incluir_gp_atletas.setObjectName(u"btn_incluir_gp_atletas")

        self.verticalLayout_7.addWidget(self.btn_incluir_gp_atletas)

        self.btn_alterar_gp_atletas = QPushButton(self.frame_7)
        self.btn_alterar_gp_atletas.setObjectName(u"btn_alterar_gp_atletas")

        self.verticalLayout_7.addWidget(self.btn_alterar_gp_atletas)

        self.btn_excluir_gp_atletas = QPushButton(self.frame_7)
        self.btn_excluir_gp_atletas.setObjectName(u"btn_excluir_gp_atletas")

        self.verticalLayout_7.addWidget(self.btn_excluir_gp_atletas)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)


        self.horizontalLayout_6.addWidget(self.frame_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.tabWidget.addTab(self.cad_gp_atletas, "")
        self.cad_tp_dispensa = QWidget()
        self.cad_tp_dispensa.setObjectName(u"cad_tp_dispensa")
        self.verticalLayout_10 = QVBoxLayout(self.cad_tp_dispensa)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tbl_tp_dispensa = QTreeWidget(self.cad_tp_dispensa)
        self.tbl_tp_dispensa.setObjectName(u"tbl_tp_dispensa")

        self.horizontalLayout_7.addWidget(self.tbl_tp_dispensa)

        self.frame_8 = QFrame(self.cad_tp_dispensa)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_incluir_tp_dispensa = QPushButton(self.frame_8)
        self.btn_incluir_tp_dispensa.setObjectName(u"btn_incluir_tp_dispensa")

        self.verticalLayout_9.addWidget(self.btn_incluir_tp_dispensa)

        self.btn_alterar_tp_dispensa = QPushButton(self.frame_8)
        self.btn_alterar_tp_dispensa.setObjectName(u"btn_alterar_tp_dispensa")

        self.verticalLayout_9.addWidget(self.btn_alterar_tp_dispensa)

        self.btn_excluir_tp_dispensa = QPushButton(self.frame_8)
        self.btn_excluir_tp_dispensa.setObjectName(u"btn_excluir_tp_dispensa")

        self.verticalLayout_9.addWidget(self.btn_excluir_tp_dispensa)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_8)


        self.horizontalLayout_7.addWidget(self.frame_8)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.tabWidget.addTab(self.cad_tp_dispensa, "")
        self.cad_tp_treino = QWidget()
        self.cad_tp_treino.setObjectName(u"cad_tp_treino")
        self.verticalLayout_11 = QVBoxLayout(self.cad_tp_treino)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tbl_tp_treino = QTreeWidget(self.cad_tp_treino)
        self.tbl_tp_treino.setObjectName(u"tbl_tp_treino")

        self.horizontalLayout_5.addWidget(self.tbl_tp_treino)

        self.frame_6 = QFrame(self.cad_tp_treino)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_incluir_tp_treino = QPushButton(self.frame_6)
        self.btn_incluir_tp_treino.setObjectName(u"btn_incluir_tp_treino")

        self.verticalLayout_6.addWidget(self.btn_incluir_tp_treino)

        self.btn_alterar_tp_treino = QPushButton(self.frame_6)
        self.btn_alterar_tp_treino.setObjectName(u"btn_alterar_tp_treino")

        self.verticalLayout_6.addWidget(self.btn_alterar_tp_treino)

        self.btn_excluir_tp_treino = QPushButton(self.frame_6)
        self.btn_excluir_tp_treino.setObjectName(u"btn_excluir_tp_treino")

        self.verticalLayout_6.addWidget(self.btn_excluir_tp_treino)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)


        self.horizontalLayout_5.addWidget(self.frame_6)


        self.verticalLayout_11.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.cad_tp_treino, "")
        self.cad_treinadores = QWidget()
        self.cad_treinadores.setObjectName(u"cad_treinadores")
        self.verticalLayout_14 = QVBoxLayout(self.cad_treinadores)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tbl_treinadores = QTreeWidget(self.cad_treinadores)
        self.tbl_treinadores.setObjectName(u"tbl_treinadores")

        self.horizontalLayout_8.addWidget(self.tbl_treinadores)

        self.frame_10 = QFrame(self.cad_treinadores)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.btn_incluir_treinadores = QPushButton(self.frame_10)
        self.btn_incluir_treinadores.setObjectName(u"btn_incluir_treinadores")

        self.verticalLayout_13.addWidget(self.btn_incluir_treinadores)

        self.btn_alterar_treinadores = QPushButton(self.frame_10)
        self.btn_alterar_treinadores.setObjectName(u"btn_alterar_treinadores")

        self.verticalLayout_13.addWidget(self.btn_alterar_treinadores)

        self.btn_excluir_treinadores = QPushButton(self.frame_10)
        self.btn_excluir_treinadores.setObjectName(u"btn_excluir_treinadores")

        self.verticalLayout_13.addWidget(self.btn_excluir_treinadores)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_10)


        self.horizontalLayout_8.addWidget(self.frame_10)


        self.verticalLayout_14.addLayout(self.horizontalLayout_8)

        self.tabWidget.addTab(self.cad_treinadores, "")
        self.cad_usuarios = QWidget()
        self.cad_usuarios.setObjectName(u"cad_usuarios")
        self.verticalLayout_4 = QVBoxLayout(self.cad_usuarios)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tbl_usuarios = QTreeWidget(self.cad_usuarios)
        self.tbl_usuarios.setObjectName(u"tbl_usuarios")

        self.horizontalLayout_4.addWidget(self.tbl_usuarios)

        self.frame_9 = QFrame(self.cad_usuarios)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.btn_incluir_usuarios = QPushButton(self.frame_9)
        self.btn_incluir_usuarios.setObjectName(u"btn_incluir_usuarios")

        self.verticalLayout_12.addWidget(self.btn_incluir_usuarios)

        self.btn_alterar_usuarios = QPushButton(self.frame_9)
        self.btn_alterar_usuarios.setObjectName(u"btn_alterar_usuarios")

        self.verticalLayout_12.addWidget(self.btn_alterar_usuarios)

        self.btn_excluir_usuarios = QPushButton(self.frame_9)
        self.btn_excluir_usuarios.setObjectName(u"btn_excluir_usuarios")

        self.verticalLayout_12.addWidget(self.btn_excluir_usuarios)

        self.btn_trocar_senha_usuarios = QPushButton(self.frame_9)
        self.btn_trocar_senha_usuarios.setObjectName(u"btn_trocar_senha_usuarios")

        self.verticalLayout_12.addWidget(self.btn_trocar_senha_usuarios)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_9)


        self.horizontalLayout_4.addWidget(self.frame_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.cad_usuarios, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        self.pages.addWidget(self.pg_cadastro)
        self.pg_cad_usuario = QWidget()
        self.pg_cad_usuario.setObjectName(u"pg_cad_usuario")
        self.verticalLayout_18 = QVBoxLayout(self.pg_cad_usuario)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_3 = QLabel(self.pg_cad_usuario)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        self.label_3.setFont(font1)

        self.verticalLayout_17.addWidget(self.label_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_4 = QLabel(self.pg_cad_usuario)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_4.setFont(font2)

        self.horizontalLayout_10.addWidget(self.label_4)

        self.txt_nome_usuario = QLineEdit(self.pg_cad_usuario)
        self.txt_nome_usuario.setObjectName(u"txt_nome_usuario")
        self.txt_nome_usuario.setFont(font1)
        self.txt_nome_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.txt_nome_usuario)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)


        self.verticalLayout_17.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_14)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.pg_cad_usuario)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setFont(font2)

        self.horizontalLayout_11.addWidget(self.label_5)

        self.txt_email_usuario = QLineEdit(self.pg_cad_usuario)
        self.txt_email_usuario.setObjectName(u"txt_email_usuario")
        self.txt_email_usuario.setFont(font1)
        self.txt_email_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.txt_email_usuario)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)


        self.verticalLayout_17.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_15)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_8 = QLabel(self.pg_cad_usuario)
        self.label_8.setObjectName(u"label_8")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_8.setFont(font3)

        self.horizontalLayout_12.addWidget(self.label_8)

        self.box_tp_usuario = QComboBox(self.pg_cad_usuario)
        self.box_tp_usuario.addItem("")
        self.box_tp_usuario.addItem("")
        self.box_tp_usuario.addItem("")
        self.box_tp_usuario.setObjectName(u"box_tp_usuario")
        font4 = QFont()
        font4.setPointSize(10)
        self.box_tp_usuario.setFont(font4)
        self.box_tp_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.box_tp_usuario)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)


        self.verticalLayout_17.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_16)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_6 = QLabel(self.pg_cad_usuario)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setFont(font2)

        self.horizontalLayout_13.addWidget(self.label_6)

        self.txt_senha_usuario = QLineEdit(self.pg_cad_usuario)
        self.txt_senha_usuario.setObjectName(u"txt_senha_usuario")
        self.txt_senha_usuario.setFont(font1)
        self.txt_senha_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.txt_senha_usuario)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_7)


        self.verticalLayout_17.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_17 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_17)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_7 = QLabel(self.pg_cad_usuario)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setFont(font2)

        self.horizontalLayout_14.addWidget(self.label_7)

        self.txt_confirma_senha_usuario = QLineEdit(self.pg_cad_usuario)
        self.txt_confirma_senha_usuario.setObjectName(u"txt_confirma_senha_usuario")
        self.txt_confirma_senha_usuario.setFont(font1)
        self.txt_confirma_senha_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_14.addWidget(self.txt_confirma_senha_usuario)

        self.horizontalSpacer_8 = QSpacerItem(300, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_8)


        self.verticalLayout_17.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_13)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_20)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_19)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_18)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_12)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_3)

        self.btn_salvar_usuario = QPushButton(self.pg_cad_usuario)
        self.btn_salvar_usuario.setObjectName(u"btn_salvar_usuario")
        self.btn_salvar_usuario.setFont(font4)

        self.horizontalLayout_15.addWidget(self.btn_salvar_usuario)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_4)


        self.verticalLayout_17.addLayout(self.horizontalLayout_15)


        self.verticalLayout_18.addLayout(self.verticalLayout_17)

        self.pages.addWidget(self.pg_cad_usuario)

        self.verticalLayout_2.addWidget(self.pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_cadastro.setText(QCoreApplication.translate("MainWindow", u"CADASTRO", None))
        self.btn_registro.setText(QCoreApplication.translate("MainWindow", u"REGISTRO", None))
        self.btn_relatorios.setText(QCoreApplication.translate("MainWindow", u"RELAT\u00d3RIOS", None))
        self.btn_conta.setText(QCoreApplication.translate("MainWindow", u"CONTA", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:700;\">Gerenciador de Treinos</span></p></body></html>", None))
        ___qtreewidgetitem = self.tbl_atletas.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Grupo", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Data nascimento", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Nome", None));
        self.btn_incluir_atletas.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_alterar_atletas.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_atletas.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cad_atletas), QCoreApplication.translate("MainWindow", u"Atletas", None))
        ___qtreewidgetitem1 = self.tbl_gp_atletas.headerItem()
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Nome", None));
        self.btn_incluir_gp_atletas.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_alterar_gp_atletas.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_gp_atletas.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cad_gp_atletas), QCoreApplication.translate("MainWindow", u"Grupos Atletas", None))
        ___qtreewidgetitem2 = self.tbl_tp_dispensa.headerItem()
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Nome", None));
        self.btn_incluir_tp_dispensa.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_alterar_tp_dispensa.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_tp_dispensa.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cad_tp_dispensa), QCoreApplication.translate("MainWindow", u"Tipos Dispensa", None))
        ___qtreewidgetitem3 = self.tbl_tp_treino.headerItem()
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Nome", None));
        self.btn_incluir_tp_treino.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_alterar_tp_treino.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_tp_treino.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cad_tp_treino), QCoreApplication.translate("MainWindow", u"Tipos Treino", None))
        ___qtreewidgetitem4 = self.tbl_treinadores.headerItem()
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"Nome", None));
        self.btn_incluir_treinadores.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_alterar_treinadores.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_treinadores.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cad_treinadores), QCoreApplication.translate("MainWindow", u"Treinadores", None))
        ___qtreewidgetitem5 = self.tbl_usuarios.headerItem()
        ___qtreewidgetitem5.setText(2, QCoreApplication.translate("MainWindow", u"e-mail", None));
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"Nome", None));
        self.btn_incluir_usuarios.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_alterar_usuarios.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_usuarios.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_trocar_senha_usuarios.setText(QCoreApplication.translate("MainWindow", u"Trocar senha", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cad_usuarios), QCoreApplication.translate("MainWindow", u"Usu\u00e1rios", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">Cadastro de usu\u00e1rio</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nome: ", None))
        self.txt_nome_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o nome de usu\u00e1rio", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"e-mail: ", None))
        self.txt_email_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o e-mail de restaura\u00e7\u00e3o de senha", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Perfil: ", None))
        self.box_tp_usuario.setItemText(0, QCoreApplication.translate("MainWindow", u"Gerenciador", None))
        self.box_tp_usuario.setItemText(1, QCoreApplication.translate("MainWindow", u"Registrador", None))
        self.box_tp_usuario.setItemText(2, QCoreApplication.translate("MainWindow", u"Leitor", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Senha: ", None))
        self.txt_senha_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite a senha de acesso", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Senha: ", None))
        self.txt_confirma_senha_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Repita a senha de acesso", None))
        self.btn_salvar_usuario.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
    # retranslateUi

