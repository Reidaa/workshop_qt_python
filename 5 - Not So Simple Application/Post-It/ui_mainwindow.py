# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(264, 308)
        MainWindow.setAutoFillBackground(True)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.closeButton = QPushButton(self.centralWidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(25, 25))
        self.closeButton.setMaximumSize(QSize(25, 25))
        self.closeButton.setBaseSize(QSize(2, 0))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.closeButton.setFont(font)
        self.closeButton.setLayoutDirection(Qt.LeftToRight)
        self.closeButton.setStyleSheet(u"QPushButton {\n"
"    border: 0px;\n"
"}")
        self.closeButton.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.closeButton)

        self.horizontalSpacer = QSpacerItem(237, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.moreButton = QPushButton(self.centralWidget)
        self.moreButton.setObjectName(u"moreButton")
        self.moreButton.setMinimumSize(QSize(25, 25))
        self.moreButton.setMaximumSize(QSize(25, 25))
        self.moreButton.setFont(font)
        self.moreButton.setStyleSheet(u"QPushButton {\n"
"    border: 0px;\n"
"}")
        self.moreButton.setIconSize(QSize(8, 8))

        self.horizontalLayout.addWidget(self.moreButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textEdit = QTextEdit(self.centralWidget)
        self.textEdit.setObjectName(u"textEdit")
        font1 = QFont()
        font1.setPointSize(18)
        self.textEdit.setFont(font1)
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setLineWidth(0)

        self.verticalLayout.addWidget(self.textEdit)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.closeButton.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.moreButton.setText(QCoreApplication.translate("MainWindow", u"\uff0b", None))
    # retranslateUi

