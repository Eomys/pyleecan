# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitHub\pyleecan\GUI\Dialog\DMachineSetup\SWSlot\PWSlot25\PWSlot25.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PWSlot25(object):
    def setupUi(self, PWSlot25):
        PWSlot25.setObjectName("PWSlot25")
        PWSlot25.resize(630, 470)
        PWSlot25.setMinimumSize(QtCore.QSize(630, 470))
        PWSlot25.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(PWSlot25)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.img_slot = QtWidgets.QLabel(PWSlot25)
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
            QtGui.QPixmap(":/images/images/MachineSetup/WSlot/Slot_25.PNG")
        )
        self.img_slot.setScaledContents(True)
        self.img_slot.setObjectName("img_slot")
        self.verticalLayout_2.addWidget(self.img_slot)
        self.textEdit = QtWidgets.QTextEdit(PWSlot25)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 60))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 60))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.in_W3 = QtWidgets.QLabel(PWSlot25)
        self.in_W3.setObjectName("in_W3")
        self.gridLayout.addWidget(self.in_W3, 0, 0, 1, 1)
        self.lf_W3 = FloatEdit(PWSlot25)
        self.lf_W3.setObjectName("lf_W3")
        self.gridLayout.addWidget(self.lf_W3, 0, 1, 1, 1)
        self.unit_W3 = QtWidgets.QLabel(PWSlot25)
        self.unit_W3.setObjectName("unit_W3")
        self.gridLayout.addWidget(self.unit_W3, 0, 2, 1, 1)
        self.in_W4 = QtWidgets.QLabel(PWSlot25)
        self.in_W4.setObjectName("in_W4")
        self.gridLayout.addWidget(self.in_W4, 1, 0, 1, 1)
        self.lf_W4 = FloatEdit(PWSlot25)
        self.lf_W4.setObjectName("lf_W4")
        self.gridLayout.addWidget(self.lf_W4, 1, 1, 1, 1)
        self.unit_W4 = QtWidgets.QLabel(PWSlot25)
        self.unit_W4.setObjectName("unit_W4")
        self.gridLayout.addWidget(self.unit_W4, 1, 2, 1, 1)
        self.in_H1 = QtWidgets.QLabel(PWSlot25)
        self.in_H1.setObjectName("in_H1")
        self.gridLayout.addWidget(self.in_H1, 2, 0, 1, 1)
        self.lf_H1 = FloatEdit(PWSlot25)
        self.lf_H1.setObjectName("lf_H1")
        self.gridLayout.addWidget(self.lf_H1, 2, 1, 1, 1)
        self.unit_H1 = QtWidgets.QLabel(PWSlot25)
        self.unit_H1.setObjectName("unit_H1")
        self.gridLayout.addWidget(self.unit_H1, 2, 2, 1, 1)
        self.in_H2 = QtWidgets.QLabel(PWSlot25)
        self.in_H2.setObjectName("in_H2")
        self.gridLayout.addWidget(self.in_H2, 3, 0, 1, 1)
        self.lf_H2 = FloatEdit(PWSlot25)
        self.lf_H2.setObjectName("lf_H2")
        self.gridLayout.addWidget(self.lf_H2, 3, 1, 1, 1)
        self.unit_H2 = QtWidgets.QLabel(PWSlot25)
        self.unit_H2.setObjectName("unit_H2")
        self.gridLayout.addWidget(self.unit_H2, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.w_out = WWSlotOut(PWSlot25)
        self.w_out.setObjectName("w_out")
        self.verticalLayout.addWidget(self.w_out)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(PWSlot25)
        QtCore.QMetaObject.connectSlotsByName(PWSlot25)

    def retranslateUi(self, PWSlot25):
        _translate = QtCore.QCoreApplication.translate
        PWSlot25.setWindowTitle(_translate("PWSlot25", "Form"))
        self.textEdit.setHtml(
            _translate(
                "PWSlot25",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Constant tooth width</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Slot edges are not radial</span></p></body></html>',
            )
        )
        self.in_W3.setText(_translate("PWSlot25", "W3 :"))
        self.unit_W3.setText(_translate("PWSlot25", "m"))
        self.in_W4.setText(_translate("PWSlot25", "W4 :"))
        self.unit_W4.setText(_translate("PWSlot25", "m"))
        self.in_H1.setText(_translate("PWSlot25", "H1 :"))
        self.unit_H1.setText(_translate("PWSlot25", "m"))
        self.in_H2.setText(_translate("PWSlot25", "H2 :"))
        self.unit_H2.setText(_translate("PWSlot25", "m"))


from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.WWSlotOut.WWSlotOut import WWSlotOut
from pyleecan.GUI.Tools.FloatEdit import FloatEdit
from pyleecan.GUI.Resources import pyleecan_rc
