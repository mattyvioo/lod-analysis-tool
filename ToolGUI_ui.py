# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ToolGUI.ui'
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
        MainWindow.resize(1000, 484)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.runButton = QPushButton(self.centralwidget)
        self.runButton.setObjectName(u"runButton")
        self.runButton.setGeometry(QRect(630, 60, 141, 71))
        font = QFont()
        font.setPointSize(15)
        self.runButton.setFont(font)
        self.lbl_assetName = QLabel(self.centralwidget)
        self.lbl_assetName.setObjectName(u"lbl_assetName")
        self.lbl_assetName.setGeometry(QRect(170, 90, 141, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.lbl_assetName.setFont(font1)
        self.lbl_assetName.setFrameShape(QFrame.Box)
        self.lbl_assetName.setScaledContents(True)
        self.lbl_assetName.setAlignment(Qt.AlignCenter)
        self.lbl_assetName.setWordWrap(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(390, 10, 220, 41))
        font2 = QFont()
        font2.setPointSize(20)
        self.label.setFont(font2)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.lbl_assetName_3 = QLabel(self.centralwidget)
        self.lbl_assetName_3.setObjectName(u"lbl_assetName_3")
        self.lbl_assetName_3.setGeometry(QRect(170, 130, 141, 21))
        self.lbl_assetName_3.setFont(font1)
        self.lbl_assetName_3.setFrameShape(QFrame.Box)
        self.lbl_assetName_3.setScaledContents(True)
        self.lbl_assetName_3.setAlignment(Qt.AlignCenter)
        self.lbl_assetName_3.setWordWrap(False)
        self.lbl_assetName_4 = QLabel(self.centralwidget)
        self.lbl_assetName_4.setObjectName(u"lbl_assetName_4")
        self.lbl_assetName_4.setGeometry(QRect(170, 170, 141, 21))
        self.lbl_assetName_4.setFont(font1)
        self.lbl_assetName_4.setFrameShape(QFrame.Box)
        self.lbl_assetName_4.setScaledContents(True)
        self.lbl_assetName_4.setAlignment(Qt.AlignCenter)
        self.lbl_assetName_4.setWordWrap(False)
        self.tbl_analysis = QTableWidget(self.centralwidget)
        if (self.tbl_analysis.columnCount() < 7):
            self.tbl_analysis.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_analysis.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_analysis.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_analysis.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_analysis.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_analysis.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_analysis.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbl_analysis.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tbl_analysis.setObjectName(u"tbl_analysis")
        self.tbl_analysis.setGeometry(QRect(20, 250, 960, 192))
        self.tbl_analysis.horizontalHeader().setMinimumSectionSize(39)
        self.tbl_analysis.horizontalHeader().setDefaultSectionSize(130)
        self.tbl_analysis.verticalHeader().setCascadingSectionResizes(False)
        self.tbl_analysis.verticalHeader().setStretchLastSection(False)
        self.lbl_editAssetName = QLabel(self.centralwidget)
        self.lbl_editAssetName.setObjectName(u"lbl_editAssetName")
        self.lbl_editAssetName.setGeometry(QRect(320, 90, 211, 21))
        self.lbl_editAssetName.setFont(font1)
        self.lbl_editAssetName.setFrameShape(QFrame.NoFrame)
        self.lbl_editAssetName.setScaledContents(True)
        self.lbl_editAssetName.setAlignment(Qt.AlignCenter)
        self.lbl_editAssetName.setWordWrap(False)
        self.lbl_editNumberLods = QLabel(self.centralwidget)
        self.lbl_editNumberLods.setObjectName(u"lbl_editNumberLods")
        self.lbl_editNumberLods.setGeometry(QRect(350, 130, 171, 21))
        self.lbl_editNumberLods.setFont(font1)
        self.lbl_editNumberLods.setFrameShape(QFrame.NoFrame)
        self.lbl_editNumberLods.setScaledContents(True)
        self.lbl_editNumberLods.setAlignment(Qt.AlignCenter)
        self.lbl_editNumberLods.setWordWrap(False)
        self.lbl_editNumberMats = QLabel(self.centralwidget)
        self.lbl_editNumberMats.setObjectName(u"lbl_editNumberMats")
        self.lbl_editNumberMats.setGeometry(QRect(350, 170, 171, 21))
        self.lbl_editNumberMats.setFont(font1)
        self.lbl_editNumberMats.setFrameShape(QFrame.NoFrame)
        self.lbl_editNumberMats.setScaledContents(True)
        self.lbl_editNumberMats.setAlignment(Qt.AlignCenter)
        self.lbl_editNumberMats.setWordWrap(False)
        self.exportButton = QPushButton(self.centralwidget)
        self.exportButton.setObjectName(u"exportButton")
        self.exportButton.setEnabled(False)
        self.exportButton.setGeometry(QRect(600, 150, 201, 71))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportButton.sizePolicy().hasHeightForWidth())
        self.exportButton.setSizePolicy(sizePolicy)
        self.exportButton.setFont(font)
        self.exportButton.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.runButton.setText(QCoreApplication.translate("MainWindow", u"Run Analysis", None))
        self.lbl_assetName.setText(QCoreApplication.translate("MainWindow", u"Asset name", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Lod Analysis Tool", None))
        self.lbl_assetName_3.setText(QCoreApplication.translate("MainWindow", u"Number of LODs", None))
        self.lbl_assetName_4.setText(QCoreApplication.translate("MainWindow", u"Number of MATs", None))
        ___qtablewidgetitem = self.tbl_analysis.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Asset Name", None));
        ___qtablewidgetitem1 = self.tbl_analysis.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Lod Index", None));
        ___qtablewidgetitem2 = self.tbl_analysis.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Triangles", None));
        ___qtablewidgetitem3 = self.tbl_analysis.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Vertex Density tris/m\u00b3", None));
        ___qtablewidgetitem4 = self.tbl_analysis.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Screen Switch %", None));
        ___qtablewidgetitem5 = self.tbl_analysis.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"No. MicroTriangles", None));
        ___qtablewidgetitem6 = self.tbl_analysis.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"No. ThinTriangles", None));
        self.lbl_editAssetName.setText(QCoreApplication.translate("MainWindow", u"asset_name", None))
        self.lbl_editNumberLods.setText(QCoreApplication.translate("MainWindow", u"number_of_lods", None))
        self.lbl_editNumberMats.setText(QCoreApplication.translate("MainWindow", u"number_of_mats", None))
        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"Export data to CSV", None))
    # retranslateUi

