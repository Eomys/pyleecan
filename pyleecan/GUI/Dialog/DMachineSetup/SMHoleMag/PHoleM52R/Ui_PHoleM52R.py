# -*- coding: utf-8 -*-

# File generated according to PHoleM52R.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ......GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect
from ......GUI.Tools.FloatEdit import FloatEdit

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PHoleM52R(object):
    def setupUi(self, PHoleM52R):
        if not PHoleM52R.objectName():
            PHoleM52R.setObjectName(u"PHoleM52R")
        PHoleM52R.resize(934, 440)
        PHoleM52R.setMinimumSize(QSize(740, 440))
        PHoleM52R.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PHoleM52R)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.img_slot = QLabel(PHoleM52R)
        self.img_slot.setObjectName(u"img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMinimumSize(QSize(0, 0))
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setPixmap(
            QPixmap(
                u":/images/images/MachineSetup/SMHoleMag/HoleM52R_mag_int_rotor.png"
            )
        )
        self.img_slot.setScaledContents(False)
        self.img_slot.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.img_slot)

        self.txt_constraint = QTextEdit(PHoleM52R)
        self.txt_constraint.setObjectName(u"txt_constraint")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.txt_constraint.sizePolicy().hasHeightForWidth()
        )
        self.txt_constraint.setSizePolicy(sizePolicy1)
        self.txt_constraint.setMinimumSize(QSize(200, 0))
        self.txt_constraint.setMaximumSize(QSize(16777215, 75))
        self.txt_constraint.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_constraint.setTextInteractionFlags(
            Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse
        )

        self.verticalLayout_3.addWidget(self.txt_constraint)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.scrollArea = QScrollArea(PHoleM52R)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 420))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.in_R0 = QLabel(self.scrollAreaWidgetContents)
        self.in_R0.setObjectName(u"in_R0")

        self.gridLayout.addWidget(self.in_R0, 5, 0, 1, 1)

        self.lf_R0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_R0.setObjectName(u"lf_R0")

        self.gridLayout.addWidget(self.lf_R0, 5, 1, 1, 1)

        self.unit_R0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_R0.setObjectName(u"unit_R0")

        self.gridLayout.addWidget(self.unit_R0, 5, 2, 1, 1)

        self.in_W1 = QLabel(self.scrollAreaWidgetContents)
        self.in_W1.setObjectName(u"in_W1")

        self.gridLayout.addWidget(self.in_W1, 4, 0, 1, 1)

        self.lf_W1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W1.setObjectName(u"lf_W1")

        self.gridLayout.addWidget(self.lf_W1, 4, 1, 1, 1)

        self.unit_W1 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W1.setObjectName(u"unit_W1")

        self.gridLayout.addWidget(self.unit_W1, 4, 2, 1, 1)

        self.lf_H0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H0.setObjectName(u"lf_H0")

        self.gridLayout.addWidget(self.lf_H0, 0, 1, 1, 1)

        self.in_H0 = QLabel(self.scrollAreaWidgetContents)
        self.in_H0.setObjectName(u"in_H0")

        self.gridLayout.addWidget(self.in_H0, 0, 0, 1, 1)

        self.unit_H1 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H1.setObjectName(u"unit_H1")

        self.gridLayout.addWidget(self.unit_H1, 1, 2, 1, 1)

        self.lf_H1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H1.setObjectName(u"lf_H1")

        self.gridLayout.addWidget(self.lf_H1, 1, 1, 1, 1)

        self.in_H1 = QLabel(self.scrollAreaWidgetContents)
        self.in_H1.setObjectName(u"in_H1")

        self.gridLayout.addWidget(self.in_H1, 1, 0, 1, 1)

        self.unit_H0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H0.setObjectName(u"unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 0, 2, 1, 1)

        self.in_H2 = QLabel(self.scrollAreaWidgetContents)
        self.in_H2.setObjectName(u"in_H2")

        self.gridLayout.addWidget(self.in_H2, 2, 0, 1, 1)

        self.lf_H2 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H2.setObjectName(u"lf_H2")

        self.gridLayout.addWidget(self.lf_H2, 2, 1, 1, 1)

        self.unit_H2 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H2.setObjectName(u"unit_H2")

        self.gridLayout.addWidget(self.unit_H2, 2, 2, 1, 1)

        self.in_W0 = QLabel(self.scrollAreaWidgetContents)
        self.in_W0.setObjectName(u"in_W0")

        self.gridLayout.addWidget(self.in_W0, 3, 0, 1, 1)

        self.lf_W0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W0.setObjectName(u"lf_W0")

        self.gridLayout.addWidget(self.lf_W0, 3, 1, 1, 1)

        self.unit_W0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W0.setObjectName(u"unit_W0")

        self.gridLayout.addWidget(self.unit_W0, 3, 2, 1, 1)

        self.verticalLayout_4.addLayout(self.gridLayout)

        self.w_mat_0 = WMatSelect(self.scrollAreaWidgetContents)
        self.w_mat_0.setObjectName(u"w_mat_0")
        self.w_mat_0.setMinimumSize(QSize(100, 0))

        self.verticalLayout_4.addWidget(self.w_mat_0)

        self.w_mat_1 = WMatSelect(self.scrollAreaWidgetContents)
        self.w_mat_1.setObjectName(u"w_mat_1")
        self.w_mat_1.setMinimumSize(QSize(100, 0))

        self.verticalLayout_4.addWidget(self.w_mat_1)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.g_output = QGroupBox(self.scrollAreaWidgetContents)
        self.g_output.setObjectName(u"g_output")
        self.g_output.setMinimumSize(QSize(200, 0))
        self.verticalLayout = QVBoxLayout(self.g_output)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.out_slot_surface = QLabel(self.g_output)
        self.out_slot_surface.setObjectName(u"out_slot_surface")

        self.verticalLayout.addWidget(self.out_slot_surface)

        self.out_magnet_surface = QLabel(self.g_output)
        self.out_magnet_surface.setObjectName(u"out_magnet_surface")

        self.verticalLayout.addWidget(self.out_magnet_surface)

        self.out_alpha = QLabel(self.g_output)
        self.out_alpha.setObjectName(u"out_alpha")

        self.verticalLayout.addWidget(self.out_alpha)

        self.verticalLayout_4.addWidget(self.g_output)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.lf_H0, self.lf_H1)
        QWidget.setTabOrder(self.lf_H1, self.lf_H2)
        QWidget.setTabOrder(self.lf_H2, self.lf_W0)
        QWidget.setTabOrder(self.lf_W0, self.lf_W1)
        QWidget.setTabOrder(self.lf_W1, self.txt_constraint)

        self.retranslateUi(PHoleM52R)

        QMetaObject.connectSlotsByName(PHoleM52R)

    # setupUi

    def retranslateUi(self, PHoleM52R):
        PHoleM52R.setWindowTitle(QCoreApplication.translate("PHoleM52R", u"Form", None))
        self.img_slot.setText("")
        self.txt_constraint.setHtml(
            QCoreApplication.translate(
                "PHoleM52R",
                u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt; font-weight:600; text-decoration: underline;">Constraints :</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">H2 &lt; H1</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-fami'
                "ly:'DejaVu Sans'; font-size:10pt;\">R0 &lt; W1</span></p>\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">R0 &lt; H1 - H2</span></p>\n'
                '<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'DejaVu Sans\'; font-size:8pt;"><br /></p></body></html>',
                None,
            )
        )
        self.in_R0.setText(QCoreApplication.translate("PHoleM52R", u"R0", None))
        self.unit_R0.setText(QCoreApplication.translate("PHoleM52R", u"m", None))
        self.in_W1.setText(QCoreApplication.translate("PHoleM52R", u"W1", None))
        self.unit_W1.setText(QCoreApplication.translate("PHoleM52R", u"m", None))
        self.in_H0.setText(QCoreApplication.translate("PHoleM52R", u"H0", None))
        self.unit_H1.setText(QCoreApplication.translate("PHoleM52R", u"m", None))
        self.in_H1.setText(QCoreApplication.translate("PHoleM52R", u"H1", None))
        self.unit_H0.setText(QCoreApplication.translate("PHoleM52R", u"m", None))
        self.in_H2.setText(QCoreApplication.translate("PHoleM52R", u"H2", None))
        self.unit_H2.setText(QCoreApplication.translate("PHoleM52R", u"m", None))
        self.in_W0.setText(QCoreApplication.translate("PHoleM52R", u"W0", None))
        self.unit_W0.setText(QCoreApplication.translate("PHoleM52R", u"m", None))
        self.g_output.setTitle(QCoreApplication.translate("PHoleM52R", u"Output", None))
        self.out_slot_surface.setText(
            QCoreApplication.translate("PHoleM52R", u"Slot suface : ?", None)
        )
        self.out_magnet_surface.setText(
            QCoreApplication.translate("PHoleM52R", u"Magnet surface : ?", None)
        )
        self.out_alpha.setText(
            QCoreApplication.translate("PHoleM52R", u"Alpha : ?", None)
        )

    # retranslateUi
