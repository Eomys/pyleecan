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

# from ...Classes.HoleUD import HoleUD


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
        # self.w_path_selector.extension = ".DXF" # <--- TODO fix the bug

        # Format w_surface_list (QTableWidget)
        self.w_surface_list.setColumnCount(3)
        self.w_surface_list.horizontalHeader().hide()
        self.w_surface_list.verticalHeader().hide()
        self.w_surface_list.setColumnWidth(2, 24)

        # Connect signals to slot
        self.w_path_selector.pathChanged.connect(self.open_document)
        self.viewer.surface_added.connect(self.new_surface)
        self.b_save.pressed.connect(self.save)

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
        pass

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
        # HoleUD()
        print("Saving")
