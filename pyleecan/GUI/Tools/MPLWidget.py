from qtpy.QtCore import Qt
from qtpy.QtWidgets import QHBoxLayout, QSizePolicy, QVBoxLayout, QWidget

from .MPLCanvas import MPLCanvas

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT

"""
class NavigationToolbar(NavigationToolbar2QT):
    # only display the buttons we need
    toolitems = [t for t in NavigationToolbar2QT.toolitems if
                 t[0] in ('Home', 'Pan', 'Zoom', 'Save', None)]
"""


class MPLWidget(QWidget):
    def __init__(self, *args, is_toolbar=True, is_horizontal=True, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setupUi(is_toolbar=is_toolbar, is_horizontal=is_horizontal)

    def setupUi(self, is_toolbar=True, is_horizontal=False):
        # toolbar; only use 'vertical' with coordinates 'False' due to size issue
        coords = False
        orient = Qt.Vertical
        if is_horizontal:
            coords = True
            orient = Qt.Horizontal

        # === Widgets ===
        self.canvas = MPLCanvas()
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.toolbar = NavigationToolbar2QT(self.canvas, self, coordinates=coords)
        self.toolbar.setOrientation(orient)

        # === Layout ===
        if is_horizontal:  # the layout is opposite to the toolbar orientation
            self.mainLayout = QVBoxLayout()
        else:
            self.mainLayout = QHBoxLayout()

        if is_toolbar:
            self.mainLayout.addWidget(self.toolbar)
        self.mainLayout.addWidget(self.canvas)
        self.setLayout(self.mainLayout)

    def get_figure(self):
        fig = self.canvas.fig
        return fig

    def draw(self):
        self.canvas.draw()
