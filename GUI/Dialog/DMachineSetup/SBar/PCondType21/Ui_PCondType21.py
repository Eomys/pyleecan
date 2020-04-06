# -*- coding: utf-8 -*-

# File generated according to PCondType21.ui
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PCondType21(object):
    def setupUi(self, PCondType21):
        PCondType21.setObjectName("PCondType21")
        PCondType21.resize(416, 124)
        self.horizontalLayout = QtWidgets.QHBoxLayout(PCondType21)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lf_Hbar = FloatEdit(PCondType21)
        self.lf_Hbar.setMinimumSize(QtCore.QSize(70, 0))
        self.lf_Hbar.setMaximumSize(QtCore.QSize(100, 20))
        self.lf_Hbar.setObjectName("lf_Hbar")
        self.gridLayout.addWidget(self.lf_Hbar, 0, 1, 1, 1)
        self.in_Hbar = QtWidgets.QLabel(PCondType21)
        self.in_Hbar.setMinimumSize(QtCore.QSize(40, 0))
        self.in_Hbar.setObjectName("in_Hbar")
        self.gridLayout.addWidget(self.in_Hbar, 0, 0, 1, 1)
        self.unit_Hbar = QtWidgets.QLabel(PCondType21)
        self.unit_Hbar.setMinimumSize(QtCore.QSize(0, 0))
        self.unit_Hbar.setObjectName("unit_Hbar")
        self.gridLayout.addWidget(self.unit_Hbar, 0, 2, 1, 1)
        self.lf_Wbar = FloatEdit(PCondType21)
        self.lf_Wbar.setMinimumSize(QtCore.QSize(70, 0))
        self.lf_Wbar.setMaximumSize(QtCore.QSize(100, 20))
        self.lf_Wbar.setObjectName("lf_Wbar")
        self.gridLayout.addWidget(self.lf_Wbar, 1, 1, 1, 1)
        self.unit_Wbar = QtWidgets.QLabel(PCondType21)
        self.unit_Wbar.setMinimumSize(QtCore.QSize(0, 0))
        self.unit_Wbar.setObjectName("unit_Wbar")
        self.gridLayout.addWidget(self.unit_Wbar, 1, 2, 1, 1)
        self.in_Wbar = QtWidgets.QLabel(PCondType21)
        self.in_Wbar.setMinimumSize(QtCore.QSize(40, 0))
        self.in_Wbar.setObjectName("in_Wbar")
        self.gridLayout.addWidget(self.in_Wbar, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.w_mat = WMatSelect(PCondType21)
        self.w_mat.setObjectName("w_mat")
        self.verticalLayout_2.addWidget(self.w_mat)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.w_out = WBarOut(PCondType21)
        self.w_out.setObjectName("w_out")
        self.horizontalLayout.addWidget(self.w_out)

        self.retranslateUi(PCondType21)
        QtCore.QMetaObject.connectSlotsByName(PCondType21)
        PCondType21.setTabOrder(self.lf_Hbar, self.lf_Wbar)

    def retranslateUi(self, PCondType21):
        _translate = QtCore.QCoreApplication.translate
        PCondType21.setWindowTitle(_translate("PCondType21", "Form"))
        self.in_Hbar.setText(_translate("PCondType21", "Hbar :"))
        self.unit_Hbar.setText(_translate("PCondType21", "m"))
        self.unit_Wbar.setText(_translate("PCondType21", "m"))
        self.in_Wbar.setText(_translate("PCondType21", "Wbar :"))
from pyleecan.GUI.Dialog.DMachineSetup.SBar.WBarOut.WBarOut import WBarOut
from pyleecan.GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect
from pyleecan.GUI.Tools.FloatEdit import FloatEdit
