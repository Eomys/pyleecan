# -*- coding: utf-8 -*-

# File generated according to SWinding.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .....GUI.Tools.MPLCanvas import MPLCanvas
from .....GUI.Tools.SpinBox import SpinBox

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SWinding(object):
    def setupUi(self, SWinding):
        if not SWinding.objectName():
            SWinding.setObjectName(u"SWinding")
        SWinding.resize(1103, 866)
        SWinding.setMinimumSize(QSize(650, 550))
        self.gridLayout_3 = QGridLayout(SWinding)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.b_previous = QPushButton(SWinding)
        self.b_previous.setObjectName(u"b_previous")

        self.horizontalLayout_3.addWidget(self.b_previous)

        self.b_next = QPushButton(SWinding)
        self.b_next.setObjectName(u"b_next")

        self.horizontalLayout_3.addWidget(self.b_next)

        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)

        self.scrollArea = QScrollArea(SWinding)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(300, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 277, 843))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.g_pattern = QGroupBox(self.scrollAreaWidgetContents)
        self.g_pattern.setObjectName(u"g_pattern")
        self.gridLayout_2 = QGridLayout(self.g_pattern)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.in_Zs_2 = QLabel(self.g_pattern)
        self.in_Zs_2.setObjectName(u"in_Zs_2")

        self.gridLayout_2.addWidget(self.in_Zs_2, 0, 0, 1, 1)

        self.c_wind_type = QComboBox(self.g_pattern)
        self.c_wind_type.addItem("")
        self.c_wind_type.addItem("")
        self.c_wind_type.setObjectName(u"c_wind_type")

        self.gridLayout_2.addWidget(self.c_wind_type, 0, 1, 1, 1)

        self.in_Zs = QLabel(self.g_pattern)
        self.in_Zs.setObjectName(u"in_Zs")

        self.gridLayout_2.addWidget(self.in_Zs, 1, 0, 1, 2)

        self.in_p = QLabel(self.g_pattern)
        self.in_p.setObjectName(u"in_p")

        self.gridLayout_2.addWidget(self.in_p, 2, 0, 1, 2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.si_qs = SpinBox(self.g_pattern)
        self.si_qs.setObjectName(u"si_qs")

        self.gridLayout.addWidget(self.si_qs, 0, 1, 1, 1)

        self.in_qs = QLabel(self.g_pattern)
        self.in_qs.setObjectName(u"in_qs")

        self.gridLayout.addWidget(self.in_qs, 0, 0, 1, 1)

        self.si_coil_pitch = SpinBox(self.g_pattern)
        self.si_coil_pitch.setObjectName(u"si_coil_pitch")

        self.gridLayout.addWidget(self.si_coil_pitch, 2, 1, 1, 1)

        self.in_Npcp = QLabel(self.g_pattern)
        self.in_Npcp.setObjectName(u"in_Npcp")

        self.gridLayout.addWidget(self.in_Npcp, 4, 0, 1, 1)

        self.si_Ntcoil = SpinBox(self.g_pattern)
        self.si_Ntcoil.setObjectName(u"si_Ntcoil")

        self.gridLayout.addWidget(self.si_Ntcoil, 3, 1, 1, 1)

        self.in_coil_pitch = QLabel(self.g_pattern)
        self.in_coil_pitch.setObjectName(u"in_coil_pitch")

        self.gridLayout.addWidget(self.in_coil_pitch, 2, 0, 1, 1)

        self.si_Npcp = SpinBox(self.g_pattern)
        self.si_Npcp.setObjectName(u"si_Npcp")
        self.si_Npcp.setMaximum(999999999)
        self.si_Npcp.setValue(12345)

        self.gridLayout.addWidget(self.si_Npcp, 4, 1, 1, 1)

        self.in_Ntcoil = QLabel(self.g_pattern)
        self.in_Ntcoil.setObjectName(u"in_Ntcoil")

        self.gridLayout.addWidget(self.in_Ntcoil, 3, 0, 1, 1)

        self.c_layer_def = QComboBox(self.g_pattern)
        self.c_layer_def.addItem("")
        self.c_layer_def.addItem("")
        self.c_layer_def.addItem("")
        self.c_layer_def.setObjectName(u"c_layer_def")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c_layer_def.sizePolicy().hasHeightForWidth())
        self.c_layer_def.setSizePolicy(sizePolicy)
        self.c_layer_def.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.c_layer_def, 1, 0, 1, 2)

        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 2)

        self.b_generate = QPushButton(self.g_pattern)
        self.b_generate.setObjectName(u"b_generate")

        self.gridLayout_2.addWidget(self.b_generate, 4, 0, 1, 2)

        self.b_import = QPushButton(self.g_pattern)
        self.b_import.setObjectName(u"b_import")

        self.gridLayout_2.addWidget(self.b_import, 5, 0, 1, 2)

        self.verticalLayout_5.addWidget(self.g_pattern)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.g_edit = QGroupBox(self.scrollAreaWidgetContents)
        self.g_edit.setObjectName(u"g_edit")
        self.verticalLayout = QVBoxLayout(self.g_edit)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.in_Nslot = QLabel(self.g_edit)
        self.in_Nslot.setObjectName(u"in_Nslot")
        self.in_Nslot.setMinimumSize(QSize(0, 0))
        self.in_Nslot.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.in_Nslot)

        self.si_Nslot = SpinBox(self.g_edit)
        self.si_Nslot.setObjectName(u"si_Nslot")
        self.si_Nslot.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_4.addWidget(self.si_Nslot)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.is_permute_B_C = QCheckBox(self.g_edit)
        self.is_permute_B_C.setObjectName(u"is_permute_B_C")

        self.verticalLayout.addWidget(self.is_permute_B_C)

        self.is_reverse = QCheckBox(self.g_edit)
        self.is_reverse.setObjectName(u"is_reverse")

        self.verticalLayout.addWidget(self.is_reverse)

        self.is_reverse_layer = QCheckBox(self.g_edit)
        self.is_reverse_layer.setObjectName(u"is_reverse_layer")

        self.verticalLayout.addWidget(self.is_reverse_layer)

        self.b_edit_wind_mat = QPushButton(self.g_edit)
        self.b_edit_wind_mat.setObjectName(u"b_edit_wind_mat")

        self.verticalLayout.addWidget(self.b_edit_wind_mat)

        self.verticalLayout_5.addWidget(self.g_edit)

        self.g_output = QGroupBox(self.scrollAreaWidgetContents)
        self.g_output.setObjectName(u"g_output")
        self.g_output.setMinimumSize(QSize(200, 0))
        self.verticalLayout_3 = QVBoxLayout(self.g_output)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.out_rot_dir = QLabel(self.g_output)
        self.out_rot_dir.setObjectName(u"out_rot_dir")
        self.out_rot_dir.setMinimumSize(QSize(175, 0))

        self.verticalLayout_3.addWidget(self.out_rot_dir)

        self.out_ms = QLabel(self.g_output)
        self.out_ms.setObjectName(u"out_ms")

        self.verticalLayout_3.addWidget(self.out_ms)

        self.out_Nperw = QLabel(self.g_output)
        self.out_Nperw.setObjectName(u"out_Nperw")

        self.verticalLayout_3.addWidget(self.out_Nperw)

        self.out_Ntspc = QLabel(self.g_output)
        self.out_Ntspc.setObjectName(u"out_Ntspc")

        self.verticalLayout_3.addWidget(self.out_Ntspc)

        self.out_Ncspc = QLabel(self.g_output)
        self.out_Ncspc.setObjectName(u"out_Ncspc")

        self.verticalLayout_3.addWidget(self.out_Ncspc)

        self.b_plot_mmf = QPushButton(self.g_output)
        self.b_plot_mmf.setObjectName(u"b_plot_mmf")

        self.verticalLayout_3.addWidget(self.b_plot_mmf)

        self.b_plot_linear = QPushButton(self.g_output)
        self.b_plot_linear.setObjectName(u"b_plot_linear")

        self.verticalLayout_3.addWidget(self.b_plot_linear)

        self.b_plot_radial = QPushButton(self.g_output)
        self.b_plot_radial.setObjectName(u"b_plot_radial")

        self.verticalLayout_3.addWidget(self.b_plot_radial)

        self.b_export = QPushButton(self.g_output)
        self.b_export.setObjectName(u"b_export")

        self.verticalLayout_3.addWidget(self.b_export)

        self.verticalLayout_5.addWidget(self.g_output)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 1, 1, 1)

        self.w_viewer = MPLCanvas(SWinding)
        self.w_viewer.setObjectName(u"w_viewer")
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
        SWinding.setWindowTitle(QCoreApplication.translate("SWinding", u"Form", None))
        self.b_previous.setText(
            QCoreApplication.translate("SWinding", u"Previous", None)
        )
        self.b_next.setText(QCoreApplication.translate("SWinding", u"Next", None))
        self.g_pattern.setTitle(
            QCoreApplication.translate("SWinding", u"Winding pattern", None)
        )
        self.in_Zs_2.setText(
            QCoreApplication.translate("SWinding", u"Generation method", None)
        )
        self.c_wind_type.setItemText(
            0, QCoreApplication.translate("SWinding", u"Star of Slot", None)
        )
        self.c_wind_type.setItemText(
            1, QCoreApplication.translate("SWinding", u"User Defined", None)
        )

        self.in_Zs.setText(
            QCoreApplication.translate("SWinding", u"Slot number=123", None)
        )
        self.in_p.setText(
            QCoreApplication.translate("SWinding", u"Pole pair number=32", None)
        )
        self.in_qs.setText(
            QCoreApplication.translate("SWinding", u"Phases number", None)
        )
        self.in_Npcp.setText(
            QCoreApplication.translate("SWinding", u"Parallel circuits", None)
        )
        self.in_coil_pitch.setText(
            QCoreApplication.translate("SWinding", u"Throw", None)
        )
        self.in_Ntcoil.setText(
            QCoreApplication.translate("SWinding", u"Turns per coil", None)
        )
        self.c_layer_def.setItemText(
            0, QCoreApplication.translate("SWinding", u"Single Layer", None)
        )
        self.c_layer_def.setItemText(
            1, QCoreApplication.translate("SWinding", u"Double Layer overlapping", None)
        )
        self.c_layer_def.setItemText(
            2,
            QCoreApplication.translate(
                "SWinding", u"Double Layer non-overlapping", None
            ),
        )

        self.b_generate.setText(
            QCoreApplication.translate("SWinding", u"Generate", None)
        )
        self.b_import.setText(
            QCoreApplication.translate("SWinding", u"Import from CSV", None)
        )
        self.g_edit.setTitle(
            QCoreApplication.translate("SWinding", u"Winding transformation", None)
        )
        self.in_Nslot.setText(
            QCoreApplication.translate("SWinding", u"Slot shift", None)
        )
        self.is_permute_B_C.setText(
            QCoreApplication.translate("SWinding", u"Permute B-C phases", None)
        )
        self.is_reverse.setText(
            QCoreApplication.translate("SWinding", u"Reverse winding", None)
        )
        self.is_reverse_layer.setText(
            QCoreApplication.translate("SWinding", u"Reverse layer", None)
        )
        self.b_edit_wind_mat.setText(
            QCoreApplication.translate("SWinding", u"Edit Winding Matrix", None)
        )
        self.g_output.setTitle(QCoreApplication.translate("SWinding", u"Output", None))
        # if QT_CONFIG(tooltip)
        self.out_rot_dir.setToolTip(
            QCoreApplication.translate(
                "SWinding",
                u"<qt><nobr>Fundamental field rotation direction when feeding the</nobr> winding with direct AC current</qt>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.out_rot_dir.setStatusTip(
            QCoreApplication.translate(
                "SWinding",
                u"Fundamental field rotation direction when feeding the winding with direct AC current",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.out_rot_dir.setWhatsThis(
            QCoreApplication.translate(
                "SWinding",
                u"Fundamental field rotation direction when feeding the winding with direct AC current",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.out_rot_dir.setText(
            QCoreApplication.translate("SWinding", u"Rotation Direction", None)
        )
        self.out_ms.setText(
            QCoreApplication.translate(
                "SWinding", u"Number of slot per pole per phase", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.out_Nperw.setToolTip(
            QCoreApplication.translate(
                "SWinding", u"<qt><nobr>Winding periodicity</nobr></qt>", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.out_Nperw.setText(
            QCoreApplication.translate("SWinding", u"Winding periodicity", None)
        )
        # if QT_CONFIG(tooltip)
        self.out_Ntspc.setToolTip(
            QCoreApplication.translate(
                "SWinding",
                u"<qt><nobr>Winding number of turns in series per phase</nobr></qt>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.out_Ntspc.setStatusTip(
            QCoreApplication.translate(
                "SWinding", u"Winding number of turns in series per phase", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.out_Ntspc.setWhatsThis(
            QCoreApplication.translate(
                "SWinding", u"Winding number of turns in series per phase", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.out_Ntspc.setText(
            QCoreApplication.translate(
                "SWinding", u"Number of turns in series per phase", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.out_Ncspc.setToolTip(
            QCoreApplication.translate(
                "SWinding",
                u"<qt><nobr>Number of coils in series per parallel circuit</nobr></qt>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.out_Ncspc.setStatusTip(
            QCoreApplication.translate(
                "SWinding", u"Number of coils in series per parallel circuit", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.out_Ncspc.setWhatsThis(
            QCoreApplication.translate(
                "SWinding", u"Number of coils in series per parallel circuit", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.out_Ncspc.setText(
            QCoreApplication.translate(
                "SWinding", u"Number of coils in series per parallel circuit", None
            )
        )
        self.b_plot_mmf.setText(
            QCoreApplication.translate("SWinding", u"Plot Stator Unit MMF", None)
        )
        self.b_plot_linear.setText(
            QCoreApplication.translate("SWinding", u"Plot Winding Linear Pattern", None)
        )
        self.b_plot_radial.setText(
            QCoreApplication.translate("SWinding", u"Plot Winding Radial Pattern", None)
        )
        self.b_export.setText(
            QCoreApplication.translate("SWinding", u"Export to CSV", None)
        )

    # retranslateUi
