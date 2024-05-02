from qtpy.QtWidgets import QWidget

from .....Classes.ImportGenVectLin import ImportGenVectLin
from .....GUI.Tools.WImport.WImportLinspace.Ui_WImportLinspace import Ui_WImportLinspace
from qtpy.QtCore import Qt
from qtpy.QtCore import Signal


class WImportLinspace(Ui_WImportLinspace, QWidget):
    import_name = "Define as Linspace"
    import_type = ImportGenVectLin
    saveNeeded = Signal()
    dataTypeChanged = Signal()

    def __init__(self, parent=None, data=None, plot_title="", expected_shape=None):
        """Initialization of the widget

        Parameters
        ----------
        data : ImportGenVectLin
            Data import to define
        plot_title : str
            Name of the imported data
        expected_shape : list
            List to enforce a shape, [None, 2] enforce 2D matrix with 2 columns
        """
        QWidget.__init__(self, parent=parent)
        self.setupUi(self)

        if data is None:
            self.data = ImportGenVectLin()
        else:
            self.data = data
        self.plot_title = plot_title
        self.expected_shape = expected_shape
        self.update()

        # Connect the slot/signal
        self.lf_start.editingFinished.connect(self.set_start)
        self.lf_stop.editingFinished.connect(self.set_stop)
        self.si_N.editingFinished.connect(self.set_N)
        self.is_end.toggled.connect(self.set_is_end)
        self.c_type_lin.currentIndexChanged.connect(self.set_type_lin)

    def update(self):
        """Fill the widget with the current value of the data"""
        self.c_type_lin.setCurrentIndex(0)  # Start, Stop, N
        self.set_type_lin()
        self.lf_start.setValue(self.data.start)
        self.lf_stop.setValue(self.data.stop)
        if self.data.num is None:
            self.data.num = 100
        self.si_N.setValue(self.data.num)
        if self.data.endpoint:
            self.is_end.setCheckState(Qt.Checked)
        else:
            self.is_end.setCheckState(Qt.Unchecked)

    def set_type_lin(self):
        if self.c_type_lin.currentIndex() == 0:
            self.in_N.show()
            self.si_N.show()
            self.in_step.hide()
            self.lf_step.hide()
        else:
            self.in_N.hide()
            self.si_N.hide()
            self.in_step.show()
            self.lf_step.show()

    def set_start(self):
        """Change the value according to the widget"""
        self.data.start = self.lf_start.value()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_stop(self):
        """Change the value according to the widget"""
        self.data.stop = self.lf_stop.value()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_N(self):
        """Change the value according to the widget"""
        self.data.num = self.si_N.value()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_is_end(self, is_checked):
        """Signal to update the value of is_internal according to the widget

        Parameters
        ----------
        self : WImportLinspace
            A WImportLinspace object
        is_checked : bool
            State of is_internal
        """

        self.data.endpoint = is_checked
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()
