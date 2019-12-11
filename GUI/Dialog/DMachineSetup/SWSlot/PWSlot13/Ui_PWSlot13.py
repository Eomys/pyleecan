# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitHub\pyleecan\GUI\Dialog\DMachineSetup\SWSlot\PWSlot13\PWSlot13.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PWSlot13(object):
    def setupUi(self, PWSlot13):
        PWSlot13.setObjectName("PWSlot13")
        PWSlot13.resize(630, 470)
        PWSlot13.setMinimumSize(QtCore.QSize(630, 470))
        PWSlot13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(PWSlot13)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.img_slot = QtWidgets.QLabel(PWSlot13)
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
            QtGui.QPixmap(":/images/images/MachineSetup/WSlot/Slot 13.PNG")
        )
        self.img_slot.setScaledContents(True)
        self.img_slot.setObjectName("img_slot")
        self.verticalLayout_2.addWidget(self.img_slot)
        self.txt_constraint = QtWidgets.QTextEdit(PWSlot13)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.txt_constraint.sizePolicy().hasHeightForWidth()
        )
        self.txt_constraint.setSizePolicy(sizePolicy)
        self.txt_constraint.setMaximumSize(QtCore.QSize(16777215, 70))
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
        self.in_W0 = QtWidgets.QLabel(PWSlot13)
        self.in_W0.setObjectName("in_W0")
        self.gridLayout.addWidget(self.in_W0, 0, 0, 1, 1)
        self.lf_W0 = FloatEdit(PWSlot13)
        self.lf_W0.setObjectName("lf_W0")
        self.gridLayout.addWidget(self.lf_W0, 0, 1, 1, 1)
        self.unit_W0 = QtWidgets.QLabel(PWSlot13)
        self.unit_W0.setObjectName("unit_W0")
        self.gridLayout.addWidget(self.unit_W0, 0, 2, 1, 1)
        self.in_W1 = QtWidgets.QLabel(PWSlot13)
        self.in_W1.setObjectName("in_W1")
        self.gridLayout.addWidget(self.in_W1, 1, 0, 1, 1)
        self.lf_W1 = FloatEdit(PWSlot13)
        self.lf_W1.setObjectName("lf_W1")
        self.gridLayout.addWidget(self.lf_W1, 1, 1, 1, 1)
        self.unit_W1 = QtWidgets.QLabel(PWSlot13)
        self.unit_W1.setObjectName("unit_W1")
        self.gridLayout.addWidget(self.unit_W1, 1, 2, 1, 1)
        self.in_W2 = QtWidgets.QLabel(PWSlot13)
        self.in_W2.setObjectName("in_W2")
        self.gridLayout.addWidget(self.in_W2, 2, 0, 1, 1)
        self.lf_W2 = FloatEdit(PWSlot13)
        self.lf_W2.setObjectName("lf_W2")
        self.gridLayout.addWidget(self.lf_W2, 2, 1, 1, 1)
        self.unit_W2 = QtWidgets.QLabel(PWSlot13)
        self.unit_W2.setObjectName("unit_W2")
        self.gridLayout.addWidget(self.unit_W2, 2, 2, 1, 1)
        self.in_W3 = QtWidgets.QLabel(PWSlot13)
        self.in_W3.setObjectName("in_W3")
        self.gridLayout.addWidget(self.in_W3, 3, 0, 1, 1)
        self.lf_W3 = FloatEdit(PWSlot13)
        self.lf_W3.setObjectName("lf_W3")
        self.gridLayout.addWidget(self.lf_W3, 3, 1, 1, 1)
        self.unit_W3 = QtWidgets.QLabel(PWSlot13)
        self.unit_W3.setObjectName("unit_W3")
        self.gridLayout.addWidget(self.unit_W3, 3, 2, 1, 1)
        self.in_H0 = QtWidgets.QLabel(PWSlot13)
        self.in_H0.setObjectName("in_H0")
        self.gridLayout.addWidget(self.in_H0, 4, 0, 1, 1)
        self.lf_H0 = FloatEdit(PWSlot13)
        self.lf_H0.setObjectName("lf_H0")
        self.gridLayout.addWidget(self.lf_H0, 4, 1, 1, 1)
        self.unit_H0 = QtWidgets.QLabel(PWSlot13)
        self.unit_H0.setObjectName("unit_H0")
        self.gridLayout.addWidget(self.unit_H0, 4, 2, 1, 1)
        self.in_H1 = QtWidgets.QLabel(PWSlot13)
        self.in_H1.setObjectName("in_H1")
        self.gridLayout.addWidget(self.in_H1, 5, 0, 1, 1)
        self.lf_H1 = FloatEdit(PWSlot13)
        self.lf_H1.setObjectName("lf_H1")
        self.gridLayout.addWidget(self.lf_H1, 5, 1, 1, 1)
        self.c_H1_unit = QtWidgets.QComboBox(PWSlot13)
        self.c_H1_unit.setObjectName("c_H1_unit")
        self.c_H1_unit.addItem("")
        self.c_H1_unit.addItem("")
        self.c_H1_unit.addItem("")
        self.gridLayout.addWidget(self.c_H1_unit, 5, 2, 1, 1)
        self.in_H2 = QtWidgets.QLabel(PWSlot13)
        self.in_H2.setObjectName("in_H2")
        self.gridLayout.addWidget(self.in_H2, 6, 0, 1, 1)
        self.lf_H2 = FloatEdit(PWSlot13)
        self.lf_H2.setObjectName("lf_H2")
        self.gridLayout.addWidget(self.lf_H2, 6, 1, 1, 1)
        self.unit_H2 = QtWidgets.QLabel(PWSlot13)
        self.unit_H2.setObjectName("unit_H2")
        self.gridLayout.addWidget(self.unit_H2, 6, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.w_out = WWSlotOut(PWSlot13)
        self.w_out.setObjectName("w_out")
        self.verticalLayout.addWidget(self.w_out)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(PWSlot13)
        QtCore.QMetaObject.connectSlotsByName(PWSlot13)
        PWSlot13.setTabOrder(self.lf_W0, self.lf_W1)
        PWSlot13.setTabOrder(self.lf_W1, self.lf_W2)
        PWSlot13.setTabOrder(self.lf_W2, self.lf_W3)
        PWSlot13.setTabOrder(self.lf_W3, self.lf_H0)
        PWSlot13.setTabOrder(self.lf_H0, self.lf_H1)
        PWSlot13.setTabOrder(self.lf_H1, self.c_H1_unit)
        PWSlot13.setTabOrder(self.c_H1_unit, self.lf_H2)
        PWSlot13.setTabOrder(self.lf_H2, self.txt_constraint)

    def retranslateUi(self, PWSlot13):
        _translate = QtCore.QCoreApplication.translate
        PWSlot13.setWindowTitle(_translate("PWSlot13", "Form"))
        self.txt_constraint.setHtml(
            _translate(
                "PWSlot13",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; text-decoration: underline;">Constraints :</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">W0 &lt;= W1</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">W2 &lt;= W1</span></p></body></html>',
            )
        )
        self.in_W0.setText(_translate("PWSlot13", "W0 :"))
        self.unit_W0.setText(_translate("PWSlot13", "m"))
        self.in_W1.setText(_translate("PWSlot13", "W1 :"))
        self.unit_W1.setText(_translate("PWSlot13", "m"))
        self.in_W2.setText(_translate("PWSlot13", "W2 :"))
        self.unit_W2.setText(_translate("PWSlot13", "m"))
        self.in_W3.setText(_translate("PWSlot13", "W3 :"))
        self.unit_W3.setText(_translate("PWSlot13", "m"))
        self.in_H0.setText(_translate("PWSlot13", "H0 :"))
        self.unit_H0.setText(_translate("PWSlot13", "m"))
        self.in_H1.setText(_translate("PWSlot13", "H1 :"))
        self.c_H1_unit.setItemText(0, _translate("PWSlot13", "m"))
        self.c_H1_unit.setItemText(1, _translate("PWSlot13", "rad"))
        self.c_H1_unit.setItemText(2, _translate("PWSlot13", "deg"))
        self.in_H2.setText(_translate("PWSlot13", "H2 :"))
        self.unit_H2.setText(_translate("PWSlot13", "m"))


from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.WWSlotOut.WWSlotOut import WWSlotOut
from pyleecan.GUI.Tools.FloatEdit import FloatEdit
from pyleecan.GUI.Resources import pyleecan_rc
