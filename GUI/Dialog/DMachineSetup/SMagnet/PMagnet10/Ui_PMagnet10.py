# -*- coding: utf-8 -*-

# File generated according to PMagnet10.ui
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PMagnet10(object):
    def setupUi(self, PMagnet10):
        PMagnet10.setObjectName("PMagnet10")
        PMagnet10.resize(531, 222)
        PMagnet10.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalLayout = QtWidgets.QHBoxLayout(PMagnet10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img_magnet = QtWidgets.QLabel(PMagnet10)
        self.img_magnet.setMinimumSize(QtCore.QSize(300, 200))
        self.img_magnet.setMaximumSize(QtCore.QSize(550, 350))
        self.img_magnet.setText("")
        self.img_magnet.setPixmap(
            QtGui.QPixmap(
                ":/images/images/MachineSetup/P_Magnet/Surface Magnet type 10.PNG"
            )
        )
        self.img_magnet.setScaledContents(True)
        self.img_magnet.setObjectName("img_magnet")
        self.horizontalLayout.addWidget(self.img_magnet)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lf_Wmag = FloatEdit(PMagnet10)
        self.lf_Wmag.setMinimumSize(QtCore.QSize(100, 0))
        self.lf_Wmag.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lf_Wmag.setObjectName("lf_Wmag")
        self.gridLayout.addWidget(self.lf_Wmag, 0, 1, 1, 1)
        self.in_H0 = QtWidgets.QLabel(PMagnet10)
        self.in_H0.setObjectName("in_H0")
        self.gridLayout.addWidget(self.in_H0, 2, 0, 1, 1)
        self.unit_Hmag = QtWidgets.QLabel(PMagnet10)
        self.unit_Hmag.setObjectName("unit_Hmag")
        self.gridLayout.addWidget(self.unit_Hmag, 1, 2, 1, 1)
        self.lf_Hmag = FloatEdit(PMagnet10)
        self.lf_Hmag.setMinimumSize(QtCore.QSize(100, 0))
        self.lf_Hmag.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lf_Hmag.setObjectName("lf_Hmag")
        self.gridLayout.addWidget(self.lf_Hmag, 1, 1, 1, 1)
        self.unit_Wmag = QtWidgets.QLabel(PMagnet10)
        self.unit_Wmag.setObjectName("unit_Wmag")
        self.gridLayout.addWidget(self.unit_Wmag, 0, 2, 1, 1)
        self.lf_H0 = FloatEdit(PMagnet10)
        self.lf_H0.setMinimumSize(QtCore.QSize(100, 0))
        self.lf_H0.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lf_H0.setObjectName("lf_H0")
        self.gridLayout.addWidget(self.lf_H0, 2, 1, 1, 1)
        self.in_Hmag = QtWidgets.QLabel(PMagnet10)
        self.in_Hmag.setObjectName("in_Hmag")
        self.gridLayout.addWidget(self.in_Hmag, 1, 0, 1, 1)
        self.unit_H0 = QtWidgets.QLabel(PMagnet10)
        self.unit_H0.setObjectName("unit_H0")
        self.gridLayout.addWidget(self.unit_H0, 2, 2, 1, 1)
        self.in_Wmag = QtWidgets.QLabel(PMagnet10)
        self.in_Wmag.setObjectName("in_Wmag")
        self.gridLayout.addWidget(self.in_Wmag, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.w_out = WMagnetOut(PMagnet10)
        self.w_out.setObjectName("w_out")
        self.verticalLayout.addWidget(self.w_out)
        spacerItem = QtWidgets.QSpacerItem(
            17, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(PMagnet10)
        QtCore.QMetaObject.connectSlotsByName(PMagnet10)
        PMagnet10.setTabOrder(self.lf_Wmag, self.lf_Hmag)
        PMagnet10.setTabOrder(self.lf_Hmag, self.lf_H0)

    def retranslateUi(self, PMagnet10):
        _translate = QtCore.QCoreApplication.translate
        PMagnet10.setWindowTitle(_translate("PMagnet10", "Form"))
        self.in_H0.setText(_translate("PMagnet10", "H0      :"))
        self.unit_Hmag.setText(_translate("PMagnet10", "m"))
        self.unit_Wmag.setText(_translate("PMagnet10", "m"))
        self.in_Hmag.setText(_translate("PMagnet10", "Hmag  :"))
        self.unit_H0.setText(_translate("PMagnet10", "m"))
        self.in_Wmag.setText(_translate("PMagnet10", "Wmag :"))


from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.WMagnetOut.WMagnetOut import WMagnetOut
from pyleecan.GUI.Tools.FloatEdit import FloatEdit
from pyleecan.GUI.Resources import pyleecan_rc
