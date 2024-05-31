# -*- coding: utf-8 -*-

# File generated according to DXF_Hole.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from ...GUI.Tools.FloatEdit import FloatEdit
from ...GUI.Tools.WPathSelector.WPathSelector import WPathSelector

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_DXF_Hole(object):
    def setupUi(self, DXF_Hole):
        if not DXF_Hole.objectName():
            DXF_Hole.setObjectName("DXF_Hole")
        DXF_Hole.resize(864, 653)
        icon = QIcon()
        icon.addFile(
            ":/images/images/icon/pyleecan_64.png", QSize(), QIcon.Normal, QIcon.Off
        )
        DXF_Hole.setWindowIcon(icon)
        self.horizontalLayout_5 = QHBoxLayout(DXF_Hole)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.layout_plot = QVBoxLayout()
        self.layout_plot.setObjectName("layout_plot")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.b_reset = QPushButton(DXF_Hole)
        self.b_reset.setObjectName("b_reset")

        self.horizontalLayout.addWidget(self.b_reset)

        self.b_cancel = QPushButton(DXF_Hole)
        self.b_cancel.setObjectName("b_cancel")

        self.horizontalLayout.addWidget(self.b_cancel)

        self.b_tuto = QPushButton(DXF_Hole)
        self.b_tuto.setObjectName("b_tuto")
        self.b_tuto.setEnabled(False)

        self.horizontalLayout.addWidget(self.b_tuto)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.layout_plot.addLayout(self.horizontalLayout)

        self.textBrowser = QTextBrowser(DXF_Hole)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setMaximumSize(QSize(16777215, 200))

        self.layout_plot.addWidget(self.textBrowser)

        self.horizontalLayout_5.addLayout(self.layout_plot)

        self.w_side = QWidget(DXF_Hole)
        self.w_side.setObjectName("w_side")
        self.w_side.setMinimumSize(QSize(400, 0))
        self.w_side.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.w_side)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.g_import = QGroupBox(self.w_side)
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

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.in_zh = QLabel(self.w_side)
        self.in_zh.setObjectName("in_zh")

        self.gridLayout.addWidget(self.in_zh, 0, 0, 1, 1)

        self.si_Zh = QSpinBox(self.w_side)
        self.si_Zh.setObjectName("si_Zh")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.si_Zh.sizePolicy().hasHeightForWidth())
        self.si_Zh.setSizePolicy(sizePolicy2)
        self.si_Zh.setMinimum(1)
        self.si_Zh.setMaximum(1000)
        self.si_Zh.setSingleStep(0)
        self.si_Zh.setValue(36)

        self.gridLayout.addWidget(self.si_Zh, 0, 1, 1, 1)

        self.in_mag_len = QLabel(self.w_side)
        self.in_mag_len.setObjectName("in_mag_len")

        self.gridLayout.addWidget(self.in_mag_len, 1, 0, 1, 1)

        self.lf_mag_len = FloatEdit(self.w_side)
        self.lf_mag_len.setObjectName("lf_mag_len")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lf_mag_len.sizePolicy().hasHeightForWidth())
        self.lf_mag_len.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.lf_mag_len, 1, 1, 1, 1)

        self.unit_mag_len = QLabel(self.w_side)
        self.unit_mag_len.setObjectName("unit_mag_len")
        self.unit_mag_len.setMaximumSize(QSize(40, 16777215))

        self.gridLayout.addWidget(self.unit_mag_len, 1, 2, 1, 1)

        self.in_axe_angle = QLabel(self.w_side)
        self.in_axe_angle.setObjectName("in_axe_angle")

        self.gridLayout.addWidget(self.in_axe_angle, 2, 0, 1, 1)

        self.lf_axe_angle = FloatEdit(self.w_side)
        self.lf_axe_angle.setObjectName("lf_axe_angle")
        sizePolicy1.setHeightForWidth(
            self.lf_axe_angle.sizePolicy().hasHeightForWidth()
        )
        self.lf_axe_angle.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.lf_axe_angle, 2, 1, 1, 1)

        self.unit_axe_angle = QLabel(self.w_side)
        self.unit_axe_angle.setObjectName("unit_axe_angle")

        self.gridLayout.addWidget(self.unit_axe_angle, 2, 2, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.g_center = QGroupBox(self.w_side)
        self.g_center.setObjectName("g_center")
        self.gridLayout_3 = QGridLayout(self.g_center)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.in_coord_center_X = QLabel(self.g_center)
        self.in_coord_center_X.setObjectName("in_coord_center_X")

        self.gridLayout_3.addWidget(self.in_coord_center_X, 0, 0, 1, 1)

        self.lf_center_x = FloatEdit(self.g_center)
        self.lf_center_x.setObjectName("lf_center_x")
        sizePolicy3.setHeightForWidth(self.lf_center_x.sizePolicy().hasHeightForWidth())
        self.lf_center_x.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.lf_center_x, 0, 1, 1, 1)

        self.in_coord_center_Y = QLabel(self.g_center)
        self.in_coord_center_Y.setObjectName("in_coord_center_Y")

        self.gridLayout_3.addWidget(self.in_coord_center_Y, 1, 0, 1, 1)

        self.lf_center_y = FloatEdit(self.g_center)
        self.lf_center_y.setObjectName("lf_center_y")
        self.lf_center_y.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lf_center_y.sizePolicy().hasHeightForWidth())
        self.lf_center_y.setSizePolicy(sizePolicy3)
        self.lf_center_y.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.lf_center_y, 1, 1, 1, 1)

        self.verticalLayout_2.addWidget(self.g_center)

        self.w_surface_list = QTableWidget(self.w_side)
        if self.w_surface_list.columnCount() < 5:
            self.w_surface_list.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.w_surface_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.w_surface_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.w_surface_list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.w_surface_list.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.w_surface_list.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.w_surface_list.setObjectName("w_surface_list")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.w_surface_list.sizePolicy().hasHeightForWidth()
        )
        self.w_surface_list.setSizePolicy(sizePolicy4)
        self.w_surface_list.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.w_surface_list)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.in_scaling = QLabel(self.w_side)
        self.in_scaling.setObjectName("in_scaling")

        self.horizontalLayout_4.addWidget(self.in_scaling)

        self.lf_scaling = FloatEdit(self.w_side)
        self.lf_scaling.setObjectName("lf_scaling")
        sizePolicy3.setHeightForWidth(self.lf_scaling.sizePolicy().hasHeightForWidth())
        self.lf_scaling.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.lf_scaling)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.b_plot = QPushButton(self.w_side)
        self.b_plot.setObjectName("b_plot")

        self.horizontalLayout_2.addWidget(self.b_plot)

        self.b_save = QPushButton(self.w_side)
        self.b_save.setObjectName("b_save")

        self.horizontalLayout_2.addWidget(self.b_save)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5.addWidget(self.w_side)

        self.retranslateUi(DXF_Hole)

        QMetaObject.connectSlotsByName(DXF_Hole)

    # setupUi

    def retranslateUi(self, DXF_Hole):
        DXF_Hole.setWindowTitle(
            QCoreApplication.translate("DXF_Hole", "Define Hole from DXF", None)
        )
        self.b_reset.setText(QCoreApplication.translate("DXF_Hole", "Reset View", None))
        self.b_cancel.setText(
            QCoreApplication.translate("DXF_Hole", "Cancel Selection", None)
        )
        self.b_tuto.setText(
            QCoreApplication.translate("DXF_Hole", "Open Tutorial", None)
        )
        self.textBrowser.setHtml(
            QCoreApplication.translate(
                "DXF_Hole",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'DejaVu Sans'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">1) Import your DXF file in [m] or set a scaling factor</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">FEMM convertion enables to merge close points according to tolerance in [local unit] and converts lines to arcs and segments (splines need to be converted)</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0p'
                'x; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">2) Click on lines and arcs to define a closed area</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">3) Select all the surfaces of a single hole (air + magnet)</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">4) Assign the surface type (air or magnet)</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">5) Define the magnetization direction of each magnet with:</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-siz'
                'e:10pt;">- Mag ref: line index whose normal is used as reference</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">- Mag offset: will be added to angle of the line normal [deg]</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">6) Plot to check and save</span></p>\n'
                '<p align="justify" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;"><br /></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">Hint: When clicking twice on a line, its color changes to define this line as magnetization reference for the magne'
                "t.</span></p>\n"
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">Hint: &quot;Show&quot; highlights the surface and display the index of each line/arc. </span></p></body></html>',
                None,
            )
        )
        self.g_import.setTitle(
            QCoreApplication.translate("DXF_Hole", "DXF file import", None)
        )
        self.is_convert.setText(
            QCoreApplication.translate("DXF_Hole", "Convert through FEMM", None)
        )
        self.in_tol.setText(
            QCoreApplication.translate("DXF_Hole", "Merge tolerance [l.u.]", None)
        )
        self.lf_tol.setText(QCoreApplication.translate("DXF_Hole", "1e-5", None))
        self.in_zh.setText(
            QCoreApplication.translate("DXF_Hole", "Number of holes", None)
        )
        self.in_mag_len.setText(
            QCoreApplication.translate("DXF_Hole", "Magnet length", None)
        )
        self.lf_mag_len.setText(QCoreApplication.translate("DXF_Hole", "1", None))
        self.unit_mag_len.setText(QCoreApplication.translate("DXF_Hole", "[m]", None))
        self.in_axe_angle.setText(
            QCoreApplication.translate("DXF_Hole", "Hole main axe angle", None)
        )
        self.lf_axe_angle.setText(QCoreApplication.translate("DXF_Hole", "0", None))
        self.unit_axe_angle.setText(
            QCoreApplication.translate("DXF_Hole", "[rad]", None)
        )
        self.g_center.setTitle(
            QCoreApplication.translate("DXF_Hole", "Machine Center", None)
        )
        self.in_coord_center_X.setText(
            QCoreApplication.translate("DXF_Hole", "X coordinate [l.u.]", None)
        )
        self.lf_center_x.setText(QCoreApplication.translate("DXF_Hole", "0", None))
        self.in_coord_center_Y.setText(
            QCoreApplication.translate("DXF_Hole", "Y coordinate [l.u.]", None)
        )
        self.lf_center_y.setText(QCoreApplication.translate("DXF_Hole", "0", None))
        ___qtablewidgetitem = self.w_surface_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("DXF_Hole", "Delete", None)
        )
        ___qtablewidgetitem1 = self.w_surface_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("DXF_Hole", "Show", None)
        )
        ___qtablewidgetitem2 = self.w_surface_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("DXF_Hole", "Type", None)
        )
        ___qtablewidgetitem3 = self.w_surface_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("DXF_Hole", "Mag Ref", None)
        )
        ___qtablewidgetitem4 = self.w_surface_list.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("DXF_Hole", "Mag Offset [deg]", None)
        )
        self.in_scaling.setText(
            QCoreApplication.translate("DXF_Hole", "Scaling factor [l.u.] to [m]", None)
        )
        self.lf_scaling.setText(QCoreApplication.translate("DXF_Hole", "1", None))
        self.b_plot.setText(QCoreApplication.translate("DXF_Hole", "Plot", None))
        self.b_save.setText(QCoreApplication.translate("DXF_Hole", "Save", None))

    # retranslateUi
