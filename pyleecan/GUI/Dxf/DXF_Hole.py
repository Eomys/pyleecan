from logging import getLogger
from os.path import dirname, isfile
import matplotlib.pyplot as plt
from ezdxf import readfile
from numpy import angle as np_angle
from numpy import array, pi, argmax, argmin
from numpy import max as np_max, min as np_min
from PySide2.QtCore import QUrl, Qt
from PySide2.QtGui import QIcon, QPixmap,QDesktopServices
from PySide2.QtWidgets import (
    QComboBox,
    QDialog,
    QFileDialog,
    QMessageBox,
    QPushButton,
    QHeaderView,
)

from ...Classes.HoleUD import HoleUD
from ...Classes.Magnet import Magnet
from ...Classes.SurfLine import SurfLine
from ...GUI.Dxf.dxf_to_pyleecan_list import dxf_to_pyleecan_list
from ...GUI.Resources import pixmap_dict
from ...GUI.Tools.MPLCanvas import MPLCanvas2
from ...GUI.Tools.FloatEdit import FloatEdit
from ...GUI import gui_option
from ...loggers import GUI_LOG_NAME
from .Ui_DXF_Hole import Ui_DXF_Hole

# Column index for table

DEL_COL = 0
HL_COL = 1
TYPE_COL = 2
REF_COL = 3
OFF_COL = 4

ICON_SIZE = 24
# Unselected, selected, selected-bottom-mag
COLOR_LIST = ["k", "r", "c"]
Z_TOL = 1e-4  # Point comparison tolerance


class DXF_Hole(Ui_DXF_Hole, QDialog):
    """Dialog to create HoleUD objects from DXF files"""

    def __init__(self, dxf_path=None, Zh=None, Lmag=None, lam=None):
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

        # Tutorial video link
        self.url = "https://pyleecan.org/videos.html#feature-tutorials"
        self.b_tuto.setEnabled(True)

        # Set units
        self.lf_mag_len.unit = "m"
        wid_list = [
            self.unit_mag_len,
        ]
        for wid in wid_list:
            wid.setText("[" + gui_option.unit.get_m_name() + "]")

        # Initialize the graph
        self.init_graph()

        # Not used yet
        self.in_coord_center.hide()
        self.lf_center_x.hide()
        self.lf_center_y.hide()
        self.lf_axe_angle.hide()
        self.in_axe_angle.hide()
        self.unit_axe_angle.hide()

        # Set default values
        if Zh is not None:
            self.si_Zh.setValue(Zh)
        if Lmag is not None:
            self.lf_mag_len.setValue(Lmag)
        if lam is None:
            self.lam = lam
        else:
            self.lam = lam.copy()

        # Init properties
        self.line_list = list()  # List of line from DXF
        self.selected_list = list()  # List of currently selected lines
        self.surf_list = list()  # List of defined surfaces
        self.lf_center_x.setValue(0)
        self.lf_center_y.setValue(0)
        self.lf_scaling.validator().setBottom(0)
        self.lf_scaling.setValue(1)

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

        # Set table column width
        header = self.w_surface_list.horizontalHeader()
        header.setSectionResizeMode(DEL_COL, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(HL_COL, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(TYPE_COL, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(REF_COL, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(OFF_COL, QHeaderView.ResizeToContents)

        # Connect signals to slot
        self.w_path_selector.pathChanged.connect(self.open_document)
        self.b_save.pressed.connect(self.save)
        self.b_plot.pressed.connect(self.plot)
        self.b_reset.pressed.connect(self.update_graph)
        self.b_cancel.pressed.connect(self.remove_selection)
        self.b_tuto.pressed.connect(self.open_tuto)

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
            self.surf_list = list()
            self.w_surface_list.setRowCount(0)
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
                if abs(p1 - p2) < Z_TOL:
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
        index_list = list()
        for ii, line in enumerate(self.line_list):
            if self.selected_list[ii]:
                index_list.append(str(ii))
                line_list.append(line.copy())
        # Sort the lines (begin = end)
        curve_list = list()
        curve_list.append(line_list.pop())
        while len(line_list) > 0:
            end = curve_list[-1].get_end()
            for ii in range(len(line_list)):
                if abs(line_list[ii].get_begin() - end) < Z_TOL:
                    break
                if abs(line_list[ii].get_end() - end) < Z_TOL:
                    line_list[ii].reverse()
                    break
            curve_list.append(line_list.pop(ii))
        # Create the Surface object
        self.surf_list.append(SurfLine(line_list=curve_list))
        self.surf_list[-1].comp_point_ref(is_set=True)

        # Add a line in the Table
        nrows = self.w_surface_list.rowCount()
        self.w_surface_list.setRowCount(nrows + 1)
        # Adding Surface Type combobox
        combobox = QComboBox()
        combobox.addItems(["Hole", "Magnet"])
        self.w_surface_list.setCellWidget(
            nrows,
            TYPE_COL,
            combobox,
        )
        if 2 in self.selected_list:
            combobox.setCurrentIndex(1)  # Magnet
        combobox.currentIndexChanged.connect(self.enable_magnetization)

        # Adding Delete button
        del_button = QPushButton("")
        del_button.setIcon(QIcon(self.delete_icon))
        del_button.pressed.connect(self.delete_surface)
        self.w_surface_list.setCellWidget(
            nrows,
            DEL_COL,
            del_button,
        )

        # Adding Highlight button
        HL_button = QPushButton("")
        HL_button.setIcon(QIcon(self.highlight_icon))
        HL_button.pressed.connect(self.highlight_surface)
        self.w_surface_list.setCellWidget(
            nrows,
            HL_COL,
            HL_button,
        )

        # Add reference combobox
        combobox = QComboBox()
        combobox.addItems(index_list)
        self.w_surface_list.setCellWidget(
            nrows,
            REF_COL,
            combobox,
        )
        if 2 in self.selected_list:
            combobox.setCurrentIndex(
                index_list.index(str(self.selected_list.index(2)))
            )  #
        else:
            combobox.setEnabled(False)

        # Add Offset FloatEdit
        lf_off = FloatEdit()
        lf_off.validator().setBottom(-360)
        lf_off.validator().setTop(360)
        lf_off.setValue(0)
        # lf_off.setText("0")
        lf_off.setEnabled(2 in self.selected_list)
        self.w_surface_list.setCellWidget(
            nrows,
            OFF_COL,
            lf_off,
        )

        # Remove selection to start new one
        self.remove_selection()

    def enable_magnetization(self):
        """Enable/Disable the combobox/float edit for magnetization according to type"""
        for ii in range(self.w_surface_list.rowCount()):
            if self.w_surface_list.cellWidget(ii, TYPE_COL).currentIndex() == 0:
                self.w_surface_list.cellWidget(ii, REF_COL).setEnabled(False)
                self.w_surface_list.cellWidget(ii, OFF_COL).setEnabled(False)
            else:
                self.w_surface_list.cellWidget(ii, REF_COL).setEnabled(True)
                self.w_surface_list.cellWidget(ii, OFF_COL).setEnabled(True)

    def remove_selection(self):
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

        if self.lf_scaling.value() == 0:  # Avoid error
            self.lf_scaling.setValue(1)
        hole = HoleUD(surf_list=[])
        bottom_list = list()
        offset_list = list()
        # Set labels
        Nmag = 0
        for ii in range(self.w_surface_list.rowCount()):
            hole.surf_list.append(self.surf_list[ii].copy())
            hole.surf_list[ii].scale(self.lf_scaling.value())
            if self.w_surface_list.cellWidget(ii, TYPE_COL).currentIndex() == 0:
                hole.surf_list[ii].label = "Hole"
            else:
                hole.surf_list[ii].label = "HoleMagnet"
                Nmag += 1
            bottom_list.append(
                self.line_list[
                    int(self.w_surface_list.cellWidget(ii, REF_COL).currentText())
                ]
            )
            offset_list.append(self.w_surface_list.cellWidget(ii, OFF_COL).value())
        # Create magnet objects
        hole.magnet_dict = dict()
        for ii in range(Nmag):
            hole.magnet_dict["magnet_" + str(ii)] = Magnet(type_magnetization=1)

        # Sort the surfaces
        angles = [np_angle(surf.point_ref) for surf in hole.surf_list]
        idx = sorted(range(len(angles)), key=lambda k: angles[k])
        surf_list_sorted = [hole.surf_list[ii] for ii in idx]
        bottom_list_sorted = [bottom_list[ii] for ii in idx]
        offset_list_sorted = [offset_list[ii] for ii in idx]
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
                line = bottom_list_sorted[ii].copy()
                line.rotate(-1 * np_angle(Zref))
                mag_dict["magnet_" + str(Nmag)] = line.comp_normal()
                mag_dict["magnet_" + str(Nmag)] += offset_list_sorted[ii] * pi / 180
                Nmag += 1
        hole.magnetization_dict_offset = mag_dict

        # Set metadata
        hole.Zh = self.si_Zh.value()
        for magnet in hole.magnet_dict.values():
            magnet.Lmag = self.lf_mag_len.value()

        # Remove all materials => To be set in GUI
        hole.mat_void = None
        for magnet in hole.magnet_dict.values():
            magnet.mat_type = None

        # Sort Hole then magnets
        # (for plot when Magnets are inside Hole surface)
        mag_list = list()
        hole_list = list()
        for surf in hole.surf_list:
            if "HoleMagnet" in surf.label:
                mag_list.append(surf)
            else:
                hole_list.append(surf)
        hole.surf_list = hole_list + mag_list

        # Correct hole ref_point (when Magnets are inside Hole surface)
        for surf in hole.surf_list:
            if "HoleMagnet" not in surf.label:
                line_list = surf.get_lines()
                # Get middle list
                middle_array = array([line.get_middle() for line in line_list])
                # Get the extrema line on the top or bottom of the hole
                if np_min(middle_array.imag) > 0 and np_max(middle_array.imag) > 0:
                    start_idx = argmax(middle_array.imag)
                else:
                    start_idx = argmin(middle_array.imag)
                # Get the two lines middle besides the extrema line middle
                if start_idx == 0:
                    ref_mid = [middle_array[-1], middle_array[0], middle_array[1]]
                elif start_idx == len(line_list) - 1:
                    ref_mid = [middle_array[-2], middle_array[-1], middle_array[0]]
                else:
                    ref_mid = [
                        middle_array[start_idx - 1],
                        middle_array[start_idx],
                        middle_array[start_idx + 1],
                    ]
                # Barycenter of these middles as new reference
                surf.point_ref = sum(ref_mid) / 3

        return hole

    def plot(self):
        """Plot the current state of the hole

        Parameters
        ----------
        self : DXF_Hole
            a DXF_Hole object
        """
        hole = self.get_hole()
        if self.lam is None:
            hole.plot(is_add_arrow=True)
        else:
            fig, (ax1, ax2) = plt.subplots(1, 2)
            hole.plot(fig=fig, ax=ax1, is_add_arrow=True, is_add_ref=False)
            self.lam.hole = [hole]
            self.lam.plot(fig=fig, ax=ax2)

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
                if abs(mid - line.get_middle()) < Z_TOL:
                    self.selected_list[ii] = 1
                    self.w_viewer.axes.text(
                        mid.real,
                        mid.imag,
                        str(ii),
                        # fontsize=fontsize,
                    )
        self.update_graph()
        # Add Label
        for ii in range(len(self.selected_list)):
            if self.selected_list[ii] == 1:
                Zmid = self.line_list[ii].get_middle()
                self.w_viewer.axes.text(
                    Zmid.real,
                    Zmid.imag,
                    str(ii),
                    # fontsize=fontsize,
                )

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

    def open_tuto(self):
        """Open the tutorial video in a web browser"""
        QDesktopServices.openUrl(QUrl(self.url))