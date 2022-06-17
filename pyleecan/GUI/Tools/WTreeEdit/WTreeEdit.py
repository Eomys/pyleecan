# -*- coding: utf-8 -*-

# from numpy import ndarray

from PySide2 import QtGui
from PySide2.QtCore import Qt, Signal
from PySide2.QtWidgets import QLabel, QSplitter, QStatusBar, QTreeView, QWidget
from PySide2.QtWidgets import QVBoxLayout, QSizePolicy

from ....Classes._ClassInfo import ClassInfo

# from ....definitions import config_dict
# from ....GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
# from ...Dialog.DMatLib.DMatLib import DMatLib
# from ...Dialog.DMatLib.MatLib import MatLib

from ..WTableParameterEdit.WTableParameterEdit import WTableParameterEdit
from ..WTableData.WTableData import WTableData
from .TreeEditContextMenu import TreeEditContextMenu
from .TreeEditModel import TreeEditModel
from ..WMeshSolution.WMeshSolution import WMeshSolution

# from ....Functions.Save.save_json import JSON_SETTINGS

# TODO force tree view to keep default / user selected width


class WTreeEdit(QWidget):
    """TreeEdit widget is to show and edit all of the pyleecan objects data."""

    # Signals
    dataChanged = Signal()

    def __init__(self, obj, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.class_dict = ClassInfo().get_dict()
        self.treeDict = None  # helper to track changes
        self.obj = obj  # the object
        self.is_save_needed = False

        self.model = TreeEditModel(obj)

        self.setupUi()

        # === Signals ===
        self.selectionModel.selectionChanged.connect(self.onSelectionChanged)
        self.treeView.collapsed.connect(self.onItemCollapse)
        self.treeView.expanded.connect(self.onItemExpand)
        self.treeView.customContextMenuRequested.connect(self.openContextMenu)
        self.model.dataChanged.connect(self.onDataChanged)
        self.dataChanged.connect(self.setSaveNeeded)

        # === Finalize ===
        # set 'root' the selected item and resize columns
        self.treeView.setCurrentIndex(self.treeView.model().index(0, 0))
        self.treeView.resizeColumnToContents(0)

    def setupUi(self):
        """Setup the UI"""
        # === Widgets ===
        # TreeView
        self.treeView = QTreeView()
        # self.treeView.rootNode = model.invisibleRootItem()
        self.treeView.setModel(self.model)
        self.treeView.setAlternatingRowColors(False)

        # self.treeView.setColumnWidth(0, 150)
        self.treeView.setMinimumWidth(100)

        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.selectionModel = self.treeView.selectionModel()

        self.statusBar = QStatusBar()
        self.statusBar.setSizeGripEnabled(False)
        self.statusBar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.statusBar.setStyleSheet(
            "QStatusBar {border: 1px solid rgb(200, 200, 200)}"
        )
        self.saveLabel = QLabel("unsaved")
        self.saveLabel.setVisible(False)
        self.statusBar.addPermanentWidget(self.saveLabel)

        # Splitters
        self.leftSplitter = QSplitter()
        self.leftSplitter.setStretchFactor(0, 0)
        self.leftSplitter.setStretchFactor(1, 1)

        # === Layout ===
        # Horizontal Div.
        self.hLayout = QVBoxLayout()
        self.hLayout.setContentsMargins(0, 0, 0, 0)
        self.hLayout.setSpacing(0)

        # add widgets to layout
        self.hLayout.addWidget(self.leftSplitter)
        self.hLayout.addWidget(self.statusBar)

        # add widgets
        self.leftSplitter.addWidget(self.treeView)

        self.setLayout(self.hLayout)

    def update(self, obj):
        """Check if object has changed and update tree in case."""
        if not obj is self.obj:
            self.obj = obj
            self.model = TreeEditModel(obj)
            self.treeView.setModel(self.model)
            self.model.dataChanged.connect(self.onDataChanged)
            self.selectionModel = self.treeView.selectionModel()
            self.selectionModel.selectionChanged.connect(self.onSelectionChanged)
            self.treeView.setCurrentIndex(self.treeView.model().index(0, 0))
            self.setSaveNeeded(True)

    def setSaveNeeded(self, state=True):
        self.is_save_needed = state
        self.saveLabel.setVisible(state)

    def openContextMenu(self, point):
        """Generate and open context the menu at the given point position."""
        index = self.treeView.indexAt(point)
        pos = QtGui.QCursor.pos()

        if not index.isValid():
            return

        # get the data
        item = self.model.item(index)
        obj_info = self.model.get_obj_info(item)

        # init the menu
        menu = TreeEditContextMenu(obj_dict=obj_info, parent=self)
        menu.exec_(pos)

        self.onSelectionChanged(self.selectionModel.selection())

    def onItemCollapse(self, index):
        """Slot for item collapsed"""
        # dynamic resize
        for ii in range(3):
            self.treeView.resizeColumnToContents(ii)

    def onItemExpand(self, index):
        """Slot for item expand"""
        # dynamic resize
        for ii in range(3):
            self.treeView.resizeColumnToContents(ii)

    def onDataChanged(self, first=None, last=None):
        """Slot for changed data"""
        self.dataChanged.emit()
        self.onSelectionChanged(self.selectionModel.selection())

    def onSelectionChanged(self, itemSelection):
        """Slot for changed item selection"""
        # get the index
        if itemSelection.indexes():
            index = itemSelection.indexes()[0]
        else:
            index = self.treeView.model().index(0, 0)
            self.treeView.setCurrentIndex(index)
            return

        # get the data
        item = self.model.item(index)
        obj = item.object()
        typ = type(obj).__name__
        obj_info = self.model.get_obj_info(item)
        ref_typ = obj_info["ref_typ"] if obj_info else None

        # set statusbar information on class typ
        msg = f"{typ} (Ref: {ref_typ})" if ref_typ else f"{typ}"
        self.statusBar.showMessage(msg)

        # --- choose the respective widget by class type ---
        # numpy array -> table editor
        if typ == "ndarray":
            widget = WTableData(obj, editable=True)
            widget.dataChanged.connect(self.dataChanged.emit)

        elif typ == "MeshSolution":
            widget = WMeshSolution(obj)  # only a view (not editable)

        # list (no pyleecan type, non empty) -> table editor
        # TODO add another widget for lists of non 'primitive' types (e.g. DataND)
        elif isinstance(obj, list) and not self.isListType(ref_typ) and obj:
            widget = WTableData(obj, editable=True)
            widget.dataChanged.connect(self.dataChanged.emit)

        elif (
            obj and ref_typ and ref_typ.startswith("SciDataTool")
        ) or "SciDataTool" in obj.__class__.__module__:
            # check if object has plot method
            try:
                widget = obj.plot(is_create_appli=False)
            except Exception as e:
                widget = WTableParameterEdit(obj)
                widget.dataChanged.connect(self.dataChanged.emit)
        # generic editor
        else:
            # widget = SimpleInputWidget().generate(obj)
            widget = WTableParameterEdit(obj)
            widget.dataChanged.connect(self.dataChanged.emit)

        # --- show the widget ---
        if self.leftSplitter.widget(1) is None:
            self.leftSplitter.addWidget(widget)
        else:
            self.leftSplitter.replaceWidget(1, widget)
            widget.setParent(self.leftSplitter)  # workaround for PySide2 replace bug
            widget.show()
        pass

    def isListType(self, typ):
        if not typ:
            return False
        return typ[0] == "[" and typ[-1] == "]" and typ[1:-1] in self.class_dict

    def isDictType(self, typ):
        if not typ:
            return False
        return typ[0] == "{" and typ[-1] == "}" and typ[1:-1] in self.class_dict
