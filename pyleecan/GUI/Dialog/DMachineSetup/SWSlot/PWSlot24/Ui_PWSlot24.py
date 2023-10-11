# -*- coding: utf-8 -*-

# File generated according to PWSlot24.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMachineSetup.SWSlot.WWSlotOut.WWSlotOut import WWSlotOut

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PWSlot24(object):
    def setupUi(self, PWSlot24):
        if not PWSlot24.objectName():
            PWSlot24.setObjectName(u"PWSlot24")
        PWSlot24.resize(792, 470)
        PWSlot24.setMinimumSize(QSize(270, 470))
        PWSlot24.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PWSlot24)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.img_slot = QLabel(PWSlot24)
        self.img_slot.setObjectName(u"img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setPixmap(
            QPixmap(u":/images/images/MachineSetup/WSlot/SlotW24_wind_ext_stator.png")
        )
        self.img_slot.setScaledContents(False)
        self.img_slot.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.img_slot)

        self.textEdit = QTextEdit(PWSlot24)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_2.addWidget(self.textEdit)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.scrollArea = QScrollArea(PWSlot24)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 446))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.in_W3 = QLabel(self.scrollAreaWidgetContents)
        self.in_W3.setObjectName(u"in_W3")

        self.gridLayout.addWidget(self.in_W3, 0, 0, 1, 1)

        self.lf_W3 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W3.setObjectName(u"lf_W3")

        self.gridLayout.addWidget(self.lf_W3, 0, 1, 1, 1)

        self.unit_W3 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W3.setObjectName(u"unit_W3")

        self.gridLayout.addWidget(self.unit_W3, 0, 2, 1, 1)

        self.in_H2 = QLabel(self.scrollAreaWidgetContents)
        self.in_H2.setObjectName(u"in_H2")

        self.gridLayout.addWidget(self.in_H2, 1, 0, 1, 1)

        self.lf_H2 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H2.setObjectName(u"lf_H2")

        self.gridLayout.addWidget(self.lf_H2, 1, 1, 1, 1)

        self.unit_H2 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H2.setObjectName(u"unit_H2")

        self.gridLayout.addWidget(self.unit_H2, 1, 2, 1, 1)

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

        self.retranslateUi(PWSlot24)

        QMetaObject.connectSlotsByName(PWSlot24)

    # setupUi

    def retranslateUi(self, PWSlot24):
        PWSlot24.setWindowTitle(QCoreApplication.translate("PWSlot24", u"Form", None))
        self.img_slot.setText("")
        self.textEdit.setHtml(
            QCoreApplication.translate(
                "PWSlot24",
                u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'DejaVu Sans'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">Constant tooth width</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">Slot edges are not radial</span></p></body></html>',
                None,
            )
        )
        self.in_W3.setText(QCoreApplication.translate("PWSlot24", u"W3", None))
        self.unit_W3.setText(QCoreApplication.translate("PWSlot24", u"m", None))
        self.in_H2.setText(QCoreApplication.translate("PWSlot24", u"H2", None))
        self.unit_H2.setText(QCoreApplication.translate("PWSlot24", u"m", None))

    # retranslateUi
