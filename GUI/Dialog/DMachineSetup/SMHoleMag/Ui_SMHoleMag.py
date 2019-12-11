# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitHub\pyleecan\GUI\Dialog\DMachineSetup\SMHoleMag\SMHoleMag.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SMHoleMag(object):
    def setupUi(self, SMHoleMag):
        SMHoleMag.setObjectName("SMHoleMag")
        SMHoleMag.resize(650, 610)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SMHoleMag.sizePolicy().hasHeightForWidth())
        SMHoleMag.setSizePolicy(sizePolicy)
        SMHoleMag.setMinimumSize(QtCore.QSize(650, 610))
        self.verticalLayout = QtWidgets.QVBoxLayout(SMHoleMag)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.b_help = HelpButton(SMHoleMag)
        self.b_help.setText("")
        self.b_help.setPixmap(QtGui.QPixmap(":/images/images/icon/help_16.png"))
        self.b_help.setObjectName("b_help")
        self.horizontalLayout_2.addWidget(self.b_help)
        self.out_hole_pitch = QtWidgets.QLabel(SMHoleMag)
        self.out_hole_pitch.setObjectName("out_hole_pitch")
        self.horizontalLayout_2.addWidget(self.out_hole_pitch)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem)
        self.w_mat = WMatSelect(SMHoleMag)
        self.w_mat.setMinimumSize(QtCore.QSize(100, 0))
        self.w_mat.setObjectName("w_mat")
        self.horizontalLayout_2.addWidget(self.w_mat)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.b_add = QtWidgets.QPushButton(SMHoleMag)
        self.b_add.setObjectName("b_add")
        self.horizontalLayout_3.addWidget(self.b_add)
        self.b_remove = QtWidgets.QPushButton(SMHoleMag)
        self.b_remove.setObjectName("b_remove")
        self.horizontalLayout_3.addWidget(self.b_remove)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tab_hole = QtWidgets.QTabWidget(SMHoleMag)
        self.tab_hole.setMinimumSize(QtCore.QSize(630, 500))
        self.tab_hole.setObjectName("tab_hole")
        self.verticalLayout.addWidget(self.tab_hole)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem2)
        self.b_plot = QtWidgets.QPushButton(SMHoleMag)
        self.b_plot.setObjectName("b_plot")
        self.horizontalLayout.addWidget(self.b_plot)
        self.b_previous = QtWidgets.QPushButton(SMHoleMag)
        self.b_previous.setObjectName("b_previous")
        self.horizontalLayout.addWidget(self.b_previous)
        self.b_next = QtWidgets.QPushButton(SMHoleMag)
        self.b_next.setEnabled(True)
        self.b_next.setObjectName("b_next")
        self.horizontalLayout.addWidget(self.b_next)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SMHoleMag)
        self.tab_hole.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(SMHoleMag)

    def retranslateUi(self, SMHoleMag):
        _translate = QtCore.QCoreApplication.translate
        SMHoleMag.setWindowTitle(_translate("SMHoleMag", "Form"))
        self.out_hole_pitch.setText(
            _translate("SMHoleMag", "Slot pitch = 2*Pi / Zs = ")
        )
        self.b_add.setText(_translate("SMHoleMag", "Add new slots"))
        self.b_remove.setText(_translate("SMHoleMag", "Remove last slot"))
        self.b_plot.setText(_translate("SMHoleMag", "Preview"))
        self.b_previous.setText(_translate("SMHoleMag", "Previous"))
        self.b_next.setText(_translate("SMHoleMag", "Save"))


from pyleecan.GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect
from pyleecan.GUI.Tools.HelpButton import HelpButton
from pyleecan.GUI.Resources import pyleecan_rc
