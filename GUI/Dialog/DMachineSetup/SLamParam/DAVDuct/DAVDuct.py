# -*- coding: utf-8 -*-


from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QMessageBox, QSpinBox, QTableWidgetItem

from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.GUI.Dialog.DMachineSetup.SLamParam.DAVDuct.Ui_DAVDuct import Ui_DAVDuct
from pyleecan.GUI.Dialog.DMachineSetup.SLamParam.DAVDuct.WVent.WVent import WVent


class DAVDuct(Ui_DAVDuct, QDialog):
    """Dialog to setup the ventilations
    """

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
        self.setupUi(self)

        self.obj = lamination  # Current object
        self.lam = Lamination(
            init_dict=Lamination.as_dict(lamination)
        )  # Copy to modify

        # Init the GUI
        if len(self.lam.axial_vent) == 0:  # No vent => init circle
            self.lam.axial_vent.append(VentilationCirc())
            self.lam.axial_vent[0]._set_None()

        self.tab_vent.clear()
        for vent in self.lam.axial_vent:
            self.s_add(vent)
        self.tab_vent.setCurrentIndex(0)

        # Set Help URL
        self.b_help.url = "https://eomys.com/produits/manatee/howtos/article/"
        self.b_help.url += "how-to-add-ventilation-ducts"

        self.b_new.clicked.connect(self.s_add)
        self.b_remove.clicked.connect(self.s_remove)
        self.b_plot.clicked.connect(self.plot)
        self.b_cancel.clicked.connect(self.reject)
        self.b_ok.clicked.connect(self.valid_vent)

    def s_add(self, vent=False):
        """Signal to add a new hole

        Parameters
        ----------
        self : DAVDuct
            A DAVDuct widget
        vent : Ventilation
            The ventilation to init the GUI with
        """
        # Create a new hole if needed
        if type(vent) is bool:
            # Default Hole is Circular
            vent_obj = VentilationCirc()
            vent_obj._set_None()
            self.lam.axial_vent.append(vent_obj)
            index = len(self.lam.axial_vent) - 1
        else:
            index = self.lam.axial_vent.index(vent)
        tab = WVent(self.lam, index=index)
        self.tab_vent.addTab(tab, "Vent " + str(index + 1))

    def s_remove(self):
        """Signal to remove the last hole

        Parameters
        ----------
        self : DAVDuct
            a DAVDuct object
        """
        if len(self.lam.axial_vent) > 1:
            self.tab_vent.removeTab(len(self.lam.axial_vent) - 1)
            self.lam.axial_vent.pop(-1)

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
