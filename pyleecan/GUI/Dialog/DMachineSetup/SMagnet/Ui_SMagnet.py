# -*- coding: utf-8 -*-

# File generated according to SMagnet.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .....GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect
from pyleecan.GUI.Tools.HelpButton import HelpButton

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SMagnet(object):
    def setupUi(self, SMagnet):
        if not SMagnet.objectName():
            SMagnet.setObjectName(u"SMagnet")
        SMagnet.resize(650, 550)
        SMagnet.setMinimumSize(QSize(650, 550))
        self.main_layout = QVBoxLayout(SMagnet)
        self.main_layout.setObjectName(u"main_layout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.b_help = HelpButton(SMagnet)
        self.b_help.setObjectName(u"b_help")
        self.b_help.setPixmap(QPixmap(u":/images/images/icon/help_16.png"))

        self.horizontalLayout_3.addWidget(self.b_help)

        self.c_type = QComboBox(SMagnet)
        self.c_type.addItem("")
        self.c_type.addItem("")
        self.c_type.addItem("")
        self.c_type.addItem("")
        self.c_type.addItem("")
        self.c_type.setObjectName(u"c_type")
        self.c_type.setMinimumSize(QSize(100, 0))
        self.c_type.setAutoFillBackground(False)

        self.horizontalLayout_3.addWidget(self.c_type)

        self.out_Nmag = QLabel(SMagnet)
        self.out_Nmag.setObjectName(u"out_Nmag")

        self.horizontalLayout_3.addWidget(self.out_Nmag)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.main_layout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.w_mat = WMatSelect(SMagnet)
        self.w_mat.setObjectName(u"w_mat")

        self.horizontalLayout.addWidget(self.w_mat)

        self.in_type_magnetization = QLabel(SMagnet)
        self.in_type_magnetization.setObjectName(u"in_type_magnetization")

        self.horizontalLayout.addWidget(self.in_type_magnetization)

        self.c_type_magnetization = QComboBox(SMagnet)
        self.c_type_magnetization.addItem("")
        self.c_type_magnetization.addItem("")
        self.c_type_magnetization.addItem("")
        self.c_type_magnetization.setObjectName(u"c_type_magnetization")

        self.horizontalLayout.addWidget(self.c_type_magnetization)

        self.main_layout.addLayout(self.horizontalLayout)

        self.w_mag = QWidget(SMagnet)
        self.w_mag.setObjectName(u"w_mag")

        self.main_layout.addWidget(self.w_mag)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.b_plot = QPushButton(SMagnet)
        self.b_plot.setObjectName(u"b_plot")

        self.horizontalLayout_2.addWidget(self.b_plot)

        self.b_previous = QPushButton(SMagnet)
        self.b_previous.setObjectName(u"b_previous")

        self.horizontalLayout_2.addWidget(self.b_previous)

        self.b_next = QPushButton(SMagnet)
        self.b_next.setObjectName(u"b_next")
        self.b_next.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.b_next)

        self.main_layout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SMagnet)

        QMetaObject.connectSlotsByName(SMagnet)

    # setupUi

    def retranslateUi(self, SMagnet):
        SMagnet.setWindowTitle(QCoreApplication.translate("SMagnet", u"Form", None))
        self.b_help.setText("")
        self.c_type.setItemText(
            0, QCoreApplication.translate("SMagnet", u"Rectangular", None)
        )
        self.c_type.setItemText(
            1, QCoreApplication.translate("SMagnet", u"Polar", None)
        )
        self.c_type.setItemText(
            2, QCoreApplication.translate("SMagnet", u"Flat bottom, polar top", None)
        )
        self.c_type.setItemText(
            3, QCoreApplication.translate("SMagnet", u"Flat bottom, curved top", None)
        )
        self.c_type.setItemText(
            4, QCoreApplication.translate("SMagnet", u"Polar bottom, curved top", None)
        )

        self.out_Nmag.setText(
            QCoreApplication.translate("SMagnet", u"Number of magnet = 2 * p = ?", None)
        )
        self.in_type_magnetization.setText(
            QCoreApplication.translate("SMagnet", u"type_magnetization:", None)
        )
        self.c_type_magnetization.setItemText(
            0, QCoreApplication.translate("SMagnet", u"Radial", None)
        )
        self.c_type_magnetization.setItemText(
            1, QCoreApplication.translate("SMagnet", u"Parallel", None)
        )
        self.c_type_magnetization.setItemText(
            2, QCoreApplication.translate("SMagnet", u"HallBach", None)
        )

        self.b_plot.setText(QCoreApplication.translate("SMagnet", u"Preview", None))
        self.b_previous.setText(
            QCoreApplication.translate("SMagnet", u"Previous", None)
        )
        self.b_next.setText(QCoreApplication.translate("SMagnet", u"Save", None))

    # retranslateUi
