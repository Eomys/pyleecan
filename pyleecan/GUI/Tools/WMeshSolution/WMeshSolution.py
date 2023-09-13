# -*- coding: utf-8 -*-
import matplotlib.cm as cm

from numpy import sqrt

from PySide2.QtWidgets import QAbstractSpinBox, QSpinBox, QWidget, QLabel
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout

from ..MPLWidget import MPLWidget
from ..CheckableComboBox import CheckableComboBox
from ..FloatEdit import FloatEdit


ALL_GROUPS = "all"


class WMeshSolution(QWidget):
    """Widget to view the data on a MeshSolution object."""

    def __init__(self, obj, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        # the object and some data cache
        self.obj = obj
        self._meshsolution = None
        self._mesh = None
        self._label = None
        self._axes = None
        self._field = None
        self._vmin = 0
        self._vmax = 1

        # the plot widget
        self.plotWidget = MPLWidget(is_toolbar=True, is_horizontal=True)

        self.setupUi()

        # signals
        self.groupSelection.selectionChanged.connect(self.onSelectionChanged)
        self.labelSelection.selectionChanged.connect(self.onSelectionChanged)
        self.indexSelection.valueChanged.connect(self.onIndexChanged)
        self.colorLevelEdit.editingFinished.connect(self.plot)
        self.minValueEdit.editingFinished.connect(self.onRangeChanged)
        self.maxValueEdit.editingFinished.connect(self.onRangeChanged)

        # finalize
        self.onSelectionChanged()  # trigger initial plot

    def setupUi(self):
        self.mainLayout = QVBoxLayout()
        self.subLayout = QHBoxLayout()

        groups = [ALL_GROUPS]
        groups.extend(list(self.obj.group.keys()))
        self.groupSelection = CheckableComboBox(label="Groups", allowNoSelection=False)
        self.groupSelection.addItems(groups)

        self.labelSelection = CheckableComboBox(
            label="Solution", allowNoSelection=False, singleSelection=True
        )
        self.labelSelection.addItems([sol.label for sol in self.obj.solution])

        self.indexLabel = QLabel()
        self.indexSelection = QSpinBox()
        self.indexSelection.setMinimum(0)
        self.indexSelection.setMaximum(0)
        self.indexSelection.setValue(0)

        self.colorLevelEdit = QSpinBox()
        self.colorLevelEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.colorLevelEdit.setMinimum(256)
        self.colorLevelEdit.setMinimum(2)
        self.colorLevelEdit.setValue(11)

        self.minValueEdit = FloatEdit()
        self.maxValueEdit = FloatEdit()

        self.mainLayout.addWidget(self.groupSelection)
        self.mainLayout.addWidget(self.labelSelection)
        self.mainLayout.addLayout(self.subLayout)
        self.mainLayout.addWidget(self.plotWidget)

        self.subLayout.addWidget(self.indexLabel)
        self.subLayout.addWidget(self.indexSelection)
        self.subLayout.addWidget(QLabel("Min."))
        self.subLayout.addWidget(self.minValueEdit)

        self.subLayout.addWidget(QLabel("Max."))
        self.subLayout.addWidget(self.maxValueEdit)

        self.subLayout.addWidget(QLabel("Color Levels"))
        self.subLayout.addWidget(self.colorLevelEdit)

        self.setLayout(self.mainLayout)

        self.setMinimumWidth(700)

    def onIndexChanged(self):
        self.plot()

    def onRangeChanged(self):
        vmin, vmax = self.minValueEdit.value(), self.maxValueEdit.value()
        self._vmin = vmin or self._vmin
        self._vmax = vmax or self._vmax
        self.plot()

    def onSelectionChanged(self):
        labels = self.labelSelection.currentData()
        groups = self.groupSelection.currentData()

        if labels and groups:
            is_update_range = False
            if self._label != labels[0]:
                self._label = labels[0]
                is_update_range = True

            if ALL_GROUPS in groups:
                self._meshsolution = self.obj
            else:
                self._meshsolution = self.obj.get_group(groups)
            self._mesh = self._meshsolution.get_mesh().copy()
            self._mesh.renum()  # TODO a bug? mesh should already be renumbered

            axes, siz = self._meshsolution.get_solution(self._label).get_axes_list()
            if axes[0] not in ["component", "indice"]:
                self.indexSelection.setMaximum(siz[0] - 1)
                self.indexLabel.setText(f"'{axes[0]}' axis index")

            self._axes = axes
            self._field = self._meshsolution.get_field(
                *axes, label=self._label, is_squeeze=False
            )

            if "component" in axes:
                ii = axes.index("component")
                self._field = sqrt((self._field ** 2).sum(axis=ii))

            if is_update_range:
                self.resetRange()

            self.plot()
        else:
            self.clear()

    def plot(self, levels=11):
        """Plot Filled Contour Clipped by Polygon

        Parameters
        ----------
        levels : int
            numbers of colors in the plot

        Outputs
        -------
        none :

        """
        # get figure
        fig = self.plotWidget.get_figure()
        fig.clear()
        ax = fig.add_subplot(111)

        # get the data to plot
        field = self._field
        if self._axes[0] not in ["component", "indice"]:
            index = self.indexSelection.value()
            field = field[index]

        xy = self._mesh.get_node()
        tri = self._mesh.get_cell()[0]["triangle"]

        # plot
        x, y = xy[:, 0], xy[:, 1]
        kwargs = {
            "cmap": cm.get_cmap("jet", lut=self.colorLevelEdit.value()),
            "vmin": self._vmin,
            "vmax": self._vmax,
            # "shading": "gouraud"  # doesn't work with facecolors
        }
        cont1 = ax.tripcolor(x, y, tri, facecolors=field, **kwargs)

        # generate a colorbar
        cbar = fig.colorbar(cont1, ax=ax)
        # cbar.set_ticks(cont1.levels)
        # cbar.set_ticklabels(np_round(cont1.levels, 2))
        if self._label not in ["", None]:
            cbar.ax.set_title(self._label)

        # plt.grid(c='k', ls='-', alpha=0.3)
        # cbar.set_label(axislabel[2])

        # ax.set_xlim(x_max, x_min)
        # ax.set_ylim(y_max, y_min)
        ax.set_aspect(1)

        self.plotWidget.draw()

    def clear(self):
        fig = self.plotWidget.get_figure()
        fig.clear()
        self.plotWidget.draw()

    def resetRange(self):
        self._vmin, self._vmax = self._field.min(), self._field.max()
        self._vmin = 0 if self._vmin > 0 else self._vmin
        self.minValueEdit.setValue(self._vmin)
        self.maxValueEdit.setValue(self._vmax)
