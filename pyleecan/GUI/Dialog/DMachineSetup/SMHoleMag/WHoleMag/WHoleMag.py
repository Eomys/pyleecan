# -*- coding: utf-8 -*-


from PySide2.QtCore import Signal
from PySide2.QtWidgets import QMessageBox, QWidget

from ......GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM50.PHoleM50 import PHoleM50
from ......GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM51.PHoleM51 import PHoleM51
from ......GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM52.PHoleM52 import PHoleM52
from ......GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM52R.PHoleM52R import PHoleM52R
from ......GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM53.PHoleM53 import PHoleM53
from ......GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM54.PHoleM54 import PHoleM54
from ......GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM57.PHoleM57 import PHoleM57
from ......GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM58.PHoleM58 import PHoleM58
from ......GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM60.PHoleM60 import PHoleM60
from ......GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM61.PHoleM61 import PHoleM61
from ......GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM62.PHoleM62 import PHoleM62
from ......GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM63.PHoleM63 import PHoleM63
from ......GUI.Dialog.DMachineSetup.SMHoleMag.PHoleMUD.PHoleMUD import PHoleMUD
from ......GUI.Dialog.DMachineSetup.SMHoleMag.WHoleMag.Ui_WHoleMag import Ui_WHoleMag


class WHoleMag(Ui_WHoleMag, QWidget):
    """Widget to Setup a single Hole in a list"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()

    def __init__(self, parent, is_mag, index, material_dict):
        """Initialize the GUI according to lamination

        Parameters
        ----------
        self : WHoleMag
            A WHoleMag object
        parent :
            A parent object containing the lamination (LamHole) to edit
        is_mag : bool
            False: no magnet in the Hole (for the SyRM)
        index : int
            Index of the hole to edit
        material_dict: dict
            Materials dictionary (library + machine)
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        self.is_stator = False
        self.obj = parent.obj
        self.index = index
        self.is_mag = is_mag
        self.parent = parent
        self.material_dict = material_dict

        # Adapt the GUI to the current machine
        if is_mag:  # IPMSM
            self.wid_list = [
                PHoleM50,
                PHoleM51,
                PHoleM52,
                PHoleM52R,
                PHoleM53,
                PHoleM57,
                PHoleM58,
                PHoleM60,
                PHoleM61,
                PHoleM62,
                PHoleM63,
                PHoleMUD,
            ]
        else:  # SyRM
            self.wid_list = [
                PHoleM50,
                PHoleM51,
                PHoleM52,
                PHoleM52R,
                PHoleM53,
                PHoleM54,
                PHoleM57,
                PHoleM58,
                PHoleM60,
                PHoleM61,
                PHoleM62,
                PHoleM63,
                PHoleMUD,
            ]
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
        self.c_hole_type.setCurrentIndex(
            self.type_list.index(type(self.obj.hole[index]))
        )

        # Regenerate the pages with the new values
        self.w_hole.setParent(None)
        self.w_hole = self.wid_list[self.c_hole_type.currentIndex()](
            hole=self.obj.hole[index], material_dict=self.material_dict
        )
        # Refresh the GUI
        self.main_layout.removeWidget(self.w_hole)
        self.main_layout.insertWidget(1, self.w_hole)

        # Connect the slot
        self.c_hole_type.currentIndexChanged.connect(self.set_hole_type)

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
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
        if self.previous_hole[self.type_list[c_index]] is None:
            # No previous hole of this type
            self.obj.hole[self.index] = self.type_list[c_index]()
            self.obj.hole[self.index]._set_None()  # No default value
            self.obj.hole[self.index].Zh = Zh
            if self.is_mag and self.obj.hole[self.index].has_magnet():  # IPMSM
                magnet = hole.get_magnet_by_id(0)
                self.obj.hole[self.index].set_magnet_by_id(0, magnet)
            elif self.obj.hole[self.index].has_magnet():  # SyRM
                self.obj.hole[self.index].remove_magnet()
        else:  # Load the previous hole of this type
            self.obj.hole[self.index] = self.previous_hole[self.type_list[c_index]]

        # Update the GUI
        self.w_hole.setParent(None)
        self.w_hole = self.wid_list[c_index](
            hole=self.obj.hole[self.index], material_dict=self.material_dict
        )
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
