# -*- coding: utf-8 -*-

# File generated according to DXF_Slot.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ...GUI.Tools.WPathSelector.WPathSelector import WPathSelector
from ...GUI.Tools.MPLCanvas import MPLCanvas2
from ...GUI.Tools.FloatEdit import FloatEdit

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_DXF_Slot(object):
    def setupUi(self, DXF_Slot):
        if not DXF_Slot.objectName():
            DXF_Slot.setObjectName(u"DXF_Slot")
        DXF_Slot.resize(745, 486)
        icon = QIcon()
        icon.addFile(
            u":/images/images/icon/pyleecan_64.png", QSize(), QIcon.Normal, QIcon.Off
        )
        DXF_Slot.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(DXF_Slot)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.w_viewer = MPLCanvas2(DXF_Slot)
        self.w_viewer.setObjectName(u"w_viewer")

        self.horizontalLayout.addWidget(self.w_viewer)

        self.widget = QWidget(DXF_Slot)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.w_path_selector = WPathSelector(self.widget)
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
        self.in_Zs = QLabel(self.widget)
        self.in_Zs.setObjectName(u"in_Zs")

        self.gridLayout.addWidget(self.in_Zs, 0, 0, 1, 1)

        self.si_Zs = QSpinBox(self.widget)
        self.si_Zs.setObjectName(u"si_Zs")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.si_Zs.sizePolicy().hasHeightForWidth())
        self.si_Zs.setSizePolicy(sizePolicy1)
        self.si_Zs.setMinimum(1)
        self.si_Zs.setMaximum(1000)
        self.si_Zs.setSingleStep(0)
        self.si_Zs.setValue(36)

        self.gridLayout.addWidget(self.si_Zs, 0, 1, 1, 1)

        self.in_wind_begin_index = QLabel(self.widget)
        self.in_wind_begin_index.setObjectName(u"in_wind_begin_index")

        self.gridLayout.addWidget(self.in_wind_begin_index, 1, 0, 1, 1)

        self.si_wind_begin_index = QSpinBox(self.widget)
        self.si_wind_begin_index.setObjectName(u"si_wind_begin_index")

        self.gridLayout.addWidget(self.si_wind_begin_index, 1, 1, 1, 1)

        self.in_wind_end_index = QLabel(self.widget)
        self.in_wind_end_index.setObjectName(u"in_wind_end_index")

        self.gridLayout.addWidget(self.in_wind_end_index, 2, 0, 1, 1)

        self.si_wind_end_index = QSpinBox(self.widget)
        self.si_wind_end_index.setObjectName(u"si_wind_end_index")

        self.gridLayout.addWidget(self.si_wind_end_index, 2, 1, 1, 1)

        self.in_type_line = QLabel(self.widget)
        self.in_type_line.setObjectName(u"in_type_line")

        self.gridLayout.addWidget(self.in_type_line, 3, 0, 1, 1)

        self.c_type_line = QComboBox(self.widget)
        self.c_type_line.addItem("")
        self.c_type_line.addItem("")
        self.c_type_line.setObjectName(u"c_type_line")

        self.gridLayout.addWidget(self.c_type_line, 3, 1, 1, 1)

        self.in_axe_angle = QLabel(self.widget)
        self.in_axe_angle.setObjectName(u"in_axe_angle")

        self.gridLayout.addWidget(self.in_axe_angle, 4, 0, 1, 1)

        self.lf_axe_angle = FloatEdit(self.widget)
        self.lf_axe_angle.setObjectName(u"lf_axe_angle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.lf_axe_angle.sizePolicy().hasHeightForWidth()
        )
        self.lf_axe_angle.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lf_axe_angle, 4, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.in_coord_center = QLabel(self.widget)
        self.in_coord_center.setObjectName(u"in_coord_center")

        self.horizontalLayout_5.addWidget(self.in_coord_center)

        self.lf_center_x = FloatEdit(self.widget)
        self.lf_center_x.setObjectName(u"lf_center_x")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lf_center_x.sizePolicy().hasHeightForWidth())
        self.lf_center_x.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.lf_center_x)

        self.lf_center_y = FloatEdit(self.widget)
        self.lf_center_y.setObjectName(u"lf_center_y")
        self.lf_center_y.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lf_center_y.sizePolicy().hasHeightForWidth())
        self.lf_center_y.setSizePolicy(sizePolicy3)
        self.lf_center_y.setMaximumSize(QSize(137, 16777215))

        self.horizontalLayout_5.addWidget(self.lf_center_y)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.b_plot = QPushButton(self.widget)
        self.b_plot.setObjectName(u"b_plot")

        self.horizontalLayout_2.addWidget(self.b_plot)

        self.b_save = QPushButton(self.widget)
        self.b_save.setObjectName(u"b_save")

        self.horizontalLayout_2.addWidget(self.b_save)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(DXF_Slot)

        QMetaObject.connectSlotsByName(DXF_Slot)

    # setupUi

    def retranslateUi(self, DXF_Slot):
        DXF_Slot.setWindowTitle(
            QCoreApplication.translate("DXF_Slot", u"Define Slot from DXF", None)
        )
        self.in_Zs.setText(
            QCoreApplication.translate("DXF_Slot", u"Number of slot", None)
        )
        self.in_wind_begin_index.setText(
            QCoreApplication.translate("DXF_Slot", u"Index start of winding", None)
        )
        self.in_wind_end_index.setText(
            QCoreApplication.translate("DXF_Slot", u"Index end of winding", None)
        )
        self.in_type_line.setText(
            QCoreApplication.translate("DXF_Slot", u"Type closing line", None)
        )
        self.c_type_line.setItemText(
            0, QCoreApplication.translate("DXF_Slot", u"Segment", None)
        )
        self.c_type_line.setItemText(
            1, QCoreApplication.translate("DXF_Slot", u"Arc1", None)
        )

        self.in_axe_angle.setText(
            QCoreApplication.translate("DXF_Slot", u"Slot axe angle shift", None)
        )
        self.lf_axe_angle.setText(QCoreApplication.translate("DXF_Slot", u"0", None))
        self.in_coord_center.setText(
            QCoreApplication.translate("DXF_Slot", u"Machine center (x,y)", None)
        )
        self.lf_center_x.setText(QCoreApplication.translate("DXF_Slot", u"0", None))
        self.lf_center_y.setText(QCoreApplication.translate("DXF_Slot", u"0", None))
        self.b_plot.setText(QCoreApplication.translate("DXF_Slot", u"Plot", None))
        self.b_save.setText(QCoreApplication.translate("DXF_Slot", u"Save", None))

    # retranslateUi
