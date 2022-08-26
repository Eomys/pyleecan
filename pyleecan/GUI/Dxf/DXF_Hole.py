from logging import getLogger
from os.path import dirname, isfile, splitext, basename
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT as NavigationToolbar,
)
from ezdxf import readfile
import numpy as np
from PySide2.QtCore import QUrl, Qt
from PySide2.QtGui import QIcon, QPixmap, QDesktopServices
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
from ...GUI.Dxf.dxf_to_pyleecan import dxf_to_pyleecan_list, convert_dxf_with_FEMM
from ...GUI.Resources import pixmap_dict
from ...GUI.Tools.MPLCanvas import MPLCanvas
from ...GUI.Tools.FloatEdit import FloatEdit
from ...GUI import gui_option
from ...loggers import GUI_LOG_NAME
from .Ui_DXF_Hole import Ui_DXF_Hole
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
AUTO_SELECT = True
IS_ADD_LINE_ID = False  # For debug


class DXF_Hole(Ui_DXF_Hole, QDialog):
    """Dialog to create HoleUD objects from DXF files"""

    convert_dxf_with_FEMM = convert_dxf_with_FEMM

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
        self.line_list = list()  # List of lines from DXF
        self.selected_line = np.array([])  # Array of selected lines indices
        self.surf_list = list()  # List of defined surfaces
        self.Zcenter = 0  # For translate offset

        # Connection related variables
        # matrix of points coordinates (ndarray[Npoint, 2])
        self.point_coord = None
        # start point id (in point_coord) and end point id for each line (ndarray[Nline, 2])
        self.line2point = None
        # lines id (in line_list) connected to each point (list[Npoints, n])
        self.point2line = None

        # Set DXF edit widget
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
        self : DXF_Hole
            a DXF_Hole object
        """

        # Check convertion
        if self.is_convert.isChecked() and "_converted" not in basename(self.dxf_path):
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
            # selected line: 0: unselected, 1:selected, 2: selected bottom magnet
            self.selected_line = np.zeros(len(self.line_list), dtype=int)
            self.surf_list = list()
            self.w_surface_list.setRowCount(0)
            # Calculate connection matrix and matrix of points coordinates
            if AUTO_SELECT:
                self.comp_connection()
            # Display
            self.update_graph()
        except Exception as e:
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr("Error while reading dxf file:\n" + str(e)),
            )

    def comp_connection(self):
        """Calculate connection matrices:
            - line2point: start point id and end point id for each line (ndarray[Nline, 2])
            - point2lines: lines id connected to each point (list[Npoints, n])
            - point_coord: matrix of points coordinates (ndarray[Npoint, 2])

        Parameters
        ----------
        self : DXF_Hole
            a DXF_Hole object
        """

        line2point = np.zeros((len(self.line_list), 2), dtype=int)
        point_coord = list()
        point2line = list()
        for ii, line in enumerate(self.line_list):
            # Add begin point
            point_begin = line.get_begin()
            # Tolerance to avoid duplicate points
            index = np.where(np.abs(np.array(point_coord) - point_begin) < Z_TOL)[0]
            if len(index) == 1:
                point_id = index[0]
                line2point[ii, 0] = point_id
                point2line[point_id].append(ii)
            else:
                point_coord.append(point_begin)
                line2point[ii, 0] = len(point_coord) - 1
                point2line.append([ii])
            # Add end point
            point_end = line.get_end()
            index = np.where(np.abs(np.array(point_coord) - point_end) < Z_TOL)[0]
            if len(index) == 1:
                point_id = index[0]
                line2point[ii, 1] = point_id
                point2line[point_id].append(ii)
            else:
                point_coord.append(point_end)
                line2point[ii, 1] = len(point_coord) - 1
                point2line.append([ii])

        # Store connection matrix for later use
        self.line2point = line2point
        self.point2line = point2line

        # Convert point list to matrix
        point_coord = np.array(point_coord, dtype=complex)
        self.point_coord = np.zeros((point_coord.size, 2))
        self.point_coord[:, 0] = np.real(point_coord)
        self.point_coord[:, 1] = np.imag(point_coord)

    def get_closest_line_id(self, X, Y):
        """Get closest line id to input X and Y coordinates

        Parameters
        ----------
        self : DXF_Hole
            a DXF_Hole object
        X: float
            x coordinate
        Y: float
            y coordinate
        """

        point2line = self.point2line
        line_list = self.line_list

        # Get 10 closest points to click coordinates
        x = self.point_coord[:, 0]
        y = self.point_coord[:, 1]
        Npts = min([10, x.size])
        Ipts = np.argpartition((x - X) ** 2 + (y - Y) ** 2, Npts)[:Npts]

        # Find all line indices containing 10 closest
        Ilin = list()
        for ii in Ipts:
            Ilin.extend(point2line[ii])
        Ilin = np.unique(Ilin)

        # Find id of closest line
        Z = X + 1j * Y  # XY position as complex number
        point_dist = [line_list[ii].comp_distance(Z) for ii in Ilin]
        closest_id = Ilin[np.argmin(point_dist)]

        return closest_id

    def get_connected_lines(self, connected_lines, lin_curr, pt_curr):
        """Get connected lines to the current line starting at the current point
        (need to call method on both end points of the lines)
        return if the connected lines results in a closed surface and extend connected_lines

        Parameters
        ----------
        self : DXF_Hole
            a DXF_Hole object
        connected_lines: list
            List of line index connected to current line and point
        lin_curr: int
            current line id
        pt_curr: int
            current point id

        Results
        ----------
        is_closed: bool
            True if the connected lines results in a closed surface
        """

        line2point = self.line2point
        point2line = self.point2line

        is_closed = False
        is_next = True  # Is there another line to select
        while is_next:
            l_i = point2line[pt_curr]  # list of line connected to the point
            if len(l_i) == 2:
                # We select the next line only if the point is connected to 2 lines
                next_line = l_i[0] if l_i[1] == lin_curr else l_i[1]
                if next_line not in connected_lines:
                    connected_lines.append(next_line)
                    lin_curr = next_line
                    p_i = line2point[lin_curr]
                    pt_curr = p_i[0] if p_i[1] == pt_curr else p_i[1]
                else:  # Next line is already in connected lines
                    is_next = False
                    is_closed = True
            else:
                is_next = False

        return is_closed

    def init_graph(self):
        """Initialize the viewer

        Parameters
        ----------
        self : DXF_Hole
            a DXF_Hole object
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
        canvas.get_default_filename = "DXF_hole_visu.png"
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

                # Get id of closest line to click
                closest_id = self.get_closest_line_id(X, Y)

                connected_lines = [closest_id]
                is_closed = False
                # If the line is not already selected (else edit only the line)
                if self.selected_line[closest_id] == 0 and AUTO_SELECT:
                    # Select all points starting from begin point
                    lin_curr = closest_id
                    pt_curr = self.line2point[closest_id, 0]
                    is_closed = self.get_connected_lines(
                        connected_lines, lin_curr, pt_curr
                    )
                    # Select all points starting from end point
                    if not is_closed:
                        lin_curr = closest_id
                        pt_curr = self.line2point[closest_id, 1]
                        is_closed = self.get_connected_lines(
                            connected_lines, lin_curr, pt_curr
                        )
                    # Make sure that all the lines will be set to "1"
                    for index in connected_lines:
                        self.selected_line[index] = 0

                # Select/unselect line (needed for add_surface)
                for id_line in connected_lines:
                    if self.selected_line[id_line] == 0:
                        # Unselected to selected
                        self.selected_line[id_line] = 1
                    elif self.selected_line[id_line] == 1:
                        # Selected to selected bottom mag
                        Imag = np.where(self.selected_line == 2)[0]
                        if Imag.size > 0:
                            current_bot_mag = Imag[0]
                            # Only one selected bottom mag line at the time
                            point_list = np.array(
                                self.line_list[current_bot_mag].discretize(20)
                            )
                            self.selected_line[current_bot_mag] = 1
                            axes.plot(
                                point_list.real,
                                point_list.imag,
                                COLOR_LIST[1],
                                zorder=2,
                            )
                        self.selected_line[id_line] = 2
                    elif self.selected_line[id_line] == 2:
                        # selected bottom mag to Unselected
                        self.selected_line[id_line] = 0

                # Check if the surface is complete
                # (is_close=True: surface selected in one click)
                if is_closed or self.check_selection():
                    self.add_surface()
                else:  # Update line color on plot
                    for id_line in connected_lines:
                        point_list = np.array(self.line_list[id_line].discretize(20))
                        color = COLOR_LIST[self.selected_line[id_line]]
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
        self : DXF_Hole
            a DXF_Hole object
        """

        _, axes = self.fig, self.axes
        axes.clear()
        axes.set_axis_off()

        # Draw the lines in the correct color
        for ii, line in enumerate(self.line_list):
            point_list = np.array(line.discretize(20))
            color = COLOR_LIST[self.selected_line[ii]]
            axes.plot(point_list.real, point_list.imag, color, zorder=1)
            if IS_ADD_LINE_ID:
                Zmid = line.get_middle()
                axes.text(Zmid.real, Zmid.imag, str(ii))
        # Add lamination center
        axes.plot(self.Zcenter.real, self.Zcenter.imag, "rx", zorder=0)
        axes.text(self.Zcenter.real, self.Zcenter.imag, "O")

        self.canvas.draw()

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

        Iselect = np.where(self.selected_line)[0]
        if len(Iselect) == 0:  # No line selected
            return False
        # line2point contains index (int), no need for Z_tol
        _, count0 = np.unique(self.line2point[Iselect, :].ravel(), return_counts=True)

        return np.all(count0 == 2)

    def sort_lines(self):
        """Sort selected lines so that current line's starting point is the same as previous line's ending point
        and that current line's ending point is the same as next line's start point

        Parameters
        ----------
        self : DXF_Hole
            a DXF_Hole object

        Returns
        -------
        curve_list : [Line]
            List of sorted lines
        str_list: [str]
            List of line indices as str (to be printed in combobox)
        """

        Iselect = np.where(self.selected_line)[0]

        l2p = self.line2point

        p2l_select = list()
        for lines in self.point2line:
            if len(lines) == 2:
                p2l_select.append(lines)
            else:
                p2l_select.append([ll for ll in lines if ll in Iselect])

        ii = Iselect[0]
        pt_start = l2p[ii, 0]
        pt_curr = l2p[ii, 1]
        index_list = [ii]
        curve_list = [self.line_list[ii].copy()]
        while pt_curr != pt_start:
            l_i = p2l_select[pt_curr]
            kk = l_i[1] if l_i[0] in index_list else l_i[0]
            index_list.append(kk)
            line_k = self.line_list[kk].copy()
            if pt_curr == l2p[kk, 0]:
                pt_curr = l2p[kk, 1]
            elif pt_curr == l2p[kk, 1]:
                pt_curr = l2p[kk, 0]
                line_k.reverse()
            curve_list.append(line_k)

        str_list = [str(kk) for kk in index_list]

        return curve_list, str_list

    def add_surface(self):
        """Validate the selection and create a surface object

        Parameters
        ----------
        self : DXF_Hole
            a DXF_Hole object
        """

        # Sort the selected lines (begin = end)
        curve_list, str_list = self.sort_lines()

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
        if np.any(self.selected_line == 2):
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
        combobox.addItems(str_list)
        self.w_surface_list.setCellWidget(
            nrows,
            REF_COL,
            combobox,
        )
        Imag = np.where(self.selected_line == 2)[0]
        if Imag.size > 0:
            combobox.setCurrentIndex(str_list.index(str(Imag[0])))
        else:
            combobox.setEnabled(False)

        # Add Offset FloatEdit
        lf_off = FloatEdit()
        lf_off.validator().setBottom(-360)
        lf_off.validator().setTop(360)
        lf_off.setValue(0)
        # lf_off.setText("0")
        lf_off.setEnabled(np.any(self.selected_line == 2))
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
        self.selected_line = np.zeros(len(self.line_list), dtype=int)
        # Redraw all the lines (in black)
        for ii, line in enumerate(self.line_list):
            point_list = np.array(line.discretize(20))
            color = COLOR_LIST[self.selected_line[ii]]
            self.axes.plot(point_list.real, point_list.imag, color, zorder=2)
        self.canvas.draw()

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
                hole.surf_list[ii].label = HOLEV_LAB
            else:
                hole.surf_list[ii].label = HOLEM_LAB
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
        angles = [np.angle(surf.point_ref) for surf in hole.surf_list]
        idx = sorted(range(len(angles)), key=lambda k: angles[k])
        surf_list_sorted = [hole.surf_list[ii] for ii in idx]
        bottom_list_sorted = [bottom_list[ii] for ii in idx]
        offset_list_sorted = [offset_list[ii] for ii in idx]
        hole.surf_list = surf_list_sorted

        # Translate
        if self.Zcenter != 0:
            for surf in hole.surf_list:
                surf.translate(-self.Zcenter * self.lf_scaling.value())

        # Rotation
        Zref = sum([surf.point_ref for surf in hole.surf_list])
        for surf in hole.surf_list:
            surf.rotate(-1 * np.angle(Zref))

        # Magnetization dict
        mag_dict = dict()
        Nmag = 0
        for ii in range(len(hole.surf_list)):
            if HOLEM_LAB in hole.surf_list[ii].label:
                line = bottom_list_sorted[ii].copy()
                line.rotate(-1 * np.angle(Zref))
                mag_dict["magnet_" + str(Nmag)] = line.comp_normal()
                mag_dict["magnet_" + str(Nmag)] += offset_list_sorted[ii] * np.pi / 180
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
            if HOLEM_LAB in surf.label:
                mag_list.append(surf)
            else:
                hole_list.append(surf)
        hole.surf_list = hole_list + mag_list

        # Correct hole ref_point (when Magnets are inside Hole surface)
        for surf in hole.surf_list:
            if HOLEV_LAB in surf.label:
                line_list = surf.get_lines()
                # Get middle list
                middle_array = np.array([line.get_middle() for line in line_list])
                # Get the extrema line on the top or bottom of the hole
                if np.min(middle_array.imag) > 0 and np.max(middle_array.imag) > 0:
                    start_idx = np.argmax(middle_array.imag)
                else:
                    start_idx = np.argmin(middle_array.imag)
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
        self.selected_line = np.zeros(len(self.line_list), dtype=int)
        surf = self.surf_list[self.w_surface_list.currentRow()]
        # Find the index of the surface line in self.line_list
        for surf_line in surf.line_list:
            mid = surf_line.get_middle()
            for ii, line in enumerate(self.line_list):
                if abs(mid - line.get_middle()) < Z_TOL:
                    self.selected_line[ii] = 1
                    self.axes.text(
                        mid.real,
                        mid.imag,
                        str(ii),
                        # fontsize=fontsize,
                    )
        self.update_graph()
        # Add Label
        for ii in range(len(self.selected_line)):
            if self.selected_line[ii] == 1:
                Zmid = self.line_list[ii].get_middle()
                self.axes.text(
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
