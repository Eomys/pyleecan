from PyQt5 import QtWidgets, QtGui, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.pyplot import subplots

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

