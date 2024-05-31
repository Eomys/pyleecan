# -*- coding: utf-8 -*-

# File generated according to WSlotCirc.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMachineSetup.SWSlot.WWSlotOut.WWSlotOut import WWSlotOut

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_WSlotCirc(object):
    def setupUi(self, WSlotCirc):
        if not WSlotCirc.objectName():
            WSlotCirc.setObjectName("WSlotCirc")
        WSlotCirc.resize(933, 470)
        WSlotCirc.setMinimumSize(QSize(630, 470))
        WSlotCirc.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(WSlotCirc)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.img_slot = QLabel(WSlotCirc)
        self.img_slot.setObjectName("img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setPixmap(
            QPixmap(":/images/images/MachineSetup/WMSlot/SlotCirc_empty_int_rot.png")
        )
        self.img_slot.setScaledContents(False)
        self.img_slot.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.img_slot)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.scrollArea = QScrollArea(WSlotCirc)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 446))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.in_H0_bore = QLabel(self.scrollAreaWidgetContents)
        self.in_H0_bore.setObjectName("in_H0_bore")

        self.horizontalLayout_2.addWidget(self.in_H0_bore)

        self.c_H0_bore = QComboBox(self.scrollAreaWidgetContents)
        self.c_H0_bore.addItem("")
        self.c_H0_bore.addItem("")
        self.c_H0_bore.setObjectName("c_H0_bore")

        self.horizontalLayout_2.addWidget(self.c_H0_bore)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.unit_H0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H0.setObjectName("unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 1, 2, 1, 1)

        self.in_H0 = QLabel(self.scrollAreaWidgetContents)
        self.in_H0.setObjectName("in_H0")

        self.gridLayout.addWidget(self.in_H0, 1, 0, 1, 1)

        self.unit_W0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W0.setObjectName("unit_W0")

        self.gridLayout.addWidget(self.unit_W0, 0, 2, 1, 1)

        self.in_W0 = QLabel(self.scrollAreaWidgetContents)
        self.in_W0.setObjectName("in_W0")

        self.gridLayout.addWidget(self.in_W0, 0, 0, 1, 1)

        self.lf_H0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H0.setObjectName("lf_H0")

        self.gridLayout.addWidget(self.lf_H0, 1, 1, 1, 1)

        self.lf_W0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W0.setObjectName("lf_W0")

        self.gridLayout.addWidget(self.lf_W0, 0, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.w_out = WWSlotOut(self.scrollAreaWidgetContents)
        self.w_out.setObjectName("w_out")

        self.verticalLayout.addWidget(self.w_out)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.lf_W0, self.lf_H0)

        self.retranslateUi(WSlotCirc)

        QMetaObject.connectSlotsByName(WSlotCirc)

    # setupUi

    def retranslateUi(self, WSlotCirc):
        WSlotCirc.setWindowTitle(QCoreApplication.translate("WSlotCirc", "Form", None))
        self.img_slot.setText("")
        self.in_H0_bore.setText(
            QCoreApplication.translate("WSlotCirc", "H0 definition:", None)
        )
        self.c_H0_bore.setItemText(
            0, QCoreApplication.translate("WSlotCirc", "Opening Arc", None)
        )
        self.c_H0_bore.setItemText(
            1, QCoreApplication.translate("WSlotCirc", "Opening Segment", None)
        )

        self.unit_H0.setText(QCoreApplication.translate("WSlotCirc", "[m]", None))
        self.in_H0.setText(QCoreApplication.translate("WSlotCirc", "H0", None))
        self.unit_W0.setText(QCoreApplication.translate("WSlotCirc", "[m]", None))
        self.in_W0.setText(QCoreApplication.translate("WSlotCirc", "W0", None))

    # retranslateUi
