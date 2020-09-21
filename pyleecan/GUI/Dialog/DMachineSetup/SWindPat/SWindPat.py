# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QWidget

from .....Classes.Winding import Winding
from .....Classes.WindingCW1L import WindingCW1L
from .....Classes.WindingCW2LR import WindingCW2LR
from .....Classes.WindingCW2LT import WindingCW2LT
from .....Classes.WindingDW1L import WindingDW1L
from .....Classes.WindingDW2L import WindingDW2L
from .....Functions.Winding.comp_wind_sym import comp_wind_sym
from .....GUI.Dialog.DMachineSetup.SWindPat.Gen_SWindPat import Gen_SWindPat
from .....GUI.Resources import pixmap_dict
from .....Methods.Machine.Winding import WindingError

# For the Pattern combobox
TYPE_INDEX = [WindingCW2LT, WindingCW1L, WindingDW2L, WindingDW1L, WindingCW2LR]


class SWindPat(Gen_SWindPat, QWidget):
    """Step to define the winding pattern"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = pyqtSignal()
    # Information for DMachineSetup nav
    step_name = "Winding Pattern"

    def __init__(self, machine, matlib, is_stator=False):
        """Initialize the GUI according to machine

        Parameters
        ----------
        self : SWindPat
            A SWindPat widget
        machine : Machine
            current machine to edit
        matlib : MatLib
            Material Library
        is_stator : bool
            To adapt the GUI to set either the stator or the rotor
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Set Help URL
        self.b_help.url = "https://eomys.com/produits/manatee/howtos/article/"
        self.b_help.url += "how-to-set-up-the-winding"

        # Saving arguments
        self.machine = machine
        self.matlib = matlib
        self.is_stator = is_stator

        # Fill the fields with the machine values (if they're filled)
        if self.is_stator:
            self.obj = machine.stator
        else:
            self.obj = machine.rotor

        if machine.type_machine == 9 and not self.is_stator:
            # Enforce tooth winding for WRSM rotor
            self.obj.winding = WindingCW2LT(init_dict=self.obj.winding.as_dict())
            self.obj.winding.qs = 1
            self.b_preview.setEnabled(False)
            self.si_qs.setEnabled(False)
            self.c_wind_type.setEnabled(False)
            self.c_wind_type.setCurrentIndex(0)
            self.c_wind_type.setItemText(0, "DC wound winding for salient pole")
        else:
            self.b_preview.setEnabled(True)
            self.si_qs.setEnabled(True)
            self.c_wind_type.setEnabled(True)
            self.c_wind_type.setItemText(0, "Double Layer Concentrated Orthoradial")

        # Set the current Winding pattern
        if self.obj.winding is None or type(self.obj.winding) is Winding:
            # The default type_winding is WindingCW2LT
            self.obj.winding = WindingCW2LT(init_dict=self.obj.winding.as_dict())
            self.c_wind_type.setCurrentIndex(0)
        else:
            self.c_wind_type.setCurrentIndex(TYPE_INDEX.index(type(self.obj.winding)))
        self.update_image()

        if type(self.obj.winding) is WindingDW2L:
            if self.obj.winding.coil_pitch is None:
                self.obj.winding.coil_pitch = 0
            self.si_coil_pitch.setValue(self.obj.winding.coil_pitch)

        if self.obj.winding.Nslot_shift_wind is not None:
            self.si_Nslot.setValue(self.obj.winding.Nslot_shift_wind)
        else:
            self.si_Nslot.setValue(0)
            self.obj.winding.Nslot_shift_wind = 0

        if self.obj.winding.qs is None:  # default value
            self.obj.winding.qs = 3
        self.si_qs.setValue(self.obj.winding.qs)

        if self.obj.winding.Ntcoil is None:
            self.obj.winding.Ntcoil = 1  # Default value for preview

        if self.obj.winding.is_reverse_wind is not None:
            if self.obj.winding.is_reverse_wind:
                self.is_reverse.setCheckState(Qt.Checked)
            else:
                self.is_reverse.setCheckState(Qt.Unchecked)
        else:
            self.obj.winding.is_reverse_wind = False

        # Display shape of wind_mat
        self.set_output()
        self.hide_coil_pitch()

        # Connect the signal/slot
        self.c_wind_type.currentIndexChanged.connect(self.set_type)
        self.si_qs.editingFinished.connect(self.set_qs)
        self.si_coil_pitch.editingFinished.connect(self.set_coil_pitch)
        self.si_Nslot.editingFinished.connect(self.set_Nslot)
        self.is_reverse.stateChanged.connect(self.set_is_reverse_wind)
        self.b_preview.clicked.connect(self.s_plot)

    def set_type(self, index):
        """Signal to update the winding type

        Parameters
        ----------
        self : SWindPat
            A SWindPat object
        index : int
            Index of selected type
        """

        w_dict = Winding.as_dict(self.obj.winding)
        self.obj.winding = TYPE_INDEX[index](init_dict=w_dict)

        # Update out_shape
        self.set_output()
        self.hide_coil_pitch()
        # Update image
        self.update_image()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def update_image(self):
        """Update the schematics to the current winding pattern

        Parameters
        ----------
        self : SWindPat
            A SWindPat object
        """
        self.img_wind_pat.setPixmap(
            QPixmap(pixmap_dict[type(self.obj.winding).__name__])
        )

    def set_qs(self):
        """Signal to update the value of qs according to the spinbox

        Parameters
        ----------
        self : SWindPat
            A SWindPat object
        """
        self.obj.winding.qs = self.si_qs.value()
        self.set_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_coil_pitch(self):
        """Signal to update the value of coil_pitch according to the spinbox

        Parameters
        ----------
        self : SWindPat
            A SWindPat object
        """
        self.obj.winding.coil_pitch = self.si_coil_pitch.value()
        self.set_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Nslot(self):
        """Signal to update the value of Nslot_shift_wind according to the
        spinbox

        Parameters
        ----------
        self : SWindPat
            A SWindPat object
        """
        self.obj.winding.Nslot_shift_wind = self.si_Nslot.value()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_is_reverse_wind(self, value):
        """Signal to update the value of is_reverse_wind according to the
        widget

        Parameters
        ----------
        self : SWindPat
            A SWindPat object
        value :
            New value of is_reverse_wind
        """

        value = self.is_reverse.isChecked()
        self.obj.winding.is_reverse_wind = value
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def hide_coil_pitch(self):
        """Show coil_pitch only if type(winding) is WindingDW2L

        Parameters
        ----------
        self : SWindPat
            A SWindPat object
        """
        self.si_coil_pitch.blockSignals(True)
        if type(self.obj.winding) is WindingDW2L:
            self.si_coil_pitch.show()
            self.in_coil_pitch.show()
        else:
            self.si_coil_pitch.hide()
            self.in_coil_pitch.hide()
        self.si_coil_pitch.blockSignals(False)

    def set_output(self):
        """Update the shape and period Label to match the current winding setup

        Parameters
        ----------
        self : SWindPat
            a SWindPat object
        """

        wind = self.obj.winding  # For readability
        # Wind_matrix is a matrix of dimension [Nlay_rad, Nlay_tan, Zs, qs]
        # Nlay_rad and Nlay_tan depend of the winding type
        (Nrad, Ntan) = wind.get_dim_wind()
        Nlay = str(Nrad) + ", " + str(Ntan) + ", "

        # Zs should be set, but to be sure:
        if self.obj.slot.Zs is None:
            Zs = "?, "
        else:
            Zs = str(self.obj.slot.Zs) + ", "

        if wind.qs is None:
            qs = "?]"
        else:
            qs = str(wind.qs) + "]"

        self.out_shape.setText(self.tr("Winding Matrix shape: [") + Nlay + Zs + qs)

        try:
            ms = str(self.obj.slot.Zs / (wind.p * wind.qs * 2.0))
        except TypeError:  # One of the value is None
            ms = "?"
        if self.obj.is_stator:
            self.out_ms.setText(self.tr("ms = Zs / (2*p*qs) = ") + ms)
        else:
            self.out_ms.setText(self.tr("ms = Zr / (2*p*qr) = ") + ms)

        try:
            wind_mat = wind.comp_connection_mat(self.obj.slot.Zs)
            Nperw = str(comp_wind_sym(wind_mat)[0])
        except Exception:  # Unable to compution the connection matrix
            Nperw = "?"

        self.out_Nperw.setText(self.tr("Nperw: ") + Nperw)

    def s_plot(self):
        """Plot a preview of the winding in a popup

        Parameters
        ----------
        self : SWindPat
            A SWindPat object
        """
        try:
            self.obj.plot_winding()
        except (AssertionError, WindingError) as e:
            QMessageBox().critical(self, self.tr("Error"), str(e))

    @staticmethod
    def check(lamination):
        """Check that the lamination have all the needed field set

        Parameters
        ----------
        lamination : Lamination
            Lamination to check

        Returns
        -------
        error: str
            Error message (return None if no error)
        """
        try:
            # Check that everything is set
            if lamination.winding.qs is None:
                return "You must set qs !"
        except Exception as e:
            return str(e)
