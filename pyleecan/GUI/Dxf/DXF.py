from .Ui_DXF import Ui_DXF
from PyQt5.QtWidgets import (
    QWidget,
    QGraphicsScene,
    QTableWidgetItem,
    QComboBox,
    QPushButton,
    QLineEdit,
)
from PyQt5.QtCore import pyqtSlot, QSize
import PyQt5.QtCore as QtCore
from PyQt5.QtGui import QIcon, QPixmap
from .DXFGraphicsView import DXFGraphicsView
from ...definitions import GUI_DIR

from ...Classes.HoleUD import HoleUD
from ...Classes.Magnet import Magnet
from math import pi
from cmath import phase


from matplotlib.patches import Patch
from matplotlib.pyplot import axis, legend

from ...Functions.init_fig import init_fig
from ...definitions import config_dict

MAGNET_COLOR = config_dict["PLOT"]["COLOR_DICT"]["MAGNET_COLOR"]


class DXF(Ui_DXF, QWidget):
    def __init__(self, doc=None):
        QWidget.__init__(self)
        self.setupUi(self)

        self.delete_icon = QPixmap(GUI_DIR + "/Resources/images/icon/delete_36.png")

        self.doc_name = doc
        if doc is not None:
            self.open_document()

        self.nrows = 0

        # Only select dxf files
        self.w_path_selector.obj = self
        self.w_path_selector.param_name = "doc_name"
        self.w_path_selector.verbose_name = "File"
        # self.w_path_selector.extension = ".DXF" # <--- TODO fix the bug

        self.le_center_x.resize(20, self.le_center_x.height())
        self.le_center_y.resize(20, self.le_center_y.height())

        # Format w_surface_list (QTableWidget)
        self.w_surface_list.setColumnCount(3)
        self.w_surface_list.horizontalHeader().hide()
        self.w_surface_list.verticalHeader().hide()
        self.w_surface_list.setColumnWidth(2, 24)

        # Connect signals to slot
        self.w_path_selector.pathChanged.connect(self.open_document)
        self.viewer.surface_added.connect(self.new_surface)
        self.b_save.pressed.connect(self.save)
        self.b_plot.pressed.connect(self.plot)

        self.w_surface_list.currentCellChanged.connect(self.highlight_surface)
        self.show()

    @pyqtSlot()
    def open_document(self):
        """Open a new dxf in the viewer"""
        self.viewer.open_doc(self.doc_name)

    @pyqtSlot(dict)
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

    @pyqtSlot(str)
    def edit_surface_name(self, name):
        """Edit a surface name from the QTableWidget"""
        # Get current row
        nrow = self.w_surface_list.currentRow()
        # Edit corresponding surface
        self.viewer.surface_list[nrow]["name"] = name

    @pyqtSlot()
    def plot(self):
        """Plot every selected surfaces"""
        # TODO plot with pyleecan graphic chart hole and magnet
        Zh = self.le_zh.value()
        angle = float(self.le_axe_angle.value())
        center = float(self.le_center_x.value()) + float(self.le_center_y.value()) * 1j
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
        Zh = self.le_zh.value()
        angle = float(self.le_axe_angle.value())
        center = float(self.le_center_x.value()) + float(self.le_center_y.value()) * 1j
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
