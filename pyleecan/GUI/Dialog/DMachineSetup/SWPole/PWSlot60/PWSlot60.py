# -*- coding: utf-8 -*-

import qtpy.QtCore
from qtpy.QtCore import Signal
from qtpy.QtWidgets import QWidget

from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SWPole.PWSlot60.Gen_PWSlot60 import Gen_PWSlot60
from ......Methods.Slot.Slot import SlotCheckError

translate = qtpy.QtCore.QCoreApplication.translate


class PWSlot60(Gen_PWSlot60, QWidget):
    """Page to set the Slot Type 60"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()

    def __init__(self, lamination=None):
        """Initialize the widget according to lamination

        Parameters
        ----------
        self : PWSlot60
            A PWSlot60 widget
        lamination : Lamination
            current lamination to edit
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Set FloatEdit unit
        self.lf_R1.unit = "m"
        self.lf_W1.unit = "m"
        self.lf_W2.unit = "m"
        self.lf_H1.unit = "m"
        self.lf_H2.unit = "m"
        self.lf_W3.unit = "m"
        self.lf_H3.unit = "m"
        self.lf_H4.unit = "m"

        # Set unit name (m ou mm)
        wid_list = [
            self.unit_R1,
            self.unit_W1,
            self.unit_W2,
            self.unit_H1,
            self.unit_H2,
            self.unit_W3,
            self.unit_H3,
            self.unit_H4,
        ]
        for wid in wid_list:
            wid.setText("[" + gui_option.unit.get_m_name() + "]")

        # Setup the Widget only if the correct type is selected.
        self.lamination = lamination
        self.slot = lamination.slot

        # Fill the fields with the machine values (if they're filled)
        self.lf_R1.setValue(self.slot.R1)
        self.lf_W1.setValue(self.slot.W1)
        self.lf_W2.setValue(self.slot.W2)
        self.lf_H1.setValue(self.slot.H1)
        self.lf_H2.setValue(self.slot.H2)
        self.lf_W3.setValue(self.slot.W3)
        self.lf_H3.setValue(self.slot.H3)
        self.lf_H4.setValue(self.slot.H4)

        # Display the main output of the slot (surface, height...)
        self.comp_output()

        # Connect the signal/slot
        self.lf_R1.editingFinished.connect(self.set_R1)
        self.lf_W1.editingFinished.connect(self.set_W1)
        self.lf_W2.editingFinished.connect(self.set_W2)
        self.lf_H1.editingFinished.connect(self.set_H1)
        self.lf_H2.editingFinished.connect(self.set_H2)
        self.lf_W3.editingFinished.connect(self.set_W3)
        self.lf_H3.editingFinished.connect(self.set_H3)
        self.lf_H4.editingFinished.connect(self.set_H4)

    def set_R1(self):
        """Signal to update the value of R1 according to the line edit

        Parameters
        ----------
        self : PWSlot60
            A PWSlot60 object
        """
        self.slot.R1 = self.lf_R1.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W1(self):
        """Signal to update the value of W1 according to the line edit

        Parameters
        ----------
        self : PWSlot60
            A PWSlot60 object
        """
        self.slot.W1 = self.lf_W1.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W2(self):
        """Signal to update the value of W2 according to the line edit

        Parameters
        ----------
        self : PWSlot60
            A PWSlot60 object
        """
        self.slot.W2 = self.lf_W2.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H1(self):
        """Signal to update the value of H1 according to the line edit

        Parameters
        ----------
        self : PWSlot60
            A PWSlot60 object
        """
        self.slot.H1 = self.lf_H1.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H2(self):
        """Signal to update the value of H2 according to the line edit

        Parameters
        ----------
        self : PWSlot60
            A PWSlot60 object
        """
        self.slot.H2 = self.lf_H2.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W3(self):
        """Signal to update the value of W3 according to the line edit

        Parameters
        ----------
        self : PWSlot60
            A PWSlot60 object
        """
        self.slot.W3 = self.lf_W3.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H3(self):
        """Signal to update the value of H3 according to the line edit

        Parameters
        ----------
        self : PWSlot60
            A PWSlot60 object
        """
        self.slot.H3 = self.lf_H3.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H4(self):
        """Signal to update the value of H4 according to the line edit

        Parameters
        ----------
        self : PWSlot60
            A PWSlot60 object
        """
        self.slot.H4 = self.lf_H4.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def comp_output(self):
        """Compute and display the slot output

        Parameters
        ----------
        self : PWSlot60
            A PWSlot60 object
        """

        WS_txt = self.tr("Winding surface: ")
        TS_txt = self.tr("Total surface: ")
        AO_txt = self.tr("Opening angle: ")
        # TW_txt = self.tr("Tooth average width: ")
        SH_txt = self.tr("Slot height: ")
        YH_txt = self.tr("Yoke height: ")

        Wlam = format(
            gui_option.unit.get_m(self.lamination.Rext - self.lamination.Rint), ".4g"
        )
        self.out_Wlam.setText(
            self.tr("Lamination width: ")
            + Wlam
            + " ["
            + gui_option.unit.get_m_name()
            + "]"
        )
        self.out_tooth_width.hide()
        if self.check(self.lamination) is None:
            # Compute all the needed output as string
            w_surf = format(
                gui_option.unit.get_m2(self.slot.comp_surface_active()), ".4g"
            )
            tot_surf = format(gui_option.unit.get_m2(self.slot.comp_surface()), ".4g")
            op_angle = "%.4g" % self.slot.comp_angle_opening()
            # tooth_width = format(gui_option.unit.get_m(
            #    self.slot.comp_tooth_widths()["WTooth_average"]), '.4g')
            slot_height = format(gui_option.unit.get_m(self.slot.comp_height()), ".4g")
            yoke_height = format(
                gui_option.unit.get_m(self.lamination.comp_height_yoke()), ".4g"
            )

            # Update the GUI to display the Output
            self.out_wind_surface.setText(
                WS_txt + w_surf + " [" + gui_option.unit.get_m2_name() + "]"
            )
            self.out_tot_surface.setText(
                TS_txt + tot_surf + " [" + gui_option.unit.get_m2_name() + "]"
            )
            self.out_op_angle.setText(AO_txt + op_angle + " [rad]")
            # self.out_tooth_width.setText(TW_txt + tooth_width + " " +
            #                             gui_option.unit.get_m_name())
            self.out_slot_height.setText(
                SH_txt + slot_height + " [" + gui_option.unit.get_m_name() + "]"
            )
            self.out_yoke_height.setText(
                YH_txt + yoke_height + " [" + gui_option.unit.get_m_name() + "]"
            )
        else:
            # We can't compute the output => We erase the previous version
            # (that way the user know that something is wrong)
            self.out_wind_surface.setText(WS_txt + "?")
            self.out_tot_surface.setText(TS_txt + "?")
            self.out_op_angle.setText(AO_txt + "?")
            # self.out_tooth_width.setText(TW_txt + "?")
            self.out_slot_height.setText(SH_txt + "?")
            self.out_yoke_height.setText(YH_txt + "?")

    @staticmethod
    def check(lam):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        self : PWSlot60
            A PWSlot60 object
        lam: LamSlotWind
            Lamination to check

        Returns
        -------
        error: str
            Error message (return None if no error)
        """

        # Check that everything is set
        if lam.slot.R1 is None:
            return "You must set R1 !"
        elif lam.slot.W1 is None:
            return "You must set W1 !"
        elif lam.slot.W2 is None:
            return "You must set W2 !"
        elif lam.slot.H1 is None:
            return "You must set H1 !"
        elif lam.slot.H2 is None:
            return "You must set H2 !"
        elif lam.slot.W3 is None:
            return "You must set W3 !"
        elif lam.slot.H3 is None:
            return "You must set H3 !"
        elif lam.slot.H4 is None:
            return "You must set H4 !"

        # Constraints
        try:
            lam.slot.check()
        except SlotCheckError as error:
            return str(error)

        # Output
        try:
            yoke_height = lam.comp_height_yoke()
        except Exception as error:
            return "Unable to compute yoke height:" + str(error)
        if yoke_height <= 0:
            return "The slot height is greater than the lamination !"
