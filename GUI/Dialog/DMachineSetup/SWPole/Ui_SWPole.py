# -*- coding: utf-8 -*-

# File generated according to SWPole.ui
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SWPole(object):
    def setupUi(self, SWPole):
        SWPole.setObjectName("SWPole")
        SWPole.resize(650, 550)
        SWPole.setMinimumSize(QtCore.QSize(650, 550))
        self.main_layout = QtWidgets.QVBoxLayout(SWPole)
        self.main_layout.setObjectName("main_layout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.b_help = HelpButton(SWPole)
        self.b_help.setText("")
        self.b_help.setPixmap(QtGui.QPixmap(":/images/images/icon/help_16.png"))
        self.b_help.setObjectName("b_help")
        self.horizontalLayout_2.addWidget(self.b_help)
        self.c_slot_type = QtWidgets.QComboBox(SWPole)
        self.c_slot_type.setObjectName("c_slot_type")
        self.c_slot_type.addItem("")
        self.c_slot_type.addItem("")
        self.horizontalLayout_2.addWidget(self.c_slot_type)
        self.in_Zs = QtWidgets.QLabel(SWPole)
        self.in_Zs.setObjectName("in_Zs")
        self.horizontalLayout_2.addWidget(self.in_Zs)
        self.out_Slot_pitch = QtWidgets.QLabel(SWPole)
        self.out_Slot_pitch.setObjectName("out_Slot_pitch")
        self.horizontalLayout_2.addWidget(self.out_Slot_pitch)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.main_layout.addLayout(self.horizontalLayout_2)
        self.w_slot = QtWidgets.QWidget(SWPole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_slot.sizePolicy().hasHeightForWidth())
        self.w_slot.setSizePolicy(sizePolicy)
        self.w_slot.setObjectName("w_slot")
        self.main_layout.addWidget(self.w_slot)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.b_plot = QtWidgets.QPushButton(SWPole)
        self.b_plot.setObjectName("b_plot")
        self.horizontalLayout.addWidget(self.b_plot)
        self.b_previous = QtWidgets.QPushButton(SWPole)
        self.b_previous.setObjectName("b_previous")
        self.horizontalLayout.addWidget(self.b_previous)
        self.b_next = QtWidgets.QPushButton(SWPole)
        self.b_next.setObjectName("b_next")
        self.horizontalLayout.addWidget(self.b_next)
        self.main_layout.addLayout(self.horizontalLayout)

        self.retranslateUi(SWPole)
        QtCore.QMetaObject.connectSlotsByName(SWPole)

    def retranslateUi(self, SWPole):
        _translate = QtCore.QCoreApplication.translate
        SWPole.setWindowTitle(_translate("SWPole", "Form"))
        self.c_slot_type.setItemText(0, _translate("SWPole", "Pole Type 60"))
        self.c_slot_type.setItemText(1, _translate("SWPole", "Pole Type 61"))
        self.in_Zs.setText(_translate("SWPole", "Zs = 2*p = "))
        self.out_Slot_pitch.setText(_translate("SWPole", "Slot pitch = 2*Pi / Zs = "))
        self.b_plot.setText(_translate("SWPole", "Preview"))
        self.b_previous.setText(_translate("SWPole", "Previous"))
        self.b_next.setText(_translate("SWPole", "Next"))
from pyleecan.GUI.Tools.HelpButton import HelpButton
from pyleecan.GUI.Resources import pyleecan_rc
