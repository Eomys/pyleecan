# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitHub\pyleecan\GUI\Dialog\DMachineSetup\SMagnet\SMagnet.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SMagnet(object):
    def setupUi(self, SMagnet):
        SMagnet.setObjectName("SMagnet")
        SMagnet.resize(650, 550)
        SMagnet.setMinimumSize(QtCore.QSize(650, 550))
        self.main_layout = QtWidgets.QVBoxLayout(SMagnet)
        self.main_layout.setObjectName("main_layout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.b_help = HelpButton(SMagnet)
        self.b_help.setText("")
        self.b_help.setPixmap(QtGui.QPixmap(":/images/images/icon/help_16.png"))
        self.b_help.setObjectName("b_help")
        self.horizontalLayout_3.addWidget(self.b_help)
        self.c_type = QtWidgets.QComboBox(SMagnet)
        self.c_type.setMinimumSize(QtCore.QSize(100, 0))
        self.c_type.setAutoFillBackground(False)
        self.c_type.setObjectName("c_type")
        self.c_type.addItem("")
        self.c_type.addItem("")
        self.c_type.addItem("")
        self.c_type.addItem("")
        self.c_type.addItem("")
        self.horizontalLayout_3.addWidget(self.c_type)
        self.out_Nmag = QtWidgets.QLabel(SMagnet)
        self.out_Nmag.setObjectName("out_Nmag")
        self.horizontalLayout_3.addWidget(self.out_Nmag)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem)
        self.main_layout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.w_mat = WMatSelect(SMagnet)
        self.w_mat.setObjectName("w_mat")
        self.horizontalLayout.addWidget(self.w_mat)
        self.in_type_magnetization = QtWidgets.QLabel(SMagnet)
        self.in_type_magnetization.setObjectName("in_type_magnetization")
        self.horizontalLayout.addWidget(self.in_type_magnetization)
        self.c_type_magnetization = QtWidgets.QComboBox(SMagnet)
        self.c_type_magnetization.setObjectName("c_type_magnetization")
        self.c_type_magnetization.addItem("")
        self.c_type_magnetization.addItem("")
        self.c_type_magnetization.addItem("")
        self.horizontalLayout.addWidget(self.c_type_magnetization)
        self.main_layout.addLayout(self.horizontalLayout)
        self.w_mag = QtWidgets.QWidget(SMagnet)
        self.w_mag.setObjectName("w_mag")
        self.main_layout.addWidget(self.w_mag)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem1)
        self.b_plot = QtWidgets.QPushButton(SMagnet)
        self.b_plot.setObjectName("b_plot")
        self.horizontalLayout_2.addWidget(self.b_plot)
        self.b_previous = QtWidgets.QPushButton(SMagnet)
        self.b_previous.setObjectName("b_previous")
        self.horizontalLayout_2.addWidget(self.b_previous)
        self.b_next = QtWidgets.QPushButton(SMagnet)
        self.b_next.setEnabled(True)
        self.b_next.setObjectName("b_next")
        self.horizontalLayout_2.addWidget(self.b_next)
        self.main_layout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SMagnet)
        QtCore.QMetaObject.connectSlotsByName(SMagnet)

    def retranslateUi(self, SMagnet):
        _translate = QtCore.QCoreApplication.translate
        SMagnet.setWindowTitle(_translate("SMagnet", "Form"))
        self.c_type.setItemText(0, _translate("SMagnet", "Rectangular"))
        self.c_type.setItemText(1, _translate("SMagnet", "Polar"))
        self.c_type.setItemText(2, _translate("SMagnet", "Flat bottom, polar top"))
        self.c_type.setItemText(3, _translate("SMagnet", "Flat bottom, curved top"))
        self.c_type.setItemText(4, _translate("SMagnet", "Polar bottom, curved top"))
        self.out_Nmag.setText(_translate("SMagnet", "Number of magnet = 2 * p = ?"))
        self.in_type_magnetization.setText(_translate("SMagnet", "type_magnetization:"))
        self.c_type_magnetization.setItemText(0, _translate("SMagnet", "Radial"))
        self.c_type_magnetization.setItemText(1, _translate("SMagnet", "Parallel"))
        self.c_type_magnetization.setItemText(2, _translate("SMagnet", "HallBach"))
        self.b_plot.setText(_translate("SMagnet", "Preview"))
        self.b_previous.setText(_translate("SMagnet", "Previous"))
        self.b_next.setText(_translate("SMagnet", "Save"))


from pyleecan.GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect
from pyleecan.GUI.Tools.HelpButton import HelpButton
from pyleecan.GUI.Resources import pyleecan_rc
