# -*- coding: utf-8 -*-

# File generated according to WSlotMag.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *


class Ui_WSlotMag(object):
    def setupUi(self, WSlotMag):
        if not WSlotMag.objectName():
            WSlotMag.setObjectName("WSlotMag")
        WSlotMag.resize(760, 490)
        WSlotMag.setMinimumSize(QSize(760, 490))
        self.main_layout = QVBoxLayout(WSlotMag)
        self.main_layout.setSpacing(4)
        self.main_layout.setObjectName("main_layout")
        self.main_layout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.c_slot_type = QComboBox(WSlotMag)
        self.c_slot_type.addItem("")
        self.c_slot_type.addItem("")
        self.c_slot_type.addItem("")
        self.c_slot_type.addItem("")
        self.c_slot_type.addItem("")
        self.c_slot_type.addItem("")
        self.c_slot_type.addItem("")
        self.c_slot_type.addItem("")
        self.c_slot_type.setObjectName("c_slot_type")

        self.horizontalLayout.addWidget(self.c_slot_type)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.main_layout.addLayout(self.horizontalLayout)

        self.w_slot = QWidget(WSlotMag)
        self.w_slot.setObjectName("w_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_slot.sizePolicy().hasHeightForWidth())
        self.w_slot.setSizePolicy(sizePolicy)
        self.w_slot.setMinimumSize(QSize(750, 450))

        self.main_layout.addWidget(self.w_slot)

        self.retranslateUi(WSlotMag)

        QMetaObject.connectSlotsByName(WSlotMag)

    # setupUi

    def retranslateUi(self, WSlotMag):
        WSlotMag.setWindowTitle(QCoreApplication.translate("WSlotMag", "Form", None))
        self.c_slot_type.setItemText(
            0, QCoreApplication.translate("WSlotMag", "Slot Type 50", None)
        )
        self.c_slot_type.setItemText(
            1, QCoreApplication.translate("WSlotMag", "Slot Type 51", None)
        )
        self.c_slot_type.setItemText(
            2, QCoreApplication.translate("WSlotMag", "Slot Type 52", None)
        )
        self.c_slot_type.setItemText(
            3, QCoreApplication.translate("WSlotMag", "Slot Type 52 R", None)
        )
        self.c_slot_type.setItemText(
            4, QCoreApplication.translate("WSlotMag", "Slot Type 53", None)
        )
        self.c_slot_type.setItemText(
            5, QCoreApplication.translate("WSlotMag", "Slot Type 54", None)
        )
        self.c_slot_type.setItemText(
            6, QCoreApplication.translate("WSlotMag", "Slot Type 55", None)
        )
        self.c_slot_type.setItemText(
            7, QCoreApplication.translate("WSlotMag", "Slot Type 56", None)
        )

    # retranslateUi
