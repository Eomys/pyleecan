# -*- coding: utf-8 -*-

# File generated according to SLamParam.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .....GUI.Tools.FloatEdit import FloatEdit
from .....GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SLamParam(object):
    def setupUi(self, SLamParam):
        if not SLamParam.objectName():
            SLamParam.setObjectName(u"SLamParam")
        SLamParam.resize(650, 550)
        SLamParam.setMinimumSize(QSize(650, 550))
        self.main_layout = QVBoxLayout(SLamParam)
        self.main_layout.setObjectName(u"main_layout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.in_L1 = QLabel(SLamParam)
        self.in_L1.setObjectName(u"in_L1")

        self.horizontalLayout.addWidget(self.in_L1)

        self.lf_L1 = FloatEdit(SLamParam)
        self.lf_L1.setObjectName(u"lf_L1")
        self.lf_L1.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.lf_L1)

        self.unit_L1 = QLabel(SLamParam)
        self.unit_L1.setObjectName(u"unit_L1")

        self.horizontalLayout.addWidget(self.unit_L1)

        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_8)

        self.main_layout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.in_Kf1 = QLabel(SLamParam)
        self.in_Kf1.setObjectName(u"in_Kf1")

        self.horizontalLayout_2.addWidget(self.in_Kf1)

        self.lf_Kf1 = FloatEdit(SLamParam)
        self.lf_Kf1.setObjectName(u"lf_Kf1")
        self.lf_Kf1.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_2.addWidget(self.lf_Kf1)

        self.w_mat = WMatSelect(SLamParam)
        self.w_mat.setObjectName(u"w_mat")
        self.w_mat.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.w_mat)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.main_layout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.g_ax_vent = QGroupBox(SLamParam)
        self.g_ax_vent.setObjectName(u"g_ax_vent")
        self.g_ax_vent.setMinimumSize(QSize(300, 300))
        self.g_ax_vent.setCheckable(True)
        self.g_ax_vent.setChecked(False)
        self.verticalLayout_3 = QVBoxLayout(self.g_ax_vent)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.g_ax_vent)
        self.label.setObjectName(u"label")
        self.label.setPixmap(
            QPixmap(u":/images/images/MachineSetup/LamParam/CircVentDuct.png")
        )
        self.label.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.out_axial_duct = QLabel(self.g_ax_vent)
        self.out_axial_duct.setObjectName(u"out_axial_duct")

        self.horizontalLayout_5.addWidget(self.out_axial_duct)

        self.b_axial_duct = QPushButton(self.g_ax_vent)
        self.b_axial_duct.setObjectName(u"b_axial_duct")

        self.horizontalLayout_5.addWidget(self.b_axial_duct)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3.addWidget(self.g_ax_vent)

        self.g_rad_vent = QGroupBox(SLamParam)
        self.g_rad_vent.setObjectName(u"g_rad_vent")
        self.g_rad_vent.setMinimumSize(QSize(0, 300))
        self.g_rad_vent.setFlat(False)
        self.g_rad_vent.setCheckable(True)
        self.g_rad_vent.setChecked(False)
        self.verticalLayout_2 = QVBoxLayout(self.g_rad_vent)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.img_rad_duct = QLabel(self.g_rad_vent)
        self.img_rad_duct.setObjectName(u"img_rad_duct")
        self.img_rad_duct.setMinimumSize(QSize(300, 0))
        self.img_rad_duct.setPixmap(
            QPixmap(u":/images/images/MachineSetup/LamParam/RadVentDuct.png")
        )
        self.img_rad_duct.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.img_rad_duct)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.in_Nrvd = QLabel(self.g_rad_vent)
        self.in_Nrvd.setObjectName(u"in_Nrvd")

        self.horizontalLayout_4.addWidget(self.in_Nrvd)

        self.si_Nrvd = QSpinBox(self.g_rad_vent)
        self.si_Nrvd.setObjectName(u"si_Nrvd")
        self.si_Nrvd.setMaximum(999)
        self.si_Nrvd.setValue(0)

        self.horizontalLayout_4.addWidget(self.si_Nrvd)

        self.in_Wrvd = QLabel(self.g_rad_vent)
        self.in_Wrvd.setObjectName(u"in_Wrvd")

        self.horizontalLayout_4.addWidget(self.in_Wrvd)

        self.lf_Wrvd = FloatEdit(self.g_rad_vent)
        self.lf_Wrvd.setObjectName(u"lf_Wrvd")
        self.lf_Wrvd.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_4.addWidget(self.lf_Wrvd)

        self.unit_Wrvd = QLabel(self.g_rad_vent)
        self.unit_Wrvd.setObjectName(u"unit_Wrvd")

        self.horizontalLayout_4.addWidget(self.unit_Wrvd)

        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.out_length = QLabel(self.g_rad_vent)
        self.out_length.setObjectName(u"out_length")
        self.out_length.setMinimumSize(QSize(250, 0))
        self.out_length.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_2.addWidget(self.out_length)

        self.horizontalLayout_3.addWidget(self.g_rad_vent)

        self.main_layout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_7 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.b_plot = QPushButton(SLamParam)
        self.b_plot.setObjectName(u"b_plot")

        self.horizontalLayout_6.addWidget(self.b_plot)

        self.b_previous = QPushButton(SLamParam)
        self.b_previous.setObjectName(u"b_previous")

        self.horizontalLayout_6.addWidget(self.b_previous)

        self.b_next = QPushButton(SLamParam)
        self.b_next.setObjectName(u"b_next")

        self.horizontalLayout_6.addWidget(self.b_next)

        self.main_layout.addLayout(self.horizontalLayout_6)

        QWidget.setTabOrder(self.lf_L1, self.lf_Kf1)
        QWidget.setTabOrder(self.lf_Kf1, self.b_next)
        QWidget.setTabOrder(self.b_next, self.si_Nrvd)
        QWidget.setTabOrder(self.si_Nrvd, self.lf_Wrvd)

        self.retranslateUi(SLamParam)

        QMetaObject.connectSlotsByName(SLamParam)

    # setupUi

    def retranslateUi(self, SLamParam):
        SLamParam.setWindowTitle(QCoreApplication.translate("SLamParam", u"Form", None))
        self.in_L1.setText(QCoreApplication.translate("SLamParam", u"L1 :", None))
        self.unit_L1.setText(QCoreApplication.translate("SLamParam", u"m", None))
        self.in_Kf1.setText(QCoreApplication.translate("SLamParam", u"Kf1 :", None))
        self.g_ax_vent.setTitle(
            QCoreApplication.translate("SLamParam", u"Axial Ventilation Ducts", None)
        )
        self.label.setText("")
        self.out_axial_duct.setText(
            QCoreApplication.translate("SLamParam", u"Axial : 0 set (0 ducts)", None)
        )
        self.b_axial_duct.setText(
            QCoreApplication.translate("SLamParam", u"set axial ducts", None)
        )
        self.g_rad_vent.setTitle(
            QCoreApplication.translate("SLamParam", u"Radial Ventilation Ducts", None)
        )
        self.img_rad_duct.setText("")
        self.in_Nrvd.setText(QCoreApplication.translate("SLamParam", u"Nrvd :", None))
        self.in_Wrvd.setText(QCoreApplication.translate("SLamParam", u"Wrvd :", None))
        self.unit_Wrvd.setText(QCoreApplication.translate("SLamParam", u"m", None))
        self.out_length.setText(
            QCoreApplication.translate(
                "SLamParam", u"stator total length = L1 + Nrvd * Wrvd = ?", None
            )
        )
        self.b_plot.setText(QCoreApplication.translate("SLamParam", u"Preview", None))
        self.b_previous.setText(
            QCoreApplication.translate("SLamParam", u"Previous", None)
        )
        self.b_next.setText(QCoreApplication.translate("SLamParam", u"Next", None))

    # retranslateUi
