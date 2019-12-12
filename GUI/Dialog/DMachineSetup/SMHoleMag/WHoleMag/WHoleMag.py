# -*- coding: utf-8 -*-
"""@package pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.WHoleMag
Buried Slot Setup Page
@date Created on Wed Jul 15 14:14:29 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QWidget

from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM50.PHoleM50 import PHoleM50
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM51.PHoleM51 import PHoleM51
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM52.PHoleM52 import PHoleM52
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM53.PHoleM53 import PHoleM53
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM54.PHoleM54 import PHoleM54
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.WHoleMag.Ui_WHoleMag import Ui_WHoleMag


class WHoleMag(Ui_WHoleMag, QWidget):
    """Widget to Setup a single Hole in a list
    """

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = pyqtSignal()

    def __init__(self, lam, is_mag, index):
        """Initialize the GUI according to lamination

        Parameters
        ----------
        self : WHoleMag
            A WHoleMag object
        lam : LamHole
            The lamination to edit
        is_mag : bool
            False: no magnet in the Hole (for the SyRM)
        index : int
            Index of the hole to edit
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        self.is_stator = False
        self.obj = lam
        self.index = index
        self.is_mag = is_mag

        # Adapt the GUI to the current machine
        if is_mag:  # IPMSM
            self.wid_list = [PHoleM50, PHoleM51, PHoleM52, PHoleM53]
        else:  # SyRM
            self.wid_list = [PHoleM50, PHoleM51, PHoleM52, PHoleM53, PHoleM54]
        self.type_list = [wid.hole_type for wid in self.wid_list]
        self.name_list = [wid.hole_name for wid in self.wid_list]

        # Avoid erase all the parameters when navigating though the holes
        self.previous_hole = dict()
        for hole_type in self.type_list:
            self.previous_hole[hole_type] = None

        # Fill the combobox with the available hole
        self.c_hole_type.clear()
        for hole in self.name_list:
            self.c_hole_type.addItem(hole)
        self.c_hole_type.setCurrentIndex(self.type_list.index(type(lam.hole[index])))

        # Regenerate the pages with the new values
        self.w_hole.setParent(None)
        self.w_hole = self.wid_list[self.c_hole_type.currentIndex()](lam.hole[index])
        # Refresh the GUI
        self.main_layout.removeWidget(self.w_hole)
        self.main_layout.insertWidget(1, self.w_hole)

        # Connect the slot
        self.c_hole_type.currentIndexChanged.connect(self.set_hole_type)

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup
        """
        self.saveNeeded.emit()

    def set_hole_type(self, c_index):
        """Initialize self.obj with the hole corresponding to index

        Parameters
        ----------
        self : WHoleMag
            A WHoleMag object
        c_index : int
            Index of the selected hole type in the combobox
        """

        # Save the hole
        hole = self.obj.hole[self.index]
        self.previous_hole[type(hole)] = hole

        # Call the corresponding constructor
        Zh = hole.Zh
        if self.is_mag:  # IPMSM machine
            magnet = hole.magnet_0
        if self.previous_hole[self.type_list[c_index]] is None:
            # No previous hole of this type
            self.obj.hole[self.index] = self.type_list[c_index]()
            self.obj.hole[self.index]._set_None()  # No default value
            self.obj.hole[self.index].Zh = Zh
            if self.is_mag:  # IPMSM
                self.obj.hole[self.index].magnet_0 = magnet
            elif self.obj.hole[self.index].has_magnet():  # SyRM
                self.obj.hole[self.index].remove_magnet()
        else:  # Load the previous hole of this type
            self.obj.hole[self.index] = self.previous_hole[self.type_list[c_index]]

        # Update the GUI
        self.w_hole.setParent(None)
        self.w_hole = self.wid_list[c_index](self.obj.hole[self.index])
        self.w_hole.saveNeeded.connect(self.emit_save)
        # Refresh the GUI
        self.main_layout.removeWidget(self.w_hole)
        self.main_layout.insertWidget(1, self.w_hole)

        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def check(self):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        self : WHoleMag
            A WHoleMag widget

        Returns
        -------
        error : str
            Error message (return None if no error)
        """

        return self.w_hole.check()
