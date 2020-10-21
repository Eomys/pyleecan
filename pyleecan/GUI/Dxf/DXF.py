from .Ui_DXF import Ui_DXF
from PySide2.QtWidgets import (
    QWidget,
    QGraphicsScene,
    QTableWidgetItem,
    QComboBox,
    QPushButton,
    QLineEdit,
)
from PySide2.QtCore import Signal, QSize
import PySide2.QtCore as QtCore
from PySide2.QtGui import QIcon, QPixmap
from ...definitions import GUI_DIR

from ...Classes.HoleUD import HoleUD
from ...Classes.Magnet import Magnet
from math import pi
from cmath import phase
from ...GUI.Tools.MPLCanvas import MPLCanvas2
from numpy import array
from matplotlib.patches import Patch
from matplotlib.pyplot import axis, legend

from ...Functions.init_fig import init_fig
from ...definitions import config_dict
from ezdxf import readfile
from pyleecan.GUI.Dxf.dxf_to_pyleecan_list import dxf_to_pyleecan_list
from pyleecan.GUI.Resources import pixmap_dict

MAGNET_COLOR = config_dict["PLOT"]["COLOR_DICT"]["MAGNET_COLOR"]

LINE_LIST = list()
SELECTED_LIST = list()


class DXF(Ui_DXF, QWidget):
    def __init__(self, dxf_path=None):
        QWidget.__init__(self)
        self.setupUi(self)

        self.delete_icon = QPixmap(pixmap_dict["delete_36"])

        # Initialize the graph
        self.w_viewer.setParent(None)
        self.w_viewer = MPLCanvas2(self)
        self.w_viewer.draw()
        self.main_layout.removeWidget(self.w_viewer)
        self.main_layout.insertWidget(0, self.w_viewer)

        # Load the DXF file if provided
        self.dxf_path = dxf_path
        if dxf_path is not None:
            self.open_document()

        # Setup Path selector for DXF files
        self.w_path_selector.obj = self
        self.w_path_selector.param_name = "dxf_path"
        self.w_path_selector.verbose_name = "DXF File"
        self.w_path_selector.extension = "DXF file (*.dxf)"
        self.w_path_selector.set_path_txt(self.dxf_path)

        # Format w_surface_list table (QTableWidget)
        self.w_surface_list.setColumnCount(3)
        self.w_surface_list.horizontalHeader().hide()
        self.w_surface_list.verticalHeader().hide()
        self.w_surface_list.setColumnWidth(2, 24)
        self.nrows = 0

        # Connect signals to slot
        self.w_path_selector.pathChanged.connect(self.open_document)
        self.b_save.pressed.connect(self.save)
        self.b_plot.pressed.connect(self.plot)
        self.w_surface_list.currentCellChanged.connect(self.highlight_surface)

        # Display the GUI
        self.show()

    def open_document(self):
        """Open a new dxf in the viewer"""

        document = readfile(self.dxf_path)
        # Model Space
        modelspace = document.modelspace()
        # Create pyleecan objects
        LINE_LIST = dxf_to_pyleecan_list(modelspace)
        print(len(LINE_LIST))
        SELECTED_LIST = [False for line in LINE_LIST]

        self.update_graph()

    def update_graph(self):
        # self.w_viewer.refresh_fig()
        print("Bla " + str(len(LINE_LIST)))
        fig, axes = self.w_viewer.fig, self.w_viewer.axes
        axes.set_axis_off()

        # Draw the lines in the correct color
        for ii, line in enumerate(LINE_LIST):
            point_list = array(line.discretize(20))
            if SELECTED_LIST[ii]:
                color = "r"
            else:
                color = "k"
            axes.plot(point_list.real, point_list.imag, color)

        # Setup interaction with graph
        def set_cursor(event):
            X = event.xdata  # X position of the click
            Y = event.ydata  # Y position of the click
            # Get closer pyleecan object
            Z = X + 1j * Y
            min_dist = float("inf")
            closest_id = -1
            for ii, line in enumerate(LINE_LIST):
                line_dist = line.comp_distance(Z)

                if line_dist < min_dist:
                    closest_id = ii
                    min_dist = line_dist
            print("Debug")
            print(len(SELECTED_LIST))
            print(len(LINE_LIST))
            print(closest_id)
            SELECTED_LIST[closest_id] = not SELECTED_LIST[closest_id]
            self.update_graph()

        def zoom_fun(event):
            base_scale = 0.3
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

        # Connect the cursor fonction to click on graph
        self.w_viewer.mpl_connect("button_press_event", set_cursor)

        # attach the call back
        self.w_viewer.mpl_connect("scroll_event", zoom_fun)

        axes.axis("equal")
        self.w_viewer.draw()

    def new_surface(self, element):
        """Add the new surface in the QTableWidget"""
        nrows = self.w_surface_list.rowCount()

        # Surface label
        self.w_surface_list.setRowCount(nrows + 1)
        w_name = QLineEdit(element["name"])
        self.w_surface_list.setCellWidget(nrows, 0, w_name)
        w_name.textChanged.connect(self.edit_surface_name)

        # Surface type
        combobox = QComboBox()
        combobox.addItems(["Hole", "Magnet"])
        self.w_surface_list.setCellWidget(
            nrows, 1, combobox,
        )

        # Delete button
        new_button = QPushButton()
        new_button.setIcon(QIcon(self.delete_icon))
        new_button.setIconSize(QSize(24, 24))
        new_button.pressed.connect(self.delete_surface)

        self.w_surface_list.setCellWidget(
            nrows, 2, new_button,
        )

        self.w_surface_list.setCurrentCell(nrows, 0)

    def edit_surface_name(self, name):
        """Edit a surface name from the QTableWidget"""
        # Get current row
        nrow = self.w_surface_list.currentRow()
        # Edit corresponding surface
        self.viewer.surface_list[nrow]["name"] = name

    def plot(self):
        """Plot every selected surfaces"""
        # TODO plot with pyleecan graphic chart hole and magnet
        Zh = self.si_zh.value()
        angle = float(self.lf_axe_angle.value())
        center = float(self.lf_center_x.value()) + float(self.lf_center_y.value()) * 1j
        surf_list = [e["surface"].copy() for e in self.viewer.surface_list]
        for i, surf in enumerate(surf_list):
            # Translate and rotate
            surf.translate(-center)
            surf.rotate(-angle)
            if self.w_surface_list.cellWidget(i, 1).currentText() == "Magnet":
                surf.label = "HoleMagnet"
            else:
                surf.label = "Hole"

        # TODO sort the surf_list according
        angles = [phase(surf.point_ref) for surf in surf_list]
        idx = sorted(range(len(angles)), key=lambda k: angles[k])
        surf_list_sorted = [surf_list[i] for i in idx]

        mag_list = [surf for surf in surf_list_sorted if surf.label == "HoleMagnet"]

        mag_dict = {}
        for i in range(len(mag_list)):
            mag_dict["magnet_{}".format(i)] = Magnet(type_magnetization=0, Lmag=1)

        plot_without_lam(HoleUD(Zh=8, surf_list=surf_list_sorted, magnet_dict=mag_dict))

    def highlight_surface(self, crow, ccol, prow, pcol):
        """Highlight a surface if a the user clic in the """
        # Return if the row has not changed or the surface is deleted
        if crow == prow or ccol == 2:  # or len(self.viewer.lines_selection) != 0:
            return

        if crow == -1:
            self.viewer.remove_highlight_surface()
            return

        surf_name = self.w_surface_list.cellWidget(crow, 0).text()
        self.viewer.highlight_surface(surf_name)

    def delete_surface(self):
        """Delete a surface """
        nrow = self.w_surface_list.currentRow()
        surf_name = self.w_surface_list.cellWidget(nrow, 0).text()
        for element in self.viewer.surface_list:
            if element["name"] == surf_name:
                self.viewer.surface_list.remove(element)
                break
        self.w_surface_list.removeRow(nrow)

    def save(self):
        """Save the corresponding surfaces in a HoleUD"""
        # Zh = 8
        # angle = pi / 8
        # center = 0 + 0j
        Zh = self.si_zh.value()
        angle = float(self.lf_axe_angle.value())
        center = float(self.lf_center_x.value()) + float(self.lf_center_y.value()) * 1j
        surf_list = [e["surface"].copy() for e in self.viewer.surface_list]
        for i, surf in enumerate(surf_list):
            # Translate and rotate
            surf.translate(-center)
            surf.rotate(-angle)
            if self.w_surface_list.cellWidget(i, 1).currentText() == "Magnet":
                surf.label = "HoleMagnet"
            else:
                surf.label = "Hole"

        # TODO sort the surf_list according
        angles = [phase(surf.point_ref) for surf in surf_list]
        idx = sorted(range(len(angles)), key=lambda k: angles[k])
        surf_list_sorted = [surf_list[i] for i in idx]

        mag_list = [surf for surf in surf_list_sorted if surf.label == "HoleMagnet"]

        mag_dict = {}
        for i in range(len(mag_list)):
            mag_dict["magnet_{}".format(i)] = Magnet(type_magnetization=0, Lmag=1)

        HoleUD(Zh=8, surf_list=surf_list_sorted, magnet_dict=mag_dict).save(
            "Scripts/DXF/test_holeud.pkl"
        )
        print("Saving")


def plot_without_lam(hole):
    """Plot the Hole in a matplotlib fig

    Parameters
    ----------
    self : Hole
        A Hole object
    fig :
        if None, open a new fig and plot, else add to the current
        one (Default value = None)
    display_magnet : bool
        if True, plot the magnet inside the hole, if there is any (Default value = True)

    Returns
    -------
    None
    """
    fig = None
    display_magnet = True
    display = fig is None
    if display:
        color = "k"
    else:
        color = "w"

    surf_hole = hole.build_geometry()
    patches = list()
    for surf in surf_hole:
        if "Magnet" in surf.label and display_magnet:
            patches.extend(surf.get_patches(color=MAGNET_COLOR))
        else:
            patches.extend(surf.get_patches(color=color))

    # Display the result
    (fig, axes, patch_leg, label_leg) = init_fig(fig)
    axes.set_xlabel("(m)")
    axes.set_ylabel("(m)")
    axes.set_title("Hole")

    # Add all the hole (and magnet) to fig
    for patch in patches:
        axes.add_patch(patch)

    # Axis Setup
    axis("equal")

    if display_magnet and "Magnet" in [surf.label for surf in surf_hole]:
        patch_leg.append(Patch(color=MAGNET_COLOR))
        label_leg.append("Magnet")
        legend(patch_leg, label_leg)
    fig.show()
