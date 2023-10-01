# -*- coding: utf-8 -*-

# File generated according to DClassGenerator.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyleecan.GUI.Resources import pyleecan_rc

class Ui_DClassGenerator(object):
    def setupUi(self, DClassGenerator):
        if not DClassGenerator.objectName():
            DClassGenerator.setObjectName(u"DClassGenerator")
        DClassGenerator.resize(1828, 831)
        self.widget = QWidget(DClassGenerator)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 0, 1811, 828))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.path_selector = QWidget(self.widget)
        self.path_selector.setObjectName(u"path_selector")
        self.path_selector.setMinimumSize(QSize(1039, 0))

        self.verticalLayout_2.addWidget(self.path_selector)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.treeView = QTreeView(self.widget)
        self.treeView.setObjectName(u"treeView")

        self.horizontalLayout_4.addWidget(self.treeView)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.table_prop = QTableWidget(self.widget)
        self.table_prop.setObjectName(u"table_prop")

        self.verticalLayout.addWidget(self.table_prop)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.table_meth = QTableWidget(self.widget)
        self.table_meth.setObjectName(u"table_meth")

        self.verticalLayout.addWidget(self.table_meth)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.table_meta = QTableWidget(self.widget)
        self.table_meta.setObjectName(u"table_meta")

        self.verticalLayout.addWidget(self.table_meta)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.b_load = QPushButton(self.widget)
        self.b_load.setObjectName(u"b_load")

        self.horizontalLayout.addWidget(self.b_load)

        self.b_save = QPushButton(self.widget)
        self.b_save.setObjectName(u"b_save")

        self.horizontalLayout.addWidget(self.b_save)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(DClassGenerator)

        QMetaObject.connectSlotsByName(DClassGenerator)
    # setupUi

    def retranslateUi(self, DClassGenerator):
        DClassGenerator.setWindowTitle(QCoreApplication.translate("DClassGenerator", u"Pyleecan Class Generator", None))
        self.b_load.setText(QCoreApplication.translate("DClassGenerator", u"Load", None))
        self.b_save.setText(QCoreApplication.translate("DClassGenerator", u"Save", None))
    # retranslateUi

