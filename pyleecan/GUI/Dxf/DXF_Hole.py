from logging import getLogger
from os.path import dirname, isfile

from ezdxf import readfile
from numpy import angle as np_angle
from numpy import array
from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QComboBox, QDialog, QFileDialog, QMessageBox, QPushButton

from ...Classes.HoleUD import HoleUD
from ...Classes.Magnet import Magnet
from ...Classes.SurfLine import SurfLine
from ...GUI.Dxf.dxf_to_pyleecan_list import dxf_to_pyleecan_list
from ...GUI.Resources import pixmap_dict
from ...GUI.Tools.MPLCanvas import MPLCanvas2
from ...loggers import GUI_LOG_NAME
from .Ui_DXF_Hole import Ui_DXF_Hole

# Column index for table
TYPE_COL = 0
DEL_COL = 1
HL_COL = 2
ICON_SIZE = 24
# Unselected, selected, selected-bottom-mag
COLOR_LIST = ["k", "r", "c"]


class DXF_Hole(Ui_DXF_Hole, QDialog):
    """Dialog to create HoleUD objects from DXF files"""

    def __init__(self, dxf_path=None, Zh=None, Lmag=None):
        """Initialize the Dialog

        Parameters
        ----------
        self : DXF_Hole
            a DXF_Hole object
        dxf_path : str
            Path to a dxf file to read
        """
        # Widget setup
        QDialog.__init__(self)
        self.setupUi(self)

        # Icon preparation
        self.delete_icon = QPixmap(pixmap_dict["cross"])
        self.delete_icon.scaled(ICON_SIZE, ICON_SIZE, Qt.KeepAspectRatio)
        self.highlight_icon = QPixmap(pixmap_dict["search"])
        self.highlight_icon.scaled(ICON_SIZE, ICON_SIZE, Qt.KeepAspectRatio)

        # Initialize the graph
        self.init_graph()

        # Not used yet
        self.in_coord_center.hide()
        self.lf_center_x.hide()
        self.lf_center_y.hide()
        self.lf_axe_angle.hide()
        self.in_axe_angle.hide()

        # Set default values
        if Zh is not None:
            self.si_Zh.setValue(Zh)
        if Lmag is not None:
            self.lf_mag_len.setValue(Lmag)

        # Init properties
        self.line_list = list()  # List of line from DXF
        self.selected_list = list()  # List of currently selected lines
        self.surf_list = list()  # List of defined surfaces
        self.bottom_line_list = list()  # List of bottom lines index for magnetization
        self.lf_center_x.setValue(0)
        self.lf_center_y.setValue(0)

        # Load the DXF file if provided
        self.dxf_path = dxf_path
        if dxf_path is not None and isfile(dxf_path):
            self.open_document()

        # Setup Path selector for DXF files
        self.w_path_selector.obj = self
        self.w_path_selector.param_name = "dxf_path"
        self.w_path_selector.verbose_name = "DXF File"
        self.w_path_selector.extension = "DXF file (*.dxf)"
        self.w_path_selector.set_path_txt(self.dxf_path)
        self.w_path_selector.update()

        # Format w_surface_list table (QTableWidget)
        self.w_surface_list.setColumnCount(3)
        self.w_surface_list.horizontalHeader().hide()
        self.w_surface_list.verticalHeader().hide()

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
        self : DXF_Hole
            a DXF_Hole object
        """

        getLogger(GUI_LOG_NAME).debug("Reading dxf file: " + self.dxf_path)
        # Read the DXF file
        try:
            document = readfile(self.dxf_path)
            modelspace = document.modelspace()
            # Convert DXF to pyleecan objects
            self.line_list = dxf_to_pyleecan_list(modelspace)
            # Display
            # selected line: 0: unselected, 1:selected, 2: selected bottom magnet
            self.selected_list = [0 for line in self.line_list]
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
        self : DXF_Hole
            a DXF_Hole object
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
            if self.selected_list[closest_id] == 0:  # Unselected to selected
                self.selected_list[closest_id] = 1
            elif self.selected_list[closest_id] == 1:  # Selected to selected bottom mag
                if 2 in self.selected_list:
                    current_bot_mag = self.selected_list.index(2)
                    # Only one selected bottom mag line at the time
                    point_list = array(self.line_list[current_bot_mag].discretize(20))
                    self.selected_list[current_bot_mag] = 1
                    axes.plot(point_list.real, point_list.imag, COLOR_LIST[1], zorder=2)
                self.selected_list[closest_id] = 2
            elif self.selected_list[closest_id] == 2:
                # selected bottom mag to Unselected
                self.selected_list[closest_id] = 0
            # Change line color
            point_list = array(self.line_list[closest_id].discretize(20))
            color = COLOR_LIST[self.selected_list[closest_id]]
            axes.plot(point_list.real, point_list.imag, color, zorder=2)
            self.w_viewer.draw()

            # Check if the surface is complete
            if self.check_selection():
                self.add_surface()

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
        self : DXF_Hole
            a DXF_Hole object
        """
        fig, axes = self.w_viewer.fig, self.w_viewer.axes
        axes.clear()
        axes.set_axis_off()

        # Draw the lines in the correct color
        for ii, line in enumerate(self.line_list):
            point_list = array(line.discretize(20))
            color = COLOR_LIST[self.selected_list[ii]]
            axes.plot(point_list.real, point_list.imag, color, zorder=1)

        self.w_viewer.draw()

    def check_selection(self):
        """Check if every line in the selection form a surface

        Parameters
        ----------
        self : DXF_Hole
            a DXF_Hole object

        Returns
        -------
        is_surf : bool
            True if it forms a surface
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

        for p1 in point_list:
            count = 0
            for p2 in point_list:
                if abs(p1 - p2) < 1e-9:
                    count += 1
            if count != 2:
                return False

        return True

    def add_surface(self):
        """Validate the selection and create a surface object

        Parameters
        ----------
        self : DXF_Hole
            a DXF_Hole object
        """

        # Get all the selected lines
        line_list = list()
        for ii, line in enumerate(self.line_list):
            if self.selected_list[ii]:
                line_list.append(line.copy())
        # Sort the lines (begin = end)
        curve_list = list()
        curve_list.append(line_list.pop())
        while len(line_list) > 0:
            end = curve_list[-1].get_end()
            for ii in range(len(line_list)):
                if abs(line_list[ii].get_begin() - end) < 1e-9:
                    break
                if abs(line_list[ii].get_end() - end) < 1e-9:
                    line_list[ii].reverse()
                    break
            curve_list.append(line_list.pop(ii))
        # Create the Surface object
        self.surf_list.append(SurfLine(line_list=curve_list))
        self.surf_list[-1].comp_point_ref(is_set=True)
        if 2 in self.selected_list:
            self.bottom_line_list.append(self.selected_list.index(2))
        else:
            self.bottom_line_list.append(None)

        # Update the GUI
        nrows = self.w_surface_list.rowCount()
        # Adding Surface Type combobox
        self.w_surface_list.setRowCount(nrows + 1)
        combobox = QComboBox()
        combobox.addItems(["Hole", "Magnet"])
        self.w_surface_list.setCellWidget(
            nrows, TYPE_COL, combobox,
        )
        if 2 in self.selected_list:
            combobox.setCurrentIndex(1)  # Magnet
        # Adding Delete button
        del_button = QPushButton("Delete")
        del_button.setIcon(QIcon(self.delete_icon))
        del_button.pressed.connect(self.delete_surface)
        self.w_surface_list.setCellWidget(
            nrows, DEL_COL, del_button,
        )

        # Adding Highlight button
        HL_button = QPushButton("Highlight")
        HL_button.setIcon(QIcon(self.highlight_icon))
        HL_button.pressed.connect(self.highlight_surface)
        self.w_surface_list.setCellWidget(
            nrows, HL_COL, HL_button,
        )

        # Remove selection
        self.selected_list = [0 for line in self.line_list]
        self.update_graph()

    def get_hole(self):
        """Generate the HoleUD object corresponding to the selected surfaces

        Parameters
        ----------
        self : DXF_Hole
            a DXF_Hole object

        Returns
        -------
        hole : HoleUD
            User defined hole according to selected surfaces
        """

        hole = HoleUD(surf_list=self.surf_list)
        # Set labels
        Nmag = 0
        for ii in range(self.w_surface_list.rowCount()):
            if self.w_surface_list.cellWidget(ii, TYPE_COL).currentIndex() == 0:
                hole.surf_list[ii].label = "Hole"
            else:
                hole.surf_list[ii].label = "HoleMagnet"
                Nmag += 1
        # Create magnet objects
        hole.magnet_dict = dict()
        for ii in range(Nmag):
            hole.magnet_dict["magnet_" + str(ii)] = Magnet()

        # Sort the surfaces
        angles = [np_angle(surf.point_ref) for surf in hole.surf_list]
        idx = sorted(range(len(angles)), key=lambda k: angles[k])
        surf_list_sorted = [hole.surf_list[ii] for ii in idx]
        bottom_line_list_sorted = [self.bottom_line_list[ii] for ii in idx]
        hole.surf_list = surf_list_sorted

        # Rotation
        Zref = sum([surf.point_ref for surf in hole.surf_list])
        for surf in hole.surf_list:
            surf.rotate(-1 * np_angle(Zref))

        # Magnetization dict
        mag_dict = dict()
        Nmag = 0
        for ii in range(len(hole.surf_list)):
            if "Magnet" in hole.surf_list[ii].label:
                if bottom_line_list_sorted[ii] is None:
                    mag_dict["magnet_" + str(Nmag)] = (
                        hole.surf_list[ii].get_lines()[0].comp_normal(return_type=2)
                    )
                else:
                    line = self.line_list[bottom_line_list_sorted[ii]].copy()
                    line.rotate(-1 * np_angle(Zref))
                    mag_dict["magnet_" + str(Nmag)] = line.comp_normal(return_type=2)
                Nmag += 1
        hole.magnetization_dict_enforced = mag_dict

        # Set metadata
        hole.Zh = self.si_Zh.value()
        for magnet in hole.magnet_dict.values():
            magnet.Lmag = self.lf_mag_len.value()

        # Remove all materials => To be set in GUI
        hole.mat_void = None
        for magnet in hole.magnet_dict.values():
            magnet.mat_type = None

        return hole

    def plot(self):
        """Plot the current state of the hole

        Parameters
        ----------
        self : DXF_Hole
            a DXF_Hole object
        """
        hole = self.get_hole()
        hole.plot(is_add_arrow=True)

    def delete_surface(self):
        """Delete a selected surface

        Parameters
        ----------
        self : DXF_Hole
            a DXF_Hole object
        """
        nrow = self.w_surface_list.currentRow()
        self.surf_list.pop(nrow)
        self.w_surface_list.removeRow(nrow)

    def highlight_surface(self):
        """Highlight a surface to find it on the viewer

        Parameters
        ----------
        self : DXF_Hole
            a DXF_Hole object
        """
        self.selected_list = [0 for line in self.line_list]
        surf = self.surf_list[self.w_surface_list.currentRow()]
        # Find the index of the surface line in self.line_list
        for surf_line in surf.line_list:
            mid = surf_line.get_middle()
            for ii, line in enumerate(self.line_list):
                if abs(mid - line.get_middle()) < 1e-6:
                    self.selected_list[ii] = 1
        self.update_graph()

    def save(self):
        """Save the HoleUD object in a json file

        Parameters
        ----------
        self : DXF_Hole
            a DXF_Hole object
        """

        hole = self.get_hole()

        save_file_path = QFileDialog.getSaveFileName(
            self, self.tr("Save file"), dirname(self.dxf_path), "Json (*.json)"
        )[0]
        if save_file_path not in ["", ".json", None]:
            self.save_path = save_file_path
            hole.save(save_file_path)
            self.accept()
