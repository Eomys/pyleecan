# -*- coding: utf-8 -*-

# File generated according to SWinding.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from .....GUI.Tools.MPLCanvas import MPLCanvas
from .....GUI.Tools.SpinBox import SpinBox

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SWinding(object):
    def setupUi(self, SWinding):
        if not SWinding.objectName():
            SWinding.setObjectName("SWinding")
        SWinding.resize(1103, 866)
        SWinding.setMinimumSize(QSize(650, 550))
        self.gridLayout_3 = QGridLayout(SWinding)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.b_previous = QPushButton(SWinding)
        self.b_previous.setObjectName("b_previous")

        self.horizontalLayout_3.addWidget(self.b_previous)

        self.b_next = QPushButton(SWinding)
        self.b_next.setObjectName("b_next")

        self.horizontalLayout_3.addWidget(self.b_next)

        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)

        self.scrollArea = QScrollArea(SWinding)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMinimumSize(QSize(300, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 277, 843))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.g_pattern = QGroupBox(self.scrollAreaWidgetContents)
        self.g_pattern.setObjectName("g_pattern")
        self.gridLayout_2 = QGridLayout(self.g_pattern)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.in_Zs_2 = QLabel(self.g_pattern)
        self.in_Zs_2.setObjectName("in_Zs_2")

        self.gridLayout_2.addWidget(self.in_Zs_2, 0, 0, 1, 1)

        self.c_wind_type = QComboBox(self.g_pattern)
        self.c_wind_type.addItem("")
        self.c_wind_type.addItem("")
        self.c_wind_type.setObjectName("c_wind_type")

        self.gridLayout_2.addWidget(self.c_wind_type, 0, 1, 1, 1)

        self.in_Zs = QLabel(self.g_pattern)
        self.in_Zs.setObjectName("in_Zs")

        self.gridLayout_2.addWidget(self.in_Zs, 1, 0, 1, 2)

        self.in_p = QLabel(self.g_pattern)
        self.in_p.setObjectName("in_p")

        self.gridLayout_2.addWidget(self.in_p, 2, 0, 1, 2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.si_qs = SpinBox(self.g_pattern)
        self.si_qs.setObjectName("si_qs")

        self.gridLayout.addWidget(self.si_qs, 0, 1, 1, 1)

        self.in_qs = QLabel(self.g_pattern)
        self.in_qs.setObjectName("in_qs")

        self.gridLayout.addWidget(self.in_qs, 0, 0, 1, 1)

        self.si_coil_pitch = SpinBox(self.g_pattern)
        self.si_coil_pitch.setObjectName("si_coil_pitch")

        self.gridLayout.addWidget(self.si_coil_pitch, 2, 1, 1, 1)

        self.in_Npcp = QLabel(self.g_pattern)
        self.in_Npcp.setObjectName("in_Npcp")

        self.gridLayout.addWidget(self.in_Npcp, 4, 0, 1, 1)

        self.si_Ntcoil = SpinBox(self.g_pattern)
        self.si_Ntcoil.setObjectName("si_Ntcoil")

        self.gridLayout.addWidget(self.si_Ntcoil, 3, 1, 1, 1)

        self.in_coil_pitch = QLabel(self.g_pattern)
        self.in_coil_pitch.setObjectName("in_coil_pitch")

        self.gridLayout.addWidget(self.in_coil_pitch, 2, 0, 1, 1)

        self.si_Npcp = SpinBox(self.g_pattern)
        self.si_Npcp.setObjectName("si_Npcp")
        self.si_Npcp.setMaximum(999999999)
        self.si_Npcp.setValue(12345)

        self.gridLayout.addWidget(self.si_Npcp, 4, 1, 1, 1)

        self.in_Ntcoil = QLabel(self.g_pattern)
        self.in_Ntcoil.setObjectName("in_Ntcoil")

        self.gridLayout.addWidget(self.in_Ntcoil, 3, 0, 1, 1)

        self.c_layer_def = QComboBox(self.g_pattern)
        self.c_layer_def.addItem("")
        self.c_layer_def.addItem("")
        self.c_layer_def.addItem("")
        self.c_layer_def.setObjectName("c_layer_def")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c_layer_def.sizePolicy().hasHeightForWidth())
        self.c_layer_def.setSizePolicy(sizePolicy)
        self.c_layer_def.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.c_layer_def, 1, 0, 1, 2)

        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 2)

        self.b_generate = QPushButton(self.g_pattern)
        self.b_generate.setObjectName("b_generate")

        self.gridLayout_2.addWidget(self.b_generate, 4, 0, 1, 2)

        self.b_import = QPushButton(self.g_pattern)
        self.b_import.setObjectName("b_import")

        self.gridLayout_2.addWidget(self.b_import, 5, 0, 1, 2)

        self.verticalLayout_5.addWidget(self.g_pattern)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.g_edit = QGroupBox(self.scrollAreaWidgetContents)
        self.g_edit.setObjectName("g_edit")
        self.verticalLayout = QVBoxLayout(self.g_edit)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.in_Nslot = QLabel(self.g_edit)
        self.in_Nslot.setObjectName("in_Nslot")
        self.in_Nslot.setMinimumSize(QSize(0, 0))
        self.in_Nslot.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.in_Nslot)

        self.si_Nslot = SpinBox(self.g_edit)
        self.si_Nslot.setObjectName("si_Nslot")
        self.si_Nslot.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_4.addWidget(self.si_Nslot)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.is_permute_B_C = QCheckBox(self.g_edit)
        self.is_permute_B_C.setObjectName("is_permute_B_C")

        self.verticalLayout.addWidget(self.is_permute_B_C)

        self.is_reverse = QCheckBox(self.g_edit)
        self.is_reverse.setObjectName("is_reverse")

        self.verticalLayout.addWidget(self.is_reverse)

        self.is_reverse_layer = QCheckBox(self.g_edit)
        self.is_reverse_layer.setObjectName("is_reverse_layer")

        self.verticalLayout.addWidget(self.is_reverse_layer)

        self.b_edit_wind_mat = QPushButton(self.g_edit)
        self.b_edit_wind_mat.setObjectName("b_edit_wind_mat")

        self.verticalLayout.addWidget(self.b_edit_wind_mat)

        self.verticalLayout_5.addWidget(self.g_edit)

        self.g_output = QGroupBox(self.scrollAreaWidgetContents)
        self.g_output.setObjectName("g_output")
        self.g_output.setMinimumSize(QSize(200, 0))
        self.verticalLayout_3 = QVBoxLayout(self.g_output)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.out_rot_dir = QLabel(self.g_output)
        self.out_rot_dir.setObjectName("out_rot_dir")
        self.out_rot_dir.setMinimumSize(QSize(175, 0))

        self.verticalLayout_3.addWidget(self.out_rot_dir)

        self.out_ms = QLabel(self.g_output)
        self.out_ms.setObjectName("out_ms")

        self.verticalLayout_3.addWidget(self.out_ms)

        self.out_Nperw = QLabel(self.g_output)
        self.out_Nperw.setObjectName("out_Nperw")

        self.verticalLayout_3.addWidget(self.out_Nperw)

        self.out_Ntspc = QLabel(self.g_output)
        self.out_Ntspc.setObjectName("out_Ntspc")

        self.verticalLayout_3.addWidget(self.out_Ntspc)

        self.out_Ncspc = QLabel(self.g_output)
        self.out_Ncspc.setObjectName("out_Ncspc")

        self.verticalLayout_3.addWidget(self.out_Ncspc)

        self.b_plot_mmf = QPushButton(self.g_output)
        self.b_plot_mmf.setObjectName("b_plot_mmf")

        self.verticalLayout_3.addWidget(self.b_plot_mmf)

        self.b_plot_linear = QPushButton(self.g_output)
        self.b_plot_linear.setObjectName("b_plot_linear")

        self.verticalLayout_3.addWidget(self.b_plot_linear)

        self.b_plot_radial = QPushButton(self.g_output)
        self.b_plot_radial.setObjectName("b_plot_radial")

        self.verticalLayout_3.addWidget(self.b_plot_radial)

        self.b_export = QPushButton(self.g_output)
        self.b_export.setObjectName("b_export")

        self.verticalLayout_3.addWidget(self.b_export)

        self.verticalLayout_5.addWidget(self.g_output)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 1, 1, 1)

        self.w_viewer = MPLCanvas(SWinding)
        self.w_viewer.setObjectName("w_viewer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.w_viewer.sizePolicy().hasHeightForWidth())
        self.w_viewer.setSizePolicy(sizePolicy1)
        self.w_viewer.setMinimumSize(QSize(250, 0))

        self.gridLayout_3.addWidget(self.w_viewer, 0, 0, 1, 1)

        self.retranslateUi(SWinding)

        QMetaObject.connectSlotsByName(SWinding)

    # setupUi

    def retranslateUi(self, SWinding):
        SWinding.setWindowTitle(QCoreApplication.translate("SWinding", "Form", None))
        self.b_previous.setText(
            QCoreApplication.translate("SWinding", "Previous", None)
        )
        self.b_next.setText(QCoreApplication.translate("SWinding", "Next", None))
        self.g_pattern.setTitle(
            QCoreApplication.translate("SWinding", "Winding pattern", None)
        )
        self.in_Zs_2.setText(
            QCoreApplication.translate("SWinding", "Generation method", None)
        )
        self.c_wind_type.setItemText(
            0, QCoreApplication.translate("SWinding", "Star of Slot", None)
        )
        self.c_wind_type.setItemText(
            1, QCoreApplication.translate("SWinding", "User Defined", None)
        )

        self.in_Zs.setText(
            QCoreApplication.translate("SWinding", "Slot number=123", None)
        )
        self.in_p.setText(
            QCoreApplication.translate("SWinding", "Pole pair number=32", None)
        )
        self.in_qs.setText(
            QCoreApplication.translate("SWinding", "Phases number", None)
        )
        self.in_Npcp.setText(
            QCoreApplication.translate("SWinding", "Parallel circuits", None)
        )
        self.in_coil_pitch.setText(
            QCoreApplication.translate("SWinding", "Throw", None)
        )
        self.in_Ntcoil.setText(
            QCoreApplication.translate("SWinding", "Turns per coil", None)
        )
        self.c_layer_def.setItemText(
            0, QCoreApplication.translate("SWinding", "Single Layer", None)
        )
        self.c_layer_def.setItemText(
            1, QCoreApplication.translate("SWinding", "Double Layer overlapping", None)
        )
        self.c_layer_def.setItemText(
            2,
            QCoreApplication.translate(
                "SWinding", "Double Layer non-overlapping", None
            ),
        )

        self.b_generate.setText(
            QCoreApplication.translate("SWinding", "Generate", None)
        )
        self.b_import.setText(
            QCoreApplication.translate("SWinding", "Import from CSV", None)
        )
        self.g_edit.setTitle(
            QCoreApplication.translate("SWinding", "Winding transformation", None)
        )
        self.in_Nslot.setText(
            QCoreApplication.translate("SWinding", "Slot shift", None)
        )
        self.is_permute_B_C.setText(
            QCoreApplication.translate("SWinding", "Permute B-C phases", None)
        )
        self.is_reverse.setText(
            QCoreApplication.translate("SWinding", "Reverse winding", None)
        )
        self.is_reverse_layer.setText(
            QCoreApplication.translate("SWinding", "Reverse layer", None)
        )
        self.b_edit_wind_mat.setText(
            QCoreApplication.translate("SWinding", "Edit Winding Matrix", None)
        )
        self.g_output.setTitle(QCoreApplication.translate("SWinding", "Output", None))
        # if QT_CONFIG(tooltip)
        self.out_rot_dir.setToolTip(
            QCoreApplication.translate(
                "SWinding",
                "Fundamental field rotation direction when feeding the winding with direct AC current",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.out_rot_dir.setStatusTip(
            QCoreApplication.translate(
                "SWinding",
                "Fundamental field rotation direction when feeding the winding with direct AC current",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.out_rot_dir.setWhatsThis(
            QCoreApplication.translate(
                "SWinding",
                "Fundamental field rotation direction when feeding the winding with direct AC current",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.out_rot_dir.setText(
            QCoreApplication.translate("SWinding", "Rotation Direction", None)
        )
        self.out_ms.setText(
            QCoreApplication.translate(
                "SWinding", "Number of slot per pole per phase", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.out_Nperw.setToolTip(
            QCoreApplication.translate("SWinding", "Winding periodicity", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.out_Nperw.setText(
            QCoreApplication.translate("SWinding", "Winding periodicity", None)
        )
        # if QT_CONFIG(tooltip)
        self.out_Ntspc.setToolTip(
            QCoreApplication.translate(
                "SWinding", "Winding number of turns in series per phase", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.out_Ntspc.setStatusTip(
            QCoreApplication.translate(
                "SWinding", "Winding number of turns in series per phase", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.out_Ntspc.setWhatsThis(
            QCoreApplication.translate(
                "SWinding", "Winding number of turns in series per phase", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.out_Ntspc.setText(
            QCoreApplication.translate(
                "SWinding", "Number of turns in series per phase", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.out_Ncspc.setToolTip(
            QCoreApplication.translate(
                "SWinding", "Number of coils in series per parallel circuit", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.out_Ncspc.setStatusTip(
            QCoreApplication.translate(
                "SWinding", "Number of coils in series per parallel circuit", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.out_Ncspc.setWhatsThis(
            QCoreApplication.translate(
                "SWinding", "Number of coils in series per parallel circuit", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.out_Ncspc.setText(
            QCoreApplication.translate(
                "SWinding", "Number of coils in series per parallel circuit", None
            )
        )
        self.b_plot_mmf.setText(
            QCoreApplication.translate("SWinding", "Plot Stator Unit MMF", None)
        )
        self.b_plot_linear.setText(
            QCoreApplication.translate("SWinding", "Plot Winding Linear Pattern", None)
        )
        self.b_plot_radial.setText(
            QCoreApplication.translate("SWinding", "Plot Winding Radial Pattern", None)
        )
        self.b_export.setText(
            QCoreApplication.translate("SWinding", "Export to CSV", None)
        )

    # retranslateUi
