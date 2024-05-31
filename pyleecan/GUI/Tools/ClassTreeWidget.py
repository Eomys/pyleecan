# -*- coding: utf-8 -*-

from os.path import join

from qtpy import QtGui
from qtpy.QtCore import Qt, Signal
from qtpy.QtGui import QIcon
from qtpy.QtWidgets import QDialog, QLabel, QSplitter, QTreeView
from qtpy.QtWidgets import QDialogButtonBox, QVBoxLayout, QHBoxLayout

from ...definitions import ROOT_DIR
from ...Classes._ClassInfo import ClassInfo

ICON = join(ROOT_DIR, "pyleecan/GUI/Resources/images/icon/pyleecan_64.png")


class ClassTreeWidget(QDialog):
    """
    TreeView widget to show pyleecan classes structured by their inheritance together
    with the selected class description.
    """

    def __init__(self, keys=None, expand=True):
        super(ClassTreeWidget, self).__init__()
        self.setupUi()
        self.expandAll = expand
        self.setMinimumHeight(600)

        # === default variables ===
        self.classDict = ClassInfo().get_dict()
        self.keys = keys or ClassInfo().get_base_classes()  # TODO all classes
        self.selectionModel = self.treeView.selectionModel()

        # === Signals ===
        self.selectionModel.selectionChanged.connect(self.onSelectionChanged)
        self.treeView.doubleClicked.connect(self.onClassSelected)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        # === Generate content ===
        self.generate()

    def onClassSelected(self, index):
        """Method to accept the selection if a class was double clicked."""
        if index.isValid():
            self.accept()

    def onSelectionChanged(self, itSelection):
        """ """
        index = itSelection.indexes()[0]
        desc = index.model().itemFromIndex(index).data()
        self.text.setText(desc)

    def getSelectedClass(self):
        """Get the currently selected class by its name."""
        index = self.selectionModel.selectedIndexes()[0]
        return index.model().itemFromIndex(index).text()

    def setupUi(self):
        """Init. the UI."""
        self.setWindowIcon(QIcon(ICON))
        # === Widgets ===
        # TreeView
        model = QtGui.QStandardItemModel(0, 1)
        model.setHorizontalHeaderLabels(["Class"])

        self.treeView = QTreeView()
        self.treeView.rootNode = model.invisibleRootItem()
        self.treeView.setModel(model)
        self.treeView.setAlternatingRowColors(False)

        # size options
        # setting min. width in self.generate to fit content

        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)

        # Hide Debug Columns
        # self.treeView.hideColumn(1)

        # text output
        self.text = QLabel()
        self.text.setAlignment(Qt.AlignTop)
        self.text.setWordWrap(True)
        self.text.setMinimumWidth(300)

        # Splitters
        self.splitter = QSplitter(self)
        self.splitter.setStretchFactor(0, 0)
        self.splitter.setStretchFactor(1, 1)
        self.splitter.addWidget(self.treeView)
        self.splitter.addWidget(self.text)

        # dialog buttons
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )  # window to create confirmation and cancellation buttons

        # === Layout ===
        # Horizontal Div.
        layout = QVBoxLayout()

        # layout.setContentsMargins(0, 0, 0, 0)
        # layout.setSpacing(0)

        layout.addWidget(self.splitter)
        layout.addWidget(self.buttons)

        self.setLayout(layout)

    def generate(self):
        """Method to (recursively) build the tree (view) of the data object."""
        self.treeDict = dict()
        for key in self.keys:
            self.genTreeDict(key, self.treeDict)

        self.genTreeView(self.treeDict)

        # set first row active & expand all branches
        index = self.treeView.model().index(0, 0)
        self.treeView.setCurrentIndex(index)
        self.treeView.expandAll()
        wHint = self.treeView.sizeHintForColumn(0)
        self.treeView.setMinimumWidth(wHint)
        self.treeView.setColumnWidth(0, wHint)
        if not self.expandAll:
            self.treeView.collapseAll()

    def genTreeDict(self, key, parent):
        """Generate a dict structure of the classes recursively on the parent dict."""
        parent[key] = dict()
        for typ in self.classDict[key]["daughters"]:
            if key == self.classDict[typ]["mother"]:
                self.genTreeDict(typ, parent[key])

    def genTreeView(self, tree, parent=None):
        """Generate the view item structure on the parent item."""
        # init if root
        if parent is None:
            parent = self.treeView.rootNode
            self.treeView.rootNode.removeRows(0, self.treeView.rootNode.rowCount())

        for key, item in tree.items():
            desc = (
                f"Class: {key} \nPackage: {self.classDict[key]['package']}"
                + f"\nDescription: {self.classDict[key]['desc']}"
            )
            row = self.addRow(parent, key, desc)

            if item:
                self.genTreeView(item, parent=row)

    def addRow(self, parent, name="", desc=""):
        """Add a new row to the parent item."""
        item = QtGui.QStandardItem(name)
        item.setEditable(False)
        item.setData(desc)
        parent.appendRow([item])
        return item
