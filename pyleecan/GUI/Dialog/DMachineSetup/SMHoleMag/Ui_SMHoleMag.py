# -*- coding: utf-8 -*-

# File generated according to SMHoleMag.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from pyleecan.GUI.Tools.HelpButton import HelpButton

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SMHoleMag(object):
    def setupUi(self, SMHoleMag):
        if not SMHoleMag.objectName():
            SMHoleMag.setObjectName("SMHoleMag")
        SMHoleMag.resize(780, 640)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SMHoleMag.sizePolicy().hasHeightForWidth())
        SMHoleMag.setSizePolicy(sizePolicy)
        SMHoleMag.setMinimumSize(QSize(780, 640))
        self.verticalLayout = QVBoxLayout(SMHoleMag)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.b_help = HelpButton(SMHoleMag)
        self.b_help.setObjectName("b_help")
        self.b_help.setPixmap(QPixmap(":/images/images/icon/help_16.png"))

        self.horizontalLayout_2.addWidget(self.b_help)

        self.out_hole_pitch = QLabel(SMHoleMag)
        self.out_hole_pitch.setObjectName("out_hole_pitch")

        self.horizontalLayout_2.addWidget(self.out_hole_pitch)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.b_add = QPushButton(SMHoleMag)
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

        self.tab_hole = QTabWidget(SMHoleMag)
        self.tab_hole.setObjectName("tab_hole")
        self.tab_hole.setMinimumSize(QSize(770, 500))
        self.tab_hole.setTabsClosable(True)

        self.verticalLayout.addWidget(self.tab_hole)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.b_plot = QPushButton(SMHoleMag)
        self.b_plot.setObjectName("b_plot")

        self.horizontalLayout.addWidget(self.b_plot)

        self.b_previous = QPushButton(SMHoleMag)
        self.b_previous.setObjectName("b_previous")

        self.horizontalLayout.addWidget(self.b_previous)

        self.b_next = QPushButton(SMHoleMag)
        self.b_next.setObjectName("b_next")
        self.b_next.setEnabled(True)

        self.horizontalLayout.addWidget(self.b_next)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SMHoleMag)

        self.tab_hole.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(SMHoleMag)

    # setupUi

    def retranslateUi(self, SMHoleMag):
        SMHoleMag.setWindowTitle(QCoreApplication.translate("SMHoleMag", "Form", None))
        self.b_help.setText("")
        self.out_hole_pitch.setText(
            QCoreApplication.translate("SMHoleMag", "Slot pitch = 2*Pi / Zs = ", None)
        )
        self.b_add.setText(
            QCoreApplication.translate("SMHoleMag", "Add new holes", None)
        )
        self.b_plot.setText(QCoreApplication.translate("SMHoleMag", "Preview", None))
        self.b_previous.setText(
            QCoreApplication.translate("SMHoleMag", "Previous", None)
        )
        self.b_next.setText(QCoreApplication.translate("SMHoleMag", "Save", None))

    # retranslateUi
