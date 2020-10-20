from ...Classes.Segment import Segment
from ...Classes.SurfLine import SurfLine
from ...Functions.Geometry.create_surface import create_surface
from ...Classes.Arc2 import Arc2

import math
import cmath
import matplotlib.pyplot as plt

from typing import Optional, Iterable, Tuple, List

from PyQt5 import QtWidgets as qw, QtCore as qc, QtGui as qg

import ezdxf
from ezdxf import readfile
from ezdxf.addons import odafc
from ezdxf.addons.drawing import Frontend, RenderContext
from ezdxf.addons.drawing.properties import is_dark_color, Properties
from ezdxf.addons.drawing.pyqt import (
    _get_x_scale,
    PyQtBackend,
    CorrespondingDXFEntity,
    CorrespondingDXFParentStack,
)
from ezdxf.document import Drawing
from ezdxf.entities import DXFGraphic
from ezdxf.lldxf.const import DXFStructureError

from .dxf_to_pyleecan_list import dxf_to_pyleecan_list
import matplotlib.pyplot as plt

# Symmetry line
symmetry_line = ezdxf.new().modelspace().add_line((0, 0), (1000, 0))


class DXFGraphicsView(qw.QGraphicsView):
    mouse_moved = qc.pyqtSignal(qc.QPointF)
    mouse_released = qc.pyqtSignal(qc.QPointF)
    surface_added = qc.pyqtSignal(dict)

    def __init__(
        self,
        parent,
        *,
        doc: str = None,
        view_buffer: float = 0.2,
        zoom_per_scroll_notch: float = 0.2,
        loading_overlay: bool = True,
    ):
        super().__init__(parent)
        self.doc = doc  # Document to open
        self.modelspace = []  # Document modelspace
        self.lines_selection = []  # List of pyleecan object selected
        self.surface_list = []  # List of Dict containing selected surface
        self.entities_selection = []  # List of entities selected
        self.highlighted_entities = []  # Entities surface highlighted
        self.colors = {
            "selected": "#aa2354",
            "white": "#ffffff",
            "highlight": "#007d3c",
        }
        self._zoom = 1
        self._default_zoom = 1
        self._zoom_limits = (1e-10, 1e10)
        self._zoom_per_scroll_notch = zoom_per_scroll_notch
        self._view_buffer = view_buffer
        self._loading_overlay = loading_overlay
        self._selected_items: List = []
        self._is_loading = False
        self.scale(1, -1)  # so that +y is up

        self.setTransformationAnchor(qw.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(qw.QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(qc.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(qc.Qt.ScrollBarAlwaysOff)
        self.setDragMode(qw.QGraphicsView.ScrollHandDrag)
        self.setFrameShape(qw.QFrame.NoFrame)
        self.setRenderHints(
            qg.QPainter.Antialiasing
            | qg.QPainter.TextAntialiasing
            | qg.QPainter.SmoothPixmapTransform
        )

        # Pyleecan Geometry objects
        self.pyleecan_geo = []

        # Connect signal
        self.mouse_released.connect(self._selection)

        self.setScene(qw.QGraphicsScene())
        self.backend = PyQtBackend(scene=self.scene())

        if self.doc is not None:
            self.open_doc(doc)

    def open_doc(self, doc_name):

        self.doc = doc_name
        document = readfile(doc_name)
        self.frontend = Frontend(RenderContext(doc=document), out=self.backend)
        # Model Space
        self.modelspace = document.modelspace()

        # Create pyleecan objects
        self.pyleecan_geo = dxf_to_pyleecan_list(self.modelspace)
        self.fit_to_scene()
        self.refresh_drawing()

    def clear(self):
        pass

    def refresh_drawing(self):
        """Refresh the drawing"""
        self.backend.scene.clear()
        prop = Properties()
        prop.color = "#007d00"
        # self.frontend.draw_entity(symmetry_line, prop)

        ## TODO add the symetry line : https://stackoverflow.com/questions/55444588/drawing-of-infinite-line-in-qt

        self.frontend.draw_layout(self.modelspace)

    def begin_loading(self):
        self._is_loading = True
        self.scene().invalidate(qc.QRectF(), qw.QGraphicsScene.AllLayers)
        qw.QApplication.processEvents()

    def end_loading(self, new_scene: qw.QGraphicsScene):
        self.setScene(new_scene)
        self._is_loading = False
        self.buffer_scene_rect()
        self.scene().invalidate(qc.QRectF(), qw.QGraphicsScene.AllLayers)

    def buffer_scene_rect(self):
        scene = self.scene()
        r = scene.sceneRect()
        bx, by = r.width() * self._view_buffer / 2, r.height() * self._view_buffer / 2
        scene.setSceneRect(r.adjusted(-bx, -by, bx, by))

    def fit_to_scene(self):
        x_min = float("inf")
        y_min = float("inf")
        x_max = float("-inf")
        y_max = float("-inf")

        for obj in self.pyleecan_geo:
            x_coord = [obj.get_begin().real, obj.get_end().real]
            y_coord = [obj.get_begin().imag, obj.get_end().imag]
            if x_min > min(x_coord):
                x_min = min(x_coord)
            if y_min > min(y_coord):
                y_min = min(y_coord)
            if x_max < max(x_coord):
                x_max = max(x_coord)
            if y_max < max(y_coord):
                y_max = max(y_coord)

        width = x_max - x_min
        height = y_max - y_min

        self.scene().setSceneRect(
            x_min - 0.1 * width, y_min - 0.1 * height, 1.2 * width, 1.2 * height
        )
        self.fitInView(self.sceneRect(), qc.Qt.KeepAspectRatio)
        self._default_zoom = _get_x_scale(self.transform())
        self._zoom = 1

    def highlight_surface(self, surf_name):
        """Highlight lines of an existing surface"""
        self.remove_highlight_surface()
        for element in self.surface_list:
            if surf_name == element["name"]:
                entities = element["entities"]
        self.highlighted_entities = entities
        prop = Properties()
        prop.color = self.colors["highlight"]
        for entity in entities:
            self.frontend.draw_entity(entity, prop)

    def remove_highlight_surface(self):
        """Remove the highlight of an existing surface"""
        if len(self.lines_selection) != 0:
            prop = Properties()
            for entity in self.highlighted_entities:
                if entity not in self.entities_selection:
                    prop.color = self.colors["white"]
                    self.frontend.draw_entity(entity, prop)
                else:
                    prop.color = self.colors["selected"]
                    self.frontend.draw_entity(entity, prop)
        else:
            self.refresh_drawing()
        self.highlighted_entities = []

    def _get_zoom_amount(self) -> float:
        return _get_x_scale(self.transform()) / self._default_zoom

    def wheelEvent(self, event: qg.QWheelEvent) -> None:
        # dividing by 120 gets number of notches on a typical scroll wheel. See QWheelEvent documentation
        delta_notches = event.angleDelta().y() / 120
        direction = math.copysign(1, delta_notches)
        factor = (1 + self._zoom_per_scroll_notch * direction) ** abs(delta_notches)
        resulting_zoom = self._zoom * factor
        if resulting_zoom < self._zoom_limits[0]:
            factor = self._zoom_limits[0] / self._zoom
        elif resulting_zoom > self._zoom_limits[1]:
            factor = self._zoom_limits[1] / self._zoom
        self.scale(factor, factor)
        self._zoom *= factor

    def mouseReleaseEvent(self, event: qg.QMouseEvent) -> None:
        super().mouseReleaseEvent(event)
        pos = self.mapToScene(event.pos())
        if event.button() == qc.Qt.RightButton:
            self.remove_highlight_surface()
            self.mouse_released.emit(pos)

    def check_selection(self):
        """
        Check if every line in the selection form a surface

        Parameters
        ----------
        self: DXFGraphicsView

        Returns
        -------
        bool
            True if it forms a surface
        """
        coordinates = []
        # Add every points coordinates in a list
        for obj in self.lines_selection:
            if isinstance(obj, Segment):
                coordinates.extend([obj.begin, obj.end])
            elif isinstance(obj, Arc2):
                coordinates.extend(
                    [
                        obj.begin,
                        obj.center
                        + (obj.begin - obj.center) * cmath.exp(1j * obj.angle),
                    ]
                )
        # Check with a tolerance if every point is twice in the list
        if len(coordinates) == 0:
            return False

        for p1 in coordinates:
            count = 0
            for p2 in coordinates:
                if abs(p1 - p2) < 1e-9:
                    count += 1
            if count != 2:
                return False

        return True

    def add_to_selection(self, pl_obj, dxf_obj):
        """Add a Pyleecan object to the current selection and emit a signal if a surface is selected"""
        if pl_obj not in self.lines_selection:
            self.lines_selection.append(pl_obj)
            self.entities_selection.append(dxf_obj)
            if self.check_selection():
                return self.add_surface()
            else:
                return True
        else:
            self.entities_selection.remove(dxf_obj)
            self.lines_selection.remove(pl_obj)
            # Check if every point is twice in the list
            if self.check_selection():
                return self.add_surface()
            else:
                return False

    def add_surface(self):
        """
        Add a surface from the selected lines
        """

        # Check if the surface doesn't exist
        for element in self.surface_list:
            found = True
            entites = element["entities"]
            for entity in self.entities_selection:
                if entity not in entites:
                    found = False
                    break
            if found is True:
                # Empty selection
                self.lines_selection = []
                self.entities_selection = []

                # Clear
                self.refresh_drawing()
                return element["surface"]

        # Add the surface
        names = [e["name"] for e in self.surface_list]
        name = "New"
        i = 0
        if name in names:
            while name + " ({})".format(i) in names:
                i += 1
            name += " ({})".format(i)

        surface = create_surface(self.lines_selection)
        new_element = {
            "name": name,
            "surface": surface,
            "entities": self.entities_selection,
        }
        self.surface_list.append(new_element)
        # Empty selection
        self.lines_selection = []
        self.entities_selection = []

        # Clear
        self.refresh_drawing()

        self.surface_added.emit(new_element)
        return surface

    @qc.pyqtSlot(qc.QPointF)
    def _selection(self, mouse_pos: qc.QPointF):
        # print(mouse_pos.x(), mouse_pos.y())
        self.remove_highlight_surface()

        # Get closer pyleecan object
        point = mouse_pos.x() + 1j * mouse_pos.y()
        dist = float("inf")
        close_obj = None
        index = -1
        for i, obj in enumerate(self.pyleecan_geo):
            d = obj.comp_distance(point)

            if d < dist:
                index = i
                dist = d
                close_obj = obj

        entity = self.modelspace[index]
        new_selection = self.add_to_selection(
            close_obj, entity
        )  # True if new selection, False if deselection, Surface if a surface has been created

        if new_selection is True:  # Select one element
            # Change its color
            prop = Properties()
            prop.color = self.colors["selected"]
            self.frontend.draw_entity(entity, prop)

        elif new_selection is False:  # Deselect one element
            if len(self.lines_selection) == 0:  # Clear the scene if selection is empty
                self.refresh_drawing()
            else:
                prop = Properties()
                prop.color = self.colors["white"]
                self.frontend.draw_entity(entity, prop)
