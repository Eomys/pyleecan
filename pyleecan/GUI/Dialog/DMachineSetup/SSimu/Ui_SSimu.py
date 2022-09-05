# -*- coding: utf-8 -*-

# File generated according to SSimu.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .....GUI.Tools.FloatEdit import FloatEdit
from .....GUI.Tools.WPathSelector.WPathSelectorV import WPathSelectorV
from .....GUI.Tools.MPLCanvas import MPLCanvas

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SSimu(object):
    def setupUi(self, SSimu):
        if not SSimu.objectName():
            SSimu.setObjectName(u"SSimu")
        SSimu.resize(1209, 837)
        SSimu.setMinimumSize(QSize(650, 550))
        self.verticalLayout_4 = QVBoxLayout(SSimu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.w_viewer = MPLCanvas(SSimu)
        self.w_viewer.setObjectName(u"w_viewer")
        self.w_viewer.setMinimumSize(QSize(250, 0))

        self.verticalLayout_3.addWidget(self.w_viewer)

        self.txt_tuto = QTextEdit(SSimu)
        self.txt_tuto.setObjectName(u"txt_tuto")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_tuto.sizePolicy().hasHeightForWidth())
        self.txt_tuto.setSizePolicy(sizePolicy)
        self.txt_tuto.setMaximumSize(QSize(16777215, 70))
        self.txt_tuto.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_tuto.setTextInteractionFlags(
            Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse
        )

        self.verticalLayout_3.addWidget(self.txt_tuto)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.scrollArea = QScrollArea(SSimu)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(350, 0))
        self.scrollArea.setMaximumSize(QSize(350, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 348, 774))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.g_OP = QGroupBox(self.scrollAreaWidgetContents)
        self.g_OP.setObjectName(u"g_OP")
        self.gridLayout = QGridLayout(self.g_OP)
        self.gridLayout.setObjectName(u"gridLayout")
        self.in_N0 = QLabel(self.g_OP)
        self.in_N0.setObjectName(u"in_N0")
        self.in_N0.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.in_N0, 0, 0, 1, 1)

        self.lf_N0 = FloatEdit(self.g_OP)
        self.lf_N0.setObjectName(u"lf_N0")
        self.lf_N0.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.lf_N0, 0, 1, 1, 1)

        self.unit_N0 = QLabel(self.g_OP)
        self.unit_N0.setObjectName(u"unit_N0")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.unit_N0.sizePolicy().hasHeightForWidth())
        self.unit_N0.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.unit_N0, 0, 2, 1, 1)

        self.in_I1 = QLabel(self.g_OP)
        self.in_I1.setObjectName(u"in_I1")
        self.in_I1.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.in_I1, 1, 0, 1, 1)

        self.lf_I1 = FloatEdit(self.g_OP)
        self.lf_I1.setObjectName(u"lf_I1")
        self.lf_I1.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.lf_I1, 1, 1, 1, 1)

        self.unit_I1 = QLabel(self.g_OP)
        self.unit_I1.setObjectName(u"unit_I1")
        sizePolicy1.setHeightForWidth(self.unit_I1.sizePolicy().hasHeightForWidth())
        self.unit_I1.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.unit_I1, 1, 2, 1, 1)

        self.in_I2 = QLabel(self.g_OP)
        self.in_I2.setObjectName(u"in_I2")
        self.in_I2.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.in_I2, 2, 0, 1, 1)

        self.lf_I2 = FloatEdit(self.g_OP)
        self.lf_I2.setObjectName(u"lf_I2")
        self.lf_I2.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.lf_I2, 2, 1, 1, 1)

        self.unit_I2 = QLabel(self.g_OP)
        self.unit_I2.setObjectName(u"unit_I2")
        sizePolicy1.setHeightForWidth(self.unit_I2.sizePolicy().hasHeightForWidth())
        self.unit_I2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.unit_I2, 2, 2, 1, 1)

        self.in_I3 = QLabel(self.g_OP)
        self.in_I3.setObjectName(u"in_I3")
        self.in_I3.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.in_I3, 3, 0, 1, 1)

        self.lf_I3 = FloatEdit(self.g_OP)
        self.lf_I3.setObjectName(u"lf_I3")
        self.lf_I3.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.lf_I3, 3, 1, 1, 1)

        self.unit_I3 = QLabel(self.g_OP)
        self.unit_I3.setObjectName(u"unit_I3")
        sizePolicy1.setHeightForWidth(self.unit_I3.sizePolicy().hasHeightForWidth())
        self.unit_I3.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.unit_I3, 3, 2, 1, 1)

        self.in_T_mag = QLabel(self.g_OP)
        self.in_T_mag.setObjectName(u"in_T_mag")
        self.in_T_mag.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.in_T_mag, 4, 0, 1, 1)

        self.lf_T_mag = FloatEdit(self.g_OP)
        self.lf_T_mag.setObjectName(u"lf_T_mag")
        self.lf_T_mag.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.lf_T_mag, 4, 1, 1, 1)

        self.unit_T_mag = QLabel(self.g_OP)
        self.unit_T_mag.setObjectName(u"unit_T_mag")
        sizePolicy1.setHeightForWidth(self.unit_T_mag.sizePolicy().hasHeightForWidth())
        self.unit_T_mag.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.unit_T_mag, 4, 2, 1, 1)

        self.verticalLayout_2.addWidget(self.g_OP)

        self.g_mag = QGroupBox(self.scrollAreaWidgetContents)
        self.g_mag.setObjectName(u"g_mag")
        self.gridLayout_2 = QGridLayout(self.g_mag)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.is_per_a = QCheckBox(self.g_mag)
        self.is_per_a.setObjectName(u"is_per_a")

        self.gridLayout_2.addWidget(self.is_per_a, 0, 0, 1, 1)

        self.in_Na_tot = QLabel(self.g_mag)
        self.in_Na_tot.setObjectName(u"in_Na_tot")
        self.in_Na_tot.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.in_Na_tot, 1, 0, 1, 1)

        self.si_Na_tot = QSpinBox(self.g_mag)
        self.si_Na_tot.setObjectName(u"si_Na_tot")

        self.gridLayout_2.addWidget(self.si_Na_tot, 1, 1, 1, 1)

        self.is_per_t = QCheckBox(self.g_mag)
        self.is_per_t.setObjectName(u"is_per_t")

        self.gridLayout_2.addWidget(self.is_per_t, 2, 0, 1, 1)

        self.in_Nt_tot = QLabel(self.g_mag)
        self.in_Nt_tot.setObjectName(u"in_Nt_tot")
        self.in_Nt_tot.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.in_Nt_tot, 3, 0, 1, 1)

        self.si_Nt_tot = QSpinBox(self.g_mag)
        self.si_Nt_tot.setObjectName(u"si_Nt_tot")

        self.gridLayout_2.addWidget(self.si_Nt_tot, 3, 1, 1, 1)

        self.in_Kmesh = QLabel(self.g_mag)
        self.in_Kmesh.setObjectName(u"in_Kmesh")
        self.in_Kmesh.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.in_Kmesh, 4, 0, 1, 1)

        self.lf_Kmesh = FloatEdit(self.g_mag)
        self.lf_Kmesh.setObjectName(u"lf_Kmesh")
        self.lf_Kmesh.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.lf_Kmesh, 4, 1, 1, 1)

        self.in_nb_worker = QLabel(self.g_mag)
        self.in_nb_worker.setObjectName(u"in_nb_worker")
        self.in_nb_worker.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.in_nb_worker, 5, 0, 1, 1)

        self.si_nb_worker = QSpinBox(self.g_mag)
        self.si_nb_worker.setObjectName(u"si_nb_worker")

        self.gridLayout_2.addWidget(self.si_nb_worker, 5, 1, 1, 1)

        self.verticalLayout_2.addWidget(self.g_mag)

        self.g_out = QGroupBox(self.scrollAreaWidgetContents)
        self.g_out.setObjectName(u"g_out")
        self.verticalLayout = QVBoxLayout(self.g_out)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.in_name = QLabel(self.g_out)
        self.in_name.setObjectName(u"in_name")

        self.horizontalLayout_2.addWidget(self.in_name)

        self.le_name = QLineEdit(self.g_out)
        self.le_name.setObjectName(u"le_name")

        self.horizontalLayout_2.addWidget(self.le_name)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.w_path_result = WPathSelectorV(self.g_out)
        self.w_path_result.setObjectName(u"w_path_result")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.w_path_result.sizePolicy().hasHeightForWidth()
        )
        self.w_path_result.setSizePolicy(sizePolicy2)
        self.w_path_result.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.w_path_result)

        self.is_losses = QCheckBox(self.g_out)
        self.is_losses.setObjectName(u"is_losses")

        self.verticalLayout.addWidget(self.is_losses)

        self.is_mesh_sol = QCheckBox(self.g_out)
        self.is_mesh_sol.setObjectName(u"is_mesh_sol")

        self.verticalLayout.addWidget(self.is_mesh_sol)

        self.verticalLayout_2.addWidget(self.g_out)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.b_previous = QPushButton(SSimu)
        self.b_previous.setObjectName(u"b_previous")

        self.horizontalLayout_3.addWidget(self.b_previous)

        self.b_next = QPushButton(SSimu)
        self.b_next.setObjectName(u"b_next")

        self.horizontalLayout_3.addWidget(self.b_next)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi(SSimu)

        QMetaObject.connectSlotsByName(SSimu)

    # setupUi

    def retranslateUi(self, SSimu):
        SSimu.setWindowTitle(QCoreApplication.translate("SSimu", u"Form", None))
        self.txt_tuto.setHtml(
            QCoreApplication.translate(
                "SSimu",
                u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'DejaVu Sans'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt; font-weight:600;">Only Single Speed current driven FEMM simulation is available in this GUI</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt; font-weight:600;">Other models, Sensitivity, Variable speed, Optimization are available in scripting mode</span></p></body></html>',
                None,
            )
        )
        self.g_OP.setTitle(
            QCoreApplication.translate("SSimu", u"Operating Point", None)
        )
        # if QT_CONFIG(tooltip)
        self.in_N0.setToolTip(
            QCoreApplication.translate("SSimu", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.in_N0.setText(QCoreApplication.translate("SSimu", u"N0:", None))
        # if QT_CONFIG(tooltip)
        self.lf_N0.setToolTip(
            QCoreApplication.translate("SSimu", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.lf_N0.setText(QCoreApplication.translate("SSimu", u"3000", None))
        self.unit_N0.setText(QCoreApplication.translate("SSimu", u"[rpm]", None))
        # if QT_CONFIG(tooltip)
        self.in_I1.setToolTip(
            QCoreApplication.translate("SSimu", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.in_I1.setText(QCoreApplication.translate("SSimu", u"Id:", None))
        # if QT_CONFIG(tooltip)
        self.lf_I1.setToolTip(
            QCoreApplication.translate("SSimu", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.lf_I1.setText(QCoreApplication.translate("SSimu", u"0", None))
        self.unit_I1.setText(QCoreApplication.translate("SSimu", u"[Arms]", None))
        # if QT_CONFIG(tooltip)
        self.in_I2.setToolTip(
            QCoreApplication.translate("SSimu", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.in_I2.setText(QCoreApplication.translate("SSimu", u"Iq:", None))
        # if QT_CONFIG(tooltip)
        self.lf_I2.setToolTip(
            QCoreApplication.translate("SSimu", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.lf_I2.setText(QCoreApplication.translate("SSimu", u"0", None))
        self.unit_I2.setText(QCoreApplication.translate("SSimu", u"[Arms]", None))
        # if QT_CONFIG(tooltip)
        self.in_I3.setToolTip(
            QCoreApplication.translate("SSimu", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.in_I3.setText(QCoreApplication.translate("SSimu", u"If:", None))
        # if QT_CONFIG(tooltip)
        self.lf_I3.setToolTip(
            QCoreApplication.translate("SSimu", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.unit_I3.setText(QCoreApplication.translate("SSimu", u"[Arms]", None))
        # if QT_CONFIG(tooltip)
        self.in_T_mag.setToolTip(
            QCoreApplication.translate("SSimu", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.in_T_mag.setText(QCoreApplication.translate("SSimu", u"T_mag:", None))
        # if QT_CONFIG(tooltip)
        self.lf_T_mag.setToolTip(
            QCoreApplication.translate("SSimu", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.lf_T_mag.setText(QCoreApplication.translate("SSimu", u"20", None))
        self.unit_T_mag.setText(QCoreApplication.translate("SSimu", u"[\u00b0C]", None))
        self.g_mag.setTitle(
            QCoreApplication.translate("SSimu", u"Magnetic Model", None)
        )
        self.is_per_a.setText(
            QCoreApplication.translate("SSimu", u"Angular periodicity", None)
        )
        # if QT_CONFIG(tooltip)
        self.in_Na_tot.setToolTip(
            QCoreApplication.translate("SSimu", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.in_Na_tot.setText(
            QCoreApplication.translate(
                "SSimu", u"Angular points (over 360\u00b0)", None
            )
        )
        self.is_per_t.setText(
            QCoreApplication.translate("SSimu", u"Time periodicity", None)
        )
        # if QT_CONFIG(tooltip)
        self.in_Nt_tot.setToolTip(
            QCoreApplication.translate("SSimu", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.in_Nt_tot.setText(
            QCoreApplication.translate("SSimu", u"Time steps (over one turn)", None)
        )
        # if QT_CONFIG(tooltip)
        self.in_Kmesh.setToolTip(
            QCoreApplication.translate("SSimu", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.in_Kmesh.setText(
            QCoreApplication.translate("SSimu", u"Mesh fineness factor:", None)
        )
        # if QT_CONFIG(tooltip)
        self.lf_Kmesh.setToolTip(
            QCoreApplication.translate("SSimu", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.lf_Kmesh.setText(QCoreApplication.translate("SSimu", u"1", None))
        # if QT_CONFIG(tooltip)
        self.in_nb_worker.setToolTip(
            QCoreApplication.translate("SSimu", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.in_nb_worker.setText(
            QCoreApplication.translate("SSimu", u"Number of workers:", None)
        )
        self.g_out.setTitle(QCoreApplication.translate("SSimu", u"Output", None))
        self.in_name.setText(QCoreApplication.translate("SSimu", u"Simu name:", None))
        self.is_losses.setText(
            QCoreApplication.translate("SSimu", u"Compute core and Joule losses", None)
        )
        self.is_mesh_sol.setText(
            QCoreApplication.translate("SSimu", u"Save Mesh Solution", None)
        )
        self.b_previous.setText(QCoreApplication.translate("SSimu", u"Previous", None))
        self.b_next.setText(QCoreApplication.translate("SSimu", u"Run", None))

    # retranslateUi
