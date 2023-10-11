# -*- coding: utf-8 -*-

# File generated according to PMSlot17.ui
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


class Ui_PMSlot17(object):
    def setupUi(self, PMSlot17):
        if not PMSlot17.objectName():
            PMSlot17.setObjectName(u"PMSlot17")
        PMSlot17.resize(887, 470)
        PMSlot17.setMinimumSize(QSize(630, 470))
        PMSlot17.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PMSlot17)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.img_slot = QLabel(PMSlot17)
        self.img_slot.setObjectName(u"img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setPixmap(
            QPixmap(u":/images/images/MachineSetup/WMSlot/SlotM17_mag_int_rotor.png")
        )
        self.img_slot.setScaledContents(False)
        self.img_slot.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.img_slot)

        self.txt_constraint = QTextEdit(PMSlot17)
        self.txt_constraint.setObjectName(u"txt_constraint")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.txt_constraint.sizePolicy().hasHeightForWidth()
        )
        self.txt_constraint.setSizePolicy(sizePolicy1)
        self.txt_constraint.setMaximumSize(QSize(16777215, 50))
        self.txt_constraint.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_constraint.setTextInteractionFlags(
            Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse
        )

        self.verticalLayout_2.addWidget(self.txt_constraint)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.scrollArea = QScrollArea(PMSlot17)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 450))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.w_mag = WWSlotMag(self.scrollAreaWidgetContents)
        self.w_mag.setObjectName(u"w_mag")

        self.verticalLayout.addWidget(self.w_mag)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.unit_Lmag = QLabel(self.scrollAreaWidgetContents)
        self.unit_Lmag.setObjectName(u"unit_Lmag")

        self.gridLayout.addWidget(self.unit_Lmag, 0, 2, 1, 1)

        self.lf_Lmag = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_Lmag.setObjectName(u"lf_Lmag")

        self.gridLayout.addWidget(self.lf_Lmag, 0, 1, 1, 1)

        self.in_Lmag = QLabel(self.scrollAreaWidgetContents)
        self.in_Lmag.setObjectName(u"in_Lmag")

        self.gridLayout.addWidget(self.in_Lmag, 0, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.w_out = WWSlotOut(self.scrollAreaWidgetContents)
        self.w_out.setObjectName(u"w_out")

        self.verticalLayout.addWidget(self.w_out)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.lf_Lmag, self.txt_constraint)

        self.retranslateUi(PMSlot17)

        QMetaObject.connectSlotsByName(PMSlot17)

    # setupUi

    def retranslateUi(self, PMSlot17):
        PMSlot17.setWindowTitle(QCoreApplication.translate("PMSlot17", u"Form", None))
        self.img_slot.setText("")
        self.txt_constraint.setHtml(
            QCoreApplication.translate(
                "PMSlot17",
                u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'DejaVu Sans'; font-size:8.15094pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt; font-weight:600; text-decoration: underline;">Constraints :</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">p=1</span></p></body></html>',
                None,
            )
        )
        self.unit_Lmag.setText(QCoreApplication.translate("PMSlot17", u"[m]", None))
        self.in_Lmag.setText(QCoreApplication.translate("PMSlot17", u"Lmag", None))

    # retranslateUi
