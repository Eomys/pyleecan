# -*- coding: utf-8 -*-

# File generated according to WHoleMag.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WHoleMag(object):
    def setupUi(self, WHoleMag):
        if not WHoleMag.objectName():
            WHoleMag.setObjectName(u"WHoleMag")
        WHoleMag.resize(760, 490)
        WHoleMag.setMinimumSize(QSize(760, 490))
        self.main_layout = QVBoxLayout(WHoleMag)
        self.main_layout.setSpacing(4)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.c_hole_type = QComboBox(WHoleMag)
        self.c_hole_type.addItem("")
        self.c_hole_type.addItem("")
        self.c_hole_type.addItem("")
        self.c_hole_type.addItem("")
        self.c_hole_type.addItem("")
        self.c_hole_type.addItem("")
        self.c_hole_type.addItem("")
        self.c_hole_type.addItem("")
        self.c_hole_type.setObjectName(u"c_hole_type")

        self.horizontalLayout.addWidget(self.c_hole_type)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.main_layout.addLayout(self.horizontalLayout)

        self.w_hole = QWidget(WHoleMag)
        self.w_hole.setObjectName(u"w_hole")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_hole.sizePolicy().hasHeightForWidth())
        self.w_hole.setSizePolicy(sizePolicy)
        self.w_hole.setMinimumSize(QSize(750, 450))

        self.main_layout.addWidget(self.w_hole)

        self.retranslateUi(WHoleMag)

        QMetaObject.connectSlotsByName(WHoleMag)

    # setupUi

    def retranslateUi(self, WHoleMag):
        WHoleMag.setWindowTitle(QCoreApplication.translate("WHoleMag", u"Form", None))
        self.c_hole_type.setItemText(
            0, QCoreApplication.translate("WHoleMag", u"Slot Type 50", None)
        )
        self.c_hole_type.setItemText(
            1, QCoreApplication.translate("WHoleMag", u"Slot Type 51", None)
        )
        self.c_hole_type.setItemText(
            2, QCoreApplication.translate("WHoleMag", u"Slot Type 52", None)
        )
        self.c_hole_type.setItemText(
            3, QCoreApplication.translate("WHoleMag", u"Slot Type 52 R", None)
        )
        self.c_hole_type.setItemText(
            4, QCoreApplication.translate("WHoleMag", u"Slot Type 53", None)
        )
        self.c_hole_type.setItemText(
            5, QCoreApplication.translate("WHoleMag", u"Slot Type 54", None)
        )
        self.c_hole_type.setItemText(
            6, QCoreApplication.translate("WHoleMag", u"Slot Type 55", None)
        )
        self.c_hole_type.setItemText(
            7, QCoreApplication.translate("WHoleMag", u"Slot Type 56", None)
        )

    # retranslateUi
