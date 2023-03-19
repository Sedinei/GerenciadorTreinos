# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'get_path.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
from  . import resources_rc

class Ui_get_path(object):
    def setupUi(self, get_path):
        if not get_path.objectName():
            get_path.setObjectName(u"get_path")
        get_path.resize(650, 150)
        get_path.setMinimumSize(QSize(650, 150))
        get_path.setMaximumSize(QSize(650, 150))
        icon = QIcon()
        icon.addFile(u":/images/cronometro.ico", QSize(), QIcon.Normal, QIcon.Off)
        get_path.setWindowIcon(icon)
        get_path.setStyleSheet(u"background-color: rgb(255, 203, 70);")
        self.verticalLayout = QVBoxLayout(get_path)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(get_path)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.pasta = QLineEdit(self.frame)
        self.pasta.setObjectName(u"pasta")
        self.pasta.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pasta)

        self.btn_procurar = QPushButton(self.frame)
        self.btn_procurar.setObjectName(u"btn_procurar")
        self.btn_procurar.setStyleSheet(u"background-color: rgb(218, 218, 218);")

        self.horizontalLayout.addWidget(self.btn_procurar)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(get_path)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.resposta = QLabel(self.frame_2)
        self.resposta.setObjectName(u"resposta")

        self.horizontalLayout_2.addWidget(self.resposta)

        self.btn_cancelar = QPushButton(self.frame_2)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setStyleSheet(u"background-color: rgb(218, 218, 218);")

        self.horizontalLayout_2.addWidget(self.btn_cancelar)

        self.btn_OK = QPushButton(self.frame_2)
        self.btn_OK.setObjectName(u"btn_OK")
        self.btn_OK.setStyleSheet(u"background-color: rgb(218, 218, 218);")

        self.horizontalLayout_2.addWidget(self.btn_OK)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(get_path)

        QMetaObject.connectSlotsByName(get_path)
    # setupUi

    def retranslateUi(self, get_path):
        get_path.setWindowTitle(QCoreApplication.translate("get_path", u"Pasta de trabalho", None))
        self.label.setText(QCoreApplication.translate("get_path", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Informe a pasta de trabalho: </span></p></body></html>", None))
        self.btn_procurar.setText(QCoreApplication.translate("get_path", u"Procurar...", None))
        self.resposta.setText("")
        self.btn_cancelar.setText(QCoreApplication.translate("get_path", u"Cancelar", None))
        self.btn_OK.setText(QCoreApplication.translate("get_path", u"OK", None))
    # retranslateUi

