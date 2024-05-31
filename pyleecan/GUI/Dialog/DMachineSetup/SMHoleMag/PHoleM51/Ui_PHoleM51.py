# -*- coding: utf-8 -*-

# File generated according to PHoleM51.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from ......GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect
from ......GUI.Tools.FloatEdit import FloatEdit

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PHoleM51(object):
    def setupUi(self, PHoleM51):
        if not PHoleM51.objectName():
            PHoleM51.setObjectName("PHoleM51")
        PHoleM51.resize(1082, 847)
        PHoleM51.setMinimumSize(QSize(740, 440))
        PHoleM51.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PHoleM51)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.img_slot = QLabel(PHoleM51)
        self.img_slot.setObjectName("img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMinimumSize(QSize(0, 0))
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setAutoFillBackground(False)
        self.img_slot.setFrameShape(QFrame.NoFrame)
        self.img_slot.setPixmap(
            QPixmap(":/images/images/MachineSetup/SMHoleMag/HoleM51_mag_int_rotor.png")
        )
        self.img_slot.setScaledContents(False)
        self.img_slot.setAlignment(Qt.AlignCenter)
        self.img_slot.setWordWrap(False)

        self.verticalLayout_3.addWidget(self.img_slot)

        self.txt_constraint = QTextEdit(PHoleM51)
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

        self.scrollArea = QScrollArea(PHoleM51)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 823))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.in_H0 = QLabel(self.scrollAreaWidgetContents)
        self.in_H0.setObjectName("in_H0")

        self.gridLayout.addWidget(self.in_H0, 0, 0, 1, 1)

        self.lf_H0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H0.setObjectName("lf_H0")

        self.gridLayout.addWidget(self.lf_H0, 0, 1, 1, 1)

        self.unit_H0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H0.setObjectName("unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 0, 2, 1, 1)

        self.in_H1 = QLabel(self.scrollAreaWidgetContents)
        self.in_H1.setObjectName("in_H1")

        self.gridLayout.addWidget(self.in_H1, 1, 0, 1, 1)

        self.lf_H1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H1.setObjectName("lf_H1")

        self.gridLayout.addWidget(self.lf_H1, 1, 1, 1, 1)

        self.unit_H1 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H1.setObjectName("unit_H1")

        self.gridLayout.addWidget(self.unit_H1, 1, 2, 1, 1)

        self.in_H2 = QLabel(self.scrollAreaWidgetContents)
        self.in_H2.setObjectName("in_H2")

        self.gridLayout.addWidget(self.in_H2, 2, 0, 1, 1)

        self.lf_H2 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H2.setObjectName("lf_H2")

        self.gridLayout.addWidget(self.lf_H2, 2, 1, 1, 1)

        self.unit_H2 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H2.setObjectName("unit_H2")

        self.gridLayout.addWidget(self.unit_H2, 2, 2, 1, 1)

        self.in_W0 = QLabel(self.scrollAreaWidgetContents)
        self.in_W0.setObjectName("in_W0")

        self.gridLayout.addWidget(self.in_W0, 3, 0, 1, 1)

        self.lf_W0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W0.setObjectName("lf_W0")

        self.gridLayout.addWidget(self.lf_W0, 3, 1, 1, 1)

        self.unit_W0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W0.setObjectName("unit_W0")

        self.gridLayout.addWidget(self.unit_W0, 3, 2, 1, 1)

        self.in_W1 = QLabel(self.scrollAreaWidgetContents)
        self.in_W1.setObjectName("in_W1")

        self.gridLayout.addWidget(self.in_W1, 4, 0, 1, 1)

        self.lf_W1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W1.setObjectName("lf_W1")
        self.lf_W1.setCursorPosition(0)

        self.gridLayout.addWidget(self.lf_W1, 4, 1, 1, 1)

        self.unit_W1 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W1.setObjectName("unit_W1")

        self.gridLayout.addWidget(self.unit_W1, 4, 2, 1, 1)

        self.in_W2 = QLabel(self.scrollAreaWidgetContents)
        self.in_W2.setObjectName("in_W2")

        self.gridLayout.addWidget(self.in_W2, 5, 0, 1, 1)

        self.lf_W2 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W2.setObjectName("lf_W2")

        self.gridLayout.addWidget(self.lf_W2, 5, 1, 1, 1)

        self.unit_W2 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W2.setObjectName("unit_W2")

        self.gridLayout.addWidget(self.unit_W2, 5, 2, 1, 1)

        self.in_W3 = QLabel(self.scrollAreaWidgetContents)
        self.in_W3.setObjectName("in_W3")

        self.gridLayout.addWidget(self.in_W3, 6, 0, 1, 1)

        self.lf_W3 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W3.setObjectName("lf_W3")

        self.gridLayout.addWidget(self.lf_W3, 6, 1, 1, 1)

        self.unit_W3 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W3.setObjectName("unit_W3")

        self.gridLayout.addWidget(self.unit_W3, 6, 2, 1, 1)

        self.in_W4 = QLabel(self.scrollAreaWidgetContents)
        self.in_W4.setObjectName("in_W4")

        self.gridLayout.addWidget(self.in_W4, 7, 0, 1, 1)

        self.lf_W4 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W4.setObjectName("lf_W4")

        self.gridLayout.addWidget(self.lf_W4, 7, 1, 1, 1)

        self.unit_W4 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W4.setObjectName("unit_W4")

        self.gridLayout.addWidget(self.unit_W4, 7, 2, 1, 1)

        self.in_W5 = QLabel(self.scrollAreaWidgetContents)
        self.in_W5.setObjectName("in_W5")

        self.gridLayout.addWidget(self.in_W5, 8, 0, 1, 1)

        self.lf_W5 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W5.setObjectName("lf_W5")

        self.gridLayout.addWidget(self.lf_W5, 8, 1, 1, 1)

        self.unit_W5 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W5.setObjectName("unit_W5")

        self.gridLayout.addWidget(self.unit_W5, 8, 2, 1, 1)

        self.in_W6 = QLabel(self.scrollAreaWidgetContents)
        self.in_W6.setObjectName("in_W6")

        self.gridLayout.addWidget(self.in_W6, 9, 0, 1, 1)

        self.lf_W6 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W6.setObjectName("lf_W6")

        self.gridLayout.addWidget(self.lf_W6, 9, 1, 1, 1)

        self.unit_W6 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W6.setObjectName("unit_W6")

        self.gridLayout.addWidget(self.unit_W6, 9, 2, 1, 1)

        self.in_W7 = QLabel(self.scrollAreaWidgetContents)
        self.in_W7.setObjectName("in_W7")

        self.gridLayout.addWidget(self.in_W7, 10, 0, 1, 1)

        self.lf_W7 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W7.setObjectName("lf_W7")

        self.gridLayout.addWidget(self.lf_W7, 10, 1, 1, 1)

        self.unit_W7 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W7.setObjectName("unit_W7")

        self.gridLayout.addWidget(self.unit_W7, 10, 2, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.w_mat_0 = WMatSelect(self.scrollAreaWidgetContents)
        self.w_mat_0.setObjectName("w_mat_0")
        self.w_mat_0.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.w_mat_0, 0, 1, 1, 1)

        self.is_magnet_0 = QCheckBox(self.scrollAreaWidgetContents)
        self.is_magnet_0.setObjectName("is_magnet_0")

        self.gridLayout_2.addWidget(self.is_magnet_0, 1, 0, 1, 1)

        self.w_mat_1 = WMatSelect(self.scrollAreaWidgetContents)
        self.w_mat_1.setObjectName("w_mat_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.w_mat_1.sizePolicy().hasHeightForWidth())
        self.w_mat_1.setSizePolicy(sizePolicy2)
        self.w_mat_1.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.w_mat_1, 1, 1, 1, 1)

        self.is_magnet_1 = QCheckBox(self.scrollAreaWidgetContents)
        self.is_magnet_1.setObjectName("is_magnet_1")

        self.gridLayout_2.addWidget(self.is_magnet_1, 2, 0, 1, 1)

        self.w_mat_2 = WMatSelect(self.scrollAreaWidgetContents)
        self.w_mat_2.setObjectName("w_mat_2")
        self.w_mat_2.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.w_mat_2, 2, 1, 1, 1)

        self.is_magnet_2 = QCheckBox(self.scrollAreaWidgetContents)
        self.is_magnet_2.setObjectName("is_magnet_2")

        self.gridLayout_2.addWidget(self.is_magnet_2, 3, 0, 1, 1)

        self.w_mat_3 = WMatSelect(self.scrollAreaWidgetContents)
        self.w_mat_3.setObjectName("w_mat_3")
        self.w_mat_3.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.w_mat_3, 3, 1, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.verticalSpacer_2 = QSpacerItem(
            20, 7, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.g_output = QGroupBox(self.scrollAreaWidgetContents)
        self.g_output.setObjectName("g_output")
        self.g_output.setMinimumSize(QSize(200, 0))
        self.verticalLayout = QVBoxLayout(self.g_output)
        self.verticalLayout.setObjectName("verticalLayout")
        self.out_slot_surface = QLabel(self.g_output)
        self.out_slot_surface.setObjectName("out_slot_surface")

        self.verticalLayout.addWidget(self.out_slot_surface)

        self.out_magnet_surface = QLabel(self.g_output)
        self.out_magnet_surface.setObjectName("out_magnet_surface")

        self.verticalLayout.addWidget(self.out_magnet_surface)

        self.out_alpha = QLabel(self.g_output)
        self.out_alpha.setObjectName("out_alpha")

        self.verticalLayout.addWidget(self.out_alpha)

        self.out_Whole = QLabel(self.g_output)
        self.out_Whole.setObjectName("out_Whole")

        self.verticalLayout.addWidget(self.out_Whole)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_2.addWidget(self.g_output)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.lf_H0, self.lf_H1)
        QWidget.setTabOrder(self.lf_H1, self.lf_H2)
        QWidget.setTabOrder(self.lf_H2, self.lf_W0)
        QWidget.setTabOrder(self.lf_W0, self.lf_W1)
        QWidget.setTabOrder(self.lf_W1, self.txt_constraint)

        self.retranslateUi(PHoleM51)

        QMetaObject.connectSlotsByName(PHoleM51)

    # setupUi

    def retranslateUi(self, PHoleM51):
        PHoleM51.setWindowTitle(QCoreApplication.translate("PHoleM51", "Form", None))
        self.img_slot.setText("")
        self.txt_constraint.setHtml(
            QCoreApplication.translate(
                "PHoleM51",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'DejaVu Sans'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt; font-weight:600; text-decoration: underline;">Constraints :</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">W3+W2 &lt; W0</span></p>\n'
                '<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;"><br /></p></body></html>',
                None,
            )
        )
        self.in_H0.setText(QCoreApplication.translate("PHoleM51", "H0", None))
        self.unit_H0.setText(QCoreApplication.translate("PHoleM51", "m", None))
        self.in_H1.setText(QCoreApplication.translate("PHoleM51", "H1", None))
        self.unit_H1.setText(QCoreApplication.translate("PHoleM51", "m", None))
        self.in_H2.setText(QCoreApplication.translate("PHoleM51", "H2", None))
        self.unit_H2.setText(QCoreApplication.translate("PHoleM51", "m", None))
        self.in_W0.setText(QCoreApplication.translate("PHoleM51", "W0", None))
        self.unit_W0.setText(QCoreApplication.translate("PHoleM51", "m", None))
        self.in_W1.setText(QCoreApplication.translate("PHoleM51", "W1", None))
        self.unit_W1.setText(QCoreApplication.translate("PHoleM51", "[rad]", None))
        self.in_W2.setText(QCoreApplication.translate("PHoleM51", "W2", None))
        self.unit_W2.setText(QCoreApplication.translate("PHoleM51", "m", None))
        self.in_W3.setText(QCoreApplication.translate("PHoleM51", "W3", None))
        self.unit_W3.setText(QCoreApplication.translate("PHoleM51", "m", None))
        self.in_W4.setText(QCoreApplication.translate("PHoleM51", "W4", None))
        self.unit_W4.setText(QCoreApplication.translate("PHoleM51", "m", None))
        self.in_W5.setText(QCoreApplication.translate("PHoleM51", "W5", None))
        self.unit_W5.setText(QCoreApplication.translate("PHoleM51", "m", None))
        self.in_W6.setText(QCoreApplication.translate("PHoleM51", "W6", None))
        self.unit_W6.setText(QCoreApplication.translate("PHoleM51", "m", None))
        self.in_W7.setText(QCoreApplication.translate("PHoleM51", "W7", None))
        self.unit_W7.setText(QCoreApplication.translate("PHoleM51", "m", None))
        self.is_magnet_0.setText("")
        self.is_magnet_1.setText("")
        self.is_magnet_2.setText("")
        self.g_output.setTitle(QCoreApplication.translate("PHoleM51", "Output", None))
        self.out_slot_surface.setText(
            QCoreApplication.translate("PHoleM51", "Slot suface : ?", None)
        )
        self.out_magnet_surface.setText(
            QCoreApplication.translate("PHoleM51", "Magnet surface : ?", None)
        )
        self.out_alpha.setText(
            QCoreApplication.translate("PHoleM51", "Alpha : ?", None)
        )
        self.out_Whole.setText(
            QCoreApplication.translate("PHoleM51", "Wslot : ?", None)
        )

    # retranslateUi
