# -*- coding: utf-8 -*-


from PySide2.QtCore import Signal
from PySide2.QtWidgets import QMessageBox, QWidget

from .......Classes.VentilationCirc import VentilationCirc
from .......Classes.VentilationPolar import VentilationPolar
from .......Classes.VentilationTrap import VentilationTrap
from .......GUI.Dialog.DMachineSetup.SLamParam.DAVDuct.PVentCirc.PVentCirc import (
    PVentCirc,
)
from .......GUI.Dialog.DMachineSetup.SLamParam.DAVDuct.PVentPolar.PVentPolar import (
    PVentPolar,
)
from .......GUI.Dialog.DMachineSetup.SLamParam.DAVDuct.PVentTrap.PVentTrap import (
    PVentTrap,
)
from .......GUI.Dialog.DMachineSetup.SLamParam.DAVDuct.WVent.Ui_WVent import Ui_WVent

# List to convert index of combobox to slot type
INIT_INDEX = [VentilationCirc, VentilationTrap, VentilationPolar]
PAGE_INDEX = [PVentCirc, PVentTrap, PVentPolar]


class WVent(Ui_WVent, QWidget):
    """Widget to setup a Ventilation in the list"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()

    def __init__(self, lam, index):
        """Initialize the widget according the current lamination

        Parameters
        ----------
        self : WVent
            A WVent widget
        lam : Lamination
            current lamination to edit
        index : int
            Index of the ventilation in the list to update
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)
        self.obj = lam
        self.index = index

        # Avoid erase all the parameters when navigating though the vents
        self.previous_vent = dict()
        for vent_type in INIT_INDEX:
            self.previous_vent[vent_type] = None

        self.c_vent_type.setCurrentIndex(INIT_INDEX.index(type(lam.axial_vent[index])))
        # Regenerate the pages with the new values
        self.w_vent.setParent(None)
        self.w_vent = PAGE_INDEX[self.c_vent_type.currentIndex()](
            lam=lam, vent=lam.axial_vent[index]
        )
        # Refresh the GUI
        self.main_layout.removeWidget(self.w_vent)
        self.main_layout.insertWidget(1, self.w_vent)

        # Connect the slot/signel
        self.c_vent_type.currentIndexChanged.connect(self.set_vent_type)

    def set_vent_type(self, c_index):
        """Initialize self.obj with the vent corresponding to index

        Parameters
        ----------
        self : WVent
            A WVent object
        c_index : index
            Index of the selected vent type in the combobox
        """

        # Save the vent
        vent = self.obj.axial_vent[self.index]
        self.previous_vent[type(vent)] = vent

        # Call the corresponding constructor
        if self.previous_vent[INIT_INDEX[c_index]] is None:
            # No previous vent of this type
            self.obj.axial_vent[self.index] = INIT_INDEX[c_index]()
            self.obj.axial_vent[self.index]._set_None()  # No default value
        else:  # Load the previous vent of this type
            self.obj.axial_vent[self.index] = self.previous_vent[INIT_INDEX[c_index]]

        # Update the GUI
        self.w_vent.setParent(None)
        self.w_vent = PAGE_INDEX[c_index](
            lam=self.obj, vent=self.obj.axial_vent[self.index]
        )
        # Refresh the GUI
        self.main_layout.removeWidget(self.w_vent)
        self.main_layout.insertWidget(1, self.w_vent)

        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def check(self):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        self : WVent
            A WVent object

        Returns
        -------
        error : str
            Error message (return None if no error)
        """

        return self.w_vent.check()
