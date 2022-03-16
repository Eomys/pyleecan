# -*- coding: utf-8 -*-

# File generated according to SMSlot.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyleecan.GUI.Tools.HelpButton import HelpButton
from .....GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SMSlot(object):
    def setupUi(self, SMSlot):
        if not SMSlot.objectName():
            SMSlot.setObjectName("SMSlot")
        SMSlot.resize(650, 550)
        SMSlot.setMinimumSize(QSize(650, 0))
        self.main_layout = QVBoxLayout(SMSlot)
        self.main_layout.setObjectName("main_layout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.b_help = HelpButton(SMSlot)
        self.b_help.setObjectName("b_help")
        self.b_help.setPixmap(QPixmap(":/images/images/icon/help_16.png"))

        self.horizontalLayout_2.addWidget(self.b_help)

        self.c_slot_type = QComboBox(SMSlot)
        self.c_slot_type.addItem("")
        self.c_slot_type.addItem("")
        self.c_slot_type.addItem("")
        self.c_slot_type.setObjectName("c_slot_type")

        self.horizontalLayout_2.addWidget(self.c_slot_type)

        self.out_Slot_pitch = QLabel(SMSlot)
        self.out_Slot_pitch.setObjectName("out_Slot_pitch")

        self.horizontalLayout_2.addWidget(self.out_Slot_pitch)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.main_layout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.w_mat = WMatSelect(SMSlot)
        self.w_mat.setObjectName("w_mat")

        self.horizontalLayout_3.addWidget(self.w_mat)

        self.in_type_magnetization = QLabel(SMSlot)
        self.in_type_magnetization.setObjectName("in_type_magnetization")

        self.horizontalLayout_3.addWidget(self.in_type_magnetization)

        self.c_type_magnetization = QComboBox(SMSlot)
        self.c_type_magnetization.addItem("")
        self.c_type_magnetization.addItem("")
        self.c_type_magnetization.addItem("")
        self.c_type_magnetization.setObjectName("c_type_magnetization")

        self.horizontalLayout_3.addWidget(self.c_type_magnetization)

        self.main_layout.addLayout(self.horizontalLayout_3)

        self.w_slot = QWidget(SMSlot)
        self.w_slot.setObjectName("w_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_slot.sizePolicy().hasHeightForWidth())
        self.w_slot.setSizePolicy(sizePolicy)

        self.main_layout.addWidget(self.w_slot)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.b_plot = QPushButton(SMSlot)
        self.b_plot.setObjectName("b_plot")

        self.horizontalLayout.addWidget(self.b_plot)

        self.b_previous = QPushButton(SMSlot)
        self.b_previous.setObjectName("b_previous")

        self.horizontalLayout.addWidget(self.b_previous)

        self.b_next = QPushButton(SMSlot)
        self.b_next.setObjectName("b_next")

        self.horizontalLayout.addWidget(self.b_next)

        self.main_layout.addLayout(self.horizontalLayout)

        self.retranslateUi(SMSlot)

        QMetaObject.connectSlotsByName(SMSlot)

    # setupUi

    def retranslateUi(self, SMSlot):
        SMSlot.setWindowTitle(QCoreApplication.translate("SMSlot", "Form", None))
        self.b_help.setText("")
        self.c_slot_type.setItemText(
            0, QCoreApplication.translate("SMSlot", "Slot Type 10", None)
        )
        self.c_slot_type.setItemText(
            1, QCoreApplication.translate("SMSlot", "Slot Type 11", None)
        )
        self.c_slot_type.setItemText(
            2, QCoreApplication.translate("SMSlot", "Slot Type 12", None)
        )

        self.out_Slot_pitch.setText(
            QCoreApplication.translate("SMSlot", "p = ? Slot pitch = 1.35 rad", None)
        )
        self.in_type_magnetization.setText(
            QCoreApplication.translate("SMSlot", "type_magnetization", None)
        )
        self.c_type_magnetization.setItemText(
            0, QCoreApplication.translate("SMSlot", "Radial", None)
        )
        self.c_type_magnetization.setItemText(
            1, QCoreApplication.translate("SMSlot", "Parallel", None)
        )
        self.c_type_magnetization.setItemText(
            2, QCoreApplication.translate("SMSlot", "HallBach", None)
        )

        self.b_plot.setText(QCoreApplication.translate("SMSlot", "Preview", None))
        self.b_previous.setText(QCoreApplication.translate("SMSlot", "Previous", None))
        self.b_next.setText(QCoreApplication.translate("SMSlot", "Next", None))

    # retranslateUi
