# -*- coding: utf-8 -*-

# File generated according to PWSlot22.ui
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PWSlot22(object):
    def setupUi(self, PWSlot22):
        PWSlot22.setObjectName("PWSlot22")
        PWSlot22.resize(630, 470)
        PWSlot22.setMinimumSize(QtCore.QSize(630, 470))
        PWSlot22.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(PWSlot22)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.img_slot = QtWidgets.QLabel(PWSlot22)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.img_slot.setText("")
        self.img_slot.setPixmap(
            QtGui.QPixmap(":/images/images/MachineSetup/WSlot/Slot 22.PNG")
        )
        self.img_slot.setScaledContents(True)
        self.img_slot.setObjectName("img_slot")
        self.verticalLayout_2.addWidget(self.img_slot)
        self.txt_constraint = QtWidgets.QTextEdit(PWSlot22)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.txt_constraint.sizePolicy().hasHeightForWidth()
        )
        self.txt_constraint.setSizePolicy(sizePolicy)
        self.txt_constraint.setMaximumSize(QtCore.QSize(16777215, 75))
        self.txt_constraint.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_constraint.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse
        )
        self.txt_constraint.setObjectName("txt_constraint")
        self.verticalLayout_2.addWidget(self.txt_constraint)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.in_W0 = QtWidgets.QLabel(PWSlot22)
        self.in_W0.setObjectName("in_W0")
        self.gridLayout.addWidget(self.in_W0, 0, 0, 1, 1)
        self.lf_W0 = FloatEdit(PWSlot22)
        self.lf_W0.setObjectName("lf_W0")
        self.gridLayout.addWidget(self.lf_W0, 0, 1, 1, 1)
        self.in_W2 = QtWidgets.QLabel(PWSlot22)
        self.in_W2.setObjectName("in_W2")
        self.gridLayout.addWidget(self.in_W2, 1, 0, 1, 1)
        self.lf_W2 = FloatEdit(PWSlot22)
        self.lf_W2.setObjectName("lf_W2")
        self.gridLayout.addWidget(self.lf_W2, 1, 1, 1, 1)
        self.in_H0 = QtWidgets.QLabel(PWSlot22)
        self.in_H0.setObjectName("in_H0")
        self.gridLayout.addWidget(self.in_H0, 2, 0, 1, 1)
        self.lf_H0 = FloatEdit(PWSlot22)
        self.lf_H0.setObjectName("lf_H0")
        self.gridLayout.addWidget(self.lf_H0, 2, 1, 1, 1)
        self.unit_H0 = QtWidgets.QLabel(PWSlot22)
        self.unit_H0.setObjectName("unit_H0")
        self.gridLayout.addWidget(self.unit_H0, 2, 2, 1, 1)
        self.in_H2 = QtWidgets.QLabel(PWSlot22)
        self.in_H2.setObjectName("in_H2")
        self.gridLayout.addWidget(self.in_H2, 3, 0, 1, 1)
        self.lf_H2 = FloatEdit(PWSlot22)
        self.lf_H2.setObjectName("lf_H2")
        self.gridLayout.addWidget(self.lf_H2, 3, 1, 1, 1)
        self.unit_H2 = QtWidgets.QLabel(PWSlot22)
        self.unit_H2.setObjectName("unit_H2")
        self.gridLayout.addWidget(self.unit_H2, 3, 2, 1, 1)
        self.c_W0_unit = QtWidgets.QComboBox(PWSlot22)
        self.c_W0_unit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.c_W0_unit.setObjectName("c_W0_unit")
        self.c_W0_unit.addItem("")
        self.c_W0_unit.addItem("")
        self.gridLayout.addWidget(self.c_W0_unit, 0, 2, 1, 1)
        self.c_W2_unit = QtWidgets.QComboBox(PWSlot22)
        self.c_W2_unit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.c_W2_unit.setObjectName("c_W2_unit")
        self.c_W2_unit.addItem("")
        self.c_W2_unit.addItem("")
        self.gridLayout.addWidget(self.c_W2_unit, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.w_out = WWSlotOut(PWSlot22)
        self.w_out.setObjectName("w_out")
        self.verticalLayout.addWidget(self.w_out)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(PWSlot22)
        QtCore.QMetaObject.connectSlotsByName(PWSlot22)
        PWSlot22.setTabOrder(self.lf_W0, self.lf_W2)
        PWSlot22.setTabOrder(self.lf_W2, self.lf_H0)
        PWSlot22.setTabOrder(self.lf_H0, self.lf_H2)
        PWSlot22.setTabOrder(self.lf_H2, self.txt_constraint)

    def retranslateUi(self, PWSlot22):
        _translate = QtCore.QCoreApplication.translate
        PWSlot22.setWindowTitle(_translate("PWSlot22", "Form"))
        self.txt_constraint.setHtml(
            _translate(
                "PWSlot22",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; text-decoration: underline;">Constraints :</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">W0 &lt;= W2</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">W2 &lt;= 2*pi/Zs</span></p></body></html>',
            )
        )
        self.in_W0.setText(_translate("PWSlot22", "W0 :"))
        self.in_W2.setText(_translate("PWSlot22", "W2 :"))
        self.in_H0.setText(_translate("PWSlot22", "H0 :"))
        self.unit_H0.setText(_translate("PWSlot22", "m"))
        self.in_H2.setText(_translate("PWSlot22", "H2 :"))
        self.unit_H2.setText(_translate("PWSlot22", "m"))
        self.c_W0_unit.setItemText(0, _translate("PWSlot22", "rad"))
        self.c_W0_unit.setItemText(1, _translate("PWSlot22", "deg"))
        self.c_W2_unit.setItemText(0, _translate("PWSlot22", "rad"))
        self.c_W2_unit.setItemText(1, _translate("PWSlot22", "deg"))


from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.WWSlotOut.WWSlotOut import WWSlotOut
from pyleecan.GUI.Tools.FloatEdit import FloatEdit
from pyleecan.GUI.Resources import pyleecan_rc
