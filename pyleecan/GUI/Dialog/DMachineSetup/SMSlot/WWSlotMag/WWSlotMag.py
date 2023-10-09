from PySide2.QtCore import QSize, Signal
from PySide2.QtWidgets import (
    QGroupBox,
    QLabel,
    QVBoxLayout,
    QWidget,
    QComboBox,
    QPushButton,
    QListView,
)

from .....Dialog.DMatLib.WMatSelect.WMatSelectV import WMatSelectV

from ..... import gui_option


class WWSlotMag(QGroupBox):
    """Setup of QGroupBox for output for Winding Slot"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()

    def __init__(self, parent=None):
        """Initialize the widget"""

        QGroupBox.__init__(self, parent)

        # Set main widget
        self.setTitle(self.tr("Magnet"))
        self.setMinimumSize(QSize(200, 0))
        self.setObjectName("g_magnet")
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName("layout")

        # The widget is composed object in a vertical layout
        self.in_type_magnetization = QLabel(self)
        self.in_type_magnetization.setObjectName("type_magnetization")
        self.layout.addWidget(self.in_type_magnetization)
        self.in_type_magnetization.setText("Magnetization Type")

        self.c_type_magnetization = QComboBox(self)
        self.c_type_magnetization.setObjectName("c_type_magnetization")
        self.layout.addWidget(self.c_type_magnetization)

        self.c_type_magnetization.addItem("Radial")
        self.c_type_magnetization.addItem("Parallel")
        self.c_type_magnetization.addItem("HallBach")

        self.w_mat = WMatSelectV(self)
        self.w_mat.setObjectName("w_mat")
        self.layout.addWidget(self.w_mat)
