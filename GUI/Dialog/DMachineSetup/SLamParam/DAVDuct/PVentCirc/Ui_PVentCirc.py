# -*- coding: utf-8 -*-

# File generated according to PVentCirc.ui
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PVentCirc(object):
    def setupUi(self, PVentCirc):
        PVentCirc.setObjectName("PVentCirc")
        PVentCirc.resize(630, 470)
        PVentCirc.setMinimumSize(QtCore.QSize(630, 470))
        PVentCirc.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(PVentCirc)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.img_vent = QtWidgets.QLabel(PVentCirc)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_vent.sizePolicy().hasHeightForWidth())
        self.img_vent.setSizePolicy(sizePolicy)
        self.img_vent.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.img_vent.setText("")
        self.img_vent.setPixmap(
            QtGui.QPixmap(":/images/images/MachineSetup/LamParam/CircVentDuct.png")
        )
        self.img_vent.setScaledContents(True)
        self.img_vent.setObjectName("img_vent")
        self.verticalLayout_2.addWidget(self.img_vent)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lf_D0 = FloatEdit(PVentCirc)
        self.lf_D0.setObjectName("lf_D0")
        self.gridLayout.addWidget(self.lf_D0, 2, 1, 1, 1)
        self.lf_Alpha0 = FloatEdit(PVentCirc)
        self.lf_Alpha0.setObjectName("lf_Alpha0")
        self.gridLayout.addWidget(self.lf_Alpha0, 3, 1, 1, 1)
        self.unit_D0 = QtWidgets.QLabel(PVentCirc)
        self.unit_D0.setObjectName("unit_D0")
        self.gridLayout.addWidget(self.unit_D0, 2, 2, 1, 1)
        self.in_Alpha0 = QtWidgets.QLabel(PVentCirc)
        self.in_Alpha0.setObjectName("in_Alpha0")
        self.gridLayout.addWidget(self.in_Alpha0, 3, 0, 1, 1)
        self.unit_Alpha0 = QtWidgets.QLabel(PVentCirc)
        self.unit_Alpha0.setObjectName("unit_Alpha0")
        self.gridLayout.addWidget(self.unit_Alpha0, 3, 2, 1, 1)
        self.unit_H0 = QtWidgets.QLabel(PVentCirc)
        self.unit_H0.setObjectName("unit_H0")
        self.gridLayout.addWidget(self.unit_H0, 1, 2, 1, 1)
        self.lf_H0 = FloatEdit(PVentCirc)
        self.lf_H0.setObjectName("lf_H0")
        self.gridLayout.addWidget(self.lf_H0, 1, 1, 1, 1)
        self.in_H0 = QtWidgets.QLabel(PVentCirc)
        self.in_H0.setObjectName("in_H0")
        self.gridLayout.addWidget(self.in_H0, 1, 0, 1, 1)
        self.in_D0 = QtWidgets.QLabel(PVentCirc)
        self.in_D0.setObjectName("in_D0")
        self.gridLayout.addWidget(self.in_D0, 2, 0, 1, 1)
        self.in_Zh = QtWidgets.QLabel(PVentCirc)
        self.in_Zh.setObjectName("in_Zh")
        self.gridLayout.addWidget(self.in_Zh, 0, 0, 1, 1)
        self.si_Zh = QtWidgets.QSpinBox(PVentCirc)
        self.si_Zh.setObjectName("si_Zh")
        self.gridLayout.addWidget(self.si_Zh, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.w_out = WVentOut(PVentCirc)
        self.w_out.setObjectName("w_out")
        self.verticalLayout.addWidget(self.w_out)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(PVentCirc)
        QtCore.QMetaObject.connectSlotsByName(PVentCirc)
        PVentCirc.setTabOrder(self.lf_H0, self.lf_D0)
        PVentCirc.setTabOrder(self.lf_D0, self.lf_Alpha0)

    def retranslateUi(self, PVentCirc):
        _translate = QtCore.QCoreApplication.translate
        PVentCirc.setWindowTitle(_translate("PVentCirc", "Form"))
        self.unit_D0.setText(_translate("PVentCirc", "m"))
        self.in_Alpha0.setText(_translate("PVentCirc", "Alpha0 :"))
        self.unit_Alpha0.setText(_translate("PVentCirc", "rad"))
        self.unit_H0.setText(_translate("PVentCirc", "m"))
        self.in_H0.setText(_translate("PVentCirc", "H0 :"))
        self.in_D0.setText(_translate("PVentCirc", "D0 :"))
        self.in_Zh.setText(_translate("PVentCirc", "Zh :"))


from .......GUI.Dialog.DMachineSetup.SLamParam.DAVDuct.WVentOut.WVentOut import (
    WVentOut,
)
from .......GUI.Tools.FloatEdit import FloatEdit
from .......GUI.Resources import pyleecan_rc
