from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure


class MPLCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        super(MPLCanvas, self).__init__(self.fig)

    def refresh_fig(self):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
