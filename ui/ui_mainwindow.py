# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(287, 182)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.selectComPortComboBox = QComboBox(self.centralwidget)
        self.selectComPortComboBox.setObjectName(u"selectComPortComboBox")
        self.selectComPortComboBox.setGeometry(QRect(10, 10, 161, 21))
        self.comConnectButton = QPushButton(self.centralwidget)
        self.comConnectButton.setObjectName(u"ComConnectButton")
        self.comConnectButton.setGeometry(QRect(180, 10, 91, 23))
        self.ledButtonOn = QPushButton(self.centralwidget)
        self.ledButtonOn.setObjectName(u"ledButtonOn")
        self.ledButtonOn.setGeometry(QRect(10, 40, 121, 21))
        self.ledButtonOff = QPushButton(self.centralwidget)
        self.ledButtonOff.setObjectName(u"ledButtonOff")
        self.ledButtonOff.setGeometry(QRect(150, 40, 121, 21))
        self.sendTimeButton = QPushButton(self.centralwidget)
        self.sendTimeButton.setObjectName(u"sendTimeButton")
        self.sendTimeButton.setGeometry(QRect(170, 70, 101, 23))
        self.msInput = QLineEdit(self.centralwidget)
        self.msInput.setObjectName(u"msInput")
        self.msInput.setGeometry(QRect(10, 70, 151, 20))
        self.msInput.setInputMethodHints(Qt.ImhDigitsOnly)
        self.msInput.setMaxLength(10)
        self.ledStatusTextLabel = QLabel(self.centralwidget)
        self.ledStatusTextLabel.setObjectName(u"ledStatusTextLabel")
        self.ledStatusTextLabel.setGeometry(QRect(10, 110, 131, 21))
        self.ledStatusTextLabel.setFocusPolicy(Qt.NoFocus)
        self.ledStatusTextLabel.setToolTipDuration(0)
        self.timerStatusTextLabel = QLabel(self.centralwidget)
        self.timerStatusTextLabel.setObjectName(u"timerStatusTextLabel")
        self.timerStatusTextLabel.setGeometry(QRect(156, 110, 111, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 287, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.selectComPortComboBox.setCurrentText("")
        self.comConnectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.ledButtonOn.setText(QCoreApplication.translate("MainWindow", u"Led On", None))
        self.ledButtonOff.setText(QCoreApplication.translate("MainWindow", u"Led Off", None))
        self.sendTimeButton.setText(QCoreApplication.translate("MainWindow", u"Send Time", None))
        self.ledStatusTextLabel.setText("")
        self.timerStatusTextLabel.setText("")

    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(287, 266)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.selectComPortComboBox = QComboBox(self.centralwidget)
        self.selectComPortComboBox.setObjectName(u"selectComPortComboBox")
        self.selectComPortComboBox.setGeometry(QRect(10, 10, 161, 21))
        self.comConnectButton = QPushButton(self.centralwidget)
        self.comConnectButton.setObjectName(u"ComConnectButton")
        self.comConnectButton.setGeometry(QRect(180, 10, 91, 23))
        self.ledButtonOn = QPushButton(self.centralwidget)
        self.ledButtonOn.setObjectName(u"ledButtonOn")
        self.ledButtonOn.setGeometry(QRect(10, 40, 121, 21))
        self.ledButtonOff = QPushButton(self.centralwidget)
        self.ledButtonOff.setObjectName(u"ledButtonOff")
        self.ledButtonOff.setGeometry(QRect(150, 40, 121, 21))
        self.sendTimeButton = QPushButton(self.centralwidget)
        self.sendTimeButton.setObjectName(u"sendTimeButton")
        self.sendTimeButton.setGeometry(QRect(170, 70, 101, 23))
        self.msInput = QSpinBox(self.centralwidget)
        self.msInput.setObjectName(u"msInput")
        self.msInput.setGeometry(QRect(10, 70, 151, 20))
        self.msInput.setInputMethodHints(Qt.ImhDigitsOnly)
        self.msInput.setRange(100, 99999)
        self.ledStatusTextLabel = QLabel(self.centralwidget)
        self.ledStatusTextLabel.setObjectName(u"ledStatusTextLabel")
        self.ledStatusTextLabel.setGeometry(QRect(10, 110, 131, 21))
        self.ledStatusTextLabel.setFocusPolicy(Qt.NoFocus)
        self.ledStatusTextLabel.setToolTipDuration(0)
        self.timerStatusTextLabel = QLabel(self.centralwidget)
        self.timerStatusTextLabel.setObjectName(u"timerStatusTextLabel")
        self.timerStatusTextLabel.setGeometry(QRect(156, 110, 111, 21))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 100, 261, 121))
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 287, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.selectComPortComboBox.setCurrentText("")
        self.comConnectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.ledButtonOn.setText(QCoreApplication.translate("MainWindow", u"Led On", None))
        self.ledButtonOff.setText(QCoreApplication.translate("MainWindow", u"Led Off", None))
        self.sendTimeButton.setText(QCoreApplication.translate("MainWindow", u"Send Time", None))
        self.ledStatusTextLabel.setText("")
        self.timerStatusTextLabel.setText("")

    # retranslateUi
