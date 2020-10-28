# -*- coding: utf-8 -*-

# File generated according to WPathSelector.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_WPathSelector(object):
    def setupUi(self, WPathSelector):
        if not WPathSelector.objectName():
            WPathSelector.setObjectName(u"WPathSelector")
        WPathSelector.resize(280, 32)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WPathSelector.sizePolicy().hasHeightForWidth())
        WPathSelector.setSizePolicy(sizePolicy)
        WPathSelector.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(WPathSelector)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 2, 4, 2)
        self.in_path = QLabel(WPathSelector)
        self.in_path.setObjectName(u"in_path")

        self.horizontalLayout.addWidget(self.in_path)

        self.le_path = QLineEdit(WPathSelector)
        self.le_path.setObjectName(u"le_path")
        self.le_path.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.le_path)

        self.b_path = QPushButton(WPathSelector)
        self.b_path.setObjectName(u"b_path")

        self.horizontalLayout.addWidget(self.b_path)

        self.retranslateUi(WPathSelector)

        QMetaObject.connectSlotsByName(WPathSelector)

    # setupUi

    def retranslateUi(self, WPathSelector):
        WPathSelector.setWindowTitle(
            QCoreApplication.translate("WPathSelector", u"Form", None)
        )
        self.in_path.setText(QCoreApplication.translate("WPathSelector", u"path", None))
        self.b_path.setText(
            QCoreApplication.translate("WPathSelector", u"Select Path", None)
        )

    # retranslateUi
