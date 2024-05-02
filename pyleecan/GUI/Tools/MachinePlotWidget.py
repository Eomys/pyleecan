from qtpy import QtWidgets, QtGui, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.pyplot import subplots

import numpy as np


DEBUG = True


# =============================================================================
class MachinePlotWidget(QtWidgets.QGroupBox):
    def __init__(self, parent, label="", *args, **kwargs):
        QtWidgets.QGroupBox.__init__(self, label, *args, **kwargs)
        self.parent = parent
        self.setLayout(QtWidgets.QGridLayout())

        self.fig, self.axes = subplots()
        self.canvas = FigureCanvas(self.fig)

        self.layout().addWidget(self.canvas, 0, 0, 1, 1)

        self.axes.axis("equal")

    def update(self):
        if self.parent.DesignWidget.machine is not None:
            self.axes.clear()
            # new method to be compatible with pyleecan's plot-methods
            self.fig.show = self.canvas.draw
            plot_obj = self.parent.DesignWidget.machine
            plot_obj.plot(fig=self.fig, sym=1, alpha=0, delta=0)
