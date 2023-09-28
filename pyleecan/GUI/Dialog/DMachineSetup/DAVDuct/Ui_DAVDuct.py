# -*- coding: utf-8 -*-

# File generated according to DAVDuct.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .....GUI.Tools.HelpButton import HelpButton

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_DAVDuct(object):
    def setupUi(self, DAVDuct):
        if not DAVDuct.objectName():
            DAVDuct.setObjectName(u"DAVDuct")
        DAVDuct.resize(771, 639)
        icon = QIcon()
        icon.addFile(
            u":/images/images/icon/pyleecan_64.png", QSize(), QIcon.Normal, QIcon.Off
        )
        DAVDuct.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(DAVDuct)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.b_new = QPushButton(DAVDuct)
        self.b_new.setObjectName(u"b_new")

        self.horizontalLayout_2.addWidget(self.b_new)

        self.b_help = HelpButton(DAVDuct)
        self.b_help.setObjectName(u"b_help")

        self.horizontalLayout_2.addWidget(self.b_help)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tab_vent = QTabWidget(DAVDuct)
        self.tab_vent.setObjectName(u"tab_vent")
        self.tab_vent.setTabsClosable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab_vent.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_vent.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tab_vent)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(
            218, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.b_plot = QPushButton(DAVDuct)
        self.b_plot.setObjectName(u"b_plot")

        self.horizontalLayout_4.addWidget(self.b_plot)

        self.b_cancel = QPushButton(DAVDuct)
        self.b_cancel.setObjectName(u"b_cancel")

        self.horizontalLayout_4.addWidget(self.b_cancel)

        self.b_ok = QPushButton(DAVDuct)
        self.b_ok.setObjectName(u"b_ok")

        self.horizontalLayout_4.addWidget(self.b_ok)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(DAVDuct)

        self.tab_vent.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(DAVDuct)

    # setupUi

    def retranslateUi(self, DAVDuct):
        DAVDuct.setWindowTitle(
            QCoreApplication.translate("DAVDuct", u"Set axial cooling duct", None)
        )
        self.b_new.setText(QCoreApplication.translate("DAVDuct", u"Add New Set", None))
        self.b_help.setText("")
        self.tab_vent.setTabText(
            self.tab_vent.indexOf(self.tab),
            QCoreApplication.translate("DAVDuct", u"Tab 1", None),
        )
        self.tab_vent.setTabText(
            self.tab_vent.indexOf(self.tab_2),
            QCoreApplication.translate("DAVDuct", u"Tab 2", None),
        )
        self.b_plot.setText(QCoreApplication.translate("DAVDuct", u"Preview", None))
        self.b_cancel.setText(QCoreApplication.translate("DAVDuct", u"Cancel", None))
        self.b_ok.setText(QCoreApplication.translate("DAVDuct", u"Ok", None))

    # retranslateUi
