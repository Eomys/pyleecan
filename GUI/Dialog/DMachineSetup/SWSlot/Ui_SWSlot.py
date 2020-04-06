# -*- coding: utf-8 -*-

# File generated according to SWSlot.ui
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SWSlot(object):
    def setupUi(self, SWSlot):
        SWSlot.setObjectName("SWSlot")
        SWSlot.resize(650, 550)
        SWSlot.setMinimumSize(QtCore.QSize(650, 550))
        self.main_layout = QtWidgets.QVBoxLayout(SWSlot)
        self.main_layout.setObjectName("main_layout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.b_help = HelpButton(SWSlot)
        self.b_help.setText("")
        self.b_help.setPixmap(QtGui.QPixmap(":/images/images/icon/help_16.png"))
        self.b_help.setObjectName("b_help")
        self.horizontalLayout_2.addWidget(self.b_help)
        self.c_slot_type = QtWidgets.QComboBox(SWSlot)
        self.c_slot_type.setObjectName("c_slot_type")
        self.c_slot_type.addItem("")
        self.c_slot_type.addItem("")
        self.c_slot_type.addItem("")
        self.horizontalLayout_2.addWidget(self.c_slot_type)
        self.in_Zs = QtWidgets.QLabel(SWSlot)
        self.in_Zs.setObjectName("in_Zs")
        self.horizontalLayout_2.addWidget(self.in_Zs)
        self.si_Zs = QtWidgets.QSpinBox(SWSlot)
        self.si_Zs.setMaximum(20)
        self.si_Zs.setObjectName("si_Zs")
        self.horizontalLayout_2.addWidget(self.si_Zs)
        self.out_Slot_pitch = QtWidgets.QLabel(SWSlot)
        self.out_Slot_pitch.setObjectName("out_Slot_pitch")
        self.horizontalLayout_2.addWidget(self.out_Slot_pitch)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.main_layout.addLayout(self.horizontalLayout_2)
        self.w_slot = QtWidgets.QWidget(SWSlot)
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
        self.b_plot = QtWidgets.QPushButton(SWSlot)
        self.b_plot.setObjectName("b_plot")
        self.horizontalLayout.addWidget(self.b_plot)
        self.b_previous = QtWidgets.QPushButton(SWSlot)
        self.b_previous.setObjectName("b_previous")
        self.horizontalLayout.addWidget(self.b_previous)
        self.b_next = QtWidgets.QPushButton(SWSlot)
        self.b_next.setObjectName("b_next")
        self.horizontalLayout.addWidget(self.b_next)
        self.main_layout.addLayout(self.horizontalLayout)

        self.retranslateUi(SWSlot)
        QtCore.QMetaObject.connectSlotsByName(SWSlot)

    def retranslateUi(self, SWSlot):
        _translate = QtCore.QCoreApplication.translate
        SWSlot.setWindowTitle(_translate("SWSlot", "Form"))
        self.c_slot_type.setItemText(0, _translate("SWSlot", "Slot Type 10"))
        self.c_slot_type.setItemText(1, _translate("SWSlot", "Slot Type 11"))
        self.c_slot_type.setItemText(2, _translate("SWSlot", "Slot Type 12"))
        self.in_Zs.setText(_translate("SWSlot", "Zs :"))
        self.out_Slot_pitch.setText(_translate("SWSlot", "Slot pitch = 2*Pi / Zs = "))
        self.b_plot.setText(_translate("SWSlot", "Preview"))
        self.b_previous.setText(_translate("SWSlot", "Previous"))
        self.b_next.setText(_translate("SWSlot", "Next"))
from pyleecan.GUI.Tools.HelpButton import HelpButton
from pyleecan.GUI.Resources import pyleecan_rc
