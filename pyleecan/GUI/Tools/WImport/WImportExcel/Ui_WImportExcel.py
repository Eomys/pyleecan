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
            WImportExcel.setObjectName("WImportExcel")
        WImportExcel.resize(509, 511)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WImportExcel.sizePolicy().hasHeightForWidth())
        WImportExcel.setSizePolicy(sizePolicy)
        WImportExcel.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(WImportExcel)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.w_file_path = WPathSelector(WImportExcel)
        self.w_file_path.setObjectName("w_file_path")

        self.verticalLayout_3.addWidget(self.w_file_path)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.in_sheet = QLabel(WImportExcel)
        self.in_sheet.setObjectName("in_sheet")
        self.in_sheet.setMinimumSize(QSize(45, 0))
        self.in_sheet.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout_2.addWidget(self.in_sheet)

        self.c_sheet = QComboBox(WImportExcel)
        self.c_sheet.setObjectName("c_sheet")
        self.c_sheet.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_2.addWidget(self.c_sheet)

        self.in_range = QLabel(WImportExcel)
        self.in_range.setObjectName("in_range")
        self.in_range.setMinimumSize(QSize(120, 0))
        self.in_range.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_2.addWidget(self.in_range)

        self.le_range = QLineEdit(WImportExcel)
        self.le_range.setObjectName("le_range")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_range.sizePolicy().hasHeightForWidth())
        self.le_range.setSizePolicy(sizePolicy1)
        self.le_range.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.le_range)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.g_axe1 = QGroupBox(WImportExcel)
        self.g_axe1.setObjectName("g_axe1")
        self.verticalLayout = QVBoxLayout(self.g_axe1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.c_axe1_name = QComboBox(self.g_axe1)
        self.c_axe1_name.setObjectName("c_axe1_name")

        self.horizontalLayout_3.addWidget(self.c_axe1_name)

        self.c_axe1_type = QComboBox(self.g_axe1)
        self.c_axe1_type.setObjectName("c_axe1_type")

        self.horizontalLayout_3.addWidget(self.c_axe1_type)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.w_axe1 = QWidget(self.g_axe1)
        self.w_axe1.setObjectName("w_axe1")

        self.verticalLayout.addWidget(self.w_axe1)

        self.verticalLayout_3.addWidget(self.g_axe1)

        self.g_axe2 = QGroupBox(WImportExcel)
        self.g_axe2.setObjectName("g_axe2")
        self.verticalLayout_2 = QVBoxLayout(self.g_axe2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.c_axe2_name = QComboBox(self.g_axe2)
        self.c_axe2_name.setObjectName("c_axe2_name")

        self.horizontalLayout_4.addWidget(self.c_axe2_name)

        self.c_axe2_type = QComboBox(self.g_axe2)
        self.c_axe2_type.setObjectName("c_axe2_type")

        self.horizontalLayout_4.addWidget(self.c_axe2_type)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.w_axe2 = QWidget(self.g_axe2)
        self.w_axe2.setObjectName("w_axe2")

        self.verticalLayout_2.addWidget(self.w_axe2)

        self.verticalLayout_3.addWidget(self.g_axe2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.b_convert = QPushButton(WImportExcel)
        self.b_convert.setObjectName("b_convert")

        self.horizontalLayout.addWidget(self.b_convert)

        self.b_tab = QPushButton(WImportExcel)
        self.b_tab.setObjectName("b_tab")

        self.horizontalLayout.addWidget(self.b_tab)

        self.b_plot = QPushButton(WImportExcel)
        self.b_plot.setObjectName("b_plot")

        self.horizontalLayout.addWidget(self.b_plot)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(WImportExcel)

        QMetaObject.connectSlotsByName(WImportExcel)

    # setupUi

    def retranslateUi(self, WImportExcel):
        WImportExcel.setWindowTitle(
            QCoreApplication.translate("WImportExcel", "Form", None)
        )
        self.in_sheet.setText(
            QCoreApplication.translate("WImportExcel", "Sheet: ", None)
        )
        self.in_range.setText(
            QCoreApplication.translate("WImportExcel", "Column range: ", None)
        )
        self.g_axe1.setTitle(
            QCoreApplication.translate("WImportExcel", "First axe", None)
        )
        self.g_axe2.setTitle(
            QCoreApplication.translate("WImportExcel", "Second axe", None)
        )
        self.b_convert.setText(
            QCoreApplication.translate("WImportExcel", "Convert to Table", None)
        )
        self.b_tab.setText(
            QCoreApplication.translate("WImportExcel", "Preview Table", None)
        )
        self.b_plot.setText(
            QCoreApplication.translate("WImportExcel", "Preview Plot", None)
        )

    # retranslateUi
