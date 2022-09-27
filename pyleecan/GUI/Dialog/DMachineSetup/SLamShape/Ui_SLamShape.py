# -*- coding: utf-8 -*-

# File generated according to SLamShape.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .....GUI.Tools.MPLCanvas import MPLCanvas
from .....GUI.Tools.FloatEdit import FloatEdit
from .....GUI.Dialog.DMatLib.WMatSelect.WMatSelectV import WMatSelectV

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SLamShape(object):
    def setupUi(self, SLamShape):
        if not SLamShape.objectName():
            SLamShape.setObjectName(u"SLamShape")
        SLamShape.resize(1083, 846)
        SLamShape.setMinimumSize(QSize(650, 550))
        self.verticalLayout_4 = QVBoxLayout(SLamShape)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.w_viewer = MPLCanvas(SLamShape)
        self.w_viewer.setObjectName(u"w_viewer")
        self.w_viewer.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_8.addWidget(self.w_viewer)

        self.scrollArea = QScrollArea(SLamShape)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 272, 762))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.in_L1 = QLabel(self.scrollAreaWidgetContents)
        self.in_L1.setObjectName(u"in_L1")
        self.in_L1.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.in_L1, 1, 0, 1, 1)

        self.lf_L1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_L1.setObjectName(u"lf_L1")
        self.lf_L1.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.lf_L1, 1, 1, 1, 1)

        self.unit_L1 = QLabel(self.scrollAreaWidgetContents)
        self.unit_L1.setObjectName(u"unit_L1")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unit_L1.sizePolicy().hasHeightForWidth())
        self.unit_L1.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.unit_L1, 1, 2, 1, 1)

        self.in_Kf1 = QLabel(self.scrollAreaWidgetContents)
        self.in_Kf1.setObjectName(u"in_Kf1")

        self.gridLayout_2.addWidget(self.in_Kf1, 2, 0, 1, 1)

        self.lf_Kf1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_Kf1.setObjectName(u"lf_Kf1")
        self.lf_Kf1.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_2.addWidget(self.lf_Kf1, 2, 1, 1, 1)

        self.verticalLayout_5.addLayout(self.gridLayout_2)

        self.w_mat = WMatSelectV(self.scrollAreaWidgetContents)
        self.w_mat.setObjectName(u"w_mat")
        self.w_mat.setMinimumSize(QSize(100, 0))

        self.verticalLayout_5.addWidget(self.w_mat)

        self.g_axial = QGroupBox(self.scrollAreaWidgetContents)
        self.g_axial.setObjectName(u"g_axial")
        self.g_axial.setCheckable(True)
        self.g_axial.setChecked(False)
        self.verticalLayout = QVBoxLayout(self.g_axial)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.out_axial_duct = QLabel(self.g_axial)
        self.out_axial_duct.setObjectName(u"out_axial_duct")

        self.verticalLayout.addWidget(self.out_axial_duct)

        self.b_axial_duct = QPushButton(self.g_axial)
        self.b_axial_duct.setObjectName(u"b_axial_duct")

        self.verticalLayout.addWidget(self.b_axial_duct)

        self.verticalLayout_5.addWidget(self.g_axial)

        self.g_radial = QGroupBox(self.scrollAreaWidgetContents)
        self.g_radial.setObjectName(u"g_radial")
        self.g_radial.setCheckable(True)
        self.g_radial.setChecked(False)
        self.verticalLayout_2 = QVBoxLayout(self.g_radial)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.in_Nrvd = QLabel(self.g_radial)
        self.in_Nrvd.setObjectName(u"in_Nrvd")

        self.gridLayout.addWidget(self.in_Nrvd, 0, 0, 1, 1)

        self.si_Nrvd = QSpinBox(self.g_radial)
        self.si_Nrvd.setObjectName(u"si_Nrvd")
        self.si_Nrvd.setMaximum(999)
        self.si_Nrvd.setValue(0)

        self.gridLayout.addWidget(self.si_Nrvd, 0, 1, 1, 1)

        self.in_Wrvd = QLabel(self.g_radial)
        self.in_Wrvd.setObjectName(u"in_Wrvd")

        self.gridLayout.addWidget(self.in_Wrvd, 1, 0, 1, 1)

        self.lf_Wrvd = FloatEdit(self.g_radial)
        self.lf_Wrvd.setObjectName(u"lf_Wrvd")
        self.lf_Wrvd.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.lf_Wrvd, 1, 1, 1, 1)

        self.unit_Wrvd = QLabel(self.g_radial)
        self.unit_Wrvd.setObjectName(u"unit_Wrvd")

        self.gridLayout.addWidget(self.unit_Wrvd, 1, 2, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.out_length = QLabel(self.g_radial)
        self.out_length.setObjectName(u"out_length")
        self.out_length.setMinimumSize(QSize(0, 0))
        self.out_length.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.out_length)

        self.verticalLayout_5.addWidget(self.g_radial)

        self.g_notches = QGroupBox(self.scrollAreaWidgetContents)
        self.g_notches.setObjectName(u"g_notches")
        self.g_notches.setCheckable(True)
        self.g_notches.setChecked(False)
        self.verticalLayout_3 = QVBoxLayout(self.g_notches)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.out_notch = QLabel(self.g_notches)
        self.out_notch.setObjectName(u"out_notch")

        self.verticalLayout_3.addWidget(self.out_notch)

        self.b_notch = QPushButton(self.g_notches)
        self.b_notch.setObjectName(u"b_notch")

        self.verticalLayout_3.addWidget(self.b_notch)

        self.verticalLayout_5.addWidget(self.g_notches)

        self.g_bore = QGroupBox(self.scrollAreaWidgetContents)
        self.g_bore.setObjectName(u"g_bore")
        self.g_bore.setCheckable(True)
        self.g_bore.setChecked(False)
        self.verticalLayout_6 = QVBoxLayout(self.g_bore)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.b_bore = QPushButton(self.g_bore)
        self.b_bore.setObjectName(u"b_bore")

        self.verticalLayout_6.addWidget(self.b_bore)

        self.verticalLayout_5.addWidget(self.g_bore)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_8.addWidget(self.scrollArea)

        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.b_previous = QPushButton(SLamShape)
        self.b_previous.setObjectName(u"b_previous")

        self.horizontalLayout_3.addWidget(self.b_previous)

        self.b_next = QPushButton(SLamShape)
        self.b_next.setObjectName(u"b_next")

        self.horizontalLayout_3.addWidget(self.b_next)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi(SLamShape)

        QMetaObject.connectSlotsByName(SLamShape)

    # setupUi

    def retranslateUi(self, SLamShape):
        SLamShape.setWindowTitle(QCoreApplication.translate("SLamShape", u"Form", None))
        # if QT_CONFIG(tooltip)
        self.in_L1.setToolTip(
            QCoreApplication.translate("SLamShape", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.in_L1.setText(QCoreApplication.translate("SLamShape", u"L1:", None))
        # if QT_CONFIG(tooltip)
        self.lf_L1.setToolTip(
            QCoreApplication.translate("SLamShape", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.unit_L1.setText(QCoreApplication.translate("SLamShape", u"m", None))
        self.in_Kf1.setText(QCoreApplication.translate("SLamShape", u"Kf1 :", None))
        self.g_axial.setTitle(
            QCoreApplication.translate("SLamShape", u"Axial cooling duct", None)
        )
        self.out_axial_duct.setText(
            QCoreApplication.translate("SLamShape", u"Axial : 0 set (0 ducts)", None)
        )
        self.b_axial_duct.setText(
            QCoreApplication.translate("SLamShape", u"set axial ducts", None)
        )
        self.g_radial.setTitle(
            QCoreApplication.translate("SLamShape", u"Radial cooling duct", None)
        )
        self.in_Nrvd.setText(QCoreApplication.translate("SLamShape", u"Nrvd :", None))
        self.in_Wrvd.setText(QCoreApplication.translate("SLamShape", u"Wrvd :", None))
        self.unit_Wrvd.setText(QCoreApplication.translate("SLamShape", u"m", None))
        self.out_length.setText(
            QCoreApplication.translate(
                "SLamShape", u"stator total length = L1+Nrvd*Wrvd = ?", None
            )
        )
        self.g_notches.setTitle(
            QCoreApplication.translate("SLamShape", u"Notches", None)
        )
        self.out_notch.setText(
            QCoreApplication.translate("SLamShape", u"0 set (0 notches)", None)
        )
        self.b_notch.setText(
            QCoreApplication.translate("SLamShape", u"set notches", None)
        )
        self.g_bore.setTitle(
            QCoreApplication.translate("SLamShape", u"Uneven bore shape", None)
        )
        self.b_bore.setText(
            QCoreApplication.translate("SLamShape", u"set uneven bore shape", None)
        )
        self.b_previous.setText(
            QCoreApplication.translate("SLamShape", u"Previous", None)
        )
        self.b_next.setText(QCoreApplication.translate("SLamShape", u"Next", None))

    # retranslateUi
