# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Raphael\Desktop\Git\PyManatee\pyleecan\GUI\Dialog\DMachineSetup\SWindCond\SWindCond.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SWindCond(object):
    def setupUi(self, SWindCond):
        SWindCond.setObjectName("SWindCond")
        SWindCond.resize(650, 550)
        SWindCond.setMinimumSize(QtCore.QSize(650, 550))
        self.main_layout = QtWidgets.QVBoxLayout(SWindCond)
        self.main_layout.setObjectName("main_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.in_cond_type = QtWidgets.QLabel(SWindCond)
        self.in_cond_type.setObjectName("in_cond_type")
        self.horizontalLayout.addWidget(self.in_cond_type)
        self.c_cond_type = QtWidgets.QComboBox(SWindCond)
        self.c_cond_type.setMinimumSize(QtCore.QSize(150, 0))
        self.c_cond_type.setObjectName("c_cond_type")
        self.c_cond_type.addItem("")
        self.c_cond_type.addItem("")
        self.horizontalLayout.addWidget(self.c_cond_type)
        self.w_mat = WMatSelect(SWindCond)
        self.w_mat.setMinimumSize(QtCore.QSize(100, 0))
        self.w_mat.setObjectName("w_mat")
        self.horizontalLayout.addWidget(self.w_mat)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.main_layout.addLayout(self.horizontalLayout)
        self.w_cond = QtWidgets.QWidget(SWindCond)
        self.w_cond.setObjectName("w_cond")
        self.main_layout.addWidget(self.w_cond)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem1)
        self.b_previous = QtWidgets.QPushButton(SWindCond)
        self.b_previous.setObjectName("b_previous")
        self.horizontalLayout_2.addWidget(self.b_previous)
        self.b_next = QtWidgets.QPushButton(SWindCond)
        self.b_next.setObjectName("b_next")
        self.horizontalLayout_2.addWidget(self.b_next)
        self.main_layout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SWindCond)
        QtCore.QMetaObject.connectSlotsByName(SWindCond)

    def retranslateUi(self, SWindCond):
        _translate = QtCore.QCoreApplication.translate
        SWindCond.setWindowTitle(_translate("SWindCond", "Form"))
        self.in_cond_type.setText(_translate("SWindCond", "Conductor type :"))
        self.c_cond_type.setItemText(
            0, _translate("SWindCond", "Preformed Rectangular")
        )
        self.c_cond_type.setItemText(1, _translate("SWindCond", "Random Round Wire"))
        self.b_previous.setText(_translate("SWindCond", "Previous"))
        self.b_next.setText(_translate("SWindCond", "Next"))


from pyleecan.GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect
from pyleecan.GUI.Resources import pyleecan_rc
