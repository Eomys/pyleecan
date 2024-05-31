# -*- coding: utf-8 -*-

# File generated according to SWPole.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from pyleecan.GUI.Tools.HelpButton import HelpButton

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SWPole(object):
    def setupUi(self, SWPole):
        if not SWPole.objectName():
            SWPole.setObjectName("SWPole")
        SWPole.resize(650, 550)
        SWPole.setMinimumSize(QSize(650, 550))
        self.main_layout = QVBoxLayout(SWPole)
        self.main_layout.setObjectName("main_layout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.b_help = HelpButton(SWPole)
        self.b_help.setObjectName("b_help")
        self.b_help.setPixmap(QPixmap(":/images/images/icon/help_16.png"))

        self.horizontalLayout_2.addWidget(self.b_help)

        self.c_slot_type = QComboBox(SWPole)
        self.c_slot_type.addItem("")
        self.c_slot_type.addItem("")
        self.c_slot_type.addItem("")
        self.c_slot_type.addItem("")
        self.c_slot_type.addItem("")
        self.c_slot_type.setObjectName("c_slot_type")

        self.horizontalLayout_2.addWidget(self.c_slot_type)

        self.in_Zs = QLabel(SWPole)
        self.in_Zs.setObjectName("in_Zs")

        self.horizontalLayout_2.addWidget(self.in_Zs)

        self.out_Slot_pitch = QLabel(SWPole)
        self.out_Slot_pitch.setObjectName("out_Slot_pitch")

        self.horizontalLayout_2.addWidget(self.out_Slot_pitch)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.main_layout.addLayout(self.horizontalLayout_2)

        self.w_slot = QWidget(SWPole)
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

        self.b_plot = QPushButton(SWPole)
        self.b_plot.setObjectName("b_plot")

        self.horizontalLayout.addWidget(self.b_plot)

        self.b_previous = QPushButton(SWPole)
        self.b_previous.setObjectName("b_previous")

        self.horizontalLayout.addWidget(self.b_previous)

        self.b_next = QPushButton(SWPole)
        self.b_next.setObjectName("b_next")

        self.horizontalLayout.addWidget(self.b_next)

        self.main_layout.addLayout(self.horizontalLayout)

        self.retranslateUi(SWPole)

        QMetaObject.connectSlotsByName(SWPole)

    # setupUi

    def retranslateUi(self, SWPole):
        SWPole.setWindowTitle(QCoreApplication.translate("SWPole", "Form", None))
        self.b_help.setText("")
        self.c_slot_type.setItemText(
            0, QCoreApplication.translate("SWPole", "Pole Type 60", None)
        )
        self.c_slot_type.setItemText(
            1, QCoreApplication.translate("SWPole", "Pole Type 61", None)
        )
        self.c_slot_type.setItemText(
            2, QCoreApplication.translate("SWPole", "Pole Type 62", None)
        )
        self.c_slot_type.setItemText(
            3, QCoreApplication.translate("SWPole", "Pole Type 63", None)
        )
        self.c_slot_type.setItemText(
            4, QCoreApplication.translate("SWPole", "pole Type 29", None)
        )

        self.in_Zs.setText(QCoreApplication.translate("SWPole", "Zs = 2*p = ", None))
        self.out_Slot_pitch.setText(
            QCoreApplication.translate("SWPole", "Slot pitch = 2*Pi / Zs = ", None)
        )
        self.b_plot.setText(QCoreApplication.translate("SWPole", "Preview", None))
        self.b_previous.setText(QCoreApplication.translate("SWPole", "Previous", None))
        self.b_next.setText(QCoreApplication.translate("SWPole", "Next", None))

    # retranslateUi
