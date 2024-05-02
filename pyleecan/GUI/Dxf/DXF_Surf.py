from logging import getLogger
from os.path import dirname, isfile, splitext, basename
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT as NavigationToolbar,
)
from ezdxf import readfile
from numpy import angle as np_angle
from numpy import array, pi, argmax, argmin
from numpy import max as np_max, min as np_min
from qtpy.QtCore import QUrl, Qt
from qtpy.QtGui import QIcon, QPixmap, QDesktopServices
from qtpy.QtWidgets import (
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
from ...GUI.Dxf.dxf_to_pyleecan import dxf_to_pyleecan_list, convert_dxf_with_FEMM
from ...GUI.Resources import pixmap_dict
from ...GUI.Tools.MPLCanvas import MPLCanvas
from ...GUI.Tools.FloatEdit import FloatEdit
from ...GUI import gui_option
from ...loggers import GUI_LOG_NAME
from .Ui_DXF_Surf import Ui_DXF_Surf
from ...Functions.labels import HOLEM_LAB, HOLEV_LAB
from ...Functions.init_fig import init_fig

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


class DXF_Surf(Ui_DXF_Surf, QDialog):
    """Dialog to create Vents or BoreUD objects from DXF files"""

    convert_dxf_with_FEMM = convert_dxf_with_FEMM

    def __init__(self, dxf_path=None, Zh=None, lam=None, is_vent=True):
        """Initialize the Dialog

        Parameters
        ----------
        self : DXF_Surf
            a DXF_Surf object
        dxf_path : str
            Path to a dxf file to read
        """
        # Widget setup
        QDialog.__init__(self)
        self.setupUi(self)

        # Tutorial video link
        self.url = "https://pyleecan.org/videos.html#feature-tutorials"
        self.b_tuto.setEnabled(False)

        # Initialize the graph
        self.init_graph()

        # Set default values
        if Zh is not None:
            self.si_Zh.setValue(Zh)
        if lam is None:
            self.lam = lam
        else:
            self.lam = lam.copy()

        # Init properties
        self.line_list = list()  # List of line from DXF
        self.selected_list = list()  # List of currently selected lines
        self.Zcenter = 0  # For translate offset

        # Set DXF edit widget
        self.lf_center_x.setValue(0)
        self.lf_center_y.setValue(0)
        self.lf_scaling.validator().setBottom(0)
        self.lf_scaling.setValue(1)

        # Not available Yet (for BoreUD)
        self.in_per_a.hide()
        self.si_per_a.hide()

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

        # Connect signals to slot
        self.w_path_selector.pathChanged.connect(self.open_document)
        self.b_save.pressed.connect(self.save)
        self.b_plot.pressed.connect(self.plot)
        self.b_reset.pressed.connect(self.update_graph)
        self.b_cancel.pressed.connect(self.remove_selection)
        self.b_tuto.pressed.connect(self.open_tuto)
        self.is_convert.toggled.connect(self.enable_tolerance)
        self.lf_center_x.editingFinished.connect(self.set_center)
        self.lf_center_y.editingFinished.connect(self.set_center)

        # Display the GUI
        self.show()

    def enable_tolerance(self):
        """Enable/Disable tolerance widget"""
        self.lf_tol.setEnabled(self.is_convert.isChecked())
        self.in_tol.setEnabled(self.is_convert.isChecked())

    def open_document(self):
        """Open a new dxf in the viewer

        Parameters
        ----------
        self : DXF_Surf
            a DXF_Surf object
        """

        # Check convertion
        if self.is_convert.isChecked():
            getLogger(GUI_LOG_NAME).info("Converting dxf file: " + self.dxf_path)
            self.dxf_path = self.convert_dxf_with_FEMM(
                self.dxf_path, self.lf_tol.value()
            )
            self.w_path_selector.blockSignals(True)
            self.w_path_selector.set_path_txt(self.dxf_path)
            self.w_path_selector.blockSignals(False)

        getLogger(GUI_LOG_NAME).debug("Reading dxf file: " + self.dxf_path)
        # Read the DXF file
        try:
            document = readfile(self.dxf_path)
            modelspace = document.modelspace()
            # Convert DXF to pyleecan objects
            self.line_list = dxf_to_pyleecan_list(modelspace)
            # Display
            # selected line: 0: unselected, 1:selected
            self.selected_list = [0 for line in self.line_list]
            self.surf_list = list()
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
        self : DXF_Surf
            a DXF_Surf object
        """
        # Init fig
        fig, axes = plt.subplots(tight_layout=False)
        self.fig = fig
        self.axes = axes
        # Set plot layout
        canvas = FigureCanvasQTAgg(fig)
        toolbar = NavigationToolbar(canvas, self)
        # Remove Subplots button
        unwanted_buttons = ["Subplots", "Customize", "Save"]
        for x in toolbar.actions():
            if x.text() in unwanted_buttons:
                toolbar.removeAction(x)
        # Adding custom icon on mpl toobar
        icons_buttons = [
            "Home",
            "Pan",
            "Zoom",
            "Back",
            "Forward",
        ]
        for action in toolbar.actions():
            if action.text() in icons_buttons and "mpl_" + action.text() in pixmap_dict:
                action.setIcon(QIcon(pixmap_dict["mpl_" + action.text()]))
        # Change default file name
        canvas.get_default_filename = "DXF_Surf_visu.png"
        self.layout_plot.insertWidget(1, toolbar)
        self.layout_plot.insertWidget(2, canvas)
        self.canvas = canvas
        axes.set_axis_off()
        self.toolbar = toolbar
        self.xlim = self.axes.get_xlim()
        self.ylim = self.axes.get_ylim()

        def on_draw(event):
            self.xlim = self.axes.get_xlim()
            self.ylim = self.axes.get_ylim()

        # Setup interaction with graph
        def select_line(event):
            """Function to select/unselect the closest line from click"""
            # Ignore if matplotlib action is clicked
            is_ignore = False
            for action in self.toolbar.actions():
                if action.isChecked():
                    is_ignore = True
            if not is_ignore:
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
                elif self.selected_list[closest_id] == 1:
                    # selected to Unselected
                    self.selected_list[closest_id] = 0
                # Change line color
                point_list = array(self.line_list[closest_id].discretize(20))
                color = COLOR_LIST[self.selected_list[closest_id]]
                axes.plot(point_list.real, point_list.imag, color, zorder=2)
                self.axes.set_xlim(self.xlim)
                self.axes.set_ylim(self.ylim)
                self.canvas.draw()

        def zoom(event):
            """Function to zoom/unzoom according the mouse wheel"""

            base_scale = 0.8  # Scaling factor
            # get the current x and y limits
            ax = self.axes
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
            self.canvas.draw()  # force re-draw

        # Connect the function
        self.canvas.mpl_connect("draw_event", on_draw)
        self.canvas.mpl_connect("button_press_event", select_line)
        self.canvas.mpl_connect("scroll_event", zoom)

        # Axis cleanup
        axes.axis("equal")
        axes.set_axis_off()

    def set_center(self):
        """Update the position of the center"""
        self.Zcenter = self.lf_center_x.value() + 1j * self.lf_center_y.value()
        self.update_graph()

    def update_graph(self):
        """Clean and redraw all the lines in viewer

        Parameters
        ----------
        self : DXF_Surf
            a DXF_Surf object
        """
        fig, axes = self.fig, self.axes
        axes.clear()
        axes.set_axis_off()

        # Draw the lines in the correct color
        for ii, line in enumerate(self.line_list):
            point_list = array(line.discretize(20))
            color = COLOR_LIST[self.selected_list[ii]]
            axes.plot(point_list.real, point_list.imag, color, zorder=1)
        # Add lamination center
        axes.plot(self.Zcenter.real, self.Zcenter.imag, "rx", zorder=0)
        axes.text(self.Zcenter.real, self.Zcenter.imag, "O")

        self.canvas.draw()

    def check_selection(self):
        """Check if every line in the selection form a surface

        Parameters
        ----------
        self : DXF_Surf
            a DXF_Surf object

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

    def get_surface(self):
        """Validate the selection and create a surface object

        Parameters
        ----------
        self : DXF_Surf
            a DXF_Surf object
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
        surf = SurfLine(line_list=curve_list)
        surf.comp_point_ref(is_set=True)
        return surf

    def remove_selection(self):
        # Remove selection
        self.selected_list = [0 for line in self.line_list]
        # Redraw all the lines (in black)
        for ii, line in enumerate(self.line_list):
            point_list = array(line.discretize(20))
            color = COLOR_LIST[self.selected_list[ii]]
            self.axes.plot(point_list.real, point_list.imag, color, zorder=2)
        self.canvas.draw()

    def get_hole(self):
        """Generate the HoleUD object corresponding to the selected surfaces

        Parameters
        ----------
        self : DXF_Surf
            a DXF_Surf object

        Returns
        -------
        hole : HoleUD
            User defined hole according to selected surfaces
        """

        if self.lf_scaling.value() == 0:  # Avoid error
            self.lf_scaling.setValue(1)
        surf = self.get_surface()
        surf.scale(self.lf_scaling.value())
        surf.label = HOLEV_LAB
        hole = HoleUD(surf_list=[surf])

        # Translate
        if self.Zcenter != 0:
            surf.translate(-self.Zcenter * self.lf_scaling.value())

        # Rotation
        surf.rotate(-1 * np_angle(surf.point_ref))

        # Set metadata
        hole.Zh = self.si_Zh.value()

        # Remove materials => To be set in GUI
        hole.mat_void = None

        return hole

    def plot(self):
        """Plot the current state of the hole

        Parameters
        ----------
        self : DXF_Surf
            a DXF_Surf object
        """
        hole = self.get_hole()
        if self.lam is None:
            hole.plot(is_add_arrow=True)
        else:
            fig, (ax1, ax2) = plt.subplots(1, 2)
            hole.plot(fig=fig, ax=ax1, is_add_arrow=True, is_add_ref=False)
            self.lam.axial_vent = [hole]
            self.lam.plot(fig=fig, ax=ax2)

    def save(self):
        """Save the HoleUD object in a json file

        Parameters
        ----------
        self : DXF_Surf
            a DXF_Surf object
        """

        hole = self.get_hole()

        save_file_path = QFileDialog.getSaveFileName(
            self, self.tr("Save file"), dirname(self.dxf_path), "Json (*.json)"
        )[0]
        if save_file_path not in ["", ".json", None]:
            self.save_path = save_file_path
            hole.name = splitext(basename(self.save_path))[0]
            try:
                hole.save(save_file_path)
                self.accept()
            except Exception as e:
                QMessageBox().critical(
                    self,
                    self.tr("Error"),
                    self.tr("Error while saving hole json file:\n" + str(e)),
                )

    def open_tuto(self):
        """Open the tutorial video in a web browser"""
        QDesktopServices.openUrl(QUrl(self.url))
