# -*- coding: utf-8 -*-

# File generated according to DXF_Hole.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ...GUI.Tools.FloatEdit import FloatEdit
from ...GUI.Tools.WPathSelector.WPathSelector import WPathSelector

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_DXF_Hole(object):
    def setupUi(self, DXF_Hole):
        if not DXF_Hole.objectName():
            DXF_Hole.setObjectName(u"DXF_Hole")
        DXF_Hole.resize(783, 653)
        icon = QIcon()
        icon.addFile(
            u":/images/images/icon/pyleecan_64.png", QSize(), QIcon.Normal, QIcon.Off
        )
        DXF_Hole.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(DXF_Hole)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.b_reset = QPushButton(DXF_Hole)
        self.b_reset.setObjectName(u"b_reset")

        self.horizontalLayout.addWidget(self.b_reset)

        self.b_cancel = QPushButton(DXF_Hole)
        self.b_cancel.setObjectName(u"b_cancel")

        self.horizontalLayout.addWidget(self.b_cancel)

        self.b_tuto = QPushButton(DXF_Hole)
        self.b_tuto.setObjectName(u"b_tuto")
        self.b_tuto.setEnabled(False)

        self.horizontalLayout.addWidget(self.b_tuto)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.w_side = QWidget(DXF_Hole)
        self.w_side.setObjectName(u"w_side")
        self.w_side.setMinimumSize(QSize(400, 0))
        self.w_side.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout = QVBoxLayout(self.w_side)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.w_path_selector = WPathSelector(self.w_side)
        self.w_path_selector.setObjectName(u"w_path_selector")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.w_path_selector.sizePolicy().hasHeightForWidth()
        )
        self.w_path_selector.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.w_path_selector)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.in_zh = QLabel(self.w_side)
        self.in_zh.setObjectName(u"in_zh")

        self.gridLayout.addWidget(self.in_zh, 0, 0, 1, 1)

        self.si_Zh = QSpinBox(self.w_side)
        self.si_Zh.setObjectName(u"si_Zh")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.si_Zh.sizePolicy().hasHeightForWidth())
        self.si_Zh.setSizePolicy(sizePolicy1)
        self.si_Zh.setMinimum(1)
        self.si_Zh.setMaximum(1000)
        self.si_Zh.setSingleStep(0)
        self.si_Zh.setValue(36)

        self.gridLayout.addWidget(self.si_Zh, 0, 1, 1, 1)

        self.in_mag_len = QLabel(self.w_side)
        self.in_mag_len.setObjectName(u"in_mag_len")

        self.gridLayout.addWidget(self.in_mag_len, 1, 0, 1, 1)

        self.lf_mag_len = FloatEdit(self.w_side)
        self.lf_mag_len.setObjectName(u"lf_mag_len")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lf_mag_len.sizePolicy().hasHeightForWidth())
        self.lf_mag_len.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lf_mag_len, 1, 1, 1, 1)

        self.unit_mag_len = QLabel(self.w_side)
        self.unit_mag_len.setObjectName(u"unit_mag_len")
        self.unit_mag_len.setMaximumSize(QSize(40, 16777215))

        self.gridLayout.addWidget(self.unit_mag_len, 1, 2, 1, 1)

        self.in_axe_angle = QLabel(self.w_side)
        self.in_axe_angle.setObjectName(u"in_axe_angle")

        self.gridLayout.addWidget(self.in_axe_angle, 2, 0, 1, 1)

        self.lf_axe_angle = FloatEdit(self.w_side)
        self.lf_axe_angle.setObjectName(u"lf_axe_angle")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.lf_axe_angle.sizePolicy().hasHeightForWidth()
        )
        self.lf_axe_angle.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.lf_axe_angle, 2, 1, 1, 1)

        self.unit_axe_angle = QLabel(self.w_side)
        self.unit_axe_angle.setObjectName(u"unit_axe_angle")

        self.gridLayout.addWidget(self.unit_axe_angle, 2, 2, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.g_center = QGroupBox(self.w_side)
        self.g_center.setObjectName(u"g_center")
        self.gridLayout_3 = QGridLayout(self.g_center)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.in_coord_center_X = QLabel(self.g_center)
        self.in_coord_center_X.setObjectName(u"in_coord_center_X")

        self.gridLayout_3.addWidget(self.in_coord_center_X, 0, 0, 1, 1)

        self.lf_center_x = FloatEdit(self.g_center)
        self.lf_center_x.setObjectName(u"lf_center_x")
        sizePolicy2.setHeightForWidth(self.lf_center_x.sizePolicy().hasHeightForWidth())
        self.lf_center_x.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.lf_center_x, 0, 1, 1, 1)

        self.in_coord_center_Y = QLabel(self.g_center)
        self.in_coord_center_Y.setObjectName(u"in_coord_center_Y")

        self.gridLayout_3.addWidget(self.in_coord_center_Y, 1, 0, 1, 1)

        self.lf_center_y = FloatEdit(self.g_center)
        self.lf_center_y.setObjectName(u"lf_center_y")
        self.lf_center_y.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.lf_center_y.sizePolicy().hasHeightForWidth())
        self.lf_center_y.setSizePolicy(sizePolicy2)
        self.lf_center_y.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.lf_center_y, 1, 1, 1, 1)

        self.verticalLayout.addWidget(self.g_center)

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
        self.w_surface_list.setObjectName(u"w_surface_list")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.w_surface_list.sizePolicy().hasHeightForWidth()
        )
        self.w_surface_list.setSizePolicy(sizePolicy4)
        self.w_surface_list.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.w_surface_list)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.in_scaling = QLabel(self.w_side)
        self.in_scaling.setObjectName(u"in_scaling")

        self.horizontalLayout_4.addWidget(self.in_scaling)

        self.lf_scaling = FloatEdit(self.w_side)
        self.lf_scaling.setObjectName(u"lf_scaling")
        sizePolicy2.setHeightForWidth(self.lf_scaling.sizePolicy().hasHeightForWidth())
        self.lf_scaling.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.lf_scaling)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.b_plot = QPushButton(self.w_side)
        self.b_plot.setObjectName(u"b_plot")

        self.horizontalLayout_2.addWidget(self.b_plot)

        self.b_save = QPushButton(self.w_side)
        self.b_save.setObjectName(u"b_save")

        self.horizontalLayout_2.addWidget(self.b_save)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout_2.addWidget(self.w_side, 0, 1, 3, 1)

        self.w_viewer = QVBoxLayout()
        self.w_viewer.setObjectName(u"w_viewer")
        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.w_viewer.addItem(self.verticalSpacer)

        self.gridLayout_2.addLayout(self.w_viewer, 1, 0, 1, 1)

        self.textBrowser = QTextBrowser(DXF_Hole)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(16777215, 200))

        self.gridLayout_2.addWidget(self.textBrowser, 2, 0, 1, 1)

        self.retranslateUi(DXF_Hole)

        QMetaObject.connectSlotsByName(DXF_Hole)

    # setupUi

    def retranslateUi(self, DXF_Hole):
        DXF_Hole.setWindowTitle(
            QCoreApplication.translate("DXF_Hole", u"Define Hole from DXF", None)
        )
        self.b_reset.setText(
            QCoreApplication.translate("DXF_Hole", u"Reset View", None)
        )
        self.b_cancel.setText(
            QCoreApplication.translate("DXF_Hole", u"Cancel Selection", None)
        )
        self.b_tuto.setText(
            QCoreApplication.translate("DXF_Hole", u"Open Tutorial", None)
        )
        self.in_zh.setText(
            QCoreApplication.translate("DXF_Hole", u"Number of holes", None)
        )
        self.in_mag_len.setText(
            QCoreApplication.translate("DXF_Hole", u"Magnet length", None)
        )
        self.lf_mag_len.setText(QCoreApplication.translate("DXF_Hole", u"1", None))
        self.unit_mag_len.setText(QCoreApplication.translate("DXF_Hole", u"[m]", None))
        self.in_axe_angle.setText(
            QCoreApplication.translate("DXF_Hole", u"Hole main axe angle", None)
        )
        self.lf_axe_angle.setText(QCoreApplication.translate("DXF_Hole", u"0", None))
        self.unit_axe_angle.setText(
            QCoreApplication.translate("DXF_Hole", u"[rad]", None)
        )
        self.g_center.setTitle(
            QCoreApplication.translate("DXF_Hole", u"Machine Center", None)
        )
        self.in_coord_center_X.setText(
            QCoreApplication.translate("DXF_Hole", u"X coordinate", None)
        )
        self.lf_center_x.setText(QCoreApplication.translate("DXF_Hole", u"0", None))
        self.in_coord_center_Y.setText(
            QCoreApplication.translate("DXF_Hole", u"Y coordinate", None)
        )
        self.lf_center_y.setText(QCoreApplication.translate("DXF_Hole", u"0", None))
        ___qtablewidgetitem = self.w_surface_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("DXF_Hole", u"Delete", None)
        )
        ___qtablewidgetitem1 = self.w_surface_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("DXF_Hole", u"Show", None)
        )
        ___qtablewidgetitem2 = self.w_surface_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("DXF_Hole", u"Type", None)
        )
        ___qtablewidgetitem3 = self.w_surface_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("DXF_Hole", u"Mag Ref", None)
        )
        ___qtablewidgetitem4 = self.w_surface_list.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("DXF_Hole", u"Mag Offset [deg]", None)
        )
        self.in_scaling.setText(
            QCoreApplication.translate("DXF_Hole", u"Scaling factor", None)
        )
        self.lf_scaling.setText(QCoreApplication.translate("DXF_Hole", u"1", None))
        self.b_plot.setText(QCoreApplication.translate("DXF_Hole", u"Plot", None))
        self.b_save.setText(QCoreApplication.translate("DXF_Hole", u"Save", None))
        self.textBrowser.setHtml(
            QCoreApplication.translate(
                "DXF_Hole",
                u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'MS Shell Dlg 2\'; font-size:12pt;">1) Select DXF file in [m] (or use scaling factor), spline won\'t be displayed</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'MS Shell Dlg 2\'; font-size:12pt;">2) Use mouse wheel to zoom in/out</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"'
                "><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">3) Click on lines and arcs to define a closed area</span></p>\n"
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'MS Shell Dlg 2\'; font-size:12pt;">4) Select all the surfaces of a single hole (air + magnet)</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'MS Shell Dlg 2\'; font-size:12pt;">5) Assign the surface type (air or magnet)</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'MS Shell Dlg 2\'; font-size:12pt;">6) Define the magnetization direction of each magnet with:</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; m'
                'argin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'MS Shell Dlg 2\'; font-size:12pt;">- Mag ref: Line index whose normal is used as reference</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'MS Shell Dlg 2\'; font-size:12pt;">- Mag offset: will be added to angle of the line normal [deg]</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'MS Shell Dlg 2\'; font-size:12pt;">7) Plot to check and save</span></p>\n'
                '<p align="justify" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:12pt;"><br /></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin'
                '-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'MS Shell Dlg 2\'; font-size:12pt;">Hint: When clicking twice on a line, its color changes to define this line as magnetization reference for the magnet.</span></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'MS Shell Dlg 2\'; font-size:12pt;">Hint: &quot;Show&quot; highlights the surface and display the index of each line/arc. </span></p></body></html>',
                None,
            )
        )

    # retranslateUi
