# -*- coding: utf-8 -*-

# File generated according to PVentPolar.ui
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PVentPolar(object):
    def setupUi(self, PVentPolar):
        PVentPolar.setObjectName("PVentPolar")
        PVentPolar.resize(630, 470)
        PVentPolar.setMinimumSize(QtCore.QSize(630, 470))
        PVentPolar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(PVentPolar)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.img_vent = QtWidgets.QLabel(PVentPolar)
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
            QtGui.QPixmap(":/images/images/MachineSetup/LamParam/PolarVentDuct.png")
        )
        self.img_vent.setScaledContents(True)
        self.img_vent.setObjectName("img_vent")
        self.verticalLayout_2.addWidget(self.img_vent)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.in_Zh = QtWidgets.QLabel(PVentPolar)
        self.in_Zh.setObjectName("in_Zh")
        self.gridLayout.addWidget(self.in_Zh, 0, 0, 1, 1)
        self.in_H0 = QtWidgets.QLabel(PVentPolar)
        self.in_H0.setObjectName("in_H0")
        self.gridLayout.addWidget(self.in_H0, 1, 0, 1, 1)
        self.lf_H0 = FloatEdit(PVentPolar)
        self.lf_H0.setObjectName("lf_H0")
        self.gridLayout.addWidget(self.lf_H0, 1, 1, 1, 1)
        self.unit_H0 = QtWidgets.QLabel(PVentPolar)
        self.unit_H0.setObjectName("unit_H0")
        self.gridLayout.addWidget(self.unit_H0, 1, 2, 1, 1)
        self.in_D0 = QtWidgets.QLabel(PVentPolar)
        self.in_D0.setObjectName("in_D0")
        self.gridLayout.addWidget(self.in_D0, 2, 0, 1, 1)
        self.lf_D0 = FloatEdit(PVentPolar)
        self.lf_D0.setObjectName("lf_D0")
        self.gridLayout.addWidget(self.lf_D0, 2, 1, 1, 1)
        self.unit_D0 = QtWidgets.QLabel(PVentPolar)
        self.unit_D0.setObjectName("unit_D0")
        self.gridLayout.addWidget(self.unit_D0, 2, 2, 1, 1)
        self.in_W1 = QtWidgets.QLabel(PVentPolar)
        self.in_W1.setObjectName("in_W1")
        self.gridLayout.addWidget(self.in_W1, 3, 0, 1, 1)
        self.lf_W1 = FloatEdit(PVentPolar)
        self.lf_W1.setObjectName("lf_W1")
        self.gridLayout.addWidget(self.lf_W1, 3, 1, 1, 1)
        self.unit_W1 = QtWidgets.QLabel(PVentPolar)
        self.unit_W1.setObjectName("unit_W1")
        self.gridLayout.addWidget(self.unit_W1, 3, 2, 1, 1)
        self.in_Alpha0 = QtWidgets.QLabel(PVentPolar)
        self.in_Alpha0.setObjectName("in_Alpha0")
        self.gridLayout.addWidget(self.in_Alpha0, 4, 0, 1, 1)
        self.lf_Alpha0 = FloatEdit(PVentPolar)
        self.lf_Alpha0.setObjectName("lf_Alpha0")
        self.gridLayout.addWidget(self.lf_Alpha0, 4, 1, 1, 1)
        self.unit_Alpha0 = QtWidgets.QLabel(PVentPolar)
        self.unit_Alpha0.setObjectName("unit_Alpha0")
        self.gridLayout.addWidget(self.unit_Alpha0, 4, 2, 1, 1)
        self.si_Zh = QtWidgets.QSpinBox(PVentPolar)
        self.si_Zh.setObjectName("si_Zh")
        self.gridLayout.addWidget(self.si_Zh, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.w_out = WVentOut(PVentPolar)
        self.w_out.setObjectName("w_out")
        self.verticalLayout.addWidget(self.w_out)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(PVentPolar)
        QtCore.QMetaObject.connectSlotsByName(PVentPolar)
        PVentPolar.setTabOrder(self.lf_H0, self.lf_D0)
        PVentPolar.setTabOrder(self.lf_D0, self.lf_Alpha0)

    def retranslateUi(self, PVentPolar):
        _translate = QtCore.QCoreApplication.translate
        PVentPolar.setWindowTitle(_translate("PVentPolar", "Form"))
        self.in_Zh.setText(_translate("PVentPolar", "Zh :"))
        self.in_H0.setText(_translate("PVentPolar", "H0 :"))
        self.unit_H0.setText(_translate("PVentPolar", "m"))
        self.in_D0.setText(_translate("PVentPolar", "D0 :"))
        self.unit_D0.setText(_translate("PVentPolar", "m"))
        self.in_W1.setText(_translate("PVentPolar", "W1 :"))
        self.unit_W1.setText(_translate("PVentPolar", "rad"))
        self.in_Alpha0.setText(_translate("PVentPolar", "Alpha0 :"))
        self.unit_Alpha0.setText(_translate("PVentPolar", "rad"))


from .......GUI.Dialog.DMachineSetup.SLamParam.DAVDuct.WVentOut.WVentOut import WVentOut
from .......GUI.Tools.FloatEdit import FloatEdit
from pyleecan.GUI.Resources import pyleecan_rc
