# -*- coding: utf-8 -*-

from qtpy.QtCore import Signal
from qtpy.QtWidgets import QWidget

from ......Classes.HoleM54 import HoleM54
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM54.Gen_PHoleM54 import Gen_PHoleM54
from ......Methods.Slot.Slot import SlotCheckError


class PHoleM54(Gen_PHoleM54, QWidget):
    """Page to set the Hole Type 54"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for WHoleMag
    hole_name = "Hole Type 54"
    hole_type = HoleM54

    def __init__(self, hole=None, material_dict=None):
        """Initialize the widget according to hole

        Parameters
        ----------
        self : PHoleM54
            A PHoleM54 widget
        hole : HoleM54
            current hole to edit
        material_dict: dict
            Materials dictionary (library + machine)
        """
        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Set FloatEdit unit
        self.lf_W0.unit = "rad"
        self.lf_R1.unit = "m"
        self.lf_H0.unit = "m"
        self.lf_H1.unit = "m"

        # Set unit name (m ou mm)
        self.u = gui_option.unit
        wid_list = [self.unit_R1, self.unit_H0, self.unit_H1]
        for wid in wid_list:
            wid.setText("[" + self.u.get_m_name() + "]")

        self.material_dict = material_dict
        self.hole = hole

        # Set default materials
        self.w_mat_0.setText("mat_void")
        self.w_mat_0.def_mat = "Air"
        self.w_mat_0.is_hide_button = True

        # Set current material
        self.w_mat_0.update(self.hole, "mat_void", self.material_dict)

        # Fill the fields with the machine values (if they're filled)
        self.lf_W0.setValue(self.hole.W0)
        self.lf_R1.setValue(self.hole.R1)
        self.lf_H0.setValue(self.hole.H0)
        self.lf_H1.setValue(self.hole.H1)

        # Display the main output of the hole (surface, height...)
        self.comp_output()

        # Connect the signal
        self.lf_W0.editingFinished.connect(self.set_W0)
        self.lf_R1.editingFinished.connect(self.set_R1)
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.lf_H1.editingFinished.connect(self.set_H1)

        self.w_mat_0.saveNeeded.connect(self.emit_save)

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : PHoleM54
            A PHoleM54 widget
        """
        self.hole.W0 = self.lf_W0.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_R1(self):
        """Signal to update the value of R1 according to the line edit

        Parameters
        ----------
        self : PHoleM54
            A PHoleM54 widget
        """
        self.hole.R1 = self.lf_R1.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PHoleM54
            A PHoleM54 widget
        """
        self.hole.H0 = self.lf_H0.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H1(self):
        """Signal to update the value of H1 according to the line edit

        Parameters
        ----------
        self : PHoleM54
            A PHoleM54 widget
        """
        self.hole.H1 = self.lf_H1.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def comp_output(self):
        """Compute and display the hole output

        Parameters
        ----------
        self : PHoleM54
            A PHoleM54 widget
        """
        if self.check() is None:
            # We compute the output only if the hole is correctly set
            # Compute all the needed output as string
            s_surf = format(self.u.get_m2(self.hole.comp_surface()), ".4g")

            # Update the GUI to display the Output
            self.out_slot_surface.setText(
                "Slot suface : " + s_surf + " " + self.u.get_m2_name()
            )

        else:
            # We can't compute the output => We erase the previous version
            # (that way the user know that something is wrong)
            self.out_slot_surface.setText("Slot suface : ?")

    def check(self):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        self : PHoleM54
            A PHoleM54 widget

        Returns
        -------
        error : str
            Error message (return None if no error)
        """

        # Constraints and None
        try:
            self.hole.check()
        except SlotCheckError as error:
            return str(error)
