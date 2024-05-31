# -*- coding: utf-8 -*-

# File generated according to SMachineType.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SMachineType(object):
    def setupUi(self, SMachineType):
        if not SMachineType.objectName():
            SMachineType.setObjectName("SMachineType")
        SMachineType.resize(800, 607)
        SMachineType.setMinimumSize(QSize(800, 550))
        self.verticalLayout = QVBoxLayout(SMachineType)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.in_machine_type = QLabel(SMachineType)
        self.in_machine_type.setObjectName("in_machine_type")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.in_machine_type.sizePolicy().hasHeightForWidth()
        )
        self.in_machine_type.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.in_machine_type)

        self.c_type = QComboBox(SMachineType)
        self.c_type.addItem("")
        self.c_type.addItem("")
        self.c_type.addItem("")
        self.c_type.addItem("")
        self.c_type.addItem("")
        self.c_type.addItem("")
        self.c_type.setObjectName("c_type")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.c_type.sizePolicy().hasHeightForWidth())
        self.c_type.setSizePolicy(sizePolicy1)
        self.c_type.setMinimumSize(QSize(150, 0))
        self.c_type.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_10.addWidget(self.c_type)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img_type_machine = QLabel(SMachineType)
        self.img_type_machine.setObjectName("img_type_machine")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.img_type_machine.sizePolicy().hasHeightForWidth()
        )
        self.img_type_machine.setSizePolicy(sizePolicy2)
        self.img_type_machine.setMinimumSize(QSize(400, 400))
        self.img_type_machine.setMaximumSize(QSize(400, 400))
        self.img_type_machine.setPixmap(
            QPixmap(":/images/images/MachineSetup/MachineType/machine_SCIM.png")
        )
        self.img_type_machine.setScaledContents(True)

        self.horizontalLayout.addWidget(self.img_type_machine)

        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.verticalSpacer_4 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.scrollArea = QScrollArea(SMachineType)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMaximumSize(QSize(370, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 332, 554))
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth()
        )
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy3)
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.in_machine_desc = QTextEdit(self.groupBox)
        self.in_machine_desc.setObjectName("in_machine_desc")
        self.in_machine_desc.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.in_machine_desc.sizePolicy().hasHeightForWidth()
        )
        self.in_machine_desc.setSizePolicy(sizePolicy4)
        self.in_machine_desc.setMinimumSize(QSize(0, 0))

        self.verticalLayout_4.addWidget(self.in_machine_desc)

        self.gridLayout_2.addWidget(self.groupBox, 2, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.le_name = QLineEdit(self.scrollAreaWidgetContents_2)
        self.le_name.setObjectName("le_name")
        sizePolicy1.setHeightForWidth(self.le_name.sizePolicy().hasHeightForWidth())
        self.le_name.setSizePolicy(sizePolicy1)
        self.le_name.setMinimumSize(QSize(200, 0))

        self.gridLayout.addWidget(self.le_name, 2, 1, 1, 1)

        self.c_topology = QComboBox(self.scrollAreaWidgetContents_2)
        self.c_topology.addItem("")
        self.c_topology.addItem("")
        self.c_topology.setObjectName("c_topology")
        sizePolicy1.setHeightForWidth(self.c_topology.sizePolicy().hasHeightForWidth())
        self.c_topology.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.c_topology, 1, 1, 1, 1)

        self.si_p = QSpinBox(self.scrollAreaWidgetContents_2)
        self.si_p.setObjectName("si_p")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.si_p.sizePolicy().hasHeightForWidth())
        self.si_p.setSizePolicy(sizePolicy5)
        self.si_p.setMinimum(1)
        self.si_p.setMaximum(999999)
        self.si_p.setValue(1)

        self.gridLayout.addWidget(self.si_p, 0, 1, 1, 1)

        self.in_name = QLabel(self.scrollAreaWidgetContents_2)
        self.in_name.setObjectName("in_name")
        sizePolicy5.setHeightForWidth(self.in_name.sizePolicy().hasHeightForWidth())
        self.in_name.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.in_name, 2, 0, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents_2)
        self.label.setObjectName("label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.in_p = QLabel(self.scrollAreaWidgetContents_2)
        self.in_p.setObjectName("in_p")
        sizePolicy.setHeightForWidth(self.in_p.sizePolicy().hasHeightForWidth())
        self.in_p.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.in_p, 0, 0, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_4.addWidget(self.scrollArea)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.b_previous = QPushButton(SMachineType)
        self.b_previous.setObjectName("b_previous")
        self.b_previous.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.b_previous)

        self.b_next = QPushButton(SMachineType)
        self.b_next.setObjectName("b_next")

        self.horizontalLayout_2.addWidget(self.b_next)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SMachineType)

        QMetaObject.connectSlotsByName(SMachineType)

    # setupUi

    def retranslateUi(self, SMachineType):
        SMachineType.setWindowTitle(
            QCoreApplication.translate("SMachineType", "Form", None)
        )
        self.in_machine_type.setText(
            QCoreApplication.translate("SMachineType", "Machine type :", None)
        )
        self.c_type.setItemText(
            0,
            QCoreApplication.translate(
                "SMachineType", "SCIM (Squirrel Cage Induction Machine)", None
            ),
        )
        self.c_type.setItemText(
            1,
            QCoreApplication.translate(
                "SMachineType", "DFIM (Doubly Fed Induction Machine)", None
            ),
        )
        self.c_type.setItemText(
            2,
            QCoreApplication.translate(
                "SMachineType", "WRSM (Wound Rotor Synchronous Machine)", None
            ),
        )
        self.c_type.setItemText(
            3,
            QCoreApplication.translate(
                "SMachineType",
                "SIPMSM (Surface Inset Permanent Magnet Synchronous Machine)",
                None,
            ),
        )
        self.c_type.setItemText(
            4,
            QCoreApplication.translate(
                "SMachineType",
                "IPMSM (Interior Permanent Magnet Synchronous Machine)",
                None,
            ),
        )
        self.c_type.setItemText(
            5,
            QCoreApplication.translate(
                "SMachineType", "SynRM (Synchronous Reluctance Machine)", None
            ),
        )

        self.img_type_machine.setText("")
        self.groupBox.setTitle(
            QCoreApplication.translate("SMachineType", "Machine description ", None)
        )
        self.in_machine_desc.setPlaceholderText(
            QCoreApplication.translate("SMachineType", "Machine Description", None)
        )
        self.c_topology.setItemText(
            0, QCoreApplication.translate("SMachineType", "Internal Rotor", None)
        )
        self.c_topology.setItemText(
            1, QCoreApplication.translate("SMachineType", "External Rotor", None)
        )

        self.in_name.setText(
            QCoreApplication.translate("SMachineType", "Machine name :", None)
        )
        self.label.setText(
            QCoreApplication.translate("SMachineType", "Topology : ", None)
        )
        self.in_p.setText(
            QCoreApplication.translate("SMachineType", "Pole pair number :", None)
        )
        self.b_previous.setText(
            QCoreApplication.translate("SMachineType", "Previous", None)
        )
        self.b_next.setText(QCoreApplication.translate("SMachineType", "Next", None))

    # retranslateUi
