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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTextEdit,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
from  . import resources_rc
from  . import resources_rc
from  . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(863, 533)
        icon = QIcon()
        icon.addFile(u":/images/cronometro.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        self.qtab_cadastro = QTabWidget(self.pg_cadastro)
        self.qtab_cadastro.setObjectName(u"qtab_cadastro")
        font1 = QFont()
        font1.setPointSize(10)
        self.qtab_cadastro.setFont(font1)
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
        self.btn_incluir_atleta = QPushButton(self.frame_11)
        self.btn_incluir_atleta.setObjectName(u"btn_incluir_atleta")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_incluir_atleta.sizePolicy().hasHeightForWidth())
        self.btn_incluir_atleta.setSizePolicy(sizePolicy)
        self.btn_incluir_atleta.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_incluir_atleta.setStyleSheet(u"")

        self.verticalLayout_15.addWidget(self.btn_incluir_atleta)

        self.btn_alterar_atleta = QPushButton(self.frame_11)
        self.btn_alterar_atleta.setObjectName(u"btn_alterar_atleta")
        sizePolicy.setHeightForWidth(self.btn_alterar_atleta.sizePolicy().hasHeightForWidth())
        self.btn_alterar_atleta.setSizePolicy(sizePolicy)
        self.btn_alterar_atleta.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_atleta.setStyleSheet(u"")

        self.verticalLayout_15.addWidget(self.btn_alterar_atleta)

        self.btn_excluir_atletas = QPushButton(self.frame_11)
        self.btn_excluir_atletas.setObjectName(u"btn_excluir_atletas")
        sizePolicy.setHeightForWidth(self.btn_excluir_atletas.sizePolicy().hasHeightForWidth())
        self.btn_excluir_atletas.setSizePolicy(sizePolicy)
        self.btn_excluir_atletas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_atletas.setStyleSheet(u"")

        self.verticalLayout_15.addWidget(self.btn_excluir_atletas)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_11)


        self.horizontalLayout_9.addWidget(self.frame_11)


        self.verticalLayout_16.addLayout(self.horizontalLayout_9)

        self.qtab_cadastro.addTab(self.cad_atletas, "")
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
        sizePolicy.setHeightForWidth(self.btn_incluir_gp_atletas.sizePolicy().hasHeightForWidth())
        self.btn_incluir_gp_atletas.setSizePolicy(sizePolicy)
        self.btn_incluir_gp_atletas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_incluir_gp_atletas.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.btn_incluir_gp_atletas)

        self.btn_alterar_gp_atletas = QPushButton(self.frame_7)
        self.btn_alterar_gp_atletas.setObjectName(u"btn_alterar_gp_atletas")
        sizePolicy.setHeightForWidth(self.btn_alterar_gp_atletas.sizePolicy().hasHeightForWidth())
        self.btn_alterar_gp_atletas.setSizePolicy(sizePolicy)
        self.btn_alterar_gp_atletas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_gp_atletas.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.btn_alterar_gp_atletas)

        self.btn_excluir_gp_atletas = QPushButton(self.frame_7)
        self.btn_excluir_gp_atletas.setObjectName(u"btn_excluir_gp_atletas")
        sizePolicy.setHeightForWidth(self.btn_excluir_gp_atletas.sizePolicy().hasHeightForWidth())
        self.btn_excluir_gp_atletas.setSizePolicy(sizePolicy)
        self.btn_excluir_gp_atletas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_gp_atletas.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.btn_excluir_gp_atletas)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)


        self.horizontalLayout_6.addWidget(self.frame_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.qtab_cadastro.addTab(self.cad_gp_atletas, "")
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
        sizePolicy.setHeightForWidth(self.btn_incluir_tp_dispensa.sizePolicy().hasHeightForWidth())
        self.btn_incluir_tp_dispensa.setSizePolicy(sizePolicy)
        self.btn_incluir_tp_dispensa.setMinimumSize(QSize(0, 0))
        self.btn_incluir_tp_dispensa.setFont(font1)
        self.btn_incluir_tp_dispensa.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_incluir_tp_dispensa.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.btn_incluir_tp_dispensa)

        self.btn_alterar_tp_dispensa = QPushButton(self.frame_8)
        self.btn_alterar_tp_dispensa.setObjectName(u"btn_alterar_tp_dispensa")
        sizePolicy.setHeightForWidth(self.btn_alterar_tp_dispensa.sizePolicy().hasHeightForWidth())
        self.btn_alterar_tp_dispensa.setSizePolicy(sizePolicy)
        self.btn_alterar_tp_dispensa.setMinimumSize(QSize(0, 0))
        self.btn_alterar_tp_dispensa.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_tp_dispensa.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.btn_alterar_tp_dispensa)

        self.btn_excluir_tp_dispensa = QPushButton(self.frame_8)
        self.btn_excluir_tp_dispensa.setObjectName(u"btn_excluir_tp_dispensa")
        sizePolicy.setHeightForWidth(self.btn_excluir_tp_dispensa.sizePolicy().hasHeightForWidth())
        self.btn_excluir_tp_dispensa.setSizePolicy(sizePolicy)
        self.btn_excluir_tp_dispensa.setMinimumSize(QSize(0, 0))
        self.btn_excluir_tp_dispensa.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_tp_dispensa.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.btn_excluir_tp_dispensa)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_8)


        self.horizontalLayout_7.addWidget(self.frame_8)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.qtab_cadastro.addTab(self.cad_tp_dispensa, "")
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
        sizePolicy.setHeightForWidth(self.btn_incluir_tp_treino.sizePolicy().hasHeightForWidth())
        self.btn_incluir_tp_treino.setSizePolicy(sizePolicy)
        self.btn_incluir_tp_treino.setMinimumSize(QSize(0, 0))
        self.btn_incluir_tp_treino.setFont(font1)
        self.btn_incluir_tp_treino.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_incluir_tp_treino.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.btn_incluir_tp_treino)

        self.btn_alterar_tp_treino = QPushButton(self.frame_6)
        self.btn_alterar_tp_treino.setObjectName(u"btn_alterar_tp_treino")
        sizePolicy.setHeightForWidth(self.btn_alterar_tp_treino.sizePolicy().hasHeightForWidth())
        self.btn_alterar_tp_treino.setSizePolicy(sizePolicy)
        self.btn_alterar_tp_treino.setMinimumSize(QSize(0, 0))
        self.btn_alterar_tp_treino.setFont(font1)
        self.btn_alterar_tp_treino.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_tp_treino.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.btn_alterar_tp_treino)

        self.btn_excluir_tp_treino = QPushButton(self.frame_6)
        self.btn_excluir_tp_treino.setObjectName(u"btn_excluir_tp_treino")
        sizePolicy.setHeightForWidth(self.btn_excluir_tp_treino.sizePolicy().hasHeightForWidth())
        self.btn_excluir_tp_treino.setSizePolicy(sizePolicy)
        self.btn_excluir_tp_treino.setMinimumSize(QSize(0, 0))
        self.btn_excluir_tp_treino.setFont(font1)
        self.btn_excluir_tp_treino.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_tp_treino.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.btn_excluir_tp_treino)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)


        self.horizontalLayout_5.addWidget(self.frame_6)


        self.verticalLayout_11.addLayout(self.horizontalLayout_5)

        self.qtab_cadastro.addTab(self.cad_tp_treino, "")
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
        self.btn_incluir_treinador = QPushButton(self.frame_10)
        self.btn_incluir_treinador.setObjectName(u"btn_incluir_treinador")
        sizePolicy.setHeightForWidth(self.btn_incluir_treinador.sizePolicy().hasHeightForWidth())
        self.btn_incluir_treinador.setSizePolicy(sizePolicy)
        self.btn_incluir_treinador.setMinimumSize(QSize(0, 0))
        self.btn_incluir_treinador.setFont(font1)
        self.btn_incluir_treinador.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_incluir_treinador.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.btn_incluir_treinador)

        self.btn_alterar_treinador = QPushButton(self.frame_10)
        self.btn_alterar_treinador.setObjectName(u"btn_alterar_treinador")
        sizePolicy.setHeightForWidth(self.btn_alterar_treinador.sizePolicy().hasHeightForWidth())
        self.btn_alterar_treinador.setSizePolicy(sizePolicy)
        self.btn_alterar_treinador.setMinimumSize(QSize(0, 0))
        self.btn_alterar_treinador.setFont(font1)
        self.btn_alterar_treinador.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_treinador.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.btn_alterar_treinador)

        self.btn_excluir_treinadores = QPushButton(self.frame_10)
        self.btn_excluir_treinadores.setObjectName(u"btn_excluir_treinadores")
        sizePolicy.setHeightForWidth(self.btn_excluir_treinadores.sizePolicy().hasHeightForWidth())
        self.btn_excluir_treinadores.setSizePolicy(sizePolicy)
        self.btn_excluir_treinadores.setMinimumSize(QSize(0, 0))
        self.btn_excluir_treinadores.setFont(font1)
        self.btn_excluir_treinadores.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_treinadores.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.btn_excluir_treinadores)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_10)


        self.horizontalLayout_8.addWidget(self.frame_10)


        self.verticalLayout_14.addLayout(self.horizontalLayout_8)

        self.qtab_cadastro.addTab(self.cad_treinadores, "")
        self.cad_usuarios = QWidget()
        self.cad_usuarios.setObjectName(u"cad_usuarios")
        self.verticalLayout_4 = QVBoxLayout(self.cad_usuarios)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tbl_usuarios = QTreeWidget(self.cad_usuarios)
        self.tbl_usuarios.setObjectName(u"tbl_usuarios")
        self.tbl_usuarios.setAlternatingRowColors(False)
        self.tbl_usuarios.setSelectionMode(QAbstractItemView.NoSelection)

        self.horizontalLayout_4.addWidget(self.tbl_usuarios)

        self.frame_9 = QFrame(self.cad_usuarios)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.btn_incluir_usuario = QPushButton(self.frame_9)
        self.btn_incluir_usuario.setObjectName(u"btn_incluir_usuario")
        sizePolicy.setHeightForWidth(self.btn_incluir_usuario.sizePolicy().hasHeightForWidth())
        self.btn_incluir_usuario.setSizePolicy(sizePolicy)
        self.btn_incluir_usuario.setMinimumSize(QSize(0, 0))
        self.btn_incluir_usuario.setFont(font1)
        self.btn_incluir_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_incluir_usuario.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.btn_incluir_usuario)

        self.btn_alterar_usuario = QPushButton(self.frame_9)
        self.btn_alterar_usuario.setObjectName(u"btn_alterar_usuario")
        sizePolicy.setHeightForWidth(self.btn_alterar_usuario.sizePolicy().hasHeightForWidth())
        self.btn_alterar_usuario.setSizePolicy(sizePolicy)
        self.btn_alterar_usuario.setMinimumSize(QSize(0, 0))
        self.btn_alterar_usuario.setFont(font1)
        self.btn_alterar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_usuario.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.btn_alterar_usuario)

        self.btn_excluir_usuarios = QPushButton(self.frame_9)
        self.btn_excluir_usuarios.setObjectName(u"btn_excluir_usuarios")
        sizePolicy.setHeightForWidth(self.btn_excluir_usuarios.sizePolicy().hasHeightForWidth())
        self.btn_excluir_usuarios.setSizePolicy(sizePolicy)
        self.btn_excluir_usuarios.setMinimumSize(QSize(0, 0))
        self.btn_excluir_usuarios.setFont(font1)
        self.btn_excluir_usuarios.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_usuarios.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.btn_excluir_usuarios)

        self.btn_trocar_senha_usuario = QPushButton(self.frame_9)
        self.btn_trocar_senha_usuario.setObjectName(u"btn_trocar_senha_usuario")
        sizePolicy.setHeightForWidth(self.btn_trocar_senha_usuario.sizePolicy().hasHeightForWidth())
        self.btn_trocar_senha_usuario.setSizePolicy(sizePolicy)
        self.btn_trocar_senha_usuario.setMinimumSize(QSize(0, 0))
        self.btn_trocar_senha_usuario.setFont(font1)
        self.btn_trocar_senha_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_trocar_senha_usuario.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.btn_trocar_senha_usuario)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_9)


        self.horizontalLayout_4.addWidget(self.frame_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.qtab_cadastro.addTab(self.cad_usuarios, "")

        self.verticalLayout_5.addWidget(self.qtab_cadastro)

        self.pages.addWidget(self.pg_cadastro)
        self.pg_cad_alt_usuario = QWidget()
        self.pg_cad_alt_usuario.setObjectName(u"pg_cad_alt_usuario")
        self.verticalLayout_17 = QVBoxLayout(self.pg_cad_alt_usuario)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalSpacer_32 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_32)

        self.lbl_titulo_pg_cad_alt_usuario = QLabel(self.pg_cad_alt_usuario)
        self.lbl_titulo_pg_cad_alt_usuario.setObjectName(u"lbl_titulo_pg_cad_alt_usuario")
        self.lbl_titulo_pg_cad_alt_usuario.setFont(font1)

        self.verticalLayout_17.addWidget(self.lbl_titulo_pg_cad_alt_usuario)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)

        self.label_4 = QLabel(self.pg_cad_alt_usuario)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_4.setFont(font2)

        self.horizontalLayout_10.addWidget(self.label_4)

        self.txt_nome_usuario = QLineEdit(self.pg_cad_alt_usuario)
        self.txt_nome_usuario.setObjectName(u"txt_nome_usuario")
        self.txt_nome_usuario.setFont(font1)
        self.txt_nome_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_nome_usuario.setInputMethodHints(Qt.ImhLatinOnly|Qt.ImhLowercaseOnly)

        self.horizontalLayout_10.addWidget(self.txt_nome_usuario)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)


        self.verticalLayout_17.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_14 = QSpacerItem(822, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_14)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)

        self.label_5 = QLabel(self.pg_cad_alt_usuario)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setFont(font2)

        self.horizontalLayout_11.addWidget(self.label_5)

        self.txt_email_usuario = QLineEdit(self.pg_cad_alt_usuario)
        self.txt_email_usuario.setObjectName(u"txt_email_usuario")
        self.txt_email_usuario.setFont(font1)
        self.txt_email_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_email_usuario.setInputMethodHints(Qt.ImhEmailCharactersOnly)

        self.horizontalLayout_11.addWidget(self.txt_email_usuario)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)


        self.verticalLayout_17.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_15 = QSpacerItem(822, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_15)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)

        self.label_8 = QLabel(self.pg_cad_alt_usuario)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.horizontalLayout_12.addWidget(self.label_8)

        self.box_tp_usuario = QComboBox(self.pg_cad_alt_usuario)
        self.box_tp_usuario.setObjectName(u"box_tp_usuario")
        self.box_tp_usuario.setFont(font1)
        self.box_tp_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.box_tp_usuario)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)


        self.verticalLayout_17.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_16 = QSpacerItem(822, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_16)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)

        self.label_6 = QLabel(self.pg_cad_alt_usuario)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setFont(font2)

        self.horizontalLayout_13.addWidget(self.label_6)

        self.txt_senha_usuario = QLineEdit(self.pg_cad_alt_usuario)
        self.txt_senha_usuario.setObjectName(u"txt_senha_usuario")
        self.txt_senha_usuario.setFont(font1)
        self.txt_senha_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_senha_usuario.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_13.addWidget(self.txt_senha_usuario)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_7)


        self.verticalLayout_17.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_17 = QSpacerItem(822, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_17)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_14)

        self.label_7 = QLabel(self.pg_cad_alt_usuario)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setFont(font2)

        self.horizontalLayout_14.addWidget(self.label_7)

        self.txt_confirma_senha_usuario = QLineEdit(self.pg_cad_alt_usuario)
        self.txt_confirma_senha_usuario.setObjectName(u"txt_confirma_senha_usuario")
        self.txt_confirma_senha_usuario.setFont(font1)
        self.txt_confirma_senha_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_confirma_senha_usuario.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_14.addWidget(self.txt_confirma_senha_usuario)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_8)


        self.verticalLayout_17.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_13)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_3)

        self.btn_salvar_fechar_users = QPushButton(self.pg_cad_alt_usuario)
        self.btn_salvar_fechar_users.setObjectName(u"btn_salvar_fechar_users")
        self.btn_salvar_fechar_users.setFont(font1)
        self.btn_salvar_fechar_users.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.btn_salvar_fechar_users)

        self.btn_salvar_manter_users = QPushButton(self.pg_cad_alt_usuario)
        self.btn_salvar_manter_users.setObjectName(u"btn_salvar_manter_users")

        self.horizontalLayout_15.addWidget(self.btn_salvar_manter_users)

        self.btn_voltar_users = QPushButton(self.pg_cad_alt_usuario)
        self.btn_voltar_users.setObjectName(u"btn_voltar_users")

        self.horizontalLayout_15.addWidget(self.btn_voltar_users)


        self.verticalLayout_17.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_35 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_35)

        self.pages.addWidget(self.pg_cad_alt_usuario)
        self.pg_alt_senha_usuario = QWidget()
        self.pg_alt_senha_usuario.setObjectName(u"pg_alt_senha_usuario")
        self.verticalLayout_60 = QVBoxLayout(self.pg_alt_senha_usuario)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_59 = QVBoxLayout()
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_30)

        self.label_46 = QLabel(self.pg_alt_senha_usuario)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font1)

        self.verticalLayout_59.addWidget(self.label_46)

        self.verticalSpacer_79 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_79)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalSpacer_67 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_67)

        self.label_47 = QLabel(self.pg_alt_senha_usuario)
        self.label_47.setObjectName(u"label_47")
        sizePolicy.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy)
        self.label_47.setFont(font2)

        self.horizontalLayout_56.addWidget(self.label_47)

        self.txt_nome_usuario_nova_senha = QLineEdit(self.pg_alt_senha_usuario)
        self.txt_nome_usuario_nova_senha.setObjectName(u"txt_nome_usuario_nova_senha")
        self.txt_nome_usuario_nova_senha.setEnabled(False)
        self.txt_nome_usuario_nova_senha.setFont(font1)
        self.txt_nome_usuario_nova_senha.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_nome_usuario_nova_senha.setInputMethodHints(Qt.ImhLatinOnly|Qt.ImhLowercaseOnly)

        self.horizontalLayout_56.addWidget(self.txt_nome_usuario_nova_senha)

        self.horizontalSpacer_68 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_68)


        self.verticalLayout_59.addLayout(self.horizontalLayout_56)

        self.verticalSpacer_80 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_80)

        self.verticalSpacer_82 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_82)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalSpacer_73 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_73)

        self.label_50 = QLabel(self.pg_alt_senha_usuario)
        self.label_50.setObjectName(u"label_50")
        sizePolicy1.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy1)
        self.label_50.setFont(font2)

        self.horizontalLayout_59.addWidget(self.label_50)

        self.txt_nova_senha_usuario = QLineEdit(self.pg_alt_senha_usuario)
        self.txt_nova_senha_usuario.setObjectName(u"txt_nova_senha_usuario")
        self.txt_nova_senha_usuario.setFont(font1)
        self.txt_nova_senha_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_nova_senha_usuario.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_59.addWidget(self.txt_nova_senha_usuario)

        self.horizontalSpacer_74 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_74)


        self.verticalLayout_59.addLayout(self.horizontalLayout_59)

        self.verticalSpacer_83 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_83)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalSpacer_75 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_75)

        self.label_51 = QLabel(self.pg_alt_senha_usuario)
        self.label_51.setObjectName(u"label_51")
        sizePolicy1.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy1)
        self.label_51.setFont(font2)

        self.horizontalLayout_60.addWidget(self.label_51)

        self.txt_confirma_nova_senha_usuario = QLineEdit(self.pg_alt_senha_usuario)
        self.txt_confirma_nova_senha_usuario.setObjectName(u"txt_confirma_nova_senha_usuario")
        self.txt_confirma_nova_senha_usuario.setFont(font1)
        self.txt_confirma_nova_senha_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_confirma_nova_senha_usuario.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_60.addWidget(self.txt_confirma_nova_senha_usuario)

        self.horizontalSpacer_76 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_76)


        self.verticalLayout_59.addLayout(self.horizontalLayout_60)

        self.verticalSpacer_84 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_84)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalSpacer_77 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_77)

        self.btn_salvar_nova_senha_users = QPushButton(self.pg_alt_senha_usuario)
        self.btn_salvar_nova_senha_users.setObjectName(u"btn_salvar_nova_senha_users")
        self.btn_salvar_nova_senha_users.setFont(font1)
        self.btn_salvar_nova_senha_users.setStyleSheet(u"")

        self.horizontalLayout_61.addWidget(self.btn_salvar_nova_senha_users)

        self.btn_voltar_nova_senha_users = QPushButton(self.pg_alt_senha_usuario)
        self.btn_voltar_nova_senha_users.setObjectName(u"btn_voltar_nova_senha_users")

        self.horizontalLayout_61.addWidget(self.btn_voltar_nova_senha_users)


        self.verticalLayout_59.addLayout(self.horizontalLayout_61)

        self.verticalSpacer_85 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_85)

        self.verticalSpacer_86 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_86)

        self.verticalSpacer_87 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_87)


        self.verticalLayout_60.addLayout(self.verticalLayout_59)

        self.pages.addWidget(self.pg_alt_senha_usuario)
        self.pg_cad_alt_atleta = QWidget()
        self.pg_cad_alt_atleta.setObjectName(u"pg_cad_alt_atleta")
        self.verticalLayout_20 = QVBoxLayout(self.pg_cad_alt_atleta)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_29)

        self.lbl_titulo_pg_cad_alt_atleta = QLabel(self.pg_cad_alt_atleta)
        self.lbl_titulo_pg_cad_alt_atleta.setObjectName(u"lbl_titulo_pg_cad_alt_atleta")
        self.lbl_titulo_pg_cad_alt_atleta.setFont(font1)

        self.verticalLayout_19.addWidget(self.lbl_titulo_pg_cad_alt_atleta)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_20)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_15)

        self.label_13 = QLabel(self.pg_cad_alt_atleta)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setFont(font2)

        self.horizontalLayout_16.addWidget(self.label_13)

        self.txt_nome_atleta = QLineEdit(self.pg_cad_alt_atleta)
        self.txt_nome_atleta.setObjectName(u"txt_nome_atleta")
        self.txt_nome_atleta.setMinimumSize(QSize(450, 0))
        self.txt_nome_atleta.setFont(font1)
        self.txt_nome_atleta.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_nome_atleta.setInputMethodHints(Qt.ImhLatinOnly|Qt.ImhLowercaseOnly)

        self.horizontalLayout_16.addWidget(self.txt_nome_atleta)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_16)


        self.verticalLayout_19.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_21 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_21)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_17)

        self.label_14 = QLabel(self.pg_cad_alt_atleta)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setFont(font2)

        self.horizontalLayout_17.addWidget(self.label_14)

        self.dt_nascimento = QDateEdit(self.pg_cad_alt_atleta)
        self.dt_nascimento.setObjectName(u"dt_nascimento")

        self.horizontalLayout_17.addWidget(self.dt_nascimento)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_18)


        self.verticalLayout_19.addLayout(self.horizontalLayout_17)

        self.verticalSpacer_22 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_22)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_19)

        self.label_15 = QLabel(self.pg_cad_alt_atleta)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.horizontalLayout_18.addWidget(self.label_15)

        self.box_gp_atleta = QComboBox(self.pg_cad_alt_atleta)
        self.box_gp_atleta.setObjectName(u"box_gp_atleta")
        self.box_gp_atleta.setMinimumSize(QSize(300, 0))
        self.box_gp_atleta.setFont(font1)
        self.box_gp_atleta.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_18.addWidget(self.box_gp_atleta)

        self.btn_cad_alt_atleta_incluir_grupo = QPushButton(self.pg_cad_alt_atleta)
        self.btn_cad_alt_atleta_incluir_grupo.setObjectName(u"btn_cad_alt_atleta_incluir_grupo")

        self.horizontalLayout_18.addWidget(self.btn_cad_alt_atleta_incluir_grupo)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_20)


        self.verticalLayout_19.addLayout(self.horizontalLayout_18)

        self.verticalSpacer_23 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_23)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_21)

        self.label_16 = QLabel(self.pg_cad_alt_atleta)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setFont(font2)

        self.horizontalLayout_19.addWidget(self.label_16)

        self.dt_inicio = QDateEdit(self.pg_cad_alt_atleta)
        self.dt_inicio.setObjectName(u"dt_inicio")

        self.horizontalLayout_19.addWidget(self.dt_inicio)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_22)


        self.verticalLayout_19.addLayout(self.horizontalLayout_19)

        self.verticalSpacer_24 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_24)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_23)

        self.lbl_fim_vinculo = QLabel(self.pg_cad_alt_atleta)
        self.lbl_fim_vinculo.setObjectName(u"lbl_fim_vinculo")
        self.lbl_fim_vinculo.setFont(font2)

        self.horizontalLayout_20.addWidget(self.lbl_fim_vinculo)

        self.dt_fim = QDateEdit(self.pg_cad_alt_atleta)
        self.dt_fim.setObjectName(u"dt_fim")

        self.horizontalLayout_20.addWidget(self.dt_fim)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_24)


        self.verticalLayout_19.addLayout(self.horizontalLayout_20)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_25)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_25)

        self.btn_salvar_fechar_athletes = QPushButton(self.pg_cad_alt_atleta)
        self.btn_salvar_fechar_athletes.setObjectName(u"btn_salvar_fechar_athletes")
        self.btn_salvar_fechar_athletes.setFont(font1)
        self.btn_salvar_fechar_athletes.setStyleSheet(u"")

        self.horizontalLayout_21.addWidget(self.btn_salvar_fechar_athletes)

        self.btn_salvar_manter_athletes = QPushButton(self.pg_cad_alt_atleta)
        self.btn_salvar_manter_athletes.setObjectName(u"btn_salvar_manter_athletes")

        self.horizontalLayout_21.addWidget(self.btn_salvar_manter_athletes)

        self.btn_voltar_athletes = QPushButton(self.pg_cad_alt_atleta)
        self.btn_voltar_athletes.setObjectName(u"btn_voltar_athletes")

        self.horizontalLayout_21.addWidget(self.btn_voltar_athletes)


        self.verticalLayout_19.addLayout(self.horizontalLayout_21)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_26)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_27)

        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_28)


        self.verticalLayout_20.addLayout(self.verticalLayout_19)

        self.pages.addWidget(self.pg_cad_alt_atleta)
        self.pg_dominio = QWidget()
        self.pg_dominio.setObjectName(u"pg_dominio")
        self.verticalLayout_21 = QVBoxLayout(self.pg_dominio)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalSpacer_31 = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_31)

        self.lbl_titulo_pg_cad_alt_dominio = QLabel(self.pg_dominio)
        self.lbl_titulo_pg_cad_alt_dominio.setObjectName(u"lbl_titulo_pg_cad_alt_dominio")
        self.lbl_titulo_pg_cad_alt_dominio.setFont(font1)

        self.verticalLayout_21.addWidget(self.lbl_titulo_pg_cad_alt_dominio)

        self.verticalSpacer_19 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_19)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_19 = QLabel(self.pg_dominio)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setFont(font2)

        self.horizontalLayout_22.addWidget(self.label_19)

        self.txt_nome_dominio = QLineEdit(self.pg_dominio)
        self.txt_nome_dominio.setObjectName(u"txt_nome_dominio")
        self.txt_nome_dominio.setMinimumSize(QSize(450, 0))
        self.txt_nome_dominio.setFont(font1)
        self.txt_nome_dominio.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_nome_dominio.setInputMethodHints(Qt.ImhLatinOnly|Qt.ImhLowercaseOnly)

        self.horizontalLayout_22.addWidget(self.txt_nome_dominio)


        self.verticalLayout_21.addLayout(self.horizontalLayout_22)

        self.verticalSpacer_18 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_18)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_18 = QLabel(self.pg_dominio)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setFont(font2)

        self.verticalLayout_18.addWidget(self.label_18)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_12)


        self.horizontalLayout_23.addLayout(self.verticalLayout_18)

        self.txt_descricao_dominio = QTextEdit(self.pg_dominio)
        self.txt_descricao_dominio.setObjectName(u"txt_descricao_dominio")
        self.txt_descricao_dominio.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_23.addWidget(self.txt_descricao_dominio)


        self.verticalLayout_21.addLayout(self.horizontalLayout_23)

        self.verticalSpacer_33 = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_33)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_27)

        self.btn_salvar_manter_domains = QPushButton(self.pg_dominio)
        self.btn_salvar_manter_domains.setObjectName(u"btn_salvar_manter_domains")
        self.btn_salvar_manter_domains.setFont(font1)
        self.btn_salvar_manter_domains.setStyleSheet(u"")

        self.horizontalLayout_24.addWidget(self.btn_salvar_manter_domains)

        self.btn_salvar_fechar_domains = QPushButton(self.pg_dominio)
        self.btn_salvar_fechar_domains.setObjectName(u"btn_salvar_fechar_domains")

        self.horizontalLayout_24.addWidget(self.btn_salvar_fechar_domains)

        self.btn_voltar_domains = QPushButton(self.pg_dominio)
        self.btn_voltar_domains.setObjectName(u"btn_voltar_domains")

        self.horizontalLayout_24.addWidget(self.btn_voltar_domains)


        self.verticalLayout_21.addLayout(self.horizontalLayout_24)

        self.verticalSpacer_34 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_34)

        self.pages.addWidget(self.pg_dominio)
        self.pg_registro = QWidget()
        self.pg_registro.setObjectName(u"pg_registro")
        self.label_9 = QLabel(self.pg_registro)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(220, 130, 381, 81))
        self.pages.addWidget(self.pg_registro)
        self.pg_relatorios = QWidget()
        self.pg_relatorios.setObjectName(u"pg_relatorios")
        self.label_10 = QLabel(self.pg_relatorios)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(260, 170, 381, 81))
        self.pages.addWidget(self.pg_relatorios)
        self.pg_conta = QWidget()
        self.pg_conta.setObjectName(u"pg_conta")
        self.label_11 = QLabel(self.pg_conta)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(250, 170, 381, 81))
        self.pages.addWidget(self.pg_conta)

        self.verticalLayout_2.addWidget(self.pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(1)
        self.qtab_cadastro.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gerenciador de Treinos", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_cadastro.setText(QCoreApplication.translate("MainWindow", u"CADASTRO", None))
        self.btn_registro.setText(QCoreApplication.translate("MainWindow", u"REGISTRO", None))
        self.btn_relatorios.setText(QCoreApplication.translate("MainWindow", u"RELAT\u00d3RIOS", None))
        self.btn_conta.setText(QCoreApplication.translate("MainWindow", u"CONTA", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:700;\">Gerenciador de Treinos</span></p></body></html>", None))
        ___qtreewidgetitem = self.tbl_atletas.headerItem()
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Fim", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"In\u00edcio", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Grupo", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Data nascimento", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"id", None));
        self.btn_incluir_atleta.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_alterar_atleta.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_atletas.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.qtab_cadastro.setTabText(self.qtab_cadastro.indexOf(self.cad_atletas), QCoreApplication.translate("MainWindow", u"Atletas", None))
        ___qtreewidgetitem1 = self.tbl_gp_atletas.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"id", None));
        self.btn_incluir_gp_atletas.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_alterar_gp_atletas.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_gp_atletas.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.qtab_cadastro.setTabText(self.qtab_cadastro.indexOf(self.cad_gp_atletas), QCoreApplication.translate("MainWindow", u"Grupos Atletas", None))
        ___qtreewidgetitem2 = self.tbl_tp_dispensa.headerItem()
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"id", None));
        self.btn_incluir_tp_dispensa.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_alterar_tp_dispensa.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_tp_dispensa.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.qtab_cadastro.setTabText(self.qtab_cadastro.indexOf(self.cad_tp_dispensa), QCoreApplication.translate("MainWindow", u"Tipos Dispensa", None))
        ___qtreewidgetitem3 = self.tbl_tp_treino.headerItem()
        ___qtreewidgetitem3.setText(2, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"id", None));
        self.btn_incluir_tp_treino.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_alterar_tp_treino.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_tp_treino.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.qtab_cadastro.setTabText(self.qtab_cadastro.indexOf(self.cad_tp_treino), QCoreApplication.translate("MainWindow", u"Tipos Treino", None))
        ___qtreewidgetitem4 = self.tbl_treinadores.headerItem()
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"id", None));
        self.btn_incluir_treinador.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_alterar_treinador.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_treinadores.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.qtab_cadastro.setTabText(self.qtab_cadastro.indexOf(self.cad_treinadores), QCoreApplication.translate("MainWindow", u"Treinadores", None))
        ___qtreewidgetitem5 = self.tbl_usuarios.headerItem()
        ___qtreewidgetitem5.setText(3, QCoreApplication.translate("MainWindow", u"e-mail", None));
        ___qtreewidgetitem5.setText(2, QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"id", None));
        self.btn_incluir_usuario.setText(QCoreApplication.translate("MainWindow", u"Incluir", None))
        self.btn_alterar_usuario.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_usuarios.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_trocar_senha_usuario.setText(QCoreApplication.translate("MainWindow", u"Trocar senha", None))
        self.qtab_cadastro.setTabText(self.qtab_cadastro.indexOf(self.cad_usuarios), QCoreApplication.translate("MainWindow", u"Usu\u00e1rios", None))
        self.lbl_titulo_pg_cad_alt_usuario.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">T\u00edtulo Usu\u00e1rios</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nome: ", None))
        self.txt_nome_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o nome de usu\u00e1rio", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"e-mail: ", None))
        self.txt_email_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o e-mail de restaura\u00e7\u00e3o de senha", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Perfil: ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Senha: ", None))
        self.txt_senha_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite a senha de acesso", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Senha: ", None))
        self.txt_confirma_senha_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Repita a senha de acesso", None))
        self.btn_salvar_fechar_users.setText(QCoreApplication.translate("MainWindow", u"Salvar e fechar", None))
        self.btn_salvar_manter_users.setText(QCoreApplication.translate("MainWindow", u"Salvar e manter", None))
        self.btn_voltar_users.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">Alterar senha de usu\u00e1rio</span></p></body></html>", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Nome: ", None))
        self.txt_nome_usuario_nova_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o nome de usu\u00e1rio", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Senha: ", None))
        self.txt_nova_senha_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite a senha de acesso", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Senha: ", None))
        self.txt_confirma_nova_senha_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Repita a senha de acesso", None))
        self.btn_salvar_nova_senha_users.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_voltar_nova_senha_users.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.lbl_titulo_pg_cad_alt_atleta.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">T\u00edtulo Atletas</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Nome: ", None))
        self.txt_nome_atleta.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o nome do atleta", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Data de nascimento: ", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Grupo: ", None))
        self.btn_cad_alt_atleta_incluir_grupo.setText(QCoreApplication.translate("MainWindow", u"Incluir grupo", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Data de in\u00edcio de v\u00ednculo: ", None))
        self.lbl_fim_vinculo.setText(QCoreApplication.translate("MainWindow", u"Data de fim de v\u00ednculo: ", None))
        self.btn_salvar_fechar_athletes.setText(QCoreApplication.translate("MainWindow", u"Salvar e fechar", None))
        self.btn_salvar_manter_athletes.setText(QCoreApplication.translate("MainWindow", u"Salvar e manter", None))
        self.btn_voltar_athletes.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.lbl_titulo_pg_cad_alt_dominio.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">T\u00edtulo Dom\u00ednio</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Nome: ", None))
        self.txt_nome_dominio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o nome do dom\u00ednio", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o: ", None))
        self.txt_descricao_dominio.setPlaceholderText("")
        self.btn_salvar_manter_domains.setText(QCoreApplication.translate("MainWindow", u"Salvar e manter", None))
        self.btn_salvar_fechar_domains.setText(QCoreApplication.translate("MainWindow", u"Salvar e fechar", None))
        self.btn_voltar_domains.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">P\u00e1gina de registro</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">P\u00e1gina de relat\u00f3rios</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">P\u00e1gina da conta</span></p></body></html>", None))
    # retranslateUi

