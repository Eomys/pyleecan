from logging import getLogger
from os.path import dirname, isfile

import matplotlib.pyplot as plt
from ezdxf import readfile
from numpy import angle as np_angle
from numpy import argmin, array
from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QComboBox, QDialog, QFileDialog, QMessageBox, QPushButton

from ...Classes.LamSlot import LamSlot
from ...Classes.Magnet import Magnet
from ...Classes.SlotUD import SlotUD
from ...definitions import config_dict
from ...GUI.Dxf.dxf_to_pyleecan_list import dxf_to_pyleecan_list
from ...GUI.Resources import pixmap_dict
from ...GUI.Tools.MPLCanvas import MPLCanvas2
from ...loggers import GUI_LOG_NAME
from .Ui_DXF_Slot import Ui_DXF_Slot

# Column index for table
TYPE_COL = 0
DEL_COL = 1
HL_COL = 2
WIND_COLOR = config_dict["PLOT"]["COLOR_DICT"]["BAR_COLOR"]


class DXF_Slot(Ui_DXF_Slot, QDialog):
    """Dialog to create SlotUD objects from DXF files"""

    def __init__(self, dxf_path=None, Zs=None, lam=None):
        """Initialize the Dialog

        Parameters
        ----------
        self : DXF_Slot
            a DXF_Slot object
        dxf_path : str
            Path to a dxf file to read
        """
        # Widget setup
        QDialog.__init__(self)
        self.setupUi(self)

        # Init properties
        self.line_list = list()  # List of line from DXF
        self.selected_list = list()  # List of currently selected lines
        self.lam = lam

        # Initialize the graph
        self.init_graph()

        # Not used yet
        self.in_coord_center.hide()
        self.lf_center_x.hide()
        self.lf_center_y.hide()
        self.lf_axe_angle.hide()
        self.in_axe_angle.hide()
        self.lf_center_x.setValue(0)
        self.lf_center_y.setValue(0)

        # Set default values
        if Zs is not None:
            self.si_Zs.setValue(Zs)

        # Setup Path selector for DXF files
        self.dxf_path = dxf_path
        self.w_path_selector.obj = self
        self.w_path_selector.param_name = "dxf_path"
        self.w_path_selector.verbose_name = "DXF File"
        self.w_path_selector.extension = "DXF file (*.dxf)"
        self.w_path_selector.set_path_txt(self.dxf_path)
        self.w_path_selector.update()

        # Load the DXF file if provided
        if self.dxf_path is not None and isfile(self.dxf_path):
            self.open_document()

        # Connect signals to slot
        self.w_path_selector.pathChanged.connect(self.open_document)
        self.b_save.pressed.connect(self.save)
        self.b_plot.pressed.connect(self.plot)

        # Display the GUI
        self.show()

    def open_document(self):
        """Open a new dxf in the viewer

        Parameters
        ----------
        self : DXF_Slot
            a DXF_Slot object
        """

        getLogger(GUI_LOG_NAME).debug("Reading dxf file: " + self.dxf_path)
        # Read the DXF file
        try:
            document = readfile(self.dxf_path)
            modelspace = document.modelspace()
            # Convert DXF to pyleecan objects
            self.line_list = dxf_to_pyleecan_list(modelspace)
            # Display
            self.selected_list = [False for line in self.line_list]
            self.update_graph()
        except Exception as e:
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr("Error while reading dxf file:\n" + str(e)),
            )

    def init_graph(self):
        """Initialize the viewer

        Parameters
        ----------
        self : DXF_Slot
            a DXF_Slot object
        """
        fig, axes = self.w_viewer.fig, self.w_viewer.axes
        axes.set_axis_off()

        # Setup interaction with graph
        def select_line(event):
            """Function to select/unselect the closest line from click"""
            X = event.xdata  # X position of the click
            Y = event.ydata  # Y position of the click
            # Get closer pyleecan object
            Z = X + 1j * Y
            min_dist = float("inf")
            closest_id = -1
            for ii, line in enumerate(self.line_list):
                line_dist = line.comp_distance(Z)
                if line_dist < min_dist:
                    closest_id = ii
                    min_dist = line_dist
            # Select/unselect line
            self.selected_list[closest_id] = not self.selected_list[closest_id]
            # Change line color
            point_list = array(self.line_list[closest_id].discretize(20))
            if self.selected_list[closest_id]:
                color = "r"
            else:
                color = "k"
            axes.plot(point_list.real, point_list.imag, color, zorder=2)
            self.w_viewer.draw()

        def zoom(event):
            """Function to zoom/unzoom according the mouse wheel"""

            base_scale = 0.3  # Scaling factor
            # get the current x and y limits
            ax = self.w_viewer.axes
            cur_xlim = ax.get_xlim()
            cur_ylim = ax.get_ylim()
            cur_xrange = (cur_xlim[1] - cur_xlim[0]) * 0.5
            cur_yrange = (cur_ylim[1] - cur_ylim[0]) * 0.5
            xdata = event.xdata  # get event x location
            ydata = event.ydata  # get event y location
            if event.button == "down":
                # deal with zoom in
                scale_factor = 1 / base_scale
            elif event.button == "up":
                # deal with zoom out
                scale_factor = base_scale
            else:
                # deal with something that should never happen
                scale_factor = 1
            # set new limits
            ax.set_xlim(
                [xdata - cur_xrange * scale_factor, xdata + cur_xrange * scale_factor]
            )
            ax.set_ylim(
                [ydata - cur_yrange * scale_factor, ydata + cur_yrange * scale_factor]
            )
            self.w_viewer.draw()  # force re-draw

        # Connect the function
        self.w_viewer.mpl_connect("button_press_event", select_line)
        self.w_viewer.mpl_connect("scroll_event", zoom)

        # Axis cleanup
        axes.axis("equal")
        axes.set_axis_off()

    def update_graph(self):
        """Clean and redraw all the lines in viewer

        Parameters
        ----------
        self : DXF_Slot
            a DXF_Slot object
        """
        fig, axes = self.w_viewer.fig, self.w_viewer.axes
        axes.clear()
        axes.set_axis_off()

        # Draw the lines in the correct color
        for ii, line in enumerate(self.line_list):
            point_list = array(line.discretize(20))
            if self.selected_list[ii]:
                color = "r"
            else:
                color = "k"
            axes.plot(point_list.real, point_list.imag, color, zorder=1)

        self.w_viewer.draw()

    def check_selection(self):
        """Check if every line in the selection are connected

        Parameters
        ----------
        self : DXF_Slot
            a DXF_Slot object

        Returns
        -------
        is_line : bool
            True if it forms a line
        """

        # Create list of begin and end point for all lines
        point_list = list()
        for ii, line in enumerate(self.line_list):
            if self.selected_list[ii]:
                point_list.append(line.get_begin())
                point_list.append(line.get_end())

        # Check with a tolerance if every point is twice in the list
        if len(point_list) == 0:
            return False

        # Number of point only 1 time in the list (begin and end)
        count_1 = 0
        for p1 in point_list:
            count = 0
            for p2 in point_list:
                if abs(p1 - p2) < 1e-9:
                    count += 1
            if count == 1:
                count_1 += 1
                if count_1 > 2:
                    return False
            elif count != 2:
                return False

        return True

    def get_slot(self):
        """Generate the SlotUD object corresponding to the selected lines

        Parameters
        ----------
        self : DXF_Slot
            a DXF_Slot object

        Returns
        -------
        sot : SlotUD
            User defined slot according to selected lines
        """

        # Get all the selected lines
        line_list = list()
        point_list = list()
        for ii, line in enumerate(self.line_list):
            if self.selected_list[ii]:
                line_list.append(line.copy())
                point_list.append(line.get_begin())
                point_list.append(line.get_end())
        # Find begin point
        single_list = list()
        for p1 in point_list:
            count = 0
            for p2 in point_list:
                if abs(p1 - p2) < 1e-9:
                    count += 1
            if count == 1:
                single_list.append(p1)
        assert len(single_list) == 2
        Zbegin = single_list[argmin(np_angle(array(single_list)))]
        # Get begin line
        id_list = list()
        id_list.extend(
            [
                ii
                for ii, line in enumerate(line_list)
                if abs(line.get_begin() - Zbegin) < 1e-6
            ]
        )
        # Sort the lines (begin = end)
        curve_list = list()
        curve_list.append(line_list.pop(id_list[0]))
        while len(line_list) > 0:
            end = curve_list[-1].get_end()
            for ii in range(len(line_list)):
                if abs(line_list[ii].get_begin() - end) < 1e-9:
                    break
                if abs(line_list[ii].get_end() - end) < 1e-9:
                    line_list[ii].reverse()
                    break
            curve_list.append(line_list.pop(ii))

        # Create the Slot object
        slot = SlotUD(line_list=curve_list)
        slot.type_line_wind = self.c_type_line.currentIndex()
        begin_id = self.si_wind_begin_index.value()
        end_id = self.si_wind_end_index.value()
        if (
            begin_id < len(curve_list)
            and end_id < len(curve_list)
            and begin_id < end_id
        ):
            slot.wind_begin_index = begin_id
            slot.wind_end_index = end_id
        else:
            slot.wind_begin_index = None
            slot.wind_end_index = None

        # Rotation
        Z1 = curve_list[0].get_begin()
        Z2 = curve_list[-1].get_end()
        alpha = (np_angle(Z2) + np_angle(Z1)) / 2
        for line in curve_list:
            line.rotate(-1 * alpha)

        # Set metadata
        slot.Zs = self.si_Zs.value()

        return slot

    def plot(self):
        """Plot the current state of the hole

        Parameters
        ----------
        self : DXF_Slot
            a DXF_Slot object
        """
        if self.check_selection():
            slot = self.get_slot()
            # Lamination definition
            if self.lam is None:
                lam = LamSlot(slot=slot)
                Rbo = abs(slot.line_list[0].get_begin())
            else:
                lam = self.lam.copy()
                lam.slot = slot
            slot.plot()
            # Add the winding if defined
            if slot.wind_begin_index is not None:
                surf_wind = slot.get_surface_active()
                surf_wind.plot(fig=plt.gcf(), color=WIND_COLOR, is_show_fig=False)

    def save(self):
        """Save the SlotUD object in a json file

        Parameters
        ----------
        self : DXF_Slot
            a DXF_Slot object
        """

        if self.check_selection():
            slot = self.get_slot()

            save_file_path = QFileDialog.getSaveFileName(
                self, self.tr("Save file"), dirname(self.dxf_path), "Json (*.json)"
            )[0]
            if save_file_path not in ["", ".json", None]:
                self.save_path = save_file_path
                slot.save(save_file_path)
                self.accept()
