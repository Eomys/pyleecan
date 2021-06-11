# -*- coding: utf-8 -*-

# File generated according to WImportExcel.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .....GUI.Tools.WPathSelector.WPathSelector import WPathSelector

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_WImportExcel(object):
    def setupUi(self, WImportExcel):
        if not WImportExcel.objectName():
            WImportExcel.setObjectName(u"WImportExcel")
        WImportExcel.resize(546, 511)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WImportExcel.sizePolicy().hasHeightForWidth())
        WImportExcel.setSizePolicy(sizePolicy)
        WImportExcel.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(WImportExcel)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.w_file_path = WPathSelector(WImportExcel)
        self.w_file_path.setObjectName(u"w_file_path")

        self.verticalLayout_3.addWidget(self.w_file_path)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.in_sheet = QLabel(WImportExcel)
        self.in_sheet.setObjectName(u"in_sheet")

        self.horizontalLayout_2.addWidget(self.in_sheet)

        self.c_sheet = QComboBox(WImportExcel)
        self.c_sheet.setObjectName(u"c_sheet")

        self.horizontalLayout_2.addWidget(self.c_sheet)

        self.in_range = QLabel(WImportExcel)
        self.in_range.setObjectName(u"in_range")

        self.horizontalLayout_2.addWidget(self.in_range)

        self.le_range = QLineEdit(WImportExcel)
        self.le_range.setObjectName(u"le_range")

        self.horizontalLayout_2.addWidget(self.le_range)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.g_axe1 = QGroupBox(WImportExcel)
        self.g_axe1.setObjectName(u"g_axe1")
        self.verticalLayout = QVBoxLayout(self.g_axe1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.c_axe1_name = QComboBox(self.g_axe1)
        self.c_axe1_name.setObjectName(u"c_axe1_name")

        self.horizontalLayout_3.addWidget(self.c_axe1_name)

        self.c_axe1_type = QComboBox(self.g_axe1)
        self.c_axe1_type.setObjectName(u"c_axe1_type")

        self.horizontalLayout_3.addWidget(self.c_axe1_type)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.w_axe1 = QWidget(self.g_axe1)
        self.w_axe1.setObjectName(u"w_axe1")

        self.verticalLayout.addWidget(self.w_axe1)

        self.verticalLayout_3.addWidget(self.g_axe1)

        self.g_axe2 = QGroupBox(WImportExcel)
        self.g_axe2.setObjectName(u"g_axe2")
        self.verticalLayout_2 = QVBoxLayout(self.g_axe2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.c_axe2_name = QComboBox(self.g_axe2)
        self.c_axe2_name.setObjectName(u"c_axe2_name")

        self.horizontalLayout_4.addWidget(self.c_axe2_name)

        self.c_axe2_type = QComboBox(self.g_axe2)
        self.c_axe2_type.setObjectName(u"c_axe2_type")

        self.horizontalLayout_4.addWidget(self.c_axe2_type)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.w_axe2 = QWidget(self.g_axe2)
        self.w_axe2.setObjectName(u"w_axe2")

        self.verticalLayout_2.addWidget(self.w_axe2)

        self.verticalLayout_3.addWidget(self.g_axe2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.b_convert = QPushButton(WImportExcel)
        self.b_convert.setObjectName(u"b_convert")

        self.horizontalLayout.addWidget(self.b_convert)

        self.b_tab = QPushButton(WImportExcel)
        self.b_tab.setObjectName(u"b_tab")

        self.horizontalLayout.addWidget(self.b_tab)

        self.b_plot = QPushButton(WImportExcel)
        self.b_plot.setObjectName(u"b_plot")

        self.horizontalLayout.addWidget(self.b_plot)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(WImportExcel)

        QMetaObject.connectSlotsByName(WImportExcel)

    # setupUi

    def retranslateUi(self, WImportExcel):
        WImportExcel.setWindowTitle(
            QCoreApplication.translate("WImportExcel", u"Form", None)
        )
        self.in_sheet.setText(
            QCoreApplication.translate("WImportExcel", u"Sheet: ", None)
        )
        self.in_range.setText(
            QCoreApplication.translate("WImportExcel", u"Column range: ", None)
        )
        self.g_axe1.setTitle(
            QCoreApplication.translate("WImportExcel", u"First axe", None)
        )
        self.g_axe2.setTitle(
            QCoreApplication.translate("WImportExcel", u"Second axe", None)
        )
        self.b_convert.setText(
            QCoreApplication.translate("WImportExcel", u"Convert to Matrix", None)
        )
        self.b_tab.setText(
            QCoreApplication.translate("WImportExcel", u"Preview Table", None)
        )
        self.b_plot.setText(
            QCoreApplication.translate("WImportExcel", u"Preview Plot", None)
        )

    # retranslateUi
