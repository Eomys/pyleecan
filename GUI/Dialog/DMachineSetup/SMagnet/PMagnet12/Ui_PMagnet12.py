# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitHub\pyleecan\GUI\Dialog\DMachineSetup\SMagnet\PMagnet12\PMagnet12.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PMagnet12(object):
    def setupUi(self, PMagnet12):
        PMagnet12.setObjectName("PMagnet12")
        PMagnet12.resize(531, 222)
        PMagnet12.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalLayout = QtWidgets.QHBoxLayout(PMagnet12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img_magnet = QtWidgets.QLabel(PMagnet12)
        self.img_magnet.setMinimumSize(QtCore.QSize(300, 200))
        self.img_magnet.setMaximumSize(QtCore.QSize(550, 350))
        self.img_magnet.setText("")
        self.img_magnet.setPixmap(
            QtGui.QPixmap(
                ":/images/images/MachineSetup/P_Magnet/Surface Magnet type 12.PNG"
            )
        )
        self.img_magnet.setScaledContents(True)
        self.img_magnet.setObjectName("img_magnet")
        self.horizontalLayout.addWidget(self.img_magnet)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lf_Wmag = FloatEdit(PMagnet12)
        self.lf_Wmag.setMinimumSize(QtCore.QSize(100, 0))
        self.lf_Wmag.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lf_Wmag.setObjectName("lf_Wmag")
        self.gridLayout.addWidget(self.lf_Wmag, 0, 1, 1, 1)
        self.in_H0 = QtWidgets.QLabel(PMagnet12)
        self.in_H0.setObjectName("in_H0")
        self.gridLayout.addWidget(self.in_H0, 2, 0, 1, 1)
        self.unit_Hmag = QtWidgets.QLabel(PMagnet12)
        self.unit_Hmag.setObjectName("unit_Hmag")
        self.gridLayout.addWidget(self.unit_Hmag, 1, 2, 1, 1)
        self.lf_Hmag = FloatEdit(PMagnet12)
        self.lf_Hmag.setMinimumSize(QtCore.QSize(100, 0))
        self.lf_Hmag.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lf_Hmag.setObjectName("lf_Hmag")
        self.gridLayout.addWidget(self.lf_Hmag, 1, 1, 1, 1)
        self.unit_Wmag = QtWidgets.QLabel(PMagnet12)
        self.unit_Wmag.setObjectName("unit_Wmag")
        self.gridLayout.addWidget(self.unit_Wmag, 0, 2, 1, 1)
        self.lf_H0 = FloatEdit(PMagnet12)
        self.lf_H0.setMinimumSize(QtCore.QSize(100, 0))
        self.lf_H0.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lf_H0.setObjectName("lf_H0")
        self.gridLayout.addWidget(self.lf_H0, 2, 1, 1, 1)
        self.in_Hmag = QtWidgets.QLabel(PMagnet12)
        self.in_Hmag.setObjectName("in_Hmag")
        self.gridLayout.addWidget(self.in_Hmag, 1, 0, 1, 1)
        self.unit_H0 = QtWidgets.QLabel(PMagnet12)
        self.unit_H0.setObjectName("unit_H0")
        self.gridLayout.addWidget(self.unit_H0, 2, 2, 1, 1)
        self.in_Wmag = QtWidgets.QLabel(PMagnet12)
        self.in_Wmag.setObjectName("in_Wmag")
        self.gridLayout.addWidget(self.in_Wmag, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.w_out = WMagnetOut(PMagnet12)
        self.w_out.setObjectName("w_out")
        self.verticalLayout.addWidget(self.w_out)
        spacerItem = QtWidgets.QSpacerItem(
            17, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(PMagnet12)
        QtCore.QMetaObject.connectSlotsByName(PMagnet12)
        PMagnet12.setTabOrder(self.lf_Wmag, self.lf_Hmag)
        PMagnet12.setTabOrder(self.lf_Hmag, self.lf_H0)

    def retranslateUi(self, PMagnet12):
        _translate = QtCore.QCoreApplication.translate
        PMagnet12.setWindowTitle(_translate("PMagnet12", "Form"))
        self.in_H0.setText(_translate("PMagnet12", "H0      :"))
        self.unit_Hmag.setText(_translate("PMagnet12", "m"))
        self.unit_Wmag.setText(_translate("PMagnet12", "m"))
        self.in_Hmag.setText(_translate("PMagnet12", "Hmag  :"))
        self.unit_H0.setText(_translate("PMagnet12", "m"))
        self.in_Wmag.setText(_translate("PMagnet12", "Wmag :"))


from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.WMagnetOut.WMagnetOut import WMagnetOut
from pyleecan.GUI.Tools.FloatEdit import FloatEdit
from pyleecan.GUI.Resources import pyleecan_rc
