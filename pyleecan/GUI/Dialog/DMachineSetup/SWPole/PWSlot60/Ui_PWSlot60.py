# -*- coding: utf-8 -*-

# File generated according to PWSlot60.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PWSlot60(object):
    def setupUi(self, PWSlot60):
        if not PWSlot60.objectName():
            PWSlot60.setObjectName(u"PWSlot60")
        PWSlot60.resize(913, 529)
        PWSlot60.setMinimumSize(QSize(630, 470))
        PWSlot60.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PWSlot60)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.img_slot = QLabel(PWSlot60)
        self.img_slot.setObjectName(u"img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setPixmap(
            QPixmap(u":/images/images/MachineSetup/WSlot/Slot_60.PNG")
        )
        self.img_slot.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.img_slot)

        self.txt_constraint = QTextEdit(PWSlot60)
        self.txt_constraint.setObjectName(u"txt_constraint")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.txt_constraint.sizePolicy().hasHeightForWidth()
        )
        self.txt_constraint.setSizePolicy(sizePolicy1)
        self.txt_constraint.setMaximumSize(QSize(16777215, 70))
        self.txt_constraint.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_constraint.setTextInteractionFlags(
            Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse
        )

        self.verticalLayout_2.addWidget(self.txt_constraint)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.scrollArea = QScrollArea(PWSlot60)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 268, 505))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.in_R1 = QLabel(self.scrollAreaWidgetContents_2)
        self.in_R1.setObjectName(u"in_R1")

        self.gridLayout.addWidget(self.in_R1, 0, 0, 1, 1)

        self.lf_R1 = FloatEdit(self.scrollAreaWidgetContents_2)
        self.lf_R1.setObjectName(u"lf_R1")

        self.gridLayout.addWidget(self.lf_R1, 0, 1, 1, 1)

        self.unit_R1 = QLabel(self.scrollAreaWidgetContents_2)
        self.unit_R1.setObjectName(u"unit_R1")

        self.gridLayout.addWidget(self.unit_R1, 0, 2, 1, 1)

        self.in_W1 = QLabel(self.scrollAreaWidgetContents_2)
        self.in_W1.setObjectName(u"in_W1")

        self.gridLayout.addWidget(self.in_W1, 1, 0, 1, 1)

        self.lf_W1 = FloatEdit(self.scrollAreaWidgetContents_2)
        self.lf_W1.setObjectName(u"lf_W1")

        self.gridLayout.addWidget(self.lf_W1, 1, 1, 1, 1)

        self.unit_W1 = QLabel(self.scrollAreaWidgetContents_2)
        self.unit_W1.setObjectName(u"unit_W1")

        self.gridLayout.addWidget(self.unit_W1, 1, 2, 1, 1)

        self.in_W2 = QLabel(self.scrollAreaWidgetContents_2)
        self.in_W2.setObjectName(u"in_W2")

        self.gridLayout.addWidget(self.in_W2, 2, 0, 1, 1)

        self.lf_W2 = FloatEdit(self.scrollAreaWidgetContents_2)
        self.lf_W2.setObjectName(u"lf_W2")

        self.gridLayout.addWidget(self.lf_W2, 2, 1, 1, 1)

        self.unit_W2 = QLabel(self.scrollAreaWidgetContents_2)
        self.unit_W2.setObjectName(u"unit_W2")

        self.gridLayout.addWidget(self.unit_W2, 2, 2, 1, 1)

        self.in_H1 = QLabel(self.scrollAreaWidgetContents_2)
        self.in_H1.setObjectName(u"in_H1")

        self.gridLayout.addWidget(self.in_H1, 3, 0, 1, 1)

        self.lf_H1 = FloatEdit(self.scrollAreaWidgetContents_2)
        self.lf_H1.setObjectName(u"lf_H1")

        self.gridLayout.addWidget(self.lf_H1, 3, 1, 1, 1)

        self.unit_H1 = QLabel(self.scrollAreaWidgetContents_2)
        self.unit_H1.setObjectName(u"unit_H1")

        self.gridLayout.addWidget(self.unit_H1, 3, 2, 1, 1)

        self.in_H2 = QLabel(self.scrollAreaWidgetContents_2)
        self.in_H2.setObjectName(u"in_H2")

        self.gridLayout.addWidget(self.in_H2, 4, 0, 1, 1)

        self.lf_H2 = FloatEdit(self.scrollAreaWidgetContents_2)
        self.lf_H2.setObjectName(u"lf_H2")

        self.gridLayout.addWidget(self.lf_H2, 4, 1, 1, 1)

        self.unit_H2 = QLabel(self.scrollAreaWidgetContents_2)
        self.unit_H2.setObjectName(u"unit_H2")

        self.gridLayout.addWidget(self.unit_H2, 4, 2, 1, 1)

        self.in_H3 = QLabel(self.scrollAreaWidgetContents_2)
        self.in_H3.setObjectName(u"in_H3")

        self.gridLayout.addWidget(self.in_H3, 5, 0, 1, 1)

        self.lf_H3 = FloatEdit(self.scrollAreaWidgetContents_2)
        self.lf_H3.setObjectName(u"lf_H3")

        self.gridLayout.addWidget(self.lf_H3, 5, 1, 1, 1)

        self.unit_H3 = QLabel(self.scrollAreaWidgetContents_2)
        self.unit_H3.setObjectName(u"unit_H3")

        self.gridLayout.addWidget(self.unit_H3, 5, 2, 1, 1)

        self.in_H4 = QLabel(self.scrollAreaWidgetContents_2)
        self.in_H4.setObjectName(u"in_H4")

        self.gridLayout.addWidget(self.in_H4, 6, 0, 1, 1)

        self.lf_H4 = FloatEdit(self.scrollAreaWidgetContents_2)
        self.lf_H4.setObjectName(u"lf_H4")

        self.gridLayout.addWidget(self.lf_H4, 6, 1, 1, 1)

        self.unit_H4 = QLabel(self.scrollAreaWidgetContents_2)
        self.unit_H4.setObjectName(u"unit_H4")

        self.gridLayout.addWidget(self.unit_H4, 6, 2, 1, 1)

        self.in_W3 = QLabel(self.scrollAreaWidgetContents_2)
        self.in_W3.setObjectName(u"in_W3")

        self.gridLayout.addWidget(self.in_W3, 7, 0, 1, 1)

        self.lf_W3 = FloatEdit(self.scrollAreaWidgetContents_2)
        self.lf_W3.setObjectName(u"lf_W3")

        self.gridLayout.addWidget(self.lf_W3, 7, 1, 1, 1)

        self.unit_W3 = QLabel(self.scrollAreaWidgetContents_2)
        self.unit_W3.setObjectName(u"unit_W3")

        self.gridLayout.addWidget(self.unit_W3, 7, 2, 1, 1)

        self.verticalLayout_4.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.g_output = QGroupBox(self.scrollAreaWidgetContents_2)
        self.g_output.setObjectName(u"g_output")
        self.g_output.setMinimumSize(QSize(200, 0))
        self.verticalLayout_3 = QVBoxLayout(self.g_output)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.out_Wlam = QLabel(self.g_output)
        self.out_Wlam.setObjectName(u"out_Wlam")

        self.verticalLayout_3.addWidget(self.out_Wlam)

        self.out_slot_height = QLabel(self.g_output)
        self.out_slot_height.setObjectName(u"out_slot_height")

        self.verticalLayout_3.addWidget(self.out_slot_height)

        self.out_yoke_height = QLabel(self.g_output)
        self.out_yoke_height.setObjectName(u"out_yoke_height")

        self.verticalLayout_3.addWidget(self.out_yoke_height)

        self.out_wind_surface = QLabel(self.g_output)
        self.out_wind_surface.setObjectName(u"out_wind_surface")

        self.verticalLayout_3.addWidget(self.out_wind_surface)

        self.out_tot_surface = QLabel(self.g_output)
        self.out_tot_surface.setObjectName(u"out_tot_surface")

        self.verticalLayout_3.addWidget(self.out_tot_surface)

        self.out_op_angle = QLabel(self.g_output)
        self.out_op_angle.setObjectName(u"out_op_angle")

        self.verticalLayout_3.addWidget(self.out_op_angle)

        self.out_tooth_width = QLabel(self.g_output)
        self.out_tooth_width.setObjectName(u"out_tooth_width")

        self.verticalLayout_3.addWidget(self.out_tooth_width)

        self.verticalLayout_4.addWidget(self.g_output)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.lf_R1, self.lf_W1)
        QWidget.setTabOrder(self.lf_W1, self.lf_W2)
        QWidget.setTabOrder(self.lf_W2, self.lf_H1)
        QWidget.setTabOrder(self.lf_H1, self.lf_H2)
        QWidget.setTabOrder(self.lf_H2, self.txt_constraint)

        self.retranslateUi(PWSlot60)

        QMetaObject.connectSlotsByName(PWSlot60)

    # setupUi

    def retranslateUi(self, PWSlot60):
        PWSlot60.setWindowTitle(QCoreApplication.translate("PWSlot60", u"Form", None))
        self.img_slot.setText("")
        self.txt_constraint.setHtml(
            QCoreApplication.translate(
                "PWSlot60",
                u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'DejaVu Sans'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt; font-weight:600; text-decoration: underline;">Constraints :</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">R1 &lt; Rbo</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">W2&lt; W1</span></p></body></html>',
                None,
            )
        )
        self.in_R1.setText(QCoreApplication.translate("PWSlot60", u"R1 :", None))
        self.unit_R1.setText(QCoreApplication.translate("PWSlot60", u"m", None))
        self.in_W1.setText(QCoreApplication.translate("PWSlot60", u"W1 :", None))
        self.unit_W1.setText(QCoreApplication.translate("PWSlot60", u"m", None))
        self.in_W2.setText(QCoreApplication.translate("PWSlot60", u"W2 :", None))
        self.unit_W2.setText(QCoreApplication.translate("PWSlot60", u"m", None))
        self.in_H1.setText(QCoreApplication.translate("PWSlot60", u"H1 :", None))
        self.unit_H1.setText(QCoreApplication.translate("PWSlot60", u"m", None))
        self.in_H2.setText(QCoreApplication.translate("PWSlot60", u"H2 :", None))
        self.unit_H2.setText(QCoreApplication.translate("PWSlot60", u"m", None))
        self.in_H3.setText(QCoreApplication.translate("PWSlot60", u"H3 :", None))
        self.unit_H3.setText(QCoreApplication.translate("PWSlot60", u"m", None))
        self.in_H4.setText(QCoreApplication.translate("PWSlot60", u"H4 :", None))
        self.unit_H4.setText(QCoreApplication.translate("PWSlot60", u"m", None))
        self.in_W3.setText(QCoreApplication.translate("PWSlot60", u"W3 :", None))
        self.unit_W3.setText(QCoreApplication.translate("PWSlot60", u"m", None))
        self.g_output.setTitle(QCoreApplication.translate("PWSlot60", u"Output", None))
        self.out_Wlam.setText(
            QCoreApplication.translate("PWSlot60", u"Lamination width : ?", None)
        )
        self.out_slot_height.setText(
            QCoreApplication.translate("PWSlot60", u"Slot height : ?", None)
        )
        self.out_yoke_height.setText(
            QCoreApplication.translate("PWSlot60", u"Yoke height : ?", None)
        )
        self.out_wind_surface.setText(
            QCoreApplication.translate("PWSlot60", u"Winding surface : ?", None)
        )
        self.out_tot_surface.setText(
            QCoreApplication.translate("PWSlot60", u"Total surface : ?", None)
        )
        self.out_op_angle.setText(
            QCoreApplication.translate("PWSlot60", u"Opening angle : ?", None)
        )
        self.out_tooth_width.setText(
            QCoreApplication.translate("PWSlot60", u"Tooth average width : ?", None)
        )

    # retranslateUi
