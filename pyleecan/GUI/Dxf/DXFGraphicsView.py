from ...Classes.Segment import Segment
from ...Classes.Arc2 import Arc2

import math
import cmath

from typing import Optional, Iterable, Tuple, List

from PyQt5 import QtWidgets as qw, QtCore as qc, QtGui as qg

import ezdxf
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


class DXFGraphicsView(qw.QGraphicsView):
    mouse_moved = qc.pyqtSignal(qc.QPointF)
    element_selected = qc.pyqtSignal(object, int)
    mouse_released = qc.pyqtSignal(qc.QPointF)

    def __init__(
        self,
        *,
        doc: str = None,
        view_buffer: float = 0.2,
        zoom_per_scroll_notch: float = 0.2,
        loading_overlay: bool = True,
    ):
        super().__init__()
        self.doc = doc  # Document to open
        self.modelspace = []  # Document modelspace
        self.selection = []  # List of pyleecan object selected
        self._zoom = 1
        self._default_zoom = 1
        self._zoom_limits = (0.000005, 100000)
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
        # self.element_selected.connect(self._on_element_selected)
        # self.mouse_moved.connect(self._on_mouse_moved)
        self.mouse_released.connect(self._selection)

        self.setScene(qw.QGraphicsScene())
        self.backend = PyQtBackend(scene=self.scene())

        if self.doc is not None:
            self.open_doc(doc)

        self.show()

    def open_doc(self, document):
        self.doc = document
        self.frontend = Frontend(RenderContext(doc=document), out=self.backend)

        # Model Space
        self.modelspace = document.modelspace()
        self.frontend.draw_layout(self.modelspace)

        # Create pyleecan objects
        self.pyleecan_geo = dxf_to_pyleecan_list(self.modelspace)

        self.fit_to_scene()
        self.show()

    def clear(self):
        pass

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
        self.fitInView(self.sceneRect(), qc.Qt.KeepAspectRatio)
        self._default_zoom = _get_x_scale(self.transform())
        self._zoom = 1

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

    # def drawForeground(self, painter: qg.QPainter, rect: qc.QRectF) -> None:
    #     if self._is_loading and self._loading_overlay:
    #         painter.save()
    #         # painter.fillRect(rect, qg.QColor("#aa000000"))
    #         painter.setWorldMatrixEnabled(False)
    #         r = self.viewport().rect()
    #         painter.setBrush(qc.Qt.NoBrush)
    #         painter.setPen(qc.Qt.white)
    #         painter.drawText(r.center(), "Loading...")
    #         painter.restore()

    # def mouseMoveEvent(self, event: qg.QMouseEvent) -> None:
    #     super().mouseMoveEvent(event)
    #     pos = self.mapToScene(event.pos())
    #     self.mouse_moved.emit(pos)
    #     selected_items = self.scene().items(pos)
    #     if selected_items != self._selected_items:
    #         self._selected_items = selected_items
    #         self._selected_index = 0 if self._selected_items else None
    #         self._emit_selected()

    def mouseReleaseEvent(self, event: qg.QMouseEvent) -> None:
        super().mouseReleaseEvent(event)
        pos = self.mapToScene(event.pos())
        # if event.button() == qc.Qt.LeftButton and self._selected_items:
        #     self._selected_index = (self._selected_index + 1) % len(
        #         self._selected_items
        #     )
        #     self._emit_selected()
        if event.button() == qc.Qt.RightButton:
            self.mouse_released.emit(pos)

    def add_to_selection(self, pl_obj):
        """Add a Pyleecan object to the current selection and emit a signal if a surface is selected
        """
        if pl_obj not in self.selection:
            self.selection.append(pl_obj)
            coordinates = []
            # Add every points coordinates in a list
            for obj in self.selection:
                if isinstance(obj, Segment):
                    coordinates.extend([obj.begin, obj.end])
                elif isinstance(obj, Arc2):
                    # print(obj.begin, obj.begin * cmath.exp(1j * obj.angle))
                    coordinates.extend(
                        [
                            obj.begin,
                            obj.center
                            + (obj.begin - obj.center) * cmath.exp(1j * obj.angle),
                        ]
                    )
            # Check if every point is twice in the list
            for p1 in coordinates:
                count = 0
                for p2 in coordinates:
                    if abs(p1 - p2) / abs(p1) < 1e-9:
                        count += 1
                if count != 2:
                    return 0
            self.selection = []
            return 1
        else:
            self.selection.remove(pl_obj)
            coordinates = []

            # Check if every point is twice in the list
            for p1 in coordinates:
                count = 0
                for p2 in coordinates:
                    if abs(p1 - p2) / abs(p1) < 1e-9:
                        count += 1
                if count != 2:
                    return -1
            if len(coordinates) > 0:
                self.selection = []
                return 1
            else:
                return -1

    # def _emit_selected(self):
    #     self.element_selected.emit(self._selected_items, self._selected_index)
    #     self.scene().invalidate(self.sceneRect(), qw.QGraphicsScene.ForegroundLayer)

    @qc.pyqtSlot(qc.QPointF)
    def _selection(self, mouse_pos: qc.QPointF):
        # print(mouse_pos.x(), mouse_pos.y())

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
        result = self.add_to_selection(close_obj)
        print(result)
        if result == 1 or (
            result == -1 and len(self.selection) == 0
        ):  # Selection complete
            self.backend.scene.clear()
            self.frontend.draw_layout(self.modelspace)
            # prop = Properties()
            # prop.color = "#ffffff"
            # for entity in self.modelspace:
            #     entity.rgb = (0, 0, 0)
            #     self.frontend.draw_entity(entity, prop)
        elif result == -1:  # Deselect one element
            prop = Properties()
            prop.color = "#ffffff"
            self.frontend.draw_entity(entity, prop)
        else:  # Select one element
            prop = Properties()
            prop.color = "#aa2354"
            entity.rgb = (256, 0, 0)
            self.frontend.draw_entity(entity, prop)

        # Draw corresponding entity
        # new_scene = qw.QGraphicsScene()
        # renderer = PyQtBackend(new_scene)
        # prop = Properties()
        # prop.color = "#aa2354"
        # try:
        #     Frontend(self._render_context, renderer).draw_entity(entity, prop)
        # except DXFStructureError as e:
        #     qw.QMessageBox.critical(
        #         self, "DXF Structure Error", f"Abort rendering of entity: {str(e)}",
        #     )
        # finally:
        #     renderer.finalize()
        # self.view.end_loading(new_scene)
        # self.view.buffer_scene_rect()
        # self.view.fit_to_scene()

