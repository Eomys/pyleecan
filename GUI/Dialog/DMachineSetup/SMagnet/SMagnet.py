# -*- coding: utf-8 -*-

from numpy import pi
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QMessageBox

from pyleecan.Classes.Magnet import Magnet
from pyleecan.Classes.MagnetType13 import MagnetType13
from pyleecan.Classes.Slot import Slot
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.PMagnet10.PMagnet10 import PMagnet10
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.PMagnet11.PMagnet11 import PMagnet11
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.PMagnet12.PMagnet12 import PMagnet12
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.PMagnet13.PMagnet13 import PMagnet13
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.PMagnet14.PMagnet14 import PMagnet14
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.Ui_SMagnet import Ui_SMagnet


class SMagnet(Ui_SMagnet, QDialog):
    """Step to set the magnet (and slot) for SPMSM/SIPMSM
    """

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = pyqtSignal()
    # Information for DMachineType nav
    step_name = "Magnet"

    def __init__(self, machine, matlib=[], is_stator=False):
        """Initialize the widget according to machine

        Parameters
        ----------
        self : SMagnet
            A SMagnet widget
        machine : Machine
            current machine to edit
        matlib : list
            List of available Material
        is_stator : bool
            To adapt the GUI to set either the stator or the rotor
        """
        # Build the interface according to the .ui file
        QDialog.__init__(self)
        self.setupUi(self)

        # Saving arguments
        self.machine = machine
        self.matlib = matlib
        self.is_stator = is_stator

        # Get the correct available widgets according to the machine
        if self.machine.rotor.is_internal:
            self.wid_list = [PMagnet10, PMagnet11, PMagnet12, PMagnet13, PMagnet14]
        elif self.machine.type_machine == 6:
            # For SPMSM only polar magnet for external rotor
            self.wid_list = [PMagnet11]
        else:
            # Magnet 14 not available for SIPMSM
            self.wid_list = [PMagnet10, PMagnet11, PMagnet12, PMagnet13]
        self.mag_type_index = [wid.mag_type for wid in self.wid_list]
        self.slot_type_index = [wid.slot_type for wid in self.wid_list]
        self.mag_name_index = [wid.mag_name for wid in self.wid_list]

        # Help URL
        self.b_help.url = "https://eomys.com/produits/manatee/howtos/article/"
        self.b_help.url += "how-to-set-up-inset-magnet"

        # Fill the combobox with the available magnet
        self.c_type.clear()
        for mag in self.mag_name_index:
            self.c_type.addItem(mag)

        # Avoid erase all the parameters when navigating though the magnets
        self.previous_mag = dict()
        for mag_type in self.mag_type_index:
            self.previous_mag[mag_type] = None

        # Set the GUI with the current values if provided
        if (
            type(self.machine.rotor.slot) is Slot
            or type(self.machine.rotor.slot.magnet[0]) is Magnet
        ):
            # Magnet or slot not set
            # Type 11 is default
            self.set_type(1)
            self.c_type.setCurrentIndex(1)
        else:  # The Magnet is set => load the parameter
            # Set the type
            index = self.mag_type_index.index(type(self.machine.rotor.slot.magnet[0]))
            self.set_type_gui(index)
            self.c_type.setCurrentIndex(index)
        # Only one magnet in the GUI (for now)
        self.machine.rotor.slot.W3 = 0

        # Set magnetization
        if self.machine.rotor.slot.magnet[0].type_magnetization is None:
            self.machine.rotor.slot.magnet[0].type_magnetization = 0
        self.c_type_magnetization.setCurrentIndex(
            self.machine.rotor.slot.magnet[0].type_magnetization
        )

        self.set_slot_pitch()

        # Set material
        self.w_mat.setText(self.tr("mat_mag:"))
        self.w_mat.def_mat = "Magnet1"
        self.w_mat.update(self.machine.rotor.slot.magnet[0], "mat_type", matlib)

        # Connect signals
        self.c_type.currentIndexChanged.connect(self.set_type)
        self.c_type_magnetization.currentIndexChanged.connect(
            self.s_set_type_magnetization
        )
        self.b_plot.clicked.connect(self.s_plot)
        self.w_mat.saveNeeded.connect(self.emit_save)

    def set_slot_pitch(self):
        """Update the slot pitch text

        Parameters
        ----------
        self : SMagnet
            A SMagnet object
        """
        Nmag_txt = self.tr("Number of magnets = 2p = ")
        if self.machine.rotor.slot.Zs is not None:
            Zs = self.machine.rotor.slot.Zs
            out = Nmag_txt + str(Zs) + " => "
            Slot_pitch = 360.0 / Zs
            Slot_pitch_rad = Slot_pitch * pi / 180

            pitch_txt = self.tr("Slot pitch = ")
            out += (
                pitch_txt
                + "%.4g" % (Slot_pitch)
                + u" ° ("
                + "%.4g" % (Slot_pitch_rad)
                + " rad)"
            )
            self.out_Nmag.setText(out)
        else:
            self.out_Nmag.setText(Nmag_txt + "?")

    def emit_save(self):
        """Emit the saveNeeded signal for the DMachineSetup
        """
        self.saveNeeded.emit()

    def set_type_gui(self, index):
        """Change the GUI to the correct Magnet widget

        Parameters
        ----------
        self : SMagnet
            A SMagnet object
        index : int
            Index of the Magnet type to use
        """
        # Regenerate the pages with the new values
        self.w_mag.setParent(None)
        self.w_mag = self.wid_list[index](self.machine)
        self.w_mag.saveNeeded.connect(self.emit_save)

        # Refresh the GUI
        self.main_layout.removeWidget(self.w_mag)
        self.main_layout.insertWidget(2, self.w_mag)

    def set_type_obj(self, index):
        """Set the type of magnet (update only the object)

        Parameters
        ----------
        self : SMagnet
            A SMagnet object
        index : int
            Index of the Magnet type to use
        """
        # Save the mag
        slot = self.machine.rotor.slot
        self.previous_mag[type(slot.magnet[0])] = slot

        if self.previous_mag[self.mag_type_index[index]] is None:
            # Set the slot
            Zs = self.machine.rotor.slot.Zs
            self.machine.rotor.slot = self.slot_type_index[index]()
            self.machine.rotor.slot._set_None()
            self.machine.rotor.slot.Zs = Zs
            self.machine.rotor.slot.W3 = 0
            # Set the magnet
            self.machine.rotor.slot.magnet = list()
            mag = self.mag_type_index[index]()
            self.machine.rotor.slot.magnet.append(mag)
            self.machine.rotor.slot.magnet[0]._set_None()
        else:
            self.machine.rotor.slot = self.previous_mag[self.mag_type_index[index]]

    def set_type(self, index):
        """Signal to set the type of magnet (update both the object and the gui)

        Parameters
        ----------
        self : SMagnet
            A SMagnet object
        index : int
            Index of the Magnet type to use
        """
        self.set_type_obj(index)
        self.set_type_gui(index)
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def s_plot(self):
        """Plot the current machine
        
        Parameters
        ----------
        self : SMagnet
            A SMagnet object
        """
        # We have to make sure the slot is right before truing to plot it
        error = self.check()

        if error:  # Error => Display it
            QMessageBox().critical(self, self.tr("Error"), error)
        else:  # No error => Plot the machine
            self.machine.plot()

    def check(self):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        self : SMagnet
            A SMagnet object

        Returns
        -------
        error: str
            Error message (return None if no error)
        """
        # Check that everything is set
        if self.machine.rotor.slot.magnet[0].Wmag is None:
            return self.tr("You must set Wmag !")
        if self.machine.rotor.slot.magnet[0].Hmag is None:
            return self.tr("You must set Hmag !")
        if (
            hasattr(self.machine.rotor.slot.magnet[0], "Rtop")
            and self.machine.rotor.slot.magnet[0].Rtop is None
        ):
            return self.tr("You must set Rtopm !")
        if self.machine.rotor.slot.H0 is None:
            return self.tr("You must set H0 !")

        # Check that everything is set right
        try:
            mec_gap = self.machine.comp_width_airgap_mec()
        except:
            return self.tr("Unable to draw the magnet, " "please check your geometry !")

        if mec_gap <= 0:
            return self.tr("You must have gap_min > 0 (reduce Hmag) !")
        if hasattr(self.machine.rotor.slot.magnet[0], "Rtop"):
            if (
                type(self.machine.rotor.slot.magnet[0]) is MagnetType13
                and self.machine.rotor.slot.magnet[0].Rtop
                < self.machine.rotor.slot.magnet[0].Wmag / 2.0
            ):
                return self.tr("You must have Rtopm >= Wmag/2 !")

    def s_set_type_magnetization(self, index):
        """Signal to update the value of type_magnetization according to the combobox

        Parameters
        ----------
        self : SMagnet
            A SMagnet object
        index : int
            Current index of the combobox
        """
        self.machine.rotor.slot.magnet[0].type_magnetization = index
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()
