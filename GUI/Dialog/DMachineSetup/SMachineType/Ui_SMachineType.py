# -*- coding: utf-8 -*-

# File generated according to SMachineType.ui
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SMachineType(object):
    def setupUi(self, SMachineType):
        SMachineType.setObjectName("SMachineType")
        SMachineType.resize(650, 550)
        SMachineType.setMinimumSize(QtCore.QSize(650, 550))
        self.verticalLayout = QtWidgets.QVBoxLayout(SMachineType)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_5.addItem(spacerItem)
        self.in_machine_type = QtWidgets.QLabel(SMachineType)
        self.in_machine_type.setObjectName("in_machine_type")
        self.horizontalLayout_5.addWidget(self.in_machine_type)
        self.c_type = QtWidgets.QComboBox(SMachineType)
        self.c_type.setObjectName("c_type")
        self.c_type.addItem("")
        self.c_type.addItem("")
        self.c_type.addItem("")
        self.c_type.addItem("")
        self.c_type.addItem("")
        self.c_type.addItem("")
        self.c_type.addItem("")
        self.horizontalLayout_5.addWidget(self.c_type)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.img_type_machine = QtWidgets.QLabel(SMachineType)
        self.img_type_machine.setMinimumSize(QtCore.QSize(300, 300))
        self.img_type_machine.setMaximumSize(QtCore.QSize(400, 400))
        self.img_type_machine.setText("")
        self.img_type_machine.setPixmap(
            QtGui.QPixmap(":/images/images/MachineSetup/SCIM.png")
        )
        self.img_type_machine.setScaledContents(True)
        self.img_type_machine.setObjectName("img_type_machine")
        self.horizontalLayout_4.addWidget(self.img_type_machine)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.txt_type_machine = QtWidgets.QTextEdit(SMachineType)
        self.txt_type_machine.setMaximumSize(QtCore.QSize(16777215, 30))
        self.txt_type_machine.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse
        )
        self.txt_type_machine.setObjectName("txt_type_machine")
        self.verticalLayout.addWidget(self.txt_type_machine)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.is_inner_rotor = QtWidgets.QCheckBox(SMachineType)
        self.is_inner_rotor.setChecked(True)
        self.is_inner_rotor.setObjectName("is_inner_rotor")
        self.horizontalLayout.addWidget(self.is_inner_rotor)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem2)
        self.in_name = QtWidgets.QLabel(SMachineType)
        self.in_name.setObjectName("in_name")
        self.horizontalLayout.addWidget(self.in_name)
        self.le_name = QtWidgets.QLineEdit(SMachineType)
        self.le_name.setMinimumSize(QtCore.QSize(200, 0))
        self.le_name.setObjectName("le_name")
        self.horizontalLayout.addWidget(self.le_name)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem3)
        self.in_p = QtWidgets.QLabel(SMachineType)
        self.in_p.setObjectName("in_p")
        self.horizontalLayout.addWidget(self.in_p)
        self.si_p = QtWidgets.QSpinBox(SMachineType)
        self.si_p.setMinimum(1)
        self.si_p.setMaximum(999999)
        self.si_p.setProperty("value", 1)
        self.si_p.setObjectName("si_p")
        self.horizontalLayout.addWidget(self.si_p)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem4)
        self.b_previous = QtWidgets.QPushButton(SMachineType)
        self.b_previous.setEnabled(False)
        self.b_previous.setObjectName("b_previous")
        self.horizontalLayout_2.addWidget(self.b_previous)
        self.b_next = QtWidgets.QPushButton(SMachineType)
        self.b_next.setObjectName("b_next")
        self.horizontalLayout_2.addWidget(self.b_next)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SMachineType)
        QtCore.QMetaObject.connectSlotsByName(SMachineType)
        SMachineType.setTabOrder(self.si_p, self.b_next)

    def retranslateUi(self, SMachineType):
        _translate = QtCore.QCoreApplication.translate
        SMachineType.setWindowTitle(_translate("SMachineType", "Form"))
        self.in_machine_type.setText(_translate("SMachineType", "Machine type :"))
        self.c_type.setItemText(0, _translate("SMachineType", "SCIM"))
        self.c_type.setItemText(1, _translate("SMachineType", "DFIM"))
        self.c_type.setItemText(2, _translate("SMachineType", "WRSM"))
        self.c_type.setItemText(3, _translate("SMachineType", "SPMSM"))
        self.c_type.setItemText(4, _translate("SMachineType", "SIPMSM"))
        self.c_type.setItemText(5, _translate("SMachineType", "IPMSM"))
        self.c_type.setItemText(6, _translate("SMachineType", "SyRM"))
        self.is_inner_rotor.setToolTip(
            _translate(
                "SMachineType", "1 for internal rotor topology, 0 for external rotor"
            )
        )
        self.is_inner_rotor.setText(_translate("SMachineType", "is_inner_rotor"))
        self.in_name.setText(_translate("SMachineType", "Machine name :"))
        self.in_p.setText(_translate("SMachineType", "p :"))
        self.b_previous.setText(_translate("SMachineType", "Previous"))
        self.b_next.setText(_translate("SMachineType", "Next"))


from pyleecan.GUI.Resources import pyleecan_rc
