# -*- coding: utf-8 -*-

# File generated according to SMachineDimension.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from .....GUI.Tools.FloatEdit import FloatEdit
from .....GUI.Dialog.DMatLib.WMatSelect.WMatSelectV import WMatSelectV

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SMachineDimension(object):
    def setupUi(self, SMachineDimension):
        if not SMachineDimension.objectName():
            SMachineDimension.setObjectName("SMachineDimension")
        SMachineDimension.resize(1062, 679)
        SMachineDimension.setMinimumSize(QSize(650, 550))
        self.verticalLayout_3 = QVBoxLayout(SMachineDimension)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.img_machine = QLabel(SMachineDimension)
        self.img_machine.setObjectName("img_machine")
        self.img_machine.setMinimumSize(QSize(0, 0))
        self.img_machine.setMaximumSize(QSize(16777215, 16777215))
        self.img_machine.setPixmap(
            QPixmap(
                ":/images/images/MachineSetup/MachineDimension/Dimension_Shaft_Rotor_Stator.png"
            )
        )
        self.img_machine.setScaledContents(False)
        self.img_machine.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.img_machine)

        self.scrollArea = QScrollArea(SMachineDimension)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 616))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.g_stator = QGroupBox(self.scrollAreaWidgetContents)
        self.g_stator.setObjectName("g_stator")
        self.g_stator.setMinimumSize(QSize(150, 0))
        self.g_stator.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(self.g_stator)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.in_SRext = QLabel(self.g_stator)
        self.in_SRext.setObjectName("in_SRext")
        self.in_SRext.setMinimumSize(QSize(30, 0))

        self.gridLayout_2.addWidget(self.in_SRext, 0, 0, 1, 1)

        self.lf_SRext = FloatEdit(self.g_stator)
        self.lf_SRext.setObjectName("lf_SRext")
        self.lf_SRext.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lf_SRext, 0, 1, 1, 1)

        self.unit_SRext = QLabel(self.g_stator)
        self.unit_SRext.setObjectName("unit_SRext")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unit_SRext.sizePolicy().hasHeightForWidth())
        self.unit_SRext.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.unit_SRext, 0, 2, 1, 1)

        self.in_SRint = QLabel(self.g_stator)
        self.in_SRint.setObjectName("in_SRint")
        self.in_SRint.setMinimumSize(QSize(30, 0))

        self.gridLayout_2.addWidget(self.in_SRint, 1, 0, 1, 1)

        self.lf_SRint = FloatEdit(self.g_stator)
        self.lf_SRint.setObjectName("lf_SRint")
        self.lf_SRint.setMaximumSize(QSize(100, 100))

        self.gridLayout_2.addWidget(self.lf_SRint, 1, 1, 1, 1)

        self.unit_SRint = QLabel(self.g_stator)
        self.unit_SRint.setObjectName("unit_SRint")
        sizePolicy.setHeightForWidth(self.unit_SRint.sizePolicy().hasHeightForWidth())
        self.unit_SRint.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.unit_SRint, 1, 2, 1, 1)

        self.verticalLayout_4.addWidget(self.g_stator)

        self.g_rotor = QGroupBox(self.scrollAreaWidgetContents)
        self.g_rotor.setObjectName("g_rotor")
        self.gridLayout_3 = QGridLayout(self.g_rotor)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.in_RRext = QLabel(self.g_rotor)
        self.in_RRext.setObjectName("in_RRext")
        self.in_RRext.setMinimumSize(QSize(30, 0))

        self.gridLayout_3.addWidget(self.in_RRext, 0, 0, 1, 1)

        self.lf_RRext = FloatEdit(self.g_rotor)
        self.lf_RRext.setObjectName("lf_RRext")
        self.lf_RRext.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.lf_RRext, 0, 1, 1, 1)

        self.unit_RRext = QLabel(self.g_rotor)
        self.unit_RRext.setObjectName("unit_RRext")
        sizePolicy.setHeightForWidth(self.unit_RRext.sizePolicy().hasHeightForWidth())
        self.unit_RRext.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.unit_RRext, 0, 2, 1, 1)

        self.in_RRint = QLabel(self.g_rotor)
        self.in_RRint.setObjectName("in_RRint")
        self.in_RRint.setMinimumSize(QSize(30, 0))

        self.gridLayout_3.addWidget(self.in_RRint, 1, 0, 1, 1)

        self.lf_RRint = FloatEdit(self.g_rotor)
        self.lf_RRint.setObjectName("lf_RRint")
        self.lf_RRint.setMaximumSize(QSize(100, 100))

        self.gridLayout_3.addWidget(self.lf_RRint, 1, 1, 1, 1)

        self.unit_RRint = QLabel(self.g_rotor)
        self.unit_RRint.setObjectName("unit_RRint")
        sizePolicy.setHeightForWidth(self.unit_RRint.sizePolicy().hasHeightForWidth())
        self.unit_RRint.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.unit_RRint, 1, 2, 1, 1)

        self.verticalLayout_4.addWidget(self.g_rotor)

        self.out_airgap = QLabel(self.scrollAreaWidgetContents)
        self.out_airgap.setObjectName("out_airgap")

        self.verticalLayout_4.addWidget(self.out_airgap)

        self.g_shaft = QGroupBox(self.scrollAreaWidgetContents)
        self.g_shaft.setObjectName("g_shaft")
        self.g_shaft.setMinimumSize(QSize(0, 0))
        self.g_shaft.setCheckable(True)
        self.verticalLayout = QVBoxLayout(self.g_shaft)
        self.verticalLayout.setObjectName("verticalLayout")
        self.w_mat_0 = WMatSelectV(self.g_shaft)
        self.w_mat_0.setObjectName("w_mat_0")
        self.w_mat_0.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.w_mat_0)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.in_Lshaft = QLabel(self.g_shaft)
        self.in_Lshaft.setObjectName("in_Lshaft")
        self.in_Lshaft.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_3.addWidget(self.in_Lshaft)

        self.lf_Lshaft = FloatEdit(self.g_shaft)
        self.lf_Lshaft.setObjectName("lf_Lshaft")
        self.lf_Lshaft.setMaximumSize(QSize(100, 100))

        self.horizontalLayout_3.addWidget(self.lf_Lshaft)

        self.unit_Lshaft = QLabel(self.g_shaft)
        self.unit_Lshaft.setObjectName("unit_Lshaft")
        sizePolicy.setHeightForWidth(self.unit_Lshaft.sizePolicy().hasHeightForWidth())
        self.unit_Lshaft.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.unit_Lshaft)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.out_Drsh = QLabel(self.g_shaft)
        self.out_Drsh.setObjectName("out_Drsh")

        self.verticalLayout.addWidget(self.out_Drsh)

        self.verticalLayout_4.addWidget(self.g_shaft)

        self.g_frame = QGroupBox(self.scrollAreaWidgetContents)
        self.g_frame.setObjectName("g_frame")
        self.g_frame.setCheckable(True)
        self.verticalLayout_2 = QVBoxLayout(self.g_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.w_mat_1 = WMatSelectV(self.g_frame)
        self.w_mat_1.setObjectName("w_mat_1")
        self.w_mat_1.setMinimumSize(QSize(100, 0))

        self.verticalLayout_2.addWidget(self.w_mat_1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lf_Lfra = FloatEdit(self.g_frame)
        self.lf_Lfra.setObjectName("lf_Lfra")
        self.lf_Lfra.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.lf_Lfra, 1, 1, 1, 1)

        self.in_Lfra = QLabel(self.g_frame)
        self.in_Lfra.setObjectName("in_Lfra")

        self.gridLayout.addWidget(self.in_Lfra, 1, 0, 1, 1)

        self.lf_Wfra = FloatEdit(self.g_frame)
        self.lf_Wfra.setObjectName("lf_Wfra")
        self.lf_Wfra.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.lf_Wfra, 0, 1, 1, 1)

        self.in_Wfra = QLabel(self.g_frame)
        self.in_Wfra.setObjectName("in_Wfra")

        self.gridLayout.addWidget(self.in_Wfra, 0, 0, 1, 1)

        self.unit_Lfra = QLabel(self.g_frame)
        self.unit_Lfra.setObjectName("unit_Lfra")

        self.gridLayout.addWidget(self.unit_Lfra, 1, 2, 1, 1)

        self.unit_Wfra = QLabel(self.g_frame)
        self.unit_Wfra.setObjectName("unit_Wfra")

        self.gridLayout.addWidget(self.unit_Wfra, 0, 2, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout_4.addWidget(self.g_frame)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.b_previous = QPushButton(SMachineDimension)
        self.b_previous.setObjectName("b_previous")

        self.horizontalLayout.addWidget(self.b_previous)

        self.b_next = QPushButton(SMachineDimension)
        self.b_next.setObjectName("b_next")

        self.horizontalLayout.addWidget(self.b_next)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.scrollArea, self.lf_SRext)
        QWidget.setTabOrder(self.lf_SRext, self.lf_SRint)
        QWidget.setTabOrder(self.lf_SRint, self.lf_RRext)
        QWidget.setTabOrder(self.lf_RRext, self.lf_RRint)
        QWidget.setTabOrder(self.lf_RRint, self.g_shaft)
        QWidget.setTabOrder(self.g_shaft, self.lf_Lshaft)
        QWidget.setTabOrder(self.lf_Lshaft, self.g_frame)
        QWidget.setTabOrder(self.g_frame, self.lf_Wfra)
        QWidget.setTabOrder(self.lf_Wfra, self.lf_Lfra)
        QWidget.setTabOrder(self.lf_Lfra, self.b_previous)
        QWidget.setTabOrder(self.b_previous, self.b_next)

        self.retranslateUi(SMachineDimension)

        QMetaObject.connectSlotsByName(SMachineDimension)

    # setupUi

    def retranslateUi(self, SMachineDimension):
        SMachineDimension.setWindowTitle(
            QCoreApplication.translate("SMachineDimension", "Form", None)
        )
        self.img_machine.setText("")
        self.g_stator.setTitle(
            QCoreApplication.translate("SMachineDimension", "Stator", None)
        )
        # if QT_CONFIG(tooltip)
        self.in_SRext.setToolTip(
            QCoreApplication.translate(
                "SMachineDimension", "Stator external radius", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.in_SRext.setText(
            QCoreApplication.translate("SMachineDimension", "Rext", None)
        )
        # if QT_CONFIG(tooltip)
        self.lf_SRext.setToolTip(
            QCoreApplication.translate(
                "SMachineDimension", "Stator external radius", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.unit_SRext.setText(
            QCoreApplication.translate("SMachineDimension", "m", None)
        )
        # if QT_CONFIG(tooltip)
        self.in_SRint.setToolTip(
            QCoreApplication.translate(
                "SMachineDimension", "Stator internal radius", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.in_SRint.setText(
            QCoreApplication.translate("SMachineDimension", "Rint", None)
        )
        # if QT_CONFIG(tooltip)
        self.lf_SRint.setToolTip(
            QCoreApplication.translate(
                "SMachineDimension", "Stator internal radius", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.unit_SRint.setText(
            QCoreApplication.translate("SMachineDimension", "m", None)
        )
        self.g_rotor.setTitle(
            QCoreApplication.translate("SMachineDimension", "Rotor", None)
        )
        # if QT_CONFIG(tooltip)
        self.in_RRext.setToolTip(
            QCoreApplication.translate(
                "SMachineDimension", "Rotor external radius", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.in_RRext.setText(
            QCoreApplication.translate("SMachineDimension", "Rext", None)
        )
        # if QT_CONFIG(tooltip)
        self.lf_RRext.setToolTip(
            QCoreApplication.translate(
                "SMachineDimension", "Rotor external radius", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.unit_RRext.setText(
            QCoreApplication.translate("SMachineDimension", "m", None)
        )
        # if QT_CONFIG(tooltip)
        self.in_RRint.setToolTip(
            QCoreApplication.translate(
                "SMachineDimension", "Rotor internal radius", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.in_RRint.setText(
            QCoreApplication.translate("SMachineDimension", "Rint", None)
        )
        # if QT_CONFIG(tooltip)
        self.lf_RRint.setToolTip(
            QCoreApplication.translate(
                "SMachineDimension", "Rotor internal radius", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.unit_RRint.setText(
            QCoreApplication.translate("SMachineDimension", "m", None)
        )
        # if QT_CONFIG(tooltip)
        self.out_airgap.setToolTip(
            QCoreApplication.translate(
                "SMachineDimension",
                "Magnetic airgap width (distance between stator bore and rotor bore radii)",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.out_airgap.setText(
            QCoreApplication.translate("SMachineDimension", "airgap = ", None)
        )
        self.g_shaft.setTitle(
            QCoreApplication.translate("SMachineDimension", "Shaft", None)
        )
        # if QT_CONFIG(tooltip)
        self.in_Lshaft.setToolTip(
            QCoreApplication.translate("SMachineDimension", "Shaft length", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.in_Lshaft.setText(
            QCoreApplication.translate("SMachineDimension", "Lshaft", None)
        )
        # if QT_CONFIG(tooltip)
        self.lf_Lshaft.setToolTip(
            QCoreApplication.translate("SMachineDimension", "Shaft length", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.unit_Lshaft.setText(
            QCoreApplication.translate("SMachineDimension", "m", None)
        )
        # if QT_CONFIG(tooltip)
        self.out_Drsh.setToolTip(
            QCoreApplication.translate("SMachineDimension", "Shaft Diameter", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.out_Drsh.setText(
            QCoreApplication.translate("SMachineDimension", "Drsh = 2*Rotor.Rint", None)
        )
        self.g_frame.setTitle(
            QCoreApplication.translate("SMachineDimension", "Frame", None)
        )
        # if QT_CONFIG(tooltip)
        self.lf_Lfra.setToolTip(
            QCoreApplication.translate("SMachineDimension", "Frame length", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.lf_Lfra.setWhatsThis(
            QCoreApplication.translate("SMachineDimension", "Frame length", None)
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.in_Lfra.setToolTip(
            QCoreApplication.translate("SMachineDimension", "Frame length", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.in_Lfra.setWhatsThis(
            QCoreApplication.translate("SMachineDimension", "Frame length", None)
        )
        # endif // QT_CONFIG(whatsthis)
        self.in_Lfra.setText(
            QCoreApplication.translate("SMachineDimension", "Lfra", None)
        )
        # if QT_CONFIG(tooltip)
        self.lf_Wfra.setToolTip(
            QCoreApplication.translate("SMachineDimension", "Frame width", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.lf_Wfra.setWhatsThis(
            QCoreApplication.translate("SMachineDimension", "Frame width", None)
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.in_Wfra.setToolTip(
            QCoreApplication.translate("SMachineDimension", "Frame width", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.in_Wfra.setWhatsThis(
            QCoreApplication.translate("SMachineDimension", "Frame width", None)
        )
        # endif // QT_CONFIG(whatsthis)
        self.in_Wfra.setText(
            QCoreApplication.translate("SMachineDimension", "Wfra", None)
        )
        # if QT_CONFIG(tooltip)
        self.unit_Lfra.setToolTip(
            QCoreApplication.translate("SMachineDimension", "Frame length", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.unit_Lfra.setWhatsThis(
            QCoreApplication.translate("SMachineDimension", "Frame length", None)
        )
        # endif // QT_CONFIG(whatsthis)
        self.unit_Lfra.setText(
            QCoreApplication.translate("SMachineDimension", "m", None)
        )
        # if QT_CONFIG(tooltip)
        self.unit_Wfra.setToolTip(
            QCoreApplication.translate("SMachineDimension", "Frame width", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.unit_Wfra.setWhatsThis(
            QCoreApplication.translate("SMachineDimension", "Frame width", None)
        )
        # endif // QT_CONFIG(whatsthis)
        self.unit_Wfra.setText(
            QCoreApplication.translate("SMachineDimension", "m", None)
        )
        self.b_previous.setText(
            QCoreApplication.translate("SMachineDimension", "Previous", None)
        )
        self.b_next.setText(
            QCoreApplication.translate("SMachineDimension", "Next", None)
        )

    # retranslateUi
