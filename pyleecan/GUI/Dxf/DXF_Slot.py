from logging import getLogger
from os.path import dirname, isfile, basename, splitext

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT as NavigationToolbar,
)
from ezdxf import readfile
from numpy import angle as np_angle
from numpy import argmin, array, exp, angle
from PySide2.QtCore import QSize, Qt, QUrl
from PySide2.QtGui import QIcon, QPixmap, QFont, QDesktopServices
from PySide2.QtWidgets import QComboBox, QDialog, QFileDialog, QMessageBox, QPushButton


from ...Classes.LamSlot import LamSlot
from ...Classes.SlotUD import SlotUD
from ...Classes.Segment import Segment
from ...definitions import config_dict
from ...Functions.Plot.set_plot_gui_icon import set_plot_gui_icon
from ...GUI.Dxf.dxf_to_pyleecan import dxf_to_pyleecan_list, convert_dxf_with_FEMM
from ...GUI.Resources import pixmap_dict
from ...GUI.Tools.MPLCanvas import MPLCanvas
from ...loggers import GUI_LOG_NAME
from .Ui_DXF_Slot import Ui_DXF_Slot
from ...Functions.init_fig import init_fig

# Column index for table
TYPE_COL = 0
DEL_COL = 1
HL_COL = 2
WIND_COLOR = config_dict["PLOT"]["COLOR_DICT"]["BAR_COLOR"]
FONT_SIZE = 12
FONT_NAME = config_dict["PLOT"]["FONT_NAME"]
Z_TOL = 1e-4  # Point comparison tolerance


class DXF_Slot(Ui_DXF_Slot, QDialog):
    """Dialog to create SlotUD objects from DXF files"""

    convert_dxf_with_FEMM = convert_dxf_with_FEMM

    def __init__(self, dxf_path=None, Zs=None, lam=None, is_notch=False):
        """Initialize the Dialog

        Parameters
        ----------
        self : DXF_Slot
            a DXF_Slot object
        dxf_path : str
            Path to a dxf file to read
        Zs : int
            Number of slot/notch
        lam : Lamination
            Lamination to add the slot to
        is_notch : bool
            True if the DXF is meant for a notch
        """
        # Widget setup
        QDialog.__init__(self)
        self.setupUi(self)

        # Init properties
        self.line_list = list()  # List of line from DXF
        self.selected_list = list()  # List of currently selected lines
        self.lam = lam
        self.is_notch = is_notch
        self.Zcenter = 0  # For offset

        # Tutorial video link
        self.url = "https://pyleecan.org/videos.html#feature-tutorials"
        self.b_tuto.setEnabled(True)

        # Adapt GUI for notches
        if self.is_notch:
            self.g_active.hide()
            self.in_Zs.setText("Number of notches")
            self.setWindowTitle("Define Notch from DXF")

        # Initialize the graph
        self.init_graph()

        # Not used yet
        self.lf_axe_angle.hide()
        self.in_axe_angle.hide()

        # Set DXF edit widget
        self.lf_center_x.setValue(0)
        self.lf_center_y.setValue(0)
        self.lf_scaling.validator().setBottom(0)
        self.lf_scaling.setValue(1)

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

        # Set font
        font = QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(FONT_SIZE)
        self.textBrowser.setFont(font)

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
        self : DXF_Slot
            a DXF_Slot object
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
        canvas.get_default_filename = "DXF_slot_visu.png"
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
                self.selected_list[closest_id] = not self.selected_list[closest_id]
                # Change line color
                point_list = array(self.line_list[closest_id].discretize(20))
                if self.selected_list[closest_id]:
                    color = "r"
                else:
                    color = "k"
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
        self : DXF_Slot
            a DXF_Slot object
        """
        fig, axes = self.fig, self.axes
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
        # Add lamination center
        axes.plot(self.Zcenter.real, self.Zcenter.imag, "rx", zorder=0)
        axes.text(self.Zcenter.real, self.Zcenter.imag, "O")

        self.canvas.draw()

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
                if abs(p1 - p2) < Z_TOL:
                    count += 1
            if count == 1:
                count_1 += 1
                if count_1 > 2:
                    return False
            elif count != 2:
                return False

        return True

    def remove_selection(self):
        # Remove selection
        self.selected_list = [False for line in self.line_list]
        self.update_graph()

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

        if self.lf_scaling.value() in [0, None]:  # Avoid error
            self.lf_scaling.setValue(1)

        # Get all the selected lines at proper scale
        line_list = list()
        point_list = list()  # List of all begin, end of all the lines
        for ii, line in enumerate(self.line_list):
            if self.selected_list[ii]:
                line_list.append(line.copy())
                line_list[-1].scale(self.lf_scaling.value())
                point_list.append(line_list[-1].get_begin())
                point_list.append(line_list[-1].get_end())

        # Find begin point
        single_list = list()
        # In point list all point should be present twice
        # except first and last point
        for p1 in point_list:
            count = 0
            for p2 in point_list:
                if abs(p1 - p2) < Z_TOL:
                    count += 1
            if count == 1:
                single_list.append(p1)
        assert (
            len(single_list) == 2
        ), "Unable to detect first and last point of the slot"
        # Lines must be returned in trigo order center on Ox
        # Begin selection can be wrong, corrected if needed after rotate
        Zbegin = single_list[argmin(np_angle(array(single_list)))]
        # Get First line
        id_list = list()
        id_list.extend(
            [
                ii
                for ii, line in enumerate(line_list)
                if abs(line.get_begin() - Zbegin) < Z_TOL
                or abs(line.get_end() - Zbegin) < Z_TOL
            ]
        )
        # Sort the lines (find line with current.end == line.begin)
        curve_list = list()
        curve_list.append(line_list.pop(id_list[0]))
        if abs(curve_list[0].get_end() - Zbegin) < Z_TOL:
            # Reverse begin line if line end matches with begin point
            curve_list[0].reverse()
        while len(line_list) > 0:
            end = curve_list[-1].get_end()
            for ii in range(len(line_list)):
                if abs(line_list[ii].get_begin() - end) < Z_TOL:
                    break
                if abs(line_list[ii].get_end() - end) < Z_TOL:
                    line_list[ii].reverse()
                    break
            curve_list.append(line_list.pop(ii))

        # Translate
        if self.Zcenter != 0:
            for line in curve_list:
                line.translate(-self.Zcenter * self.lf_scaling.value())

        # Check the first and last point are matching Rint
        Rbo = self.lam.get_Rbo()
        Zbegin = curve_list[0].get_begin()
        Zend = curve_list[-1].get_end()
        if abs(abs(Zbegin) - Rbo) > Z_TOL:
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr(
                    "First point of the slot is not on the bore radius:\nBore radius="
                    + format(Rbo, ".6g")
                    + ", abs(First point)="
                    + format(abs(Zbegin), ".6g")
                ),
            )

            return None
        if abs(abs(Zend) - Rbo) > Z_TOL:
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr(
                    "Last point of the slot is not on the bore radius:\nBore radius="
                    + format(Rbo, ".6g")
                    + ", abs(Last point)="
                    + format(abs(Zend), ".6g")
                ),
            )
            return None

        # Rotation
        Z1 = curve_list[0].get_begin()
        Z2 = curve_list[-1].get_end()
        alpha = (np_angle(Z2) + np_angle(Z1)) / 2
        for line in curve_list:
            line.rotate(-1 * alpha)

        # Enforce perfect match with Bore radius by adding Segments in needed
        Zbegin = curve_list[0].get_begin()
        Zb2 = Rbo * exp(1j * angle(Zbegin))
        if abs(Zb2 - Zbegin) > 1e-9:
            curve_list.insert(0, Segment(begin=Zb2, end=Zbegin))

        Zend = curve_list[-1].get_end()
        Ze2 = Rbo * exp(1j * angle(Zend))
        if abs(Ze2 - Zend) > 1e-9:
            curve_list.append(Segment(begin=Zend, end=Ze2))

        # Check that the lines are in trigo order (can be reversed for inner slot)
        if angle(curve_list[0].get_begin()) > angle(curve_list[-1].get_end()):
            curve_list = curve_list[::-1]
            for line in curve_list:
                line.reverse()

        # Create the Slot object
        slot = SlotUD(line_list=curve_list)
        slot.type_line_wind = self.c_type_line.currentIndex()
        begin_id = self.si_wind_begin_index.value()
        end_id = self.si_wind_end_index.value()
        if begin_id == 0 and end_id == 0:  # Not defined yet
            slot.wind_begin_index = None
            slot.wind_end_index = None
        elif (
            begin_id < len(curve_list)
            and end_id < len(curve_list)
            # and begin_id < end_id
        ):
            slot.wind_begin_index = begin_id
            slot.wind_end_index = end_id
        else:  # Wrong definition
            slot.wind_begin_index = None
            slot.wind_end_index = None
        if self.is_notch:
            slot.wind_begin_index = None
            slot.wind_end_index = None
        slot.Zs = self.si_Zs.value()

        return slot

    def plot(self):
        """Plot the current state of the slot

        Parameters
        ----------
        self : DXF_Slot
            a DXF_Slot object
        """
        if self.check_selection():
            try:
                slot = self.get_slot()
            except Exception as e:
                err_msg = "Error in DXF slot definition:\n" + str(e)
                QMessageBox().critical(
                    self,
                    self.tr("Error"),
                    err_msg,
                )
                return

            if slot is None:
                return  # Uncorrect slot
            # Lamination definition
            if self.lam is None:
                lam = LamSlot(slot=slot)
                Rbo = abs(slot.line_list[0].get_begin())
            else:
                lam = self.lam.copy()
                lam.slot = slot
            try:
                # Left single slot with point index, Right Lamination with slot
                fig, (ax1, ax2) = plt.subplots(1, 2)
                slot.plot(fig=fig, ax=ax1)
                # Add the winding to slot if defined
                if not self.is_notch and slot.wind_begin_index is not None:
                    surf_wind = slot.get_surface_active()
                    surf_wind.plot(fig=fig, ax=ax1, color=WIND_COLOR, is_show_fig=False)
                if not self.is_notch:
                    # Add point index for winding definition
                    index = 0
                    for line in slot.line_list:
                        Zb = line.get_begin()
                        ax1.plot(Zb.real, Zb.imag, "rx", zorder=0)
                        ax1.text(Zb.real, Zb.imag, str(index))
                        index += 1
                    Ze = slot.line_list[-1].get_end()
                    ax1.plot(Ze.real, Ze.imag, "rx", zorder=0)
                    ax1.text(Ze.real, Ze.imag, str(index))
                # Plot lamination with slot and winding (if needed)
                lam.plot(fig=fig, ax=ax2, is_lam_only=self.is_notch)
                set_plot_gui_icon()
            except Exception as e:
                err_msg = "Error while plotting DXF imported slot:\n" + str(e)
                QMessageBox().critical(
                    self,
                    self.tr("Error"),
                    err_msg,
                )
                return

    def save(self):
        """Save the SlotUD object in a json file

        Parameters
        ----------
        self : DXF_Slot
            a DXF_Slot object
        """

        if self.check_selection():
            try:
                slot = self.get_slot()
            except Exception as e:
                err_msg = "Error in DXF slot definition:\n" + str(e)
                QMessageBox().critical(
                    self,
                    self.tr("Error"),
                    err_msg,
                )
                return
            if slot is None:
                return  # Uncorrect slot
            if (
                self.si_wind_begin_index.value() == 0
                and self.si_wind_end_index.value() == 0
                and not self.is_notch  # No winding for notch
            ):
                QMessageBox().warning(
                    self,
                    self.tr("Warning"),
                    self.tr(
                        "The winding was not defined. Please use plot to see the points indices"
                    ),
                )
                return
            save_file_path = QFileDialog.getSaveFileName(
                self, self.tr("Save file"), dirname(self.dxf_path), "Json (*.json)"
            )[0]
            if save_file_path not in ["", ".json", None]:
                self.save_path = save_file_path
                slot.name = splitext(basename(self.save_path))[0]
                try:
                    slot.save(save_file_path)
                    self.accept()
                except Exception as e:
                    err_msg = "Error while saving DXF slot json file:\n" + str(e)
                    QMessageBox().critical(
                        self,
                        self.tr("Error"),
                        err_msg,
                    )
                return

    def open_tuto(self):
        """Open the tutorial video in a web browser"""
        QDesktopServices.openUrl(QUrl(self.url))
