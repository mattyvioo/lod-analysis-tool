# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences.ui'
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
        MainWindow.resize(683, 393)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 261, 341))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 10, 0, 10)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(280, 20, 251, 341))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalLayoutWidget_2.sizePolicy().hasHeightForWidth())
        self.verticalLayoutWidget_2.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSpacing(40)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.txt_triArea = QLineEdit(self.verticalLayoutWidget_2)
        self.txt_triArea.setObjectName(u"txt_triArea")

        self.verticalLayout_2.addWidget(self.txt_triArea)

        self.txt_triAngle = QLineEdit(self.verticalLayoutWidget_2)
        self.txt_triAngle.setObjectName(u"txt_triAngle")

        self.verticalLayout_2.addWidget(self.txt_triAngle)

        self.txt_allowedMicro = QLineEdit(self.verticalLayoutWidget_2)
        self.txt_allowedMicro.setObjectName(u"txt_allowedMicro")

        self.verticalLayout_2.addWidget(self.txt_allowedMicro)

        self.txt_allowedThin = QLineEdit(self.verticalLayoutWidget_2)
        self.txt_allowedThin.setObjectName(u"txt_allowedThin")

        self.verticalLayout_2.addWidget(self.txt_allowedThin)

        self.txt_allowedTolerance = QLineEdit(self.verticalLayoutWidget_2)
        self.txt_allowedTolerance.setObjectName(u"txt_allowedTolerance")

        self.verticalLayout_2.addWidget(self.txt_allowedTolerance)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(530, 140, 131, 91))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Micro Tri area treshold (cm2):</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Thin Tri angle treshold (degrees): </p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Allowed MicroTri %:</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Allowed ThinTri %:</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Allowed error tolerance %:</p></body></html>", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

