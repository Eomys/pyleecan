# -*- coding: utf-8 -*-

# File generated according to PWSlot22.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMachineSetup.SWSlot.WWSlotOut.WWSlotOut import WWSlotOut

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PWSlot22(object):
    def setupUi(self, PWSlot22):
        if not PWSlot22.objectName():
            PWSlot22.setObjectName(u"PWSlot22")
        PWSlot22.resize(630, 470)
        PWSlot22.setMinimumSize(QSize(630, 470))
        PWSlot22.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PWSlot22)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.img_slot = QLabel(PWSlot22)
        self.img_slot.setObjectName(u"img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setPixmap(
            QPixmap(u":/images/images/MachineSetup/WSlot/Slot 22.PNG")
        )
        self.img_slot.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.img_slot)

        self.txt_constraint = QTextEdit(PWSlot22)
        self.txt_constraint.setObjectName(u"txt_constraint")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.txt_constraint.sizePolicy().hasHeightForWidth()
        )
        self.txt_constraint.setSizePolicy(sizePolicy1)
        self.txt_constraint.setMaximumSize(QSize(16777215, 75))
        self.txt_constraint.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_constraint.setTextInteractionFlags(
            Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse
        )

        self.verticalLayout_2.addWidget(self.txt_constraint)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.in_W0 = QLabel(PWSlot22)
        self.in_W0.setObjectName(u"in_W0")

        self.gridLayout.addWidget(self.in_W0, 0, 0, 1, 1)

        self.lf_W0 = FloatEdit(PWSlot22)
        self.lf_W0.setObjectName(u"lf_W0")

        self.gridLayout.addWidget(self.lf_W0, 0, 1, 1, 1)

        self.in_W2 = QLabel(PWSlot22)
        self.in_W2.setObjectName(u"in_W2")

        self.gridLayout.addWidget(self.in_W2, 1, 0, 1, 1)

        self.lf_W2 = FloatEdit(PWSlot22)
        self.lf_W2.setObjectName(u"lf_W2")

        self.gridLayout.addWidget(self.lf_W2, 1, 1, 1, 1)

        self.in_H0 = QLabel(PWSlot22)
        self.in_H0.setObjectName(u"in_H0")

        self.gridLayout.addWidget(self.in_H0, 2, 0, 1, 1)

        self.lf_H0 = FloatEdit(PWSlot22)
        self.lf_H0.setObjectName(u"lf_H0")

        self.gridLayout.addWidget(self.lf_H0, 2, 1, 1, 1)

        self.unit_H0 = QLabel(PWSlot22)
        self.unit_H0.setObjectName(u"unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 2, 2, 1, 1)

        self.in_H2 = QLabel(PWSlot22)
        self.in_H2.setObjectName(u"in_H2")

        self.gridLayout.addWidget(self.in_H2, 3, 0, 1, 1)

        self.lf_H2 = FloatEdit(PWSlot22)
        self.lf_H2.setObjectName(u"lf_H2")

        self.gridLayout.addWidget(self.lf_H2, 3, 1, 1, 1)

        self.unit_H2 = QLabel(PWSlot22)
        self.unit_H2.setObjectName(u"unit_H2")

        self.gridLayout.addWidget(self.unit_H2, 3, 2, 1, 1)

        self.c_W0_unit = QComboBox(PWSlot22)
        self.c_W0_unit.addItem("")
        self.c_W0_unit.addItem("")
        self.c_W0_unit.setObjectName(u"c_W0_unit")
        self.c_W0_unit.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.c_W0_unit, 0, 2, 1, 1)

        self.c_W2_unit = QComboBox(PWSlot22)
        self.c_W2_unit.addItem("")
        self.c_W2_unit.addItem("")
        self.c_W2_unit.setObjectName(u"c_W2_unit")
        self.c_W2_unit.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.c_W2_unit, 1, 2, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.w_out = WWSlotOut(PWSlot22)
        self.w_out.setObjectName(u"w_out")

        self.verticalLayout.addWidget(self.w_out)

        self.horizontalLayout.addLayout(self.verticalLayout)

        QWidget.setTabOrder(self.lf_W0, self.lf_W2)
        QWidget.setTabOrder(self.lf_W2, self.lf_H0)
        QWidget.setTabOrder(self.lf_H0, self.lf_H2)
        QWidget.setTabOrder(self.lf_H2, self.txt_constraint)

        self.retranslateUi(PWSlot22)

        QMetaObject.connectSlotsByName(PWSlot22)

    # setupUi

    def retranslateUi(self, PWSlot22):
        PWSlot22.setWindowTitle(QCoreApplication.translate("PWSlot22", u"Form", None))
        self.img_slot.setText("")
        self.txt_constraint.setHtml(
            QCoreApplication.translate(
                "PWSlot22",
                u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; text-decoration: underline;">Constraints :</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">W0 &lt;= W2</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">W2 &lt;= 2*pi/Zs</span></p></body></html>',
                None,
            )
        )
        self.in_W0.setText(QCoreApplication.translate("PWSlot22", u"W0 :", None))
        self.in_W2.setText(QCoreApplication.translate("PWSlot22", u"W2 :", None))
        self.in_H0.setText(QCoreApplication.translate("PWSlot22", u"H0 :", None))
        self.unit_H0.setText(QCoreApplication.translate("PWSlot22", u"m", None))
        self.in_H2.setText(QCoreApplication.translate("PWSlot22", u"H2 :", None))
        self.unit_H2.setText(QCoreApplication.translate("PWSlot22", u"m", None))
        self.c_W0_unit.setItemText(
            0, QCoreApplication.translate("PWSlot22", u"rad", None)
        )
        self.c_W0_unit.setItemText(
            1, QCoreApplication.translate("PWSlot22", u"deg", None)
        )

        self.c_W2_unit.setItemText(
            0, QCoreApplication.translate("PWSlot22", u"rad", None)
        )
        self.c_W2_unit.setItemText(
            1, QCoreApplication.translate("PWSlot22", u"deg", None)
        )

    # retranslateUi
