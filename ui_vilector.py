# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vilectorDesign.ui',
# licensing of 'vilectorDesign.ui' applies.
#
# Created: Thu Jul 18 09:53:51 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(988, 794)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.leftLayout = QtWidgets.QVBoxLayout()
        self.leftLayout.setObjectName("leftLayout")
        self.Lecteur = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lecteur.sizePolicy().hasHeightForWidth())
        self.Lecteur.setSizePolicy(sizePolicy)
        self.Lecteur.setObjectName("Lecteur")
        self.leftLayout.addWidget(self.Lecteur)
        self.layoutSlider = QtWidgets.QHBoxLayout()
        self.layoutSlider.setObjectName("layoutSlider")
        self.lAvanceeTps = QtWidgets.QLabel(self.centralwidget)
        self.lAvanceeTps.setObjectName("lAvanceeTps")
        self.layoutSlider.addWidget(self.lAvanceeTps)
        self.sTpsCourant = QtWidgets.QSlider(self.centralwidget)
        self.sTpsCourant.setOrientation(QtCore.Qt.Horizontal)
        self.sTpsCourant.setObjectName("sTpsCourant")
        self.layoutSlider.addWidget(self.sTpsCourant)
        self.lRestantTps = QtWidgets.QLabel(self.centralwidget)
        self.lRestantTps.setObjectName("lRestantTps")
        self.layoutSlider.addWidget(self.lRestantTps)
        self.leftLayout.addLayout(self.layoutSlider)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pBLecture = QtWidgets.QPushButton(self.centralwidget)
        self.pBLecture.setObjectName("pBLecture")
        self.horizontalLayout_4.addWidget(self.pBLecture)
        self.pBPause = QtWidgets.QPushButton(self.centralwidget)
        self.pBPause.setObjectName("pBPause")
        self.horizontalLayout_4.addWidget(self.pBPause)
        self.pBStop = QtWidgets.QPushButton(self.centralwidget)
        self.pBStop.setObjectName("pBStop")
        self.horizontalLayout_4.addWidget(self.pBStop)
        self.pBPrecedent = QtWidgets.QPushButton(self.centralwidget)
        self.pBPrecedent.setObjectName("pBPrecedent")
        self.horizontalLayout_4.addWidget(self.pBPrecedent)
        self.pBSuivant = QtWidgets.QPushButton(self.centralwidget)
        self.pBSuivant.setObjectName("pBSuivant")
        self.horizontalLayout_4.addWidget(self.pBSuivant)
        self.leftLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.leftLayout)
        self.centralLayout = QtWidgets.QVBoxLayout()
        self.centralLayout.setObjectName("centralLayout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.centralLayout.addWidget(self.line)
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.centralLayout.addItem(spacerItem)
        self.horizontalLayout_5.addLayout(self.centralLayout)
        self.rightLayout = QtWidgets.QVBoxLayout()
        self.rightLayout.setObjectName("rightLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.rightLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.rightLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pBAjout = QtWidgets.QPushButton(self.centralwidget)
        self.pBAjout.setObjectName("pBAjout")
        self.horizontalLayout.addWidget(self.pBAjout)
        self.pBSupp = QtWidgets.QPushButton(self.centralwidget)
        self.pBSupp.setObjectName("pBSupp")
        self.horizontalLayout.addWidget(self.pBSupp)
        self.rightLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.dBVolume = QtWidgets.QDial(self.centralwidget)
        self.dBVolume.setMaximumSize(QtCore.QSize(50, 50))
        self.dBVolume.setObjectName("dBVolume")
        self.horizontalLayout_3.addWidget(self.dBVolume)
        self.suiviVol = QtWidgets.QLabel(self.centralwidget)
        self.suiviVol.setObjectName("suiviVol")
        self.horizontalLayout_3.addWidget(self.suiviVol)
        self.rightLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.rightLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 988, 21))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.lAvanceeTps.setText(QtWidgets.QApplication.translate("MainWindow", "0:00", None, -1))
        self.lRestantTps.setText(QtWidgets.QApplication.translate("MainWindow", "0:00", None, -1))
        self.pBLecture.setText(QtWidgets.QApplication.translate("MainWindow", "Lecture", None, -1))
        self.pBPause.setText(QtWidgets.QApplication.translate("MainWindow", "Pause", None, -1))
        self.pBStop.setText(QtWidgets.QApplication.translate("MainWindow", "Stop", None, -1))
        self.pBPrecedent.setText(QtWidgets.QApplication.translate("MainWindow", "Précédent", None, -1))
        self.pBSuivant.setText(QtWidgets.QApplication.translate("MainWindow", "Suivant", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Liste de lecture", None, -1))
        self.pBAjout.setText(QtWidgets.QApplication.translate("MainWindow", "+", None, -1))
        self.pBSupp.setText(QtWidgets.QApplication.translate("MainWindow", "-", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Volume :", None, -1))
        self.suiviVol.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.menuFichier.setTitle(QtWidgets.QApplication.translate("MainWindow", "Fichier", None, -1))
        self.menuAide.setTitle(QtWidgets.QApplication.translate("MainWindow", "Aide", None, -1))

