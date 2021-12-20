# -*- coding: utf-8 -*-

from numpy import pi
from PySide2.QtCore import Signal
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget, QDialog
from PySide2.QtWidgets import QMessageBox
from PySide2.QtCore import Qt
from ......Functions.load import load
from ......Classes.HoleUD import HoleUD
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.DAVDuct.PVentUD.Gen_PVentUD import (
    Gen_PVentUD,
)
from ......Methods.Slot.Slot import SlotCheckError
from ......GUI.Dxf.DXF_Surf import DXF_Surf


class PVentUD(Gen_PVentUD, QWidget):
    """Page to set the slot from DXF"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for WslotMag
    hole_name = "Import from DXF"
    hole_type = HoleUD

    def __init__(self, lam=None, vent=None):
        """Initialize the widget according the current lamination

        Parameters
        ----------
        self : PVentUD
            A PVentUD widget
        lam : Lamination
            current lamination to edit
        vent : VentUD
            current ventilation to edit
        """
        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Set properties
        self.lam = lam
        self.vent = vent
        self.u = gui_option.unit

        # Set vent values
        if self.vent.Zh is None:
            self.vent.Zh = 8
        self.si_Zh.setValue(self.vent.Zh)
        if self.vent.Alpha0 is None:
            self.vent.Alpha0 = 0
        self.lf_Alpha0.setValue(self.vent.Alpha0)

        # Setup Path selector for Json files
        self.w_path_json.obj = None
        self.w_path_json.param_name = None
        self.w_path_json.verbose_name = "Load from json"
        self.w_path_json.extension = "JSON file (*.json)"
        self.w_path_json.update()

        # Update the GUI according to the current slot
        self.update_graph()
        self.w_out.comp_output()

        # Connect the signals
        self.b_dxf.clicked.connect(self.open_DXF_Surf)
        self.w_path_json.pathChanged.connect(self.load_hole)
        self.si_Zh.editingFinished.connect(self.set_Zh)
        self.lf_Alpha0.editingFinished.connect(self.set_Alpha0)

    def set_Zh(self):
        """Signal to update the value of Zh according to the line edit

        Parameters
        ----------
        self : PVentTrap
            A PVentTrap object
        """
        self.vent.Zh = self.si_Zh.value()
        self.update_graph()
        self.w_out.comp_output()

    def set_Alpha0(self):
        """Signal to update the value of Alpha0 according to the line edit

        Parameters
        ----------
        self : PVentTrap
            A PVentTrap object
        """
        self.vent.Alpha0 = self.lf_Alpha0.value()
        self.update_graph()
        self.w_out.comp_output()

    def check(self):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        self : PVentTrap
            A PVentTrap object

        Returns
        -------
        error: str
            Error message (return None if no error)
        """

        # Check that everything is set
        if self.vent.Zh is None:
            return self.tr("You must set Zh !")
        elif self.vent.Alpha0 is None:
            return self.tr("You must set Alpha0 !")
        return None

    def update_graph(self):
        """Plot the lamination with/without the slot"""
        # Use a copy to avoid changing the main object
        lam = self.lam.copy()
        try:
            self.vent.check()
            lam.axial_vent = [self.vent]
        except SlotCheckError:
            # Plot only the lamination
            lam.axial_vent = list()
        # Plot the lamination in the viewer fig
        lam.plot(fig=self.w_viewer.fig, is_show_fig=False)

        # Update the Graph
        self.w_viewer.axes.set_axis_off()
        self.w_viewer.axes.axis("equal")
        if self.w_viewer.axes.get_legend() is not None:
            self.w_viewer.axes.get_legend().remove()
        self.w_viewer.draw()

    def load_hole(self):
        """Load the selected json file and display the hole"""
        # Check that the json file is correct
        try:
            vent = load(self.w_path_json.get_path())
        except Exception as e:
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr("Error when loading file:\n" + str(e)),
            )
            return
        # Check that the json file contain a HoleUD
        if not isinstance(vent, HoleUD):
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr(
                    "The choosen file is not a HoleUD file (" + str(type(vent)) + ")"
                ),
            )
            return

        # Update the slot object
        self.vent.__init__(init_dict=vent.as_dict())  # keep pointer
        # Update GUI widget according to hole
        self.si_Zh.blockSignals(True)
        self.lf_Alpha0.blockSignals(True)
        self.si_Zh.setValue(self.vent.Zh)
        self.lf_Alpha0.setValue(self.vent.Alpha0)
        self.si_Zh.blockSignals(False)
        self.lf_Alpha0.blockSignals(False)

        # Update the new GUI according to the new vent
        self.update_graph()
        self.w_out.comp_output()

    def open_DXF_Surf(self):
        """Open the GUI to define the HoleUD"""
        # Init GUI with lamination parameters
        self.dxf_gui = DXF_Surf(Zh=self.vent.Zh, lam=self.lam)
        self.dxf_gui.setWindowFlags(Qt.Window)  # To maximize the GUI
        self.dxf_gui.show()
        # Update the slot when saving
        self.dxf_gui.accepted.connect(self.set_dxf_path)

    def set_dxf_path(self):
        """Update the slot according to the file defined by DXF_Slot"""
        # Get the saving path from DXF_Slot
        self.w_path_json.set_path_txt(self.dxf_gui.save_path)
        # Update vent and GUI
        self.load_hole()
        self.dxf_gui = None

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()
