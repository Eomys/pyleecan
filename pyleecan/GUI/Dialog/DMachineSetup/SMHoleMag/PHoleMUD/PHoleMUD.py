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
from ......GUI.Dialog.DMachineSetup.SMHoleMag.PHoleMUD.Ui_PHoleMUD import Ui_PHoleMUD
from ......Methods.Slot.Slot import SlotCheckError
from ......GUI.Dxf.DXF_Hole import DXF_Hole
from ......GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect


class PHoleMUD(Ui_PHoleMUD, QWidget):
    """Page to set the Hole from DXF"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for WHoleMag
    hole_name = "Import from DXF"
    hole_type = HoleUD

    def __init__(self, hole=None, material_dict=None):
        """Initialize the widget according to hole

        Parameters
        ----------
        self : PHoleMUD
            A PHoleMUD widget
        hole : HoleUD
            current hole to edit
        material_dict: dict
            Materials dictionary (library + machine)
        """
        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Set properties
        self.material_dict = material_dict
        self.hole = hole
        self.u = gui_option.unit
        self.w_mat_dict = dict()  # For magnet materials

        # Setup void material
        self.w_mat_0.setText("mat_void")
        self.w_mat_0.def_mat = "Air"
        self.w_mat_0.is_hide_button = True

        # Setup Path selector for Json files
        self.w_path_json.obj = None
        self.w_path_json.param_name = None
        self.w_path_json.verbose_name = "Load from json"
        self.w_path_json.extension = "JSON file (*.json)"
        self.w_path_json.update()

        # Update the GUI according to the current hole
        self.update_mag_list()
        self.update_graph()
        self.comp_output()

        # Connect the signals
        self.b_dxf.clicked.connect(self.open_dxf_hole)
        self.w_path_json.pathChanged.connect(self.load_hole)

    def update_mag_list(self):
        """Update the material selector list according to hole magnet"""
        # Set void material
        self.w_mat_0.update(self.hole, "mat_void", self.material_dict)
        # Remove previous widget:
        for wid in self.w_mat_dict.values():
            self.g_mat_layout.removeWidget(wid)
            wid.setParent(None)
        self.w_mat_dict = dict()
        # Update Magnet materials
        magnet_dict = self.hole.magnet_dict
        for key, mag in magnet_dict.items():
            index = key.split("_")[-1]
            # Add widget
            self.w_mat_dict[key] = WMatSelect(self.g_mat)
            self.w_mat_dict[key].setObjectName("w_mat_" + str(index))
            self.g_mat_layout.insertWidget(int(index) + 1, self.w_mat_dict[key])
            # Setup Widget
            self.w_mat_dict[key].setText("Magnet " + str(index) + "")
            self.w_mat_dict[key].def_mat = "MagnetPrius"
            self.w_mat_dict[key].is_hide_button = True
            self.w_mat_dict[key].update(
                self.hole.magnet_dict["magnet_" + str(index)],
                "mat_type",
                self.material_dict,
            )

    def update_graph(self):
        """Plot the lamination with/without the hole"""
        # Use a copy to avoid changing the main object
        lam = self.hole.parent.copy()
        try:
            self.hole.check()
            lam.hole = [self.hole]
        except SlotCheckError:
            # Plot only the lamination
            lam.hole = list()
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
            hole = load(self.w_path_json.get_path())
        except Exception as e:
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr("Error when loading file:\n" + str(e)),
            )
            return
        # Check that the json file contain a HoleUD
        if not isinstance(hole, HoleUD):
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr(
                    "The choosen file is not a HoleUD file (" + str(type(hole)) + ")"
                ),
            )
            return

        # Update the hole object
        Zh = self.hole.Zh
        parent = self.hole.parent
        self.hole.__init__(init_dict=hole.as_dict())  # keep pointer
        self.hole.Zh = Zh
        self.hole.parent = parent

        # Update the new GUI according to the slot
        self.update_graph()
        self.update_mag_list()
        self.comp_output()

    def open_dxf_hole(self):
        """Open the GUI to define the HoleUD"""
        # Init GUI with lamination parameters
        self.dxf_gui = DXF_Hole(
            Zh=self.hole.Zh, Lmag=self.hole.parent.L1, lam=self.hole.parent
        )
        self.dxf_gui.setWindowFlags(Qt.Window)  # To maximize the GUI
        self.dxf_gui.show()
        # Update the hole when saving
        self.dxf_gui.accepted.connect(self.set_dxf_path)

    def set_dxf_path(self):
        """Update the hole according to the file defined by DXF_Hole"""
        # Get the saving path from DXF_Hole
        self.w_path_json.set_path_txt(self.dxf_gui.save_path)
        # Update hole and GUI
        self.load_hole()
        self.dxf_gui = None

    def comp_output(self):
        """Compute and display the hole output

        Parameters
        ----------
        self : PHoleMUD
            A PHoleMUD widget
        """
        is_set = False
        if self.check() is None:
            try:
                # We compute the output only if the hole is correctly set
                # Compute all the needed output as string
                s_surf = format(self.u.get_m2(self.hole.comp_surface()), ".4g")
                m_surf = format(self.u.get_m2(self.hole.comp_surface_magnets()), ".4g")
                (Rmin, Rmax) = self.hole.comp_radius()
                Rmin_txt = format(self.u.get_m(Rmin), ".4g")
                Rmax_txt = format(self.u.get_m(Rmax), ".4g")

                # Update the GUI to display the Output
                self.out_slot_surface.setText(
                    "Hole full surface : " + s_surf + " " + self.u.get_m2_name()
                )
                self.out_magnet_surface.setText(
                    "Hole magnet surface : " + m_surf + " " + self.u.get_m2_name()
                )
                self.out_Rmin.setText("Rmin : " + Rmin_txt + " " + self.u.get_m_name())
                self.out_Rmax.setText("Rmax : " + Rmax_txt + " " + self.u.get_m_name())
                is_set = True
            except:
                pass

        if not is_set:
            # We can't compute the output => We erase the previous version
            # (that way the user know that something is wrong)
            self.out_slot_surface.setText("Hole full surface : ?")
            self.out_magnet_surface.setText("Hole magnet surface : ?")
            self.out_Rmin.setText("Rmin : ?")
            self.out_Rmax.setText("Rmax : ?")

    def check(self):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        self : PHoleMUD
            A PHoleMUD widget

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

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()
