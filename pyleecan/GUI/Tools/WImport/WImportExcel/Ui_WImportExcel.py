# -*- coding: utf-8 -*-

# File generated according to WImportExcel.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_WImportExcel(object):
    def setupUi(self, WImportExcel):
        if not WImportExcel.objectName():
            WImportExcel.setObjectName(u"WImportExcel")
        WImportExcel.resize(509, 486)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WImportExcel.sizePolicy().hasHeightForWidth())
        WImportExcel.setSizePolicy(sizePolicy)
        WImportExcel.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(WImportExcel)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.in_sheet = QLabel(WImportExcel)
        self.in_sheet.setObjectName(u"in_sheet")
        self.in_sheet.setMinimumSize(QSize(45, 0))
        self.in_sheet.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout_2.addWidget(self.in_sheet)

        self.c_sheet = QComboBox(WImportExcel)
        self.c_sheet.setObjectName(u"c_sheet")
        self.c_sheet.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_2.addWidget(self.c_sheet)

        self.in_range = QLabel(WImportExcel)
        self.in_range.setObjectName(u"in_range")
        self.in_range.setMinimumSize(QSize(120, 0))
        self.in_range.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_2.addWidget(self.in_range)

        self.le_range = QLineEdit(WImportExcel)
        self.le_range.setObjectName(u"le_range")
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

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.in_order = QLabel(WImportExcel)
        self.in_order.setObjectName(u"in_order")

        self.horizontalLayout.addWidget(self.in_order)

        self.c_order = QComboBox(WImportExcel)
        self.c_order.addItem("")
        self.c_order.addItem("")
        self.c_order.setObjectName(u"c_order")

        self.horizontalLayout.addWidget(self.c_order)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.b_ok = QPushButton(WImportExcel)
        self.b_ok.setObjectName(u"b_ok")

        self.horizontalLayout_3.addWidget(self.b_ok)

        self.b_cancel = QPushButton(WImportExcel)
        self.b_cancel.setObjectName(u"b_cancel")

        self.horizontalLayout_3.addWidget(self.b_cancel)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.retranslateUi(WImportExcel)

        QMetaObject.connectSlotsByName(WImportExcel)

    # setupUi

    def retranslateUi(self, WImportExcel):
        WImportExcel.setWindowTitle(
            QCoreApplication.translate("WImportExcel", u"Import from Excel", None)
        )
        self.in_sheet.setText(
            QCoreApplication.translate("WImportExcel", u"Sheet: ", None)
        )
        self.in_range.setText(
            QCoreApplication.translate("WImportExcel", u"Column range: ", None)
        )
        self.le_range.setPlaceholderText(
            QCoreApplication.translate("WImportExcel", u"A6:B100", None)
        )
        self.in_order.setText(
            QCoreApplication.translate(
                "WImportExcel", u"In which order is the data :", None
            )
        )
        self.c_order.setItemText(
            0, QCoreApplication.translate("WImportExcel", u"B(H)", None)
        )
        self.c_order.setItemText(
            1, QCoreApplication.translate("WImportExcel", u"H(B)", None)
        )

        self.b_ok.setText(QCoreApplication.translate("WImportExcel", u"Ok", None))
        self.b_cancel.setText(
            QCoreApplication.translate("WImportExcel", u"Cancel", None)
        )

    # retranslateUi
