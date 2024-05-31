# -*- coding: utf-8 -*-

# File generated according to WImportExcel.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_WImportExcel(object):
    def setupUi(self, WImportExcel):
        if not WImportExcel.objectName():
            WImportExcel.setObjectName("WImportExcel")
        WImportExcel.resize(509, 486)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WImportExcel.sizePolicy().hasHeightForWidth())
        WImportExcel.setSizePolicy(sizePolicy)
        WImportExcel.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(
            ":/images/images/icon/pyleecan_64.png", QSize(), QIcon.Normal, QIcon.Off
        )
        WImportExcel.setWindowIcon(icon)
        self.verticalLayout_3 = QVBoxLayout(WImportExcel)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
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

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.in_range = QLabel(WImportExcel)
        self.in_range.setObjectName("in_range")
        self.in_range.setMinimumSize(QSize(120, 0))
        self.in_range.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_4.addWidget(self.in_range)

        self.le_range = QLineEdit(WImportExcel)
        self.le_range.setObjectName("le_range")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_range.sizePolicy().hasHeightForWidth())
        self.le_range.setSizePolicy(sizePolicy1)
        self.le_range.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_4.addWidget(self.le_range)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.in_order = QLabel(WImportExcel)
        self.in_order.setObjectName("in_order")

        self.horizontalLayout.addWidget(self.in_order)

        self.c_order = QComboBox(WImportExcel)
        self.c_order.addItem("")
        self.c_order.addItem("")
        self.c_order.setObjectName("c_order")

        self.horizontalLayout.addWidget(self.c_order)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.b_ok = QPushButton(WImportExcel)
        self.b_ok.setObjectName("b_ok")

        self.horizontalLayout_3.addWidget(self.b_ok)

        self.b_cancel = QPushButton(WImportExcel)
        self.b_cancel.setObjectName("b_cancel")

        self.horizontalLayout_3.addWidget(self.b_cancel)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.retranslateUi(WImportExcel)

        QMetaObject.connectSlotsByName(WImportExcel)

    # setupUi

    def retranslateUi(self, WImportExcel):
        WImportExcel.setWindowTitle(
            QCoreApplication.translate("WImportExcel", "Import from Excel", None)
        )
        self.in_sheet.setText(
            QCoreApplication.translate("WImportExcel", "Sheet: ", None)
        )
        self.in_range.setText(
            QCoreApplication.translate("WImportExcel", "Data range: ", None)
        )
        self.le_range.setPlaceholderText(
            QCoreApplication.translate("WImportExcel", "A6:B100", None)
        )
        self.in_order.setText(
            QCoreApplication.translate("WImportExcel", "Data order :", None)
        )
        self.c_order.setItemText(
            0, QCoreApplication.translate("WImportExcel", "B(H)", None)
        )
        self.c_order.setItemText(
            1, QCoreApplication.translate("WImportExcel", "H(B)", None)
        )

        self.b_ok.setText(QCoreApplication.translate("WImportExcel", "Ok", None))
        self.b_cancel.setText(
            QCoreApplication.translate("WImportExcel", "Cancel", None)
        )

    # retranslateUi
