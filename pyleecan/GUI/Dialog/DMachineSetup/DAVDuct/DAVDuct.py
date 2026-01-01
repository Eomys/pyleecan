from qtpy.QtCore import Qt
from qtpy.QtWidgets import QDialog, QMessageBox, QShortcut
from qtpy.QtGui import QKeySequence

from .....Classes.Lamination import Lamination
from .....Classes.VentilationCirc import VentilationCirc
from .....GUI.Dialog.DMachineSetup.DAVDuct.Ui_DAVDuct import Ui_DAVDuct
from .....GUI.Dialog.DMachineSetup.DAVDuct.WVent.WVent import WVent
from .....Functions.Plot.set_plot_gui_icon import set_plot_gui_icon


class DAVDuct(Ui_DAVDuct, QDialog):
    """Dialog to setup the ventilations"""

    def __init__(self, lamination):
        """Initialize the widget according the current lamination

        Parameters
        ----------
        self : DAVDuct
            A DAVDuct widget
        lam : Lamination
            current lamination to edit
        """
        # Build the interface according to the .ui file
        QDialog.__init__(self)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
        self.setupUi(self)

        self.obj = lamination  # Current object
        self.lam = lamination.copy()  # Copy to modify

        # Init the GUI
        if len(self.lam.axial_vent) == 0:  # No vent => init circle
            self.lam.axial_vent.append(VentilationCirc())
            self.lam.axial_vent[0]._set_None()

        self.tab_vent.clear()
        for idx_vent, vent in enumerate(self.lam.axial_vent):
            self.s_add(vent, idx_vent)
        self.tab_vent.setCurrentIndex(0)

        # Set Help URL
        self.b_help.hide()

        self.b_new.clicked.connect(lambda: self.s_add(vent=None, idx_vent=None))
        self.tab_vent.tabCloseRequested.connect(self.s_remove)
        self.b_plot.clicked.connect(self.plot)
        self.b_cancel.clicked.connect(self.reject)
        self.b_ok.clicked.connect(self.valid_vent)

    def keyPressEvent(self, event):
        if event.text() == "\r":
            self.valid_vent()
        event.accept()

    def s_add(self, vent=None, idx_vent=None):
        """Signal to add a new hole

        Parameters
        ----------
        self : DAVDuct
            A DAVDuct widget
        vent : Ventilation
            The ventilation to init the GUI with
        """
        # Create a new hole if needed
        if vent is None:
            # Default Hole is Circular
            vent_obj = VentilationCirc()
            vent_obj._set_None()
            self.lam.axial_vent.append(vent_obj)
            index = len(self.lam.axial_vent) - 1
        else:
            index = idx_vent
        tab = WVent(self.lam, index=index)
        self.tab_vent.addTab(tab, "Set " + str(index + 1))

    def s_remove(self, index):
        """Signal to remove the last hole

        Parameters
        ----------
        self : DAVDuct
            a DAVDuct object
        """
        if len(self.lam.axial_vent) > 1:
            self.tab_vent.removeTab(index)
            self.lam.axial_vent.pop(index)

        self.tab_vent.clear()
        for idx_vent, vent in enumerate(self.lam.axial_vent):
            self.s_add(vent, idx_vent)
        self.tab_vent.setCurrentIndex(0)

    def plot(self):
        """Plot the ventilation ducts according to the table

        Parameters
        ----------
        self : DAVDuct
            a DAVDuct object
        """
        # We have to make sure the hole is right before trying to plot it
        error = self.check()

        if error:  # Error => Display it
            QMessageBox().critical(self, self.tr("Error"), error)
        else:  # No error => Plot the hole (No winding for LamSquirrelCage)
            self.lam.plot()
            set_plot_gui_icon()

    def valid_vent(self):
        """Validate the new ventilation and update the lamination

        Parameters
        ----------
        self : DAVDuct
            a DAVDuct object
        """
        error = self.check()

        if error:  # Error => Display it
            QMessageBox().critical(self, self.tr("Error"), error)
        else:
            self.obj.axial_vent = self.lam.axial_vent
            self.accept()

    def check(self):
        """Check that all the ventilation are correctly set

        Parameters
        ----------
        self : DAVDuct
            a DAVDuct object
        """
        for ii in range(self.tab_vent.count()):
            error = self.tab_vent.widget(ii).check()
            if error is not None:
                return "Vent " + str(ii + 1) + ": " + error
        return None
