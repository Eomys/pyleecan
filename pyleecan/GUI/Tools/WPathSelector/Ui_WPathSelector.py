# -*- coding: utf-8 -*-

# File generated according to WPathSelector.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_WPathSelector(object):
    def setupUi(self, WPathSelector):
        if not WPathSelector.objectName():
            WPathSelector.setObjectName("WPathSelector")
        WPathSelector.resize(280, 32)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WPathSelector.sizePolicy().hasHeightForWidth())
        WPathSelector.setSizePolicy(sizePolicy)
        WPathSelector.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(WPathSelector)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 2, 4, 2)
        self.in_path = QLabel(WPathSelector)
        self.in_path.setObjectName("in_path")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.in_path.sizePolicy().hasHeightForWidth())
        self.in_path.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.in_path)

        self.le_path = QLineEdit(WPathSelector)
        self.le_path.setObjectName("le_path")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.le_path.sizePolicy().hasHeightForWidth())
        self.le_path.setSizePolicy(sizePolicy2)
        self.le_path.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.le_path)

        self.b_path = QPushButton(WPathSelector)
        self.b_path.setObjectName("b_path")

        self.horizontalLayout.addWidget(self.b_path)

        self.retranslateUi(WPathSelector)

        QMetaObject.connectSlotsByName(WPathSelector)

    # setupUi

    def retranslateUi(self, WPathSelector):
        WPathSelector.setWindowTitle(
            QCoreApplication.translate("WPathSelector", "Form", None)
        )
        self.in_path.setText(QCoreApplication.translate("WPathSelector", "path", None))
        self.b_path.setText(
            QCoreApplication.translate("WPathSelector", "Select Path", None)
        )

    # retranslateUi
