# -*- coding: utf-8 -*-

# File generated according to SSimu.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .....GUI.Tools.FloatEdit import FloatEdit
from .....GUI.Tools.WPathSelector.WPathSelector import WPathSelector

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SSimu(object):
    def setupUi(self, SSimu):
        if not SSimu.objectName():
            SSimu.setObjectName(u"SSimu")
        SSimu.resize(889, 550)
        SSimu.setMinimumSize(QSize(650, 550))
        self.verticalLayout_4 = QVBoxLayout(SSimu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(SSimu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(
            QPixmap(u":/images/images/MachineSetup/MachineType/machine_SynRM.png")
        )
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.g_OP = QGroupBox(SSimu)
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
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unit_N0.sizePolicy().hasHeightForWidth())
        self.unit_N0.setSizePolicy(sizePolicy)

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
        sizePolicy.setHeightForWidth(self.unit_I1.sizePolicy().hasHeightForWidth())
        self.unit_I1.setSizePolicy(sizePolicy)

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
        sizePolicy.setHeightForWidth(self.unit_I2.sizePolicy().hasHeightForWidth())
        self.unit_I2.setSizePolicy(sizePolicy)

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
        sizePolicy.setHeightForWidth(self.unit_I3.sizePolicy().hasHeightForWidth())
        self.unit_I3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.unit_I3, 3, 2, 1, 1)

        self.in_Tmag = QLabel(self.g_OP)
        self.in_Tmag.setObjectName(u"in_Tmag")
        self.in_Tmag.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.in_Tmag, 4, 0, 1, 1)

        self.lf_Tmag = FloatEdit(self.g_OP)
        self.lf_Tmag.setObjectName(u"lf_Tmag")
        self.lf_Tmag.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.lf_Tmag, 4, 1, 1, 1)

        self.unit_Tmag = QLabel(self.g_OP)
        self.unit_Tmag.setObjectName(u"unit_Tmag")
        sizePolicy.setHeightForWidth(self.unit_Tmag.sizePolicy().hasHeightForWidth())
        self.unit_Tmag.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.unit_Tmag, 4, 2, 1, 1)

        self.verticalLayout_3.addWidget(self.g_OP)

        self.g_mag = QGroupBox(SSimu)
        self.g_mag.setObjectName(u"g_mag")
        self.verticalLayout_2 = QVBoxLayout(self.g_mag)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.in_Na_tot = QLabel(self.g_mag)
        self.in_Na_tot.setObjectName(u"in_Na_tot")
        self.in_Na_tot.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.in_Na_tot, 0, 0, 1, 1)

        self.si_Na_tot = QSpinBox(self.g_mag)
        self.si_Na_tot.setObjectName(u"si_Na_tot")

        self.gridLayout_2.addWidget(self.si_Na_tot, 0, 1, 1, 1)

        self.is_per_a = QCheckBox(self.g_mag)
        self.is_per_a.setObjectName(u"is_per_a")

        self.gridLayout_2.addWidget(self.is_per_a, 0, 2, 1, 1)

        self.in_Nt_tot = QLabel(self.g_mag)
        self.in_Nt_tot.setObjectName(u"in_Nt_tot")
        self.in_Nt_tot.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.in_Nt_tot, 1, 0, 1, 1)

        self.si_Nt_tot = QSpinBox(self.g_mag)
        self.si_Nt_tot.setObjectName(u"si_Nt_tot")

        self.gridLayout_2.addWidget(self.si_Nt_tot, 1, 1, 1, 1)

        self.is_per_t = QCheckBox(self.g_mag)
        self.is_per_t.setObjectName(u"is_per_t")

        self.gridLayout_2.addWidget(self.is_per_t, 1, 2, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.in_Kmesh = QLabel(self.g_mag)
        self.in_Kmesh.setObjectName(u"in_Kmesh")
        self.in_Kmesh.setMinimumSize(QSize(0, 0))

        self.gridLayout_3.addWidget(self.in_Kmesh, 0, 0, 1, 1)

        self.lf_Kmesh = FloatEdit(self.g_mag)
        self.lf_Kmesh.setObjectName(u"lf_Kmesh")
        self.lf_Kmesh.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.lf_Kmesh, 0, 1, 1, 1)

        self.in_nb_worker = QLabel(self.g_mag)
        self.in_nb_worker.setObjectName(u"in_nb_worker")
        self.in_nb_worker.setMinimumSize(QSize(0, 0))

        self.gridLayout_3.addWidget(self.in_nb_worker, 1, 0, 1, 1)

        self.si_nb_worker = QSpinBox(self.g_mag)
        self.si_nb_worker.setObjectName(u"si_nb_worker")

        self.gridLayout_3.addWidget(self.si_nb_worker, 1, 1, 1, 1)

        self.horizontalLayout.addLayout(self.gridLayout_3)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_3.addWidget(self.g_mag)

        self.g_out = QGroupBox(SSimu)
        self.g_out.setObjectName(u"g_out")
        self.verticalLayout = QVBoxLayout(self.g_out)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.w_path_result = WPathSelector(self.g_out)
        self.w_path_result.setObjectName(u"w_path_result")
        sizePolicy.setHeightForWidth(
            self.w_path_result.sizePolicy().hasHeightForWidth()
        )
        self.w_path_result.setSizePolicy(sizePolicy)
        self.w_path_result.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.w_path_result)

        self.is_losses = QCheckBox(self.g_out)
        self.is_losses.setObjectName(u"is_losses")

        self.verticalLayout.addWidget(self.is_losses)

        self.is_mesh_sol = QCheckBox(self.g_out)
        self.is_mesh_sol.setObjectName(u"is_mesh_sol")

        self.verticalLayout.addWidget(self.is_mesh_sol)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_3.addWidget(self.g_out)

        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

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
        self.label_2.setText("")
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
        self.in_Tmag.setToolTip(
            QCoreApplication.translate("SSimu", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.in_Tmag.setText(QCoreApplication.translate("SSimu", u"Tmag", None))
        # if QT_CONFIG(tooltip)
        self.lf_Tmag.setToolTip(
            QCoreApplication.translate("SSimu", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.lf_Tmag.setText(QCoreApplication.translate("SSimu", u"20", None))
        self.unit_Tmag.setText(QCoreApplication.translate("SSimu", u"[degC]", None))
        self.g_mag.setTitle(
            QCoreApplication.translate("SSimu", u"Magnetic Model", None)
        )
        # if QT_CONFIG(tooltip)
        self.in_Na_tot.setToolTip(
            QCoreApplication.translate("SSimu", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.in_Na_tot.setText(
            QCoreApplication.translate("SSimu", u"Angular discretization:", None)
        )
        self.is_per_a.setText(
            QCoreApplication.translate("SSimu", u"Angular periodicity", None)
        )
        # if QT_CONFIG(tooltip)
        self.in_Nt_tot.setToolTip(
            QCoreApplication.translate("SSimu", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.in_Nt_tot.setText(
            QCoreApplication.translate("SSimu", u"Time discretization:", None)
        )
        self.is_per_t.setText(
            QCoreApplication.translate("SSimu", u"Time periodicity", None)
        )
        # if QT_CONFIG(tooltip)
        self.in_Kmesh.setToolTip(
            QCoreApplication.translate("SSimu", u"Stator external radius", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.in_Kmesh.setText(
            QCoreApplication.translate("SSimu", u"Mesh Fineness", None)
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
            QCoreApplication.translate("SSimu", u"Nb worker", None)
        )
        self.g_out.setTitle(QCoreApplication.translate("SSimu", u"Results", None))
        self.is_losses.setText(
            QCoreApplication.translate("SSimu", u"Compute Losses", None)
        )
        self.is_mesh_sol.setText(
            QCoreApplication.translate("SSimu", u"Save Mesh Solution", None)
        )
        self.b_previous.setText(QCoreApplication.translate("SSimu", u"Previous", None))
        self.b_next.setText(QCoreApplication.translate("SSimu", u"Run", None))

    # retranslateUi
