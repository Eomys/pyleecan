# -*- coding: utf-8 -*-

# File generated according to PCondType22.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import QApplication, QSizePolicy, QVBoxLayout, QWidget

from ......GUI.Dialog.DMachineSetup.SBar.WBarOut.WBarOut import WBarOut
from ......GUI.Dialog.DMatLib.WMatSelect.WMatSelectV import WMatSelectV


class Ui_PCondType22(object):
    def setupUi(self, PCondType22):
        if not PCondType22.objectName():
            PCondType22.setObjectName("PCondType22")
        PCondType22.resize(460, 124)
        self.verticalLayout = QVBoxLayout(PCondType22)
        self.verticalLayout.setObjectName("verticalLayout")
        self.w_mat = WMatSelectV(PCondType22)
        self.w_mat.setObjectName("w_mat")
        self.w_mat.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.w_mat)

        self.w_out = WBarOut(PCondType22)
        self.w_out.setObjectName("w_out")

        self.verticalLayout.addWidget(self.w_out)

        self.retranslateUi(PCondType22)

        QMetaObject.connectSlotsByName(PCondType22)

    # setupUi

    def retranslateUi(self, PCondType22):
        PCondType22.setWindowTitle(
            QCoreApplication.translate("PCondType22", "Form", None)
        )

    # retranslateUi
