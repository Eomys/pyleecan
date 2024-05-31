# -*- coding: utf-8 -*-

# File generated according to DMatLib.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from ....GUI.Dialog.DMatLib.DMatSetup.DMatSetup import DMatSetup

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_DMatLib(object):
    def setupUi(self, DMatLib):
        if not DMatLib.objectName():
            DMatLib.setObjectName("DMatLib")
        DMatLib.resize(797, 647)
        icon = QIcon()
        icon.addFile(
            ":/images/images/icon/pyleecan_64.png", QSize(), QIcon.Normal, QIcon.Off
        )
        DMatLib.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(DMatLib)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.le_search = QLineEdit(DMatLib)
        self.le_search.setObjectName("le_search")

        self.horizontalLayout_9.addWidget(self.le_search)

        self.img_search = QLabel(DMatLib)
        self.img_search.setObjectName("img_search")
        self.img_search.setPixmap(QPixmap(":/images/images/icon/search.png"))
        self.img_search.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.img_search)

        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.in_reference_mat_lib = QLabel(DMatLib)
        self.in_reference_mat_lib.setObjectName("in_reference_mat_lib")

        self.verticalLayout.addWidget(self.in_reference_mat_lib)

        self.nav_mat = QListWidget(DMatLib)
        self.nav_mat.setObjectName("nav_mat")

        self.verticalLayout.addWidget(self.nav_mat)

        self.in_machine_mat = QLabel(DMatLib)
        self.in_machine_mat.setObjectName("in_machine_mat")

        self.verticalLayout.addWidget(self.in_machine_mat)

        self.nav_mat_mach = QListWidget(DMatLib)
        self.nav_mat_mach.setObjectName("nav_mat_mach")

        self.verticalLayout.addWidget(self.nav_mat_mach)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.b_switch = QPushButton(DMatLib)
        self.b_switch.setObjectName("b_switch")

        self.horizontalLayout_8.addWidget(self.b_switch)

        self.b_new = QPushButton(DMatLib)
        self.b_new.setObjectName("b_new")

        self.horizontalLayout_8.addWidget(self.b_new)

        self.b_copy = QPushButton(DMatLib)
        self.b_copy.setObjectName("b_copy")

        self.horizontalLayout_8.addWidget(self.b_copy)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.w_setup = DMatSetup(DMatLib)
        self.w_setup.setObjectName("w_setup")

        self.horizontalLayout.addWidget(self.w_setup)

        self.retranslateUi(DMatLib)

        QMetaObject.connectSlotsByName(DMatLib)

    # setupUi

    def retranslateUi(self, DMatLib):
        DMatLib.setWindowTitle(
            QCoreApplication.translate("DMatLib", "Material Library", None)
        )
        self.le_search.setPlaceholderText(
            QCoreApplication.translate("DMatLib", "Filter...", None)
        )
        self.img_search.setText("")
        self.in_reference_mat_lib.setText(
            QCoreApplication.translate("DMatLib", "Materials in Library", None)
        )
        self.in_machine_mat.setText(
            QCoreApplication.translate("DMatLib", "Machine materials", None)
        )
        self.b_switch.setText(
            QCoreApplication.translate("DMatLib", "Edit in Machine", None)
        )
        self.b_new.setText(QCoreApplication.translate("DMatLib", "New", None))
        self.b_copy.setText(QCoreApplication.translate("DMatLib", "Copy", None))

    # retranslateUi
