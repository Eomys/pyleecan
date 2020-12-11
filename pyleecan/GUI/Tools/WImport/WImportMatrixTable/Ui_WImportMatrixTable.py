# -*- coding: utf-8 -*-

# File generated according to WImportMatrixTable.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_WImportMatrixTable(object):
    def setupUi(self, WImportMatrixTable):
        if not WImportMatrixTable.objectName():
            WImportMatrixTable.setObjectName(u"WImportMatrixTable")
        WImportMatrixTable.resize(546, 511)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            WImportMatrixTable.sizePolicy().hasHeightForWidth()
        )
        WImportMatrixTable.setSizePolicy(sizePolicy)
        WImportMatrixTable.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(WImportMatrixTable)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.in_matrix = QLabel(WImportMatrixTable)
        self.in_matrix.setObjectName(u"in_matrix")

        self.horizontalLayout.addWidget(self.in_matrix)

        self.b_convert = QPushButton(WImportMatrixTable)
        self.b_convert.setObjectName(u"b_convert")

        self.horizontalLayout.addWidget(self.b_convert)

        self.b_tab = QPushButton(WImportMatrixTable)
        self.b_tab.setObjectName(u"b_tab")

        self.horizontalLayout.addWidget(self.b_tab)

        self.b_plot = QPushButton(WImportMatrixTable)
        self.b_plot.setObjectName(u"b_plot")

        self.horizontalLayout.addWidget(self.b_plot)

        self.retranslateUi(WImportMatrixTable)

        QMetaObject.connectSlotsByName(WImportMatrixTable)

    # setupUi

    def retranslateUi(self, WImportMatrixTable):
        WImportMatrixTable.setWindowTitle(
            QCoreApplication.translate("WImportMatrixTable", u"Form", None)
        )
        self.in_matrix.setText(
            QCoreApplication.translate(
                "WImportMatrixTable", u"Matrix size (100,2)", None
            )
        )
        self.b_convert.setText(
            QCoreApplication.translate("WImportMatrixTable", u"Convert to Excel", None)
        )
        self.b_tab.setText(
            QCoreApplication.translate("WImportMatrixTable", u"Preview Table", None)
        )
        self.b_plot.setText(
            QCoreApplication.translate("WImportMatrixTable", u"Preview Plot", None)
        )

    # retranslateUi
