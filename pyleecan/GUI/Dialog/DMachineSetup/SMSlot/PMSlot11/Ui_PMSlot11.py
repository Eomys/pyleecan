# -*- coding: utf-8 -*-

# File generated according to PMSlot11.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMachineSetup.SWSlot.WWSlotOut.WWSlotOut import WWSlotOut
from ......GUI.Dialog.DMachineSetup.SMSlot.WWSlotMag.WWSlotMag import WWSlotMag
from ......GUI.Dialog.DMatLib.WMatSelect.WMatSelectV import WMatSelectV

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PMSlot11(object):
    def setupUi(self, PMSlot11):
        if not PMSlot11.objectName():
            PMSlot11.setObjectName("PMSlot11")
        PMSlot11.resize(866, 555)
        PMSlot11.setMinimumSize(QSize(630, 470))
        PMSlot11.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PMSlot11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.img_slot = QLabel(PMSlot11)
        self.img_slot.setObjectName("img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setPixmap(
            QPixmap(":/images/images/MachineSetup/WMSlot/SlotM11_mag_int_rotor.png")
        )
        self.img_slot.setScaledContents(False)
        self.img_slot.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.img_slot)

        self.txt_constraint = QTextEdit(PMSlot11)
        self.txt_constraint.setObjectName("txt_constraint")
        sizePolicy.setHeightForWidth(
            self.txt_constraint.sizePolicy().hasHeightForWidth()
        )
        self.txt_constraint.setSizePolicy(sizePolicy)
        self.txt_constraint.setMinimumSize(QSize(0, 0))
        self.txt_constraint.setMaximumSize(QSize(16777215, 70))
        self.txt_constraint.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_constraint.setTextInteractionFlags(
            Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse
        )

        self.verticalLayout_2.addWidget(self.txt_constraint)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.scrollArea = QScrollArea(PMSlot11)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 535))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.w_mag = WWSlotMag(self.scrollAreaWidgetContents)
        self.w_mag.setObjectName("w_mag")

        self.verticalLayout.addWidget(self.w_mag)

        self.g_key = QGroupBox(self.scrollAreaWidgetContents)
        self.g_key.setObjectName("g_key")
        self.g_key.setCheckable(True)
        self.g_key.setChecked(False)
        self.gridLayout_2 = QGridLayout(self.g_key)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.w_key_mat = WMatSelectV(self.g_key)
        self.w_key_mat.setObjectName("w_key_mat")

        self.gridLayout_2.addWidget(self.w_key_mat, 9, 0, 1, 2)

        self.verticalLayout.addWidget(self.g_key)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.unit_H1 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H1.setObjectName("unit_H1")

        self.gridLayout.addWidget(self.unit_H1, 4, 2, 1, 1)

        self.lf_W1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W1.setObjectName("lf_W1")

        self.gridLayout.addWidget(self.lf_W1, 2, 1, 1, 1)

        self.in_W1 = QLabel(self.scrollAreaWidgetContents)
        self.in_W1.setObjectName("in_W1")

        self.gridLayout.addWidget(self.in_W1, 2, 0, 1, 1)

        self.c_W0_unit = QComboBox(self.scrollAreaWidgetContents)
        self.c_W0_unit.addItem("")
        self.c_W0_unit.addItem("")
        self.c_W0_unit.setObjectName("c_W0_unit")

        self.gridLayout.addWidget(self.c_W0_unit, 0, 2, 1, 1)

        self.lf_H1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H1.setObjectName("lf_H1")

        self.gridLayout.addWidget(self.lf_H1, 4, 1, 1, 1)

        self.in_W0 = QLabel(self.scrollAreaWidgetContents)
        self.in_W0.setObjectName("in_W0")

        self.gridLayout.addWidget(self.in_W0, 0, 0, 1, 1)

        self.c_W1_unit = QComboBox(self.scrollAreaWidgetContents)
        self.c_W1_unit.addItem("")
        self.c_W1_unit.addItem("")
        self.c_W1_unit.setObjectName("c_W1_unit")

        self.gridLayout.addWidget(self.c_W1_unit, 2, 2, 1, 1)

        self.in_H1 = QLabel(self.scrollAreaWidgetContents)
        self.in_H1.setObjectName("in_H1")

        self.gridLayout.addWidget(self.in_H1, 4, 0, 1, 1)

        self.lf_W0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W0.setObjectName("lf_W0")
        self.lf_W0.setMinimumSize(QSize(90, 0))

        self.gridLayout.addWidget(self.lf_W0, 0, 1, 1, 1)

        self.in_H0 = QLabel(self.scrollAreaWidgetContents)
        self.in_H0.setObjectName("in_H0")

        self.gridLayout.addWidget(self.in_H0, 1, 0, 1, 1)

        self.lf_H0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H0.setObjectName("lf_H0")

        self.gridLayout.addWidget(self.lf_H0, 1, 1, 1, 1)

        self.unit_H0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H0.setObjectName("unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 1, 2, 1, 1)

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

        QWidget.setTabOrder(self.g_key, self.lf_W0)
        QWidget.setTabOrder(self.lf_W0, self.lf_H0)
        QWidget.setTabOrder(self.lf_H0, self.lf_W1)
        QWidget.setTabOrder(self.lf_W1, self.lf_H1)
        QWidget.setTabOrder(self.lf_H1, self.c_W0_unit)
        QWidget.setTabOrder(self.c_W0_unit, self.c_W1_unit)
        QWidget.setTabOrder(self.c_W1_unit, self.txt_constraint)
        QWidget.setTabOrder(self.txt_constraint, self.scrollArea)

        self.retranslateUi(PMSlot11)

        QMetaObject.connectSlotsByName(PMSlot11)

    # setupUi

    def retranslateUi(self, PMSlot11):
        PMSlot11.setWindowTitle(QCoreApplication.translate("PMSlot11", "Form", None))
        self.img_slot.setText("")
        self.txt_constraint.setHtml(
            QCoreApplication.translate(
                "PMSlot11",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'DejaVu Sans'; font-size:8.15094pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt; font-weight:600; text-decoration: underline;">Constraints :</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">W1 \u2264 W0</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">W1 &lt; \u03c0 / p</span></p></body></html>',
                None,
            )
        )
        self.g_key.setTitle(QCoreApplication.translate("PMSlot11", "Key", None))
        self.unit_H1.setText(QCoreApplication.translate("PMSlot11", "[m]", None))
        self.in_W1.setText(QCoreApplication.translate("PMSlot11", "W1", None))
        self.c_W0_unit.setItemText(
            0, QCoreApplication.translate("PMSlot11", "rad", None)
        )
        self.c_W0_unit.setItemText(
            1, QCoreApplication.translate("PMSlot11", "deg", None)
        )

        self.in_W0.setText(QCoreApplication.translate("PMSlot11", "W0", None))
        self.c_W1_unit.setItemText(
            0, QCoreApplication.translate("PMSlot11", "rad", None)
        )
        self.c_W1_unit.setItemText(
            1, QCoreApplication.translate("PMSlot11", "deg", None)
        )

        self.in_H1.setText(QCoreApplication.translate("PMSlot11", "H1", None))
        self.in_H0.setText(QCoreApplication.translate("PMSlot11", "H0", None))
        self.unit_H0.setText(QCoreApplication.translate("PMSlot11", "[m]", None))

    # retranslateUi
