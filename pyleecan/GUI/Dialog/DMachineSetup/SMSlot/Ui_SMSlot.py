# -*- coding: utf-8 -*-

# File generated according to SMSlot.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from pyleecan.GUI.Tools.HelpButton import HelpButton

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SMSlot(object):
    def setupUi(self, SMSlot):
        if not SMSlot.objectName():
            SMSlot.setObjectName("SMSlot")
        SMSlot.resize(827, 644)
        SMSlot.setMinimumSize(QSize(650, 0))
        self.main_layout = QVBoxLayout(SMSlot)
        self.main_layout.setObjectName("main_layout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.b_help = HelpButton(SMSlot)
        self.b_help.setObjectName("b_help")
        self.b_help.setPixmap(QPixmap(":/images/images/icon/help_16.png"))

        self.horizontalLayout_2.addWidget(self.b_help)

        self.in_NS_type = QLabel(SMSlot)
        self.in_NS_type.setObjectName("in_NS_type")

        self.horizontalLayout_2.addWidget(self.in_NS_type)

        self.c_NS_type = QComboBox(SMSlot)
        self.c_NS_type.addItem("")
        self.c_NS_type.addItem("")
        self.c_NS_type.setObjectName("c_NS_type")
        self.c_NS_type.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_2.addWidget(self.c_NS_type)

        self.out_Slot_pitch = QLabel(SMSlot)
        self.out_Slot_pitch.setObjectName("out_Slot_pitch")

        self.horizontalLayout_2.addWidget(self.out_Slot_pitch)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.main_layout.addLayout(self.horizontalLayout_2)

        self.tab_slot = QTabWidget(SMSlot)
        self.tab_slot.setObjectName("tab_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_slot.sizePolicy().hasHeightForWidth())
        self.tab_slot.setSizePolicy(sizePolicy)
        self.tab_slot.setMinimumSize(QSize(770, 550))
        self.tab_slot.setTabsClosable(False)

        self.main_layout.addWidget(self.tab_slot)

        self.verticalSpacer = QSpacerItem(
            20, 1, QSizePolicy.Minimum, QSizePolicy.Minimum
        )

        self.main_layout.addItem(self.verticalSpacer)

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

        self.tab_slot.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(SMSlot)

    # setupUi

    def retranslateUi(self, SMSlot):
        SMSlot.setWindowTitle(QCoreApplication.translate("SMSlot", "Form", None))
        self.b_help.setText("")
        self.in_NS_type.setText(
            QCoreApplication.translate("SMSlot", "Pole distribution", None)
        )
        self.c_NS_type.setItemText(
            0, QCoreApplication.translate("SMSlot", "Even (default)", None)
        )
        self.c_NS_type.setItemText(
            1, QCoreApplication.translate("SMSlot", "North different than South", None)
        )

        self.c_NS_type.setCurrentText(
            QCoreApplication.translate("SMSlot", "Even (default)", None)
        )
        self.out_Slot_pitch.setText(
            QCoreApplication.translate("SMSlot", "p = ? Slot pitch = 1.35 rad", None)
        )
        self.b_plot.setText(QCoreApplication.translate("SMSlot", "Preview", None))
        self.b_previous.setText(QCoreApplication.translate("SMSlot", "Previous", None))
        self.b_next.setText(QCoreApplication.translate("SMSlot", "Next", None))

    # retranslateUi
