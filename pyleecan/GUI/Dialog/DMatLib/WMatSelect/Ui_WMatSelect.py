# -*- coding: utf-8 -*-

# File generated according to WMatSelect.ui
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
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QWidget,
)
from pyleecan.GUI.Resources import pyleecan_rc


class Ui_WMatSelect(object):
    def setupUi(self, WMatSelect):
        if not WMatSelect.objectName():
            WMatSelect.setObjectName("WMatSelect")
        WMatSelect.resize(738, 40)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WMatSelect.sizePolicy().hasHeightForWidth())
        WMatSelect.setSizePolicy(sizePolicy)
        WMatSelect.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(WMatSelect)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 2, 4, 2)
        self.in_mat_type = QLabel(WMatSelect)
        self.in_mat_type.setObjectName("in_mat_type")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.in_mat_type.sizePolicy().hasHeightForWidth())
        self.in_mat_type.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.in_mat_type)

        self.c_mat_type = QComboBox(WMatSelect)
        self.c_mat_type.addItem("")
        self.c_mat_type.addItem("")
        self.c_mat_type.addItem("")
        self.c_mat_type.setObjectName("c_mat_type")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.c_mat_type.sizePolicy().hasHeightForWidth())
        self.c_mat_type.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.c_mat_type)

        self.b_matlib = QPushButton(WMatSelect)
        self.b_matlib.setObjectName("b_matlib")

        self.horizontalLayout.addWidget(self.b_matlib)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        QWidget.setTabOrder(self.c_mat_type, self.b_matlib)

        self.retranslateUi(WMatSelect)

        QMetaObject.connectSlotsByName(WMatSelect)

    # setupUi

    def retranslateUi(self, WMatSelect):
        WMatSelect.setWindowTitle(
            QCoreApplication.translate("WMatSelect", "Form", None)
        )
        self.in_mat_type.setText(
            QCoreApplication.translate("WMatSelect", "mat_type :", None)
        )
        self.c_mat_type.setItemText(
            0, QCoreApplication.translate("WMatSelect", "M400-50A", None)
        )
        self.c_mat_type.setItemText(
            1, QCoreApplication.translate("WMatSelect", "M350-50A", None)
        )
        self.c_mat_type.setItemText(
            2, QCoreApplication.translate("WMatSelect", "M330-35A", None)
        )

        self.b_matlib.setText(
            QCoreApplication.translate("WMatSelect", "Edit Materials", None)
        )

    # retranslateUi
