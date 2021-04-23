# -*- coding: utf-8 -*-

# File generated according to PWSlot25.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMachineSetup.SWSlot.WWSlotOut.WWSlotOut import WWSlotOut

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PWSlot25(object):
    def setupUi(self, PWSlot25):
        if not PWSlot25.objectName():
            PWSlot25.setObjectName(u"PWSlot25")
        PWSlot25.resize(728, 470)
        PWSlot25.setMinimumSize(QSize(630, 470))
        PWSlot25.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PWSlot25)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.img_slot = QLabel(PWSlot25)
        self.img_slot.setObjectName(u"img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setPixmap(
            QPixmap(u":/images/images/MachineSetup/WSlot/SlotW25.png")
        )
        self.img_slot.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.img_slot)

        self.textEdit = QTextEdit(PWSlot25)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setMinimumSize(QSize(0, 70))
        self.textEdit.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_2.addWidget(self.textEdit)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.widget = QWidget(PWSlot25)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(250, 0))
        self.widget.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.in_W3 = QLabel(self.widget)
        self.in_W3.setObjectName(u"in_W3")

        self.gridLayout.addWidget(self.in_W3, 0, 0, 1, 1)

        self.lf_W3 = FloatEdit(self.widget)
        self.lf_W3.setObjectName(u"lf_W3")

        self.gridLayout.addWidget(self.lf_W3, 0, 1, 1, 1)

        self.unit_W3 = QLabel(self.widget)
        self.unit_W3.setObjectName(u"unit_W3")

        self.gridLayout.addWidget(self.unit_W3, 0, 2, 1, 1)

        self.in_W4 = QLabel(self.widget)
        self.in_W4.setObjectName(u"in_W4")

        self.gridLayout.addWidget(self.in_W4, 1, 0, 1, 1)

        self.lf_W4 = FloatEdit(self.widget)
        self.lf_W4.setObjectName(u"lf_W4")

        self.gridLayout.addWidget(self.lf_W4, 1, 1, 1, 1)

        self.unit_W4 = QLabel(self.widget)
        self.unit_W4.setObjectName(u"unit_W4")

        self.gridLayout.addWidget(self.unit_W4, 1, 2, 1, 1)

        self.in_H1 = QLabel(self.widget)
        self.in_H1.setObjectName(u"in_H1")

        self.gridLayout.addWidget(self.in_H1, 2, 0, 1, 1)

        self.lf_H1 = FloatEdit(self.widget)
        self.lf_H1.setObjectName(u"lf_H1")

        self.gridLayout.addWidget(self.lf_H1, 2, 1, 1, 1)

        self.unit_H1 = QLabel(self.widget)
        self.unit_H1.setObjectName(u"unit_H1")

        self.gridLayout.addWidget(self.unit_H1, 2, 2, 1, 1)

        self.in_H2 = QLabel(self.widget)
        self.in_H2.setObjectName(u"in_H2")

        self.gridLayout.addWidget(self.in_H2, 3, 0, 1, 1)

        self.lf_H2 = FloatEdit(self.widget)
        self.lf_H2.setObjectName(u"lf_H2")

        self.gridLayout.addWidget(self.lf_H2, 3, 1, 1, 1)

        self.unit_H2 = QLabel(self.widget)
        self.unit_H2.setObjectName(u"unit_H2")

        self.gridLayout.addWidget(self.unit_H2, 3, 2, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.w_out = WWSlotOut(self.widget)
        self.w_out.setObjectName(u"w_out")

        self.verticalLayout.addWidget(self.w_out)

        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(PWSlot25)

        QMetaObject.connectSlotsByName(PWSlot25)

    # setupUi

    def retranslateUi(self, PWSlot25):
        PWSlot25.setWindowTitle(QCoreApplication.translate("PWSlot25", u"Form", None))
        self.img_slot.setText("")
        self.textEdit.setHtml(
            QCoreApplication.translate(
                "PWSlot25",
                u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Constant tooth width</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Slot edges are not radial</span></p></body></html>',
                None,
            )
        )
        self.in_W3.setText(QCoreApplication.translate("PWSlot25", u"W3", None))
        self.unit_W3.setText(QCoreApplication.translate("PWSlot25", u"m", None))
        self.in_W4.setText(QCoreApplication.translate("PWSlot25", u"W4", None))
        self.unit_W4.setText(QCoreApplication.translate("PWSlot25", u"m", None))
        self.in_H1.setText(QCoreApplication.translate("PWSlot25", u"H1", None))
        self.unit_H1.setText(QCoreApplication.translate("PWSlot25", u"m", None))
        self.in_H2.setText(QCoreApplication.translate("PWSlot25", u"H2", None))
        self.unit_H2.setText(QCoreApplication.translate("PWSlot25", u"m", None))

    # retranslateUi
