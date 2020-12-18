from PySide2 import QtWidgets, QtGui, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.pyplot import subplots
from matplotlib.figure import Figure
import numpy as np


DEBUG = True

# =============================================================================
class MPLCanvas(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setLayout(QtWidgets.QGridLayout())

        self.fig, self.axes = subplots()
        self.canvas = FigureCanvas(self.fig)
        # 'new' method to be compatible with pyleecan's plot-methods
        self.fig.show = self.canvas.draw

        self.layout().addWidget(self.canvas, 0, 0, 1, 1)


class MPLCanvas2(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        super(MPLCanvas2, self).__init__(self.fig)

    def refresh_fig(self):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
