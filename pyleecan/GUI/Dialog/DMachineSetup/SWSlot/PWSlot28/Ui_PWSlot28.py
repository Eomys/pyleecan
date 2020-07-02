# -*- coding: utf-8 -*-

# File generated according to PWSlot28.ui
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PWSlot28(object):
    def setupUi(self, PWSlot28):
        PWSlot28.setObjectName("PWSlot28")
        PWSlot28.resize(630, 470)
        PWSlot28.setMinimumSize(QtCore.QSize(630, 470))
        PWSlot28.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(PWSlot28)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.img_slot = QtWidgets.QLabel(PWSlot28)
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
            QtGui.QPixmap(":/images/images/MachineSetup/WSlot/Slot 28.PNG")
        )
        self.img_slot.setScaledContents(True)
        self.img_slot.setObjectName("img_slot")
        self.verticalLayout_2.addWidget(self.img_slot)
        self.txt_constraint = QtWidgets.QTextEdit(PWSlot28)
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
        self.in_R1 = QtWidgets.QLabel(PWSlot28)
        self.in_R1.setObjectName("in_R1")
        self.gridLayout.addWidget(self.in_R1, 4, 0, 1, 1)
        self.lf_R1 = FloatEdit(PWSlot28)
        self.lf_R1.setObjectName("lf_R1")
        self.gridLayout.addWidget(self.lf_R1, 4, 1, 1, 1)
        self.unit_R1 = QtWidgets.QLabel(PWSlot28)
        self.unit_R1.setObjectName("unit_R1")
        self.gridLayout.addWidget(self.unit_R1, 4, 2, 1, 1)
        self.unit_H3 = QtWidgets.QLabel(PWSlot28)
        self.unit_H3.setObjectName("unit_H3")
        self.gridLayout.addWidget(self.unit_H3, 3, 2, 1, 1)
        self.lf_H3 = FloatEdit(PWSlot28)
        self.lf_H3.setObjectName("lf_H3")
        self.gridLayout.addWidget(self.lf_H3, 3, 1, 1, 1)
        self.in_H3 = QtWidgets.QLabel(PWSlot28)
        self.in_H3.setObjectName("in_H3")
        self.gridLayout.addWidget(self.in_H3, 3, 0, 1, 1)
        self.unit_H0 = QtWidgets.QLabel(PWSlot28)
        self.unit_H0.setObjectName("unit_H0")
        self.gridLayout.addWidget(self.unit_H0, 2, 2, 1, 1)
        self.lf_H0 = FloatEdit(PWSlot28)
        self.lf_H0.setObjectName("lf_H0")
        self.gridLayout.addWidget(self.lf_H0, 2, 1, 1, 1)
        self.unit_W0 = QtWidgets.QLabel(PWSlot28)
        self.unit_W0.setObjectName("unit_W0")
        self.gridLayout.addWidget(self.unit_W0, 0, 2, 1, 1)
        self.lf_W0 = FloatEdit(PWSlot28)
        self.lf_W0.setObjectName("lf_W0")
        self.gridLayout.addWidget(self.lf_W0, 0, 1, 1, 1)
        self.in_H0 = QtWidgets.QLabel(PWSlot28)
        self.in_H0.setObjectName("in_H0")
        self.gridLayout.addWidget(self.in_H0, 2, 0, 1, 1)
        self.in_W0 = QtWidgets.QLabel(PWSlot28)
        self.in_W0.setObjectName("in_W0")
        self.gridLayout.addWidget(self.in_W0, 0, 0, 1, 1)
        self.lf_W3 = FloatEdit(PWSlot28)
        self.lf_W3.setObjectName("lf_W3")
        self.gridLayout.addWidget(self.lf_W3, 1, 1, 1, 1)
        self.unit_W3 = QtWidgets.QLabel(PWSlot28)
        self.unit_W3.setObjectName("unit_W3")
        self.gridLayout.addWidget(self.unit_W3, 1, 2, 1, 1)
        self.in_W3 = QtWidgets.QLabel(PWSlot28)
        self.in_W3.setObjectName("in_W3")
        self.gridLayout.addWidget(self.in_W3, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.w_out = WWSlotOut(PWSlot28)
        self.w_out.setObjectName("w_out")
        self.verticalLayout.addWidget(self.w_out)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(PWSlot28)
        QtCore.QMetaObject.connectSlotsByName(PWSlot28)
        PWSlot28.setTabOrder(self.lf_W0, self.lf_W3)
        PWSlot28.setTabOrder(self.lf_W3, self.lf_H0)
        PWSlot28.setTabOrder(self.lf_H0, self.lf_H3)
        PWSlot28.setTabOrder(self.lf_H3, self.lf_R1)
        PWSlot28.setTabOrder(self.lf_R1, self.txt_constraint)

    def retranslateUi(self, PWSlot28):
        _translate = QtCore.QCoreApplication.translate
        PWSlot28.setWindowTitle(_translate("PWSlot28", "Form"))
        self.txt_constraint.setHtml(
            _translate(
                "PWSlot28",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; text-decoration: underline;">Constraints :</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">W0 &lt; 2*R1</span></p></body></html>',
            )
        )
        self.in_R1.setText(_translate("PWSlot28", "R1:"))
        self.unit_R1.setText(_translate("PWSlot28", "m"))
        self.unit_H3.setText(_translate("PWSlot28", "m"))
        self.in_H3.setText(_translate("PWSlot28", "H3:"))
        self.unit_H0.setText(_translate("PWSlot28", "m"))
        self.unit_W0.setText(_translate("PWSlot28", "m"))
        self.in_H0.setText(_translate("PWSlot28", "H0:"))
        self.in_W0.setText(_translate("PWSlot28", "W0:"))
        self.unit_W3.setText(_translate("PWSlot28", "m"))
        self.in_W3.setText(_translate("PWSlot28", "W3:"))


from ......GUI.Dialog.DMachineSetup.SWSlot.WWSlotOut.WWSlotOut import WWSlotOut
from ......GUI.Tools.FloatEdit import FloatEdit
from pyleecan.GUI.Resources import pyleecan_rc
