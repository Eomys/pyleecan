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
        self.treeView = QTreeView(DClassGenerator)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setGeometry(QRect(12, 64, 256, 681))
        self.path_selector = QWidget(DClassGenerator)
        self.path_selector.setObjectName(u"path_selector")
        self.path_selector.setGeometry(QRect(11, 1, 1809, 16))
        self.path_selector.setMinimumSize(QSize(1039, 0))
        self.b_browse = QPushButton(DClassGenerator)
        self.b_browse.setObjectName(u"b_browse")
        self.b_browse.setGeometry(QRect(360, 320, 81, 31))
        self.lab_param = QLabel(DClassGenerator)
        self.lab_param.setObjectName(u"lab_param")
        self.lab_param.setGeometry(QRect(280, 35, 101, 21))
        self.lab_methods = QLabel(DClassGenerator)
        self.lab_methods.setObjectName(u"lab_methods")
        self.lab_methods.setGeometry(QRect(280, 330, 101, 21))
        self.lab_meta = QLabel(DClassGenerator)
        self.lab_meta.setObjectName(u"lab_meta")
        self.lab_meta.setGeometry(QRect(280, 640, 101, 21))
        self.table_prop = QTableWidget(DClassGenerator)
        self.table_prop.setObjectName(u"table_prop")
        self.table_prop.setGeometry(QRect(275, 65, 851, 251))
        self.table_meta = QTableWidget(DClassGenerator)
        self.table_meta.setObjectName(u"table_meta")
        self.table_meta.setGeometry(QRect(275, 664, 851, 81))
        self.table_meth = QTableWidget(DClassGenerator)
        self.table_meth.setObjectName(u"table_meth")
        self.table_meth.setGeometry(QRect(280, 360, 841, 261))
        self.widget = QWidget(DClassGenerator)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(14, 760, 1111, 58))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.b_saveclass = QPushButton(self.widget)
        self.b_saveclass.setObjectName(u"b_saveclass")

        self.gridLayout.addWidget(self.b_saveclass, 0, 1, 1, 1)

        self.is_black = QCheckBox(self.widget)
        self.is_black.setObjectName(u"is_black")

        self.gridLayout.addWidget(self.is_black, 1, 0, 1, 1)

        self.b_genclass = QPushButton(self.widget)
        self.b_genclass.setObjectName(u"b_genclass")

        self.gridLayout.addWidget(self.b_genclass, 1, 1, 1, 1)

        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(DClassGenerator)

        QMetaObject.connectSlotsByName(DClassGenerator)

    # setupUi

    def retranslateUi(self, DClassGenerator):
        DClassGenerator.setWindowTitle(
            QCoreApplication.translate(
                "DClassGenerator", u"Pyleecan Class Generator", None
            )
        )
        self.b_browse.setText(
            QCoreApplication.translate("DClassGenerator", u"Browse", None)
        )
        self.lab_param.setText(
            QCoreApplication.translate(
                "DClassGenerator",
                u"<html><head/><body><p><span style=\" font-family:'DejaVu Sans'; font-size:12pt; font-weight:700;\">Properties</span></p></body></html>",
                None,
            )
        )
        self.lab_methods.setText(
            QCoreApplication.translate(
                "DClassGenerator",
                u"<html><head/><body><p><span style=\" font-family:'DejaVu Sans'; font-size:12pt; font-weight:700;\">Methods</span></p></body></html>",
                None,
            )
        )
        self.lab_meta.setText(
            QCoreApplication.translate(
                "DClassGenerator",
                u"<html><head/><body><p><span style=\" font-family:'DejaVu Sans'; font-size:12pt; font-weight:700;\">Metadata</span></p></body></html>",
                None,
            )
        )
        self.b_saveclass.setText(
            QCoreApplication.translate("DClassGenerator", u"Save current class", None)
        )
        self.is_black.setText(
            QCoreApplication.translate("DClassGenerator", u"Format with black", None)
        )
        self.b_genclass.setText(
            QCoreApplication.translate("DClassGenerator", u"Generate all classes", None)
        )

    # retranslateUi
