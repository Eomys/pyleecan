# -*- coding: utf-8 -*-

# File generated according to PMSlot19.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMachineSetup.SWSlot.WWSlotOut.WWSlotOut import WWSlotOut
from ......GUI.Dialog.DMachineSetup.SMSlot.WWSlotMag.WWSlotMag import WWSlotMag

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PMSlot19(object):
    def setupUi(self, PMSlot19):
        if not PMSlot19.objectName():
            PMSlot19.setObjectName(u"PMSlot19")
        PMSlot19.resize(1076, 643)
        PMSlot19.setMinimumSize(QSize(630, 470))
        PMSlot19.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PMSlot19)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.img_slot = QLabel(PMSlot19)
        self.img_slot.setObjectName(u"img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setPixmap(
            QPixmap(u":/images/images/MachineSetup/WMSlot/SlotM19_mag_int_rotor.png")
        )
        self.img_slot.setScaledContents(False)
        self.img_slot.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.img_slot)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.scrollArea = QScrollArea(PMSlot19)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 619))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.w_mag = WWSlotMag(self.scrollAreaWidgetContents)
        self.w_mag.setObjectName(u"w_mag")

        self.verticalLayout_3.addWidget(self.w_mag)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.unit_H0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H0.setObjectName(u"unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 2, 2, 1, 1)

        self.lf_H0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H0.setObjectName(u"lf_H0")

        self.gridLayout.addWidget(self.lf_H0, 2, 1, 1, 1)

        self.in_W0 = QLabel(self.scrollAreaWidgetContents)
        self.in_W0.setObjectName(u"in_W0")

        self.gridLayout.addWidget(self.in_W0, 0, 0, 1, 1)

        self.in_H0 = QLabel(self.scrollAreaWidgetContents)
        self.in_H0.setObjectName(u"in_H0")

        self.gridLayout.addWidget(self.in_H0, 2, 0, 1, 1)

        self.unit_W0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W0.setObjectName(u"unit_W0")

        self.gridLayout.addWidget(self.unit_W0, 0, 2, 1, 1)

        self.lf_W1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W1.setObjectName(u"lf_W1")

        self.gridLayout.addWidget(self.lf_W1, 1, 1, 1, 1)

        self.lf_W0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W0.setObjectName(u"lf_W0")

        self.gridLayout.addWidget(self.lf_W0, 0, 1, 1, 1)

        self.in_W1 = QLabel(self.scrollAreaWidgetContents)
        self.in_W1.setObjectName(u"in_W1")

        self.gridLayout.addWidget(self.in_W1, 1, 0, 1, 1)

        self.unit_W1 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W1.setObjectName(u"unit_W1")

        self.gridLayout.addWidget(self.unit_W1, 1, 2, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.w_out = WWSlotOut(self.scrollAreaWidgetContents)
        self.w_out.setObjectName(u"w_out")

        self.verticalLayout_3.addWidget(self.w_out)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.lf_W0, self.lf_W1)
        QWidget.setTabOrder(self.lf_W1, self.lf_H0)

        self.retranslateUi(PMSlot19)

        QMetaObject.connectSlotsByName(PMSlot19)

    # setupUi

    def retranslateUi(self, PMSlot19):
        PMSlot19.setWindowTitle(QCoreApplication.translate("PMSlot19", u"Form", None))
        self.img_slot.setText("")
        self.unit_H0.setText(QCoreApplication.translate("PMSlot19", u"[m]", None))
        self.in_W0.setText(QCoreApplication.translate("PMSlot19", u"W0", None))
        self.in_H0.setText(QCoreApplication.translate("PMSlot19", u"H0", None))
        self.unit_W0.setText(QCoreApplication.translate("PMSlot19", u"[m]", None))
        self.in_W1.setText(QCoreApplication.translate("PMSlot19", u"W1", None))
        self.unit_W1.setText(QCoreApplication.translate("PMSlot19", u"[m]", None))

    # retranslateUi
