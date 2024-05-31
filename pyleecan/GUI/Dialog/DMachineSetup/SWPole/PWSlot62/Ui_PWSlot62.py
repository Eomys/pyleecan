# -*- coding: utf-8 -*-

# File generated according to PWSlot62.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PWSlot62(object):
    def setupUi(self, PWSlot62):
        if not PWSlot62.objectName():
            PWSlot62.setObjectName("PWSlot62")
        PWSlot62.resize(1084, 543)
        PWSlot62.setMinimumSize(QSize(630, 470))
        PWSlot62.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PWSlot62)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.img_slot = QLabel(PWSlot62)
        self.img_slot.setObjectName("img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setPixmap(
            QPixmap(":/images/images/MachineSetup/WSlot/SlotW62_wind_int_rotor.png")
        )
        self.img_slot.setScaledContents(False)
        self.img_slot.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.img_slot)

        self.txt_constraint = QTextEdit(PWSlot62)
        self.txt_constraint.setObjectName("txt_constraint")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.txt_constraint.sizePolicy().hasHeightForWidth()
        )
        self.txt_constraint.setSizePolicy(sizePolicy1)
        self.txt_constraint.setMaximumSize(QSize(16777215, 60))
        self.txt_constraint.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_constraint.setTextInteractionFlags(
            Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse
        )

        self.verticalLayout_2.addWidget(self.txt_constraint)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.scrollArea = QScrollArea(PWSlot62)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 523))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.in_H3 = QLabel(self.scrollAreaWidgetContents)
        self.in_H3.setObjectName("in_H3")

        self.gridLayout.addWidget(self.in_H3, 6, 0, 1, 1)

        self.lf_H2 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H2.setObjectName("lf_H2")

        self.gridLayout.addWidget(self.lf_H2, 5, 1, 1, 1)

        self.unit_W3 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W3.setObjectName("unit_W3")

        self.gridLayout.addWidget(self.unit_W3, 7, 2, 1, 1)

        self.unit_H2 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H2.setObjectName("unit_H2")

        self.gridLayout.addWidget(self.unit_H2, 5, 2, 1, 1)

        self.lf_H1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H1.setObjectName("lf_H1")

        self.gridLayout.addWidget(self.lf_H1, 4, 1, 1, 1)

        self.unit_W2 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W2.setObjectName("unit_W2")

        self.gridLayout.addWidget(self.unit_W2, 2, 2, 1, 1)

        self.unit_W1 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W1.setObjectName("unit_W1")

        self.gridLayout.addWidget(self.unit_W1, 1, 2, 1, 1)

        self.in_H0 = QLabel(self.scrollAreaWidgetContents)
        self.in_H0.setObjectName("in_H0")

        self.gridLayout.addWidget(self.in_H0, 3, 0, 1, 1)

        self.unit_H0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H0.setObjectName("unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 3, 2, 1, 1)

        self.in_W3 = QLabel(self.scrollAreaWidgetContents)
        self.in_W3.setObjectName("in_W3")

        self.gridLayout.addWidget(self.in_W3, 7, 0, 1, 1)

        self.unit_H1 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H1.setObjectName("unit_H1")

        self.gridLayout.addWidget(self.unit_H1, 4, 2, 1, 1)

        self.in_W1 = QLabel(self.scrollAreaWidgetContents)
        self.in_W1.setObjectName("in_W1")

        self.gridLayout.addWidget(self.in_W1, 1, 0, 1, 1)

        self.lf_W3 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W3.setObjectName("lf_W3")

        self.gridLayout.addWidget(self.lf_W3, 7, 1, 1, 1)

        self.in_H1 = QLabel(self.scrollAreaWidgetContents)
        self.in_H1.setObjectName("in_H1")

        self.gridLayout.addWidget(self.in_H1, 4, 0, 1, 1)

        self.in_H2 = QLabel(self.scrollAreaWidgetContents)
        self.in_H2.setObjectName("in_H2")

        self.gridLayout.addWidget(self.in_H2, 5, 0, 1, 1)

        self.lf_H0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H0.setObjectName("lf_H0")

        self.gridLayout.addWidget(self.lf_H0, 3, 1, 1, 1)

        self.lf_W1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W1.setObjectName("lf_W1")

        self.gridLayout.addWidget(self.lf_W1, 1, 1, 1, 1)

        self.lf_H3 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H3.setObjectName("lf_H3")

        self.gridLayout.addWidget(self.lf_H3, 6, 1, 1, 1)

        self.lf_W2 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W2.setObjectName("lf_W2")

        self.gridLayout.addWidget(self.lf_W2, 2, 1, 1, 1)

        self.unit_H3 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H3.setObjectName("unit_H3")

        self.gridLayout.addWidget(self.unit_H3, 6, 2, 1, 1)

        self.unit_W0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W0.setObjectName("unit_W0")

        self.gridLayout.addWidget(self.unit_W0, 0, 2, 1, 1)

        self.lf_W0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W0.setObjectName("lf_W0")

        self.gridLayout.addWidget(self.lf_W0, 0, 1, 1, 1)

        self.in_W0 = QLabel(self.scrollAreaWidgetContents)
        self.in_W0.setObjectName("in_W0")

        self.gridLayout.addWidget(self.in_W0, 0, 0, 1, 1)

        self.in_W2 = QLabel(self.scrollAreaWidgetContents)
        self.in_W2.setObjectName("in_W2")

        self.gridLayout.addWidget(self.in_W2, 2, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.g_output = QGroupBox(self.scrollAreaWidgetContents)
        self.g_output.setObjectName("g_output")
        self.g_output.setMinimumSize(QSize(200, 0))
        self.verticalLayout_3 = QVBoxLayout(self.g_output)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.out_Wlam = QLabel(self.g_output)
        self.out_Wlam.setObjectName("out_Wlam")

        self.verticalLayout_3.addWidget(self.out_Wlam)

        self.out_slot_height = QLabel(self.g_output)
        self.out_slot_height.setObjectName("out_slot_height")

        self.verticalLayout_3.addWidget(self.out_slot_height)

        self.out_yoke_height = QLabel(self.g_output)
        self.out_yoke_height.setObjectName("out_yoke_height")

        self.verticalLayout_3.addWidget(self.out_yoke_height)

        self.out_wind_surface = QLabel(self.g_output)
        self.out_wind_surface.setObjectName("out_wind_surface")

        self.verticalLayout_3.addWidget(self.out_wind_surface)

        self.out_tot_surface = QLabel(self.g_output)
        self.out_tot_surface.setObjectName("out_tot_surface")

        self.verticalLayout_3.addWidget(self.out_tot_surface)

        self.out_op_angle = QLabel(self.g_output)
        self.out_op_angle.setObjectName("out_op_angle")

        self.verticalLayout_3.addWidget(self.out_op_angle)

        self.out_tooth_width = QLabel(self.g_output)
        self.out_tooth_width.setObjectName("out_tooth_width")

        self.verticalLayout_3.addWidget(self.out_tooth_width)

        self.verticalLayout.addWidget(self.g_output)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.lf_W0, self.lf_W1)
        QWidget.setTabOrder(self.lf_W1, self.lf_W2)
        QWidget.setTabOrder(self.lf_W2, self.lf_H0)
        QWidget.setTabOrder(self.lf_H0, self.lf_H1)
        QWidget.setTabOrder(self.lf_H1, self.lf_H2)
        QWidget.setTabOrder(self.lf_H2, self.lf_H3)
        QWidget.setTabOrder(self.lf_H3, self.lf_W3)
        QWidget.setTabOrder(self.lf_W3, self.txt_constraint)
        QWidget.setTabOrder(self.txt_constraint, self.scrollArea)

        self.retranslateUi(PWSlot62)

        QMetaObject.connectSlotsByName(PWSlot62)

    # setupUi

    def retranslateUi(self, PWSlot62):
        PWSlot62.setWindowTitle(QCoreApplication.translate("PWSlot62", "Form", None))
        self.img_slot.setText("")
        self.txt_constraint.setHtml(
            QCoreApplication.translate(
                "PWSlot62",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'DejaVu Sans'; font-size:8.15094pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt; font-weight:600; text-decoration: underline;">Constraints :</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">H2 + H3 &lt; H0</span></p></body></html>',
                None,
            )
        )
        self.in_H3.setText(QCoreApplication.translate("PWSlot62", "H3 :", None))
        self.unit_W3.setText(QCoreApplication.translate("PWSlot62", "m", None))
        self.unit_H2.setText(QCoreApplication.translate("PWSlot62", "m", None))
        self.unit_W2.setText(QCoreApplication.translate("PWSlot62", "m", None))
        self.unit_W1.setText(QCoreApplication.translate("PWSlot62", "m", None))
        self.in_H0.setText(QCoreApplication.translate("PWSlot62", "H0 :", None))
        self.unit_H0.setText(QCoreApplication.translate("PWSlot62", "m", None))
        self.in_W3.setText(QCoreApplication.translate("PWSlot62", "W3 :", None))
        self.unit_H1.setText(QCoreApplication.translate("PWSlot62", "m", None))
        self.in_W1.setText(QCoreApplication.translate("PWSlot62", "W1 :", None))
        self.in_H1.setText(QCoreApplication.translate("PWSlot62", "H1 :", None))
        self.in_H2.setText(QCoreApplication.translate("PWSlot62", "H2 :", None))
        self.unit_H3.setText(QCoreApplication.translate("PWSlot62", "m", None))
        self.unit_W0.setText(QCoreApplication.translate("PWSlot62", "m", None))
        self.in_W0.setText(QCoreApplication.translate("PWSlot62", "W0 :", None))
        self.in_W2.setText(QCoreApplication.translate("PWSlot62", "W2 :", None))
        self.g_output.setTitle(QCoreApplication.translate("PWSlot62", "Output", None))
        self.out_Wlam.setText(
            QCoreApplication.translate("PWSlot62", "Lamination width : ?", None)
        )
        self.out_slot_height.setText(
            QCoreApplication.translate("PWSlot62", "Slot height : ?", None)
        )
        self.out_yoke_height.setText(
            QCoreApplication.translate("PWSlot62", "Yoke height : ?", None)
        )
        self.out_wind_surface.setText(
            QCoreApplication.translate("PWSlot62", "Winding surface : ?", None)
        )
        self.out_tot_surface.setText(
            QCoreApplication.translate("PWSlot62", "Total surface : ?", None)
        )
        self.out_op_angle.setText(
            QCoreApplication.translate("PWSlot62", "Opening angle : ?", None)
        )
        self.out_tooth_width.setText(
            QCoreApplication.translate("PWSlot62", "Tooth average width : ?", None)
        )

    # retranslateUi
