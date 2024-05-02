# -*- coding: utf-8 -*-


from qtpy.QtCore import Signal, Qt
from qtpy.QtWidgets import QWidget, QApplication

from ......GUI.Dialog.DMachineSetup.DAVDuct.PVentCirc.PVentCirc import (
    PVentCirc,
)
from ......GUI.Dialog.DMachineSetup.DAVDuct.PVentPolar.PVentPolar import (
    PVentPolar,
)
from ......GUI.Dialog.DMachineSetup.DAVDuct.PVentTrap.PVentTrap import (
    PVentTrap,
)
from ......GUI.Dialog.DMachineSetup.DAVDuct.PVentUD.PVentUD import (
    PVentUD,
)
from ......GUI.Dialog.DMachineSetup.DAVDuct.WVent.Gen_WVent import Gen_WVent
from ......Functions.GUI.log_error import log_error
from numpy import pi

# List to convert index of combobox to slot type
PAGE_INDEX = [PVentCirc, PVentTrap, PVentPolar, PVentUD]
INIT_INDEX = [wid.hole_type for wid in PAGE_INDEX]
HOLE_NAME = [wid.hole_name for wid in PAGE_INDEX]


class WVent(Gen_WVent, QWidget):
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
        self.is_test = False  # To skip show fig in tests

        # Fill the combobox with the available slot
        self.c_vent_type.clear()
        for hole in HOLE_NAME:
            self.c_vent_type.addItem(hole)
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
        # Alpha0 setup
        if lam.axial_vent[index].Alpha0 is None:
            lam.axial_vent[index].Alpha0 = 0
        self.lf_Alpha0.setValue(lam.axial_vent[index].Alpha0)  # Default unit is [rad]
        # Refresh the GUI
        self.main_layout.removeWidget(self.w_vent)
        self.main_layout.insertWidget(1, self.w_vent)

        # Connect the slot/signel
        self.c_vent_type.currentIndexChanged.connect(self.set_vent_type)
        self.lf_Alpha0.editingFinished.connect(self.set_Alpha0)
        self.c_Alpha0_unit.currentIndexChanged.connect(self.set_Alpha0_unit)

    def set_vent_type(self, c_index):
        """Initialize self.obj with the vent corresponding to index

        Parameters
        ----------
        self : WVent
            A WVent object
        c_index : index
            Index of the selected vent type in the combobox
        """
        try:
            # Save the vent
            vent = self.obj.axial_vent[self.index]
            self.previous_vent[type(vent)] = vent

            # Call the corresponding constructor
            if self.previous_vent[INIT_INDEX[c_index]] is None:
                # No previous vent of this type
                self.obj.axial_vent[self.index] = INIT_INDEX[c_index]()
                self.obj.axial_vent[self.index]._set_None()  # No default value
            else:  # Load the previous vent of this type
                self.obj.axial_vent[self.index] = self.previous_vent[
                    INIT_INDEX[c_index]
                ]

            self.set_Alpha0()  # Take unit into account
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
        except Exception as e:
            log_error(
                self,
                "Error while opening corresponding cooling duct widget:\n" + str(e),
            )

    def set_Alpha0(self):
        """Signal to update the value of Alpha0 according to the line edit

        Parameters
        ----------
        self : WVent
            A WVent object
        """
        vent = self.obj.axial_vent[self.index]
        if self.lf_Alpha0.value() is None:
            vent.Alpha0 = 0
        elif self.c_Alpha0_unit.currentText() == "[rad]":
            vent.Alpha0 = self.lf_Alpha0.value()
        else:
            vent.Alpha0 = self.lf_Alpha0.value() * pi / 180
        # Update lamination plot for UD
        if isinstance(self.w_vent, PVentUD):
            self.w_vent.update_graph()

    def set_Alpha0_unit(self):
        """Change current unit of Alpha0"""
        if self.c_Alpha0_unit.currentText() == "[rad]":
            self.lf_Alpha0.validator().setTop(6.29)
        else:
            self.lf_Alpha0.validator().setTop(360)
        self.set_Alpha0()

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
