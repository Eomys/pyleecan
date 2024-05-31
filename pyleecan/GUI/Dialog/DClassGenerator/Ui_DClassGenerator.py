# -*- coding: utf-8 -*-

# File generated according to DClassGenerator.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_DClassGenerator(object):
    def setupUi(self, DClassGenerator):
        if not DClassGenerator.objectName():
            DClassGenerator.setObjectName("DClassGenerator")
        DClassGenerator.resize(1828, 831)
        self.treeView = QTreeView(DClassGenerator)
        self.treeView.setObjectName("treeView")
        self.treeView.setGeometry(QRect(12, 34, 256, 711))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.layoutWidget = QWidget(DClassGenerator)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(14, 750, 1771, 58))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.b_genclass = QPushButton(self.layoutWidget)
        self.b_genclass.setObjectName("b_genclass")

        self.gridLayout.addWidget(self.b_genclass, 0, 1, 1, 1)

        self.is_black = QCheckBox(self.layoutWidget)
        self.is_black.setObjectName("is_black")

        self.gridLayout.addWidget(self.is_black, 0, 0, 1, 1)

        self.horizontalLayout.addLayout(self.gridLayout)

        self.layoutWidget1 = QWidget(DClassGenerator)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(275, 35, 1511, 711))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.table_prop = QTableWidget(self.layoutWidget1)
        self.table_prop.setObjectName("table_prop")

        self.gridLayout_4.addWidget(self.table_prop, 4, 0, 1, 5)

        self.lab_param = QLabel(self.layoutWidget1)
        self.lab_param.setObjectName("lab_param")

        self.gridLayout_4.addWidget(self.lab_param, 2, 0, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 2, 3, 1, 1)

        self.b_saveclass = QPushButton(self.layoutWidget1)
        self.b_saveclass.setObjectName("b_saveclass")

        self.gridLayout_4.addWidget(self.b_saveclass, 1, 2, 1, 1)

        self.b_addprop = QPushButton(self.layoutWidget1)
        self.b_addprop.setObjectName("b_addprop")

        self.gridLayout_4.addWidget(self.b_addprop, 2, 2, 1, 1)

        self.le_classname = QLineEdit(self.layoutWidget1)
        self.le_classname.setObjectName("le_classname")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.le_classname.sizePolicy().hasHeightForWidth()
        )
        self.le_classname.setSizePolicy(sizePolicy1)
        self.le_classname.setMaximumSize(QSize(400, 16777215))
        self.le_classname.setStyleSheet(
            'font: 700 14pt "Arial";\n' "text-decoration: underline;"
        )

        self.gridLayout_4.addWidget(self.le_classname, 1, 0, 1, 2)

        self.verticalLayout.addLayout(self.gridLayout_4)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lab_methods = QLabel(self.layoutWidget1)
        self.lab_methods.setObjectName("lab_methods")

        self.gridLayout_3.addWidget(self.lab_methods, 0, 0, 1, 1)

        self.table_meth = QTableWidget(self.layoutWidget1)
        self.table_meth.setObjectName("table_meth")

        self.gridLayout_3.addWidget(self.table_meth, 1, 0, 1, 5)

        self.b_addmeth = QPushButton(self.layoutWidget1)
        self.b_addmeth.setObjectName("b_addmeth")

        self.gridLayout_3.addWidget(self.b_addmeth, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.b_browse = QPushButton(self.layoutWidget1)
        self.b_browse.setObjectName("b_browse")

        self.gridLayout_3.addWidget(self.b_browse, 0, 3, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.table_meta = QTableWidget(self.layoutWidget1)
        self.table_meta.setObjectName("table_meta")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.table_meta.sizePolicy().hasHeightForWidth())
        self.table_meta.setSizePolicy(sizePolicy2)
        self.table_meta.setMinimumSize(QSize(700, 0))
        self.table_meta.setMaximumSize(QSize(750, 16777215))

        self.gridLayout_2.addWidget(self.table_meta, 5, 0, 1, 1)

        self.lab_meta = QLabel(self.layoutWidget1)
        self.lab_meta.setObjectName("lab_meta")

        self.gridLayout_2.addWidget(self.lab_meta, 2, 0, 1, 1)

        self.b_addconst = QPushButton(self.layoutWidget1)
        self.b_addconst.setObjectName("b_addconst")

        self.gridLayout_2.addWidget(self.b_addconst, 2, 2, 1, 1)

        self.lab_const = QLabel(self.layoutWidget1)
        self.lab_const.setObjectName("lab_const")

        self.gridLayout_2.addWidget(self.lab_const, 2, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 2, 3, 1, 1)

        self.table_const = QTableWidget(self.layoutWidget1)
        self.table_const.setObjectName("table_const")
        sizePolicy2.setHeightForWidth(self.table_const.sizePolicy().hasHeightForWidth())
        self.table_const.setSizePolicy(sizePolicy2)
        self.table_const.setMinimumSize(QSize(400, 0))
        self.table_const.setMaximumSize(QSize(1200, 16777215))

        self.gridLayout_2.addWidget(self.table_const, 5, 1, 1, 3)

        self.verticalLayout.addLayout(self.gridLayout_2)

        self.layoutWidget2 = QWidget(DClassGenerator)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 0, 731, 28))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_path_classgen = QLabel(self.layoutWidget2)
        self.label_path_classgen.setObjectName("label_path_classgen")

        self.horizontalLayout_2.addWidget(self.label_path_classgen)

        self.le_path_classgen = QLineEdit(self.layoutWidget2)
        self.le_path_classgen.setObjectName("le_path_classgen")

        self.horizontalLayout_2.addWidget(self.le_path_classgen)

        self.retranslateUi(DClassGenerator)

        QMetaObject.connectSlotsByName(DClassGenerator)

    # setupUi

    def retranslateUi(self, DClassGenerator):
        DClassGenerator.setWindowTitle(
            QCoreApplication.translate(
                "DClassGenerator", "Pyleecan Class Generator", None
            )
        )
        self.b_genclass.setText(
            QCoreApplication.translate("DClassGenerator", "Generate classes", None)
        )
        self.is_black.setText(
            QCoreApplication.translate("DClassGenerator", "Format with black", None)
        )
        self.lab_param.setText(
            QCoreApplication.translate(
                "DClassGenerator",
                "<html><head/><body><p><span style=\" font-family:'DejaVu Sans'; font-size:12pt; font-weight:700;\">Properties</span></p></body></html>",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.b_saveclass.setToolTip(
            QCoreApplication.translate(
                "DClassGenerator",
                "<html><head/><body><p>Save modifications made to current class</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.b_saveclass.setText(
            QCoreApplication.translate("DClassGenerator", "Save current class", None)
        )
        # if QT_CONFIG(tooltip)
        self.b_addprop.setToolTip(
            QCoreApplication.translate(
                "DClassGenerator",
                "<html><head/><body><p>Add new row at the bottom of property table</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.b_addprop.setText(
            QCoreApplication.translate("DClassGenerator", "Add Property", None)
        )
        self.le_classname.setText(
            QCoreApplication.translate("DClassGenerator", "Class_name", None)
        )
        self.lab_methods.setText(
            QCoreApplication.translate(
                "DClassGenerator",
                "<html><head/><body><p><span style=\" font-family:'DejaVu Sans'; font-size:12pt; font-weight:700;\">Methods</span></p></body></html>",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.b_addmeth.setToolTip(
            QCoreApplication.translate(
                "DClassGenerator",
                "<html><head/><body><p>Add new row at the bottom of method list</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.b_addmeth.setText(
            QCoreApplication.translate("DClassGenerator", "Add Method", None)
        )
        # if QT_CONFIG(tooltip)
        self.b_browse.setToolTip(
            QCoreApplication.translate(
                "DClassGenerator",
                "<html><head/><body><p>Browse to method folder in explorer</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.b_browse.setText(
            QCoreApplication.translate("DClassGenerator", "Browse Folder", None)
        )
        self.lab_meta.setText(
            QCoreApplication.translate(
                "DClassGenerator",
                "<html><head/><body><p><span style=\" font-family:'DejaVu Sans'; font-size:12pt; font-weight:700;\">Metadata</span></p></body></html>",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.b_addconst.setToolTip(
            QCoreApplication.translate(
                "DClassGenerator",
                "<html><head/><body><p>Add a new row at the bottom of constant table</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.b_addconst.setText(
            QCoreApplication.translate("DClassGenerator", "Add Constant", None)
        )
        self.lab_const.setText(
            QCoreApplication.translate(
                "DClassGenerator",
                "<html><head/><body><p><span style=\" font-family:'DejaVu Sans'; font-size:12pt; font-weight:700;\">Constants</span></p></body></html>",
                None,
            )
        )
        self.label_path_classgen.setText(
            QCoreApplication.translate(
                "DClassGenerator", "Path to generator folder:", None
            )
        )

    # retranslateUi
