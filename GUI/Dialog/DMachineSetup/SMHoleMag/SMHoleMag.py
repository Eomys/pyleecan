# -*- coding: utf-8 -*-
"""@package pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.SMHoleMag
Buried Slot Setup Page
@date Created on Wed Jul 15 14:14:29 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QWidget, QSizePolicy

from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.Ui_SMHoleMag import Ui_SMHoleMag
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.WHoleMag.WHoleMag import WHoleMag


class SMHoleMag(Ui_SMHoleMag, QWidget):
    """Step to set several Holes
    """

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = pyqtSignal()
    # Information for DMachineSetup
    step_name = "Slot"

    def __init__(self, machine, matlib=[], is_stator=False):
        """Initialize the widget according to machine

        Parameters
        ----------
        self : SMHoleMag
            A SMHoleMag widget
        machine : Machine
            current machine to edit
        matlib : list
            List of available Material
        is_stator : bool
            To adapt the GUI to set either the stator or the rotor
        """
        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Size Policy on w_mat Widgets
        sp = QSizePolicy()
        sp.setRetainSizeWhenHidden(True)
        self.w_mat_1.setSizePolicy(sp)
        self.w_mat_2.setSizePolicy(sp)
        self.w_mat_3.setSizePolicy(sp)

        # hide edit buttons
        self.w_mat_2.b_matlib.setSizePolicy(sp)
        self.w_mat_3.b_matlib.setSizePolicy(sp)
        self.w_mat_2.b_matlib.hide()
        self.w_mat_3.b_matlib.hide()

        # Saving arguments
        self.machine = machine
        self.matlib = matlib
        self.is_stator = is_stator

        # Set default materials
        self.w_mat_1.setText("Magnet 1:")
        self.w_mat_1.def_mat = "Magnet1"
        self.w_mat_2.setText("Magnet 2:")
        self.w_mat_2.def_mat = "Magnet1"
        self.w_mat_3.setText("Magnet 3:")
        self.w_mat_3.def_mat = "Magnet1"

        # Get the correct object to set
        if self.is_stator:
            self.obj = machine.stator
        else:
            self.obj = machine.rotor

        # If the hole is not set, initialize it with a HoleM50
        if len(self.obj.hole) == 0:
            self.obj.hole.append(HoleM50())
            if self.machine.type_machine == 5:  # SyRM
                self.obj.hole[0].remove_magnet()
            self.obj.hole[0]._set_None()
            self.obj.hole[0].Zh = machine.stator.winding.p * 2  # Default value
        self.set_hole_pitch(self.obj.hole[0].Zh)

        # Update all the hole tab
        # (the current hole types will be initialized)
        # print(type(self.obj.hole[0]).__name__)
        self.tab_hole.clear()
        for hole in self.obj.hole:
            self.s_add(hole)
        self.tab_hole.setCurrentIndex(0)

        # Set Help URL
        self.b_help.url = "https://eomys.com/produits/manatee/howtos/article/"
        self.b_help.url += "how-to-set-up-the-slots"

        # Connect the slot
        self.b_add.clicked.connect(self.s_add)
        self.b_remove.clicked.connect(self.s_remove)

        self.b_plot.clicked.connect(self.s_plot)
        self.w_mat_1.saveNeeded.connect(self.emit_save)
        self.w_mat_2.saveNeeded.connect(self.emit_save)
        self.w_mat_3.saveNeeded.connect(self.emit_save)

        self.tab_hole.currentChanged.connect(self.update_w_mat)

    def update_w_mat(self, idx=None):
        if idx is None:
            idx = self.tab_hole.currentIndex()
        hole = self.obj.hole[idx]
        if self.machine.type_machine == 8:  # For IPMSM only
            if type(hole).__name__ in ["HoleM50", "HoleM53"]:
                self.w_mat_1.show()
                self.w_mat_2.show()
                self.w_mat_3.hide()
                self.w_mat_1.update(hole.magnet_0, "mat_type", self.matlib)
                self.w_mat_2.update(hole.magnet_1, "mat_type", self.matlib)
            if type(hole).__name__ in ["HoleM51"]:
                self.w_mat_1.show()
                self.w_mat_2.show()
                self.w_mat_3.show()
                self.w_mat_1.update(hole.magnet_0, "mat_type", self.matlib)
                self.w_mat_2.update(hole.magnet_1, "mat_type", self.matlib)
                self.w_mat_3.update(hole.magnet_2, "mat_type", self.matlib)
            if type(hole).__name__ in ["HoleM52"]:
                self.w_mat_1.show()
                self.w_mat_2.hide()
                self.w_mat_3.hide()
                self.w_mat_1.update(hole.magnet_0, "mat_type", self.matlib)

        elif self.machine.type_machine == 5:
            self.w_mat_1.hide()
            self.w_mat_2.hide()
            self.w_mat_3.hide()

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup
        """
        self.saveNeeded.emit()

    def set_hole_pitch(self, Zh):
        """Update out_hole_pitch with the correct value

        Parameters
        ----------
        self : SMHoleMag
            A SMHoleMag object
        Zh : int
            The current value of Zh
        """
        Zh_txt = self.tr("Slot pitch = 360 / 2p = ")
        if Zh in [None, 0]:
            self.out_hole_pitch.setText(Zh_txt + "?")
        else:
            hole_pitch = 360.0 / Zh
            self.out_hole_pitch.setText(Zh_txt + "%.4g" % (hole_pitch) + u" °")

    def s_add(self, hole=False):
        """Signal to add a new hole

        Parameters
        ----------
        self : SMHoleMag
            a SMHoleMag object
        hole : HoleMag
            hole to initialize in the new page
            if None create a new empty HoleM50
        """
        # Adapt the GUI according to the machine type
        if self.machine.type_machine == 5:  # SyRM
            is_mag = False
        else:
            is_mag = True
        # Create a new hole if needed
        if type(hole) is bool:
            self.obj.hole.append(HoleM50())
            hole = self.obj.hole[-1]
            hole._set_None()
            hole_index = len(self.obj.hole) - 1
            if self.machine.type_machine == 5:
                hole.remove_magnet()
            else:
                hole.magnet_0 = self.obj.hole[0].magnet_0
            hole.Zh = self.obj.hole[0].Zh
        else:
            hole_index = self.obj.hole.index(hole)
        tab = WHoleMag(self, is_mag=is_mag, index=hole_index)
        tab.saveNeeded.connect(self.emit_save)
        self.tab_hole.addTab(tab, "Slot " + str(hole_index + 1))

    def s_remove(self):
        """Signal to remove the last hole

        Parameters
        ----------
        self : SMHoleMag
            a SMHoleMag object
        """
        if len(self.obj.hole) > 1:
            self.tab_hole.removeTab(len(self.obj.hole) - 1)
            self.obj.hole.pop(-1)

    def s_plot(self):
        """Try to plot the lamination

        Parameters
        ----------
        self : SMHoleMag
            a SMHoleMag object
        """
        # We have to make sure the hole is right before truing to plot it
        error = self.check()

        if error:  # Error => Display it
            QMessageBox().critical(self, self.tr("Error"), error)
        else:  # No error => Plot the hole (No winding for LamSquirrelCage)
            self.machine.plot()

    def check(self):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        self : SMHoleMag
            A SMHoleMag object

        Returns
        -------
        error: str
            Error message (return None if no error)
        """

        # Check that everything is set
        index = self.w_mat_1.c_mat_type.currentIndex()
        for hole in self.obj.hole:
            hole.Zh = self.machine.stator.winding.p * 2
            if self.machine.type_machine == 8:  # IPMSM machine only
                mat_mag = Material(init_dict=self.matlib[index].as_dict())
                hole.magnet_0.mat_type = mat_mag

        self.set_hole_pitch(self.obj.hole[0].Zh)

        # Call the check method of the current page (every hole type have a
        # different check method)
        for ii in range(self.tab_hole.count()):
            error = self.tab_hole.widget(ii).check()
            if error is not None:
                return "Slot " + str(ii + 1) + ": " + error
