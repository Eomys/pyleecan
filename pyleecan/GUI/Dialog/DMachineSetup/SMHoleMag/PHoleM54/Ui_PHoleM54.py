# -*- coding: utf-8 -*-

# File generated according to PHoleM54.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from ......GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect
from ......GUI.Tools.FloatEdit import FloatEdit

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PHoleM54(object):
    def setupUi(self, PHoleM54):
        if not PHoleM54.objectName():
            PHoleM54.setObjectName("PHoleM54")
        PHoleM54.resize(1157, 570)
        PHoleM54.setMinimumSize(QSize(740, 440))
        PHoleM54.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PHoleM54)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.img_slot = QLabel(PHoleM54)
        self.img_slot.setObjectName("img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMinimumSize(QSize(0, 0))
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setPixmap(
            QPixmap(":/images/images/MachineSetup/SMHoleMag/HoleM54_mag_int_rotor.png")
        )
        self.img_slot.setScaledContents(False)
        self.img_slot.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.img_slot)

        self.txt_constraint = QTextEdit(PHoleM54)
        self.txt_constraint.setObjectName("txt_constraint")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.txt_constraint.sizePolicy().hasHeightForWidth()
        )
        self.txt_constraint.setSizePolicy(sizePolicy1)
        self.txt_constraint.setMinimumSize(QSize(200, 0))
        self.txt_constraint.setMaximumSize(QSize(16777215, 50))
        self.txt_constraint.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_constraint.setTextInteractionFlags(
            Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse
        )

        self.verticalLayout_3.addWidget(self.txt_constraint)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.scrollArea = QScrollArea(PHoleM54)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 546))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.unit_H1 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H1.setObjectName("unit_H1")

        self.gridLayout.addWidget(self.unit_H1, 1, 2, 1, 1)

        self.lf_H0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H0.setObjectName("lf_H0")

        self.gridLayout.addWidget(self.lf_H0, 0, 1, 1, 1)

        self.lf_H1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H1.setObjectName("lf_H1")

        self.gridLayout.addWidget(self.lf_H1, 1, 1, 1, 1)

        self.in_H1 = QLabel(self.scrollAreaWidgetContents)
        self.in_H1.setObjectName("in_H1")

        self.gridLayout.addWidget(self.in_H1, 1, 0, 1, 1)

        self.unit_H0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H0.setObjectName("unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 0, 2, 1, 1)

        self.in_H0 = QLabel(self.scrollAreaWidgetContents)
        self.in_H0.setObjectName("in_H0")

        self.gridLayout.addWidget(self.in_H0, 0, 0, 1, 1)

        self.lf_W0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W0.setObjectName("lf_W0")

        self.gridLayout.addWidget(self.lf_W0, 2, 1, 1, 1)

        self.unit_R1 = QLabel(self.scrollAreaWidgetContents)
        self.unit_R1.setObjectName("unit_R1")

        self.gridLayout.addWidget(self.unit_R1, 3, 2, 1, 1)

        self.lf_R1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_R1.setObjectName("lf_R1")

        self.gridLayout.addWidget(self.lf_R1, 3, 1, 1, 1)

        self.in_R1 = QLabel(self.scrollAreaWidgetContents)
        self.in_R1.setObjectName("in_R1")

        self.gridLayout.addWidget(self.in_R1, 3, 0, 1, 1)

        self.unit_W0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W0.setObjectName("unit_W0")

        self.gridLayout.addWidget(self.unit_W0, 2, 2, 1, 1)

        self.in_W0 = QLabel(self.scrollAreaWidgetContents)
        self.in_W0.setObjectName("in_W0")

        self.gridLayout.addWidget(self.in_W0, 2, 0, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.w_mat_0 = WMatSelect(self.scrollAreaWidgetContents)
        self.w_mat_0.setObjectName("w_mat_0")
        self.w_mat_0.setMinimumSize(QSize(100, 0))

        self.verticalLayout_2.addWidget(self.w_mat_0)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.g_output = QGroupBox(self.scrollAreaWidgetContents)
        self.g_output.setObjectName("g_output")
        self.g_output.setMinimumSize(QSize(200, 0))
        self.verticalLayout = QVBoxLayout(self.g_output)
        self.verticalLayout.setObjectName("verticalLayout")
        self.out_slot_surface = QLabel(self.g_output)
        self.out_slot_surface.setObjectName("out_slot_surface")

        self.verticalLayout.addWidget(self.out_slot_surface)

        self.verticalLayout_2.addWidget(self.g_output)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.lf_H0, self.lf_H1)
        QWidget.setTabOrder(self.lf_H1, self.lf_W0)
        QWidget.setTabOrder(self.lf_W0, self.lf_R1)
        QWidget.setTabOrder(self.lf_R1, self.txt_constraint)

        self.retranslateUi(PHoleM54)

        QMetaObject.connectSlotsByName(PHoleM54)

    # setupUi

    def retranslateUi(self, PHoleM54):
        PHoleM54.setWindowTitle(QCoreApplication.translate("PHoleM54", "Form", None))
        self.img_slot.setText("")
        self.txt_constraint.setHtml(
            QCoreApplication.translate(
                "PHoleM54",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'DejaVu Sans'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt; font-weight:600; text-decoration: underline;">Constraints :</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">H0 &lt; R1</span></p></body></html>',
                None,
            )
        )
        self.unit_H1.setText(QCoreApplication.translate("PHoleM54", "m", None))
        self.in_H1.setText(QCoreApplication.translate("PHoleM54", "H1", None))
        self.unit_H0.setText(QCoreApplication.translate("PHoleM54", "m", None))
        self.in_H0.setText(QCoreApplication.translate("PHoleM54", "H0", None))
        self.unit_R1.setText(QCoreApplication.translate("PHoleM54", "m", None))
        self.in_R1.setText(QCoreApplication.translate("PHoleM54", "R1", None))
        self.unit_W0.setText(QCoreApplication.translate("PHoleM54", "[rad]", None))
        self.in_W0.setText(QCoreApplication.translate("PHoleM54", "W0", None))
        self.g_output.setTitle(QCoreApplication.translate("PHoleM54", "Output", None))
        self.out_slot_surface.setText(
            QCoreApplication.translate("PHoleM54", "Slot suface : ?", None)
        )

    # retranslateUi
