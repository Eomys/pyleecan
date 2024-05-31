# -*- coding: utf-8 -*-

# File generated according to DNotchTab.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_DNotchTab(object):
    def setupUi(self, DNotchTab):
        if not DNotchTab.objectName():
            DNotchTab.setObjectName("DNotchTab")
        DNotchTab.resize(784, 649)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DNotchTab.sizePolicy().hasHeightForWidth())
        DNotchTab.setSizePolicy(sizePolicy)
        DNotchTab.setMinimumSize(QSize(780, 640))
        icon = QIcon()
        icon.addFile(
            ":/images/images/icon/pyleecan_64.png", QSize(), QIcon.Normal, QIcon.Off
        )
        DNotchTab.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(DNotchTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.b_add = QPushButton(DNotchTab)
        self.b_add.setObjectName("b_add")

        self.horizontalLayout_3.addWidget(self.b_add)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.tab_notch = QTabWidget(DNotchTab)
        self.tab_notch.setObjectName("tab_notch")
        self.tab_notch.setMinimumSize(QSize(770, 500))
        self.tab_notch.setTabsClosable(True)

        self.verticalLayout.addWidget(self.tab_notch)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.b_plot = QPushButton(DNotchTab)
        self.b_plot.setObjectName("b_plot")

        self.horizontalLayout.addWidget(self.b_plot)

        self.b_cancel = QPushButton(DNotchTab)
        self.b_cancel.setObjectName("b_cancel")

        self.horizontalLayout.addWidget(self.b_cancel)

        self.b_ok = QPushButton(DNotchTab)
        self.b_ok.setObjectName("b_ok")
        self.b_ok.setEnabled(True)

        self.horizontalLayout.addWidget(self.b_ok)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DNotchTab)

        self.tab_notch.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(DNotchTab)

    # setupUi

    def retranslateUi(self, DNotchTab):
        DNotchTab.setWindowTitle(
            QCoreApplication.translate("DNotchTab", "Notches Setup", None)
        )
        self.b_add.setText(
            QCoreApplication.translate("DNotchTab", "Add new notch", None)
        )
        self.b_plot.setText(QCoreApplication.translate("DNotchTab", "Preview", None))
        self.b_cancel.setText(QCoreApplication.translate("DNotchTab", "Cancel", None))
        self.b_ok.setText(QCoreApplication.translate("DNotchTab", "Ok", None))

    # retranslateUi
