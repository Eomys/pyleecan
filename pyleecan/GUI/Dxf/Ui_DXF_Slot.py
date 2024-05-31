# -*- coding: utf-8 -*-

# File generated according to DXF_Slot.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from ...GUI.Tools.FloatEdit import FloatEdit
from ...GUI.Tools.WPathSelector.WPathSelector import WPathSelector

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_DXF_Slot(object):
    def setupUi(self, DXF_Slot):
        if not DXF_Slot.objectName():
            DXF_Slot.setObjectName("DXF_Slot")
        DXF_Slot.resize(968, 674)
        icon = QIcon()
        icon.addFile(
            ":/images/images/icon/pyleecan_64.png", QSize(), QIcon.Normal, QIcon.Off
        )
        DXF_Slot.setWindowIcon(icon)
        self.horizontalLayout_5 = QHBoxLayout(DXF_Slot)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.layout_plot = QVBoxLayout()
        self.layout_plot.setObjectName("layout_plot")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.b_reset = QPushButton(DXF_Slot)
        self.b_reset.setObjectName("b_reset")

        self.horizontalLayout.addWidget(self.b_reset)

        self.b_cancel = QPushButton(DXF_Slot)
        self.b_cancel.setObjectName("b_cancel")

        self.horizontalLayout.addWidget(self.b_cancel)

        self.b_tuto = QPushButton(DXF_Slot)
        self.b_tuto.setObjectName("b_tuto")
        self.b_tuto.setEnabled(False)

        self.horizontalLayout.addWidget(self.b_tuto)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.layout_plot.addLayout(self.horizontalLayout)

        self.textBrowser = QTextBrowser(DXF_Slot)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setMaximumSize(QSize(16777215, 200))

        self.layout_plot.addWidget(self.textBrowser)

        self.horizontalLayout_5.addLayout(self.layout_plot)

        self.widget = QWidget(DXF_Slot)
        self.widget.setObjectName("widget")
        self.widget.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.g_import = QGroupBox(self.widget)
        self.g_import.setObjectName("g_import")
        self.verticalLayout = QVBoxLayout(self.g_import)
        self.verticalLayout.setObjectName("verticalLayout")
        self.w_path_selector = WPathSelector(self.g_import)
        self.w_path_selector.setObjectName("w_path_selector")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.w_path_selector.sizePolicy().hasHeightForWidth()
        )
        self.w_path_selector.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.w_path_selector)

        self.is_convert = QCheckBox(self.g_import)
        self.is_convert.setObjectName("is_convert")
        self.is_convert.setChecked(True)

        self.verticalLayout.addWidget(self.is_convert)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.in_tol = QLabel(self.g_import)
        self.in_tol.setObjectName("in_tol")

        self.horizontalLayout_3.addWidget(self.in_tol)

        self.lf_tol = FloatEdit(self.g_import)
        self.lf_tol.setObjectName("lf_tol")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lf_tol.sizePolicy().hasHeightForWidth())
        self.lf_tol.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.lf_tol)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2.addWidget(self.g_import)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.in_Zs = QLabel(self.widget)
        self.in_Zs.setObjectName("in_Zs")

        self.horizontalLayout_7.addWidget(self.in_Zs)

        self.si_Zs = QSpinBox(self.widget)
        self.si_Zs.setObjectName("si_Zs")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.si_Zs.sizePolicy().hasHeightForWidth())
        self.si_Zs.setSizePolicy(sizePolicy2)
        self.si_Zs.setMinimum(1)
        self.si_Zs.setMaximum(1000)
        self.si_Zs.setSingleStep(0)
        self.si_Zs.setValue(36)

        self.horizontalLayout_7.addWidget(self.si_Zs)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.in_axe_angle = QLabel(self.widget)
        self.in_axe_angle.setObjectName("in_axe_angle")

        self.horizontalLayout_6.addWidget(self.in_axe_angle)

        self.lf_axe_angle = FloatEdit(self.widget)
        self.lf_axe_angle.setObjectName("lf_axe_angle")
        sizePolicy1.setHeightForWidth(
            self.lf_axe_angle.sizePolicy().hasHeightForWidth()
        )
        self.lf_axe_angle.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.lf_axe_angle)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.g_active = QGroupBox(self.widget)
        self.g_active.setObjectName("g_active")
        self.gridLayout = QGridLayout(self.g_active)
        self.gridLayout.setObjectName("gridLayout")
        self.c_type_line = QComboBox(self.g_active)
        self.c_type_line.addItem("")
        self.c_type_line.addItem("")
        self.c_type_line.setObjectName("c_type_line")

        self.gridLayout.addWidget(self.c_type_line, 0, 1, 1, 1)

        self.in_wind_begin_index = QLabel(self.g_active)
        self.in_wind_begin_index.setObjectName("in_wind_begin_index")

        self.gridLayout.addWidget(self.in_wind_begin_index, 1, 0, 1, 1)

        self.in_type_line = QLabel(self.g_active)
        self.in_type_line.setObjectName("in_type_line")

        self.gridLayout.addWidget(self.in_type_line, 0, 0, 1, 1)

        self.si_wind_begin_index = QSpinBox(self.g_active)
        self.si_wind_begin_index.setObjectName("si_wind_begin_index")

        self.gridLayout.addWidget(self.si_wind_begin_index, 1, 1, 1, 1)

        self.in_wind_end_index = QLabel(self.g_active)
        self.in_wind_end_index.setObjectName("in_wind_end_index")

        self.gridLayout.addWidget(self.in_wind_end_index, 2, 0, 1, 1)

        self.si_wind_end_index = QSpinBox(self.g_active)
        self.si_wind_end_index.setObjectName("si_wind_end_index")

        self.gridLayout.addWidget(self.si_wind_end_index, 2, 1, 1, 1)

        self.verticalLayout_2.addWidget(self.g_active)

        self.g_center = QGroupBox(self.widget)
        self.g_center.setObjectName("g_center")
        self.gridLayout_2 = QGridLayout(self.g_center)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.in_coord_center_X = QLabel(self.g_center)
        self.in_coord_center_X.setObjectName("in_coord_center_X")

        self.gridLayout_2.addWidget(self.in_coord_center_X, 0, 0, 1, 1)

        self.lf_center_x = FloatEdit(self.g_center)
        self.lf_center_x.setObjectName("lf_center_x")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lf_center_x.sizePolicy().hasHeightForWidth())
        self.lf_center_x.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.lf_center_x, 0, 1, 1, 1)

        self.in_coord_center_Y = QLabel(self.g_center)
        self.in_coord_center_Y.setObjectName("in_coord_center_Y")

        self.gridLayout_2.addWidget(self.in_coord_center_Y, 1, 0, 1, 1)

        self.lf_center_y = FloatEdit(self.g_center)
        self.lf_center_y.setObjectName("lf_center_y")
        self.lf_center_y.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lf_center_y.sizePolicy().hasHeightForWidth())
        self.lf_center_y.setSizePolicy(sizePolicy3)
        self.lf_center_y.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.lf_center_y, 1, 1, 1, 1)

        self.verticalLayout_2.addWidget(self.g_center)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.in_scaling = QLabel(self.widget)
        self.in_scaling.setObjectName("in_scaling")

        self.horizontalLayout_4.addWidget(self.in_scaling)

        self.lf_scaling = FloatEdit(self.widget)
        self.lf_scaling.setObjectName("lf_scaling")
        sizePolicy3.setHeightForWidth(self.lf_scaling.sizePolicy().hasHeightForWidth())
        self.lf_scaling.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.lf_scaling)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.b_plot = QPushButton(self.widget)
        self.b_plot.setObjectName("b_plot")

        self.horizontalLayout_2.addWidget(self.b_plot)

        self.b_save = QPushButton(self.widget)
        self.b_save.setObjectName("b_save")

        self.horizontalLayout_2.addWidget(self.b_save)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5.addWidget(self.widget)

        self.retranslateUi(DXF_Slot)

        QMetaObject.connectSlotsByName(DXF_Slot)

    # setupUi

    def retranslateUi(self, DXF_Slot):
        DXF_Slot.setWindowTitle(
            QCoreApplication.translate("DXF_Slot", "Define Slot from DXF", None)
        )
        self.b_reset.setText(QCoreApplication.translate("DXF_Slot", "Reset View", None))
        self.b_cancel.setText(
            QCoreApplication.translate("DXF_Slot", "Cancel Selection", None)
        )
        self.b_tuto.setText(
            QCoreApplication.translate("DXF_Slot", "Open Tutorial", None)
        )
        self.textBrowser.setHtml(
            QCoreApplication.translate(
                "DXF_Slot",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'DejaVu Sans'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">1) Import your DXF file in [m] or set a scaling factor</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">FEMM convertion enables to merge close points according to tolerance in [local unit] and converts lines to arcs and segments (splines need to be converted)</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0p'
                'x; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">2) Click on lines and arcs to draw the contour of a single slot</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">3) First point and last point must be on the bore radius (must match the lamination radius)</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">4) The winding area is defined by a part of the slot contour and a closing line:</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">- The points are ordered in trigonometrical order (from bore radius to bore radius)</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-'
                'bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">- First point index is 0</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">- Closing line can be either a segment or an arc (centered on X=0, Y=0)</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">5) Plot to check and save</span></p></body></html>',
                None,
            )
        )
        self.g_import.setTitle(
            QCoreApplication.translate("DXF_Slot", "DXF file import", None)
        )
        self.is_convert.setText(
            QCoreApplication.translate("DXF_Slot", "Convert through FEMM", None)
        )
        self.in_tol.setText(
            QCoreApplication.translate("DXF_Slot", "Merge tolerance [l.u.]", None)
        )
        self.lf_tol.setText(QCoreApplication.translate("DXF_Slot", "1e-5", None))
        self.in_Zs.setText(
            QCoreApplication.translate("DXF_Slot", "Number of slots", None)
        )
        self.in_axe_angle.setText(
            QCoreApplication.translate("DXF_Slot", "Slot axe angle shift", None)
        )
        self.lf_axe_angle.setText(QCoreApplication.translate("DXF_Slot", "0", None))
        self.g_active.setTitle(QCoreApplication.translate("DXF_Slot", "Winding", None))
        self.c_type_line.setItemText(
            0, QCoreApplication.translate("DXF_Slot", "Segment", None)
        )
        self.c_type_line.setItemText(
            1, QCoreApplication.translate("DXF_Slot", "Arc1", None)
        )

        self.in_wind_begin_index.setText(
            QCoreApplication.translate("DXF_Slot", "Winding start index", None)
        )
        self.in_type_line.setText(
            QCoreApplication.translate("DXF_Slot", "Closing line type", None)
        )
        self.in_wind_end_index.setText(
            QCoreApplication.translate("DXF_Slot", "Winding end index", None)
        )
        self.g_center.setTitle(
            QCoreApplication.translate("DXF_Slot", "Machine Center", None)
        )
        self.in_coord_center_X.setText(
            QCoreApplication.translate("DXF_Slot", "X coordinate [l.u.]", None)
        )
        self.lf_center_x.setText(QCoreApplication.translate("DXF_Slot", "0", None))
        self.in_coord_center_Y.setText(
            QCoreApplication.translate("DXF_Slot", "Y coordinate [l.u.]", None)
        )
        self.lf_center_y.setText(QCoreApplication.translate("DXF_Slot", "0", None))
        self.in_scaling.setText(
            QCoreApplication.translate("DXF_Slot", "Scaling factor [l.u.] to [m]", None)
        )
        self.lf_scaling.setText(QCoreApplication.translate("DXF_Slot", "1", None))
        self.b_plot.setText(QCoreApplication.translate("DXF_Slot", "Plot", None))
        self.b_save.setText(QCoreApplication.translate("DXF_Slot", "Save", None))

    # retranslateUi
