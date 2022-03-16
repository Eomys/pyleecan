# -*- coding: utf-8 -*-

# File generated according to WMatSelect.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_WMatSelect(object):
    def setupUi(self, WMatSelect):
        if not WMatSelect.objectName():
            WMatSelect.setObjectName(u"WMatSelect")
        WMatSelect.resize(283, 30)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WMatSelect.sizePolicy().hasHeightForWidth())
        WMatSelect.setSizePolicy(sizePolicy)
        WMatSelect.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(WMatSelect)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 2, 4, 2)
        self.in_mat_type = QLabel(WMatSelect)
        self.in_mat_type.setObjectName(u"in_mat_type")

        self.horizontalLayout.addWidget(self.in_mat_type)

        self.c_mat_type = QComboBox(WMatSelect)
        self.c_mat_type.addItem("")
        self.c_mat_type.addItem("")
        self.c_mat_type.addItem("")
        self.c_mat_type.setObjectName(u"c_mat_type")

        self.horizontalLayout.addWidget(self.c_mat_type)

        self.b_matlib = QPushButton(WMatSelect)
        self.b_matlib.setObjectName(u"b_matlib")

        self.horizontalLayout.addWidget(self.b_matlib)

        QWidget.setTabOrder(self.c_mat_type, self.b_matlib)

        self.retranslateUi(WMatSelect)

        QMetaObject.connectSlotsByName(WMatSelect)

    # setupUi

    def retranslateUi(self, WMatSelect):
        WMatSelect.setWindowTitle(
            QCoreApplication.translate("WMatSelect", u"Form", None)
        )
        self.in_mat_type.setText(
            QCoreApplication.translate("WMatSelect", u"mat_type :", None)
        )
        self.c_mat_type.setItemText(
            0, QCoreApplication.translate("WMatSelect", u"M400-50A", None)
        )
        self.c_mat_type.setItemText(
            1, QCoreApplication.translate("WMatSelect", u"M350-50A", None)
        )
        self.c_mat_type.setItemText(
            2, QCoreApplication.translate("WMatSelect", u"M330-35A", None)
        )

        self.b_matlib.setText(
            QCoreApplication.translate("WMatSelect", u"Edit Materials", None)
        )

    # retranslateUi
