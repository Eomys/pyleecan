# -*- coding: utf-8 -*-

# File generated according to SSkew.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from .....GUI.Tools.FloatEdit import FloatEdit
from .....GUI.Tools.MPLCanvas import MPLCanvas

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SSkew(object):
    def setupUi(self, SSkew):
        if not SSkew.objectName():
            SSkew.setObjectName("SSkew")
        SSkew.resize(972, 577)
        SSkew.setMinimumSize(QSize(650, 550))
        self.verticalLayout_4 = QVBoxLayout(SSkew)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.g_plot = QGroupBox(SSkew)
        self.g_plot.setObjectName("g_plot")
        self.g_plot.setMinimumSize(QSize(800, 0))
        self.verticalLayout_2 = QVBoxLayout(self.g_plot)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.w_viewer = MPLCanvas(self.g_plot)
        self.w_viewer.setObjectName("w_viewer")

        self.verticalLayout_2.addWidget(self.w_viewer)

        self.horizontalLayout.addWidget(self.g_plot)

        self.scrollArea = QScrollArea(SSkew)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMinimumSize(QSize(370, 0))
        self.scrollArea.setMaximumSize(QSize(370, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 368, 524))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.g_activate = QGroupBox(self.scrollAreaWidgetContents)
        self.g_activate.setObjectName("g_activate")
        self.g_activate.setMinimumSize(QSize(0, 0))
        self.g_activate.setMaximumSize(QSize(16777215, 16777215))
        self.g_activate.setCheckable(True)
        self.g_activate.setChecked(False)
        self.verticalLayout = QVBoxLayout(self.g_activate)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.in_type = QLabel(self.g_activate)
        self.in_type.setObjectName("in_type")

        self.gridLayout.addWidget(self.in_type, 0, 0, 1, 1)

        self.cb_type = QComboBox(self.g_activate)
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.setObjectName("cb_type")

        self.gridLayout.addWidget(self.cb_type, 0, 1, 1, 1)

        self.in_step = QLabel(self.g_activate)
        self.in_step.setObjectName("in_step")

        self.gridLayout.addWidget(self.in_step, 1, 0, 1, 1)

        self.cb_step = QComboBox(self.g_activate)
        self.cb_step.addItem("")
        self.cb_step.addItem("")
        self.cb_step.setObjectName("cb_step")

        self.gridLayout.addWidget(self.cb_step, 1, 1, 1, 1)

        self.label_segments = QLabel(self.g_activate)
        self.label_segments.setObjectName("label_segments")

        self.gridLayout.addWidget(self.label_segments, 2, 0, 1, 1)

        self.sb_nslice = QSpinBox(self.g_activate)
        self.sb_nslice.setObjectName("sb_nslice")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sb_nslice.sizePolicy().hasHeightForWidth())
        self.sb_nslice.setSizePolicy(sizePolicy)
        self.sb_nslice.setMaximumSize(QSize(16777215, 16777215))
        self.sb_nslice.setMinimum(2)
        self.sb_nslice.setMaximum(200)
        self.sb_nslice.setSingleStep(1)
        self.sb_nslice.setValue(152)

        self.gridLayout.addWidget(self.sb_nslice, 2, 1, 1, 1)

        self.label_rate = QLabel(self.g_activate)
        self.label_rate.setObjectName("label_rate")

        self.gridLayout.addWidget(self.label_rate, 3, 0, 1, 1)

        self.lf_angle = FloatEdit(self.g_activate)
        self.lf_angle.setObjectName("lf_angle")

        self.gridLayout.addWidget(self.lf_angle, 3, 1, 1, 1)

        self.label_deg = QLabel(self.g_activate)
        self.label_deg.setObjectName("label_deg")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_deg.sizePolicy().hasHeightForWidth())
        self.label_deg.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_deg, 3, 2, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.in_slot_pitch = QLabel(self.g_activate)
        self.in_slot_pitch.setObjectName("in_slot_pitch")

        self.verticalLayout.addWidget(self.in_slot_pitch)

        self.tab_angle = QTableWidget(self.g_activate)
        self.tab_angle.setObjectName("tab_angle")
        self.tab_angle.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tab_angle)

        self.verticalLayout_3.addWidget(self.g_activate)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalSpacer_7 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.b_previous = QPushButton(SSkew)
        self.b_previous.setObjectName("b_previous")

        self.horizontalLayout_6.addWidget(self.b_previous)

        self.b_next = QPushButton(SSkew)
        self.b_next.setObjectName("b_next")

        self.horizontalLayout_6.addWidget(self.b_next)

        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.retranslateUi(SSkew)

        self.cb_type.setCurrentIndex(3)

        QMetaObject.connectSlotsByName(SSkew)

    # setupUi

    def retranslateUi(self, SSkew):
        SSkew.setWindowTitle(QCoreApplication.translate("SSkew", "Form", None))
        self.g_plot.setTitle(QCoreApplication.translate("SSkew", "Preview", None))
        self.g_activate.setTitle(
            QCoreApplication.translate("SSkew", "Activate Rotor Skew", None)
        )
        self.in_type.setText(QCoreApplication.translate("SSkew", "Type of Skew", None))
        self.cb_type.setItemText(0, QCoreApplication.translate("SSkew", "Linear", None))
        self.cb_type.setItemText(
            1, QCoreApplication.translate("SSkew", "V-shape", None)
        )
        self.cb_type.setItemText(2, QCoreApplication.translate("SSkew", "Zigzag", None))
        self.cb_type.setItemText(
            3, QCoreApplication.translate("SSkew", "User-defined", None)
        )

        self.in_step.setText(
            QCoreApplication.translate("SSkew", "Step/Continuous", None)
        )
        self.cb_step.setItemText(0, QCoreApplication.translate("SSkew", "Step", None))
        self.cb_step.setItemText(
            1, QCoreApplication.translate("SSkew", "Continuous", None)
        )

        self.label_segments.setText(
            QCoreApplication.translate("SSkew", "Number of steps", None)
        )
        self.label_rate.setText(
            QCoreApplication.translate("SSkew", "Skew Angle ", None)
        )
        self.label_deg.setText(QCoreApplication.translate("SSkew", "[deg]", None))
        self.in_slot_pitch.setText(
            QCoreApplication.translate(
                "SSkew", "Stator slot pitch = 20 [deg] / Skew rate = %", None
            )
        )
        self.b_previous.setText(QCoreApplication.translate("SSkew", "Previous", None))
        self.b_next.setText(QCoreApplication.translate("SSkew", "Next", None))

    # retranslateUi
