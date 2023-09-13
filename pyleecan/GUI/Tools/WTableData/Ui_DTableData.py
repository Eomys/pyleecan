# -*- coding: utf-8 -*-

# File generated according to DTableData.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_DTableData(object):
    def setupUi(self, DTableData):
        if not DTableData.objectName():
            DTableData.setObjectName(u"DTableData")
        DTableData.resize(746, 536)
        icon = QIcon()
        icon.addFile(
            u":/images/images/icon/pyleecan_64.png", QSize(), QIcon.Normal, QIcon.Off
        )
        DTableData.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(DTableData)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.in_row = QLabel(DTableData)
        self.in_row.setObjectName(u"in_row")

        self.horizontalLayout.addWidget(self.in_row)

        self.si_row = QSpinBox(DTableData)
        self.si_row.setObjectName(u"si_row")
        self.si_row.setMinimum(1)
        self.si_row.setMaximum(999999999)

        self.horizontalLayout.addWidget(self.si_row)

        self.in_col = QLabel(DTableData)
        self.in_col.setObjectName(u"in_col")

        self.horizontalLayout.addWidget(self.in_col)

        self.si_col = QSpinBox(DTableData)
        self.si_col.setObjectName(u"si_col")
        self.si_col.setMinimum(1)
        self.si_col.setMaximum(999999999)

        self.horizontalLayout.addWidget(self.si_col)

        self.b_export = QPushButton(DTableData)
        self.b_export.setObjectName(u"b_export")

        self.horizontalLayout.addWidget(self.b_export)

        self.b_import = QPushButton(DTableData)
        self.b_import.setObjectName(u"b_import")

        self.horizontalLayout.addWidget(self.b_import)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.w_tab = QTableWidget(DTableData)
        self.w_tab.setObjectName(u"w_tab")

        self.verticalLayout.addWidget(self.w_tab)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.b_plot = QPushButton(DTableData)
        self.b_plot.setObjectName(u"b_plot")

        self.horizontalLayout_2.addWidget(self.b_plot)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.b_close = QDialogButtonBox(DTableData)
        self.b_close.setObjectName(u"b_close")
        self.b_close.setOrientation(Qt.Horizontal)
        self.b_close.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.b_close)

        self.retranslateUi(DTableData)
        self.b_close.accepted.connect(DTableData.accept)
        self.b_close.rejected.connect(DTableData.reject)

        QMetaObject.connectSlotsByName(DTableData)

    # setupUi

    def retranslateUi(self, DTableData):
        DTableData.setWindowTitle(
            QCoreApplication.translate("DTableData", u"Material Library", None)
        )
        self.in_row.setText(QCoreApplication.translate("DTableData", u"N_row: ", None))
        self.in_col.setText(
            QCoreApplication.translate("DTableData", u"N_column:", None)
        )
        self.b_export.setText(
            QCoreApplication.translate("DTableData", u"Export to csv", None)
        )
        self.b_import.setText(
            QCoreApplication.translate("DTableData", u"Import from csv/xlsx", None)
        )
        self.b_plot.setText(
            QCoreApplication.translate("DTableData", u"Preview Plot", None)
        )

    # retranslateUi
