# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

# === TreeView ========================================================================
class TreeView(QtWidgets.QTreeView):
    def __init__(self):
        super(QtWidgets.QTreeView, self).__init__()

        # self.__typeWidgets = {}
        # self.__typeWrappers = {}

        model = QtGui.QStandardItemModel(0, 1)
        model.setHorizontalHeaderLabels(["Name", "Value", "Unit", "Class", "Description"])

        self.rootNode = model.invisibleRootItem()

        self.setModel(model)
        self.setColumnWidth(0, 150)

        self.setAlternatingRowColors(True)

    def generate(self, data, parent=None):
        if parent is None:
            parent = self.rootNode
            self.rootNode.removeRows(0, self.rootNode.rowCount())
        if hasattr(data, "as_dict"):
            self.generate_branch(data, parent)
        else:
            pass

    def generate_branch(self, data, parent):
        for attr in data.as_dict():
            if attr[0] != "_":
                _attr = getattr(data, attr)
                # pyleecan object attributes
                if hasattr(_attr, "as_dict"):
                    branch = QtGui.QStandardItem(attr)
                    branch.setEditable(False)
                    value = QtGui.QStandardItem("")
                    value.setEditable(False)
                    unit = QtGui.QStandardItem("")
                    cls_name = QtGui.QStandardItem(type(_attr).__name__)
                    # class description rathern than attribure description
                    cls_doc = (
                        getattr(type(data), attr).__doc__
                        if _attr.__doc__ is None
                        else _attr.__doc__
                    )
                    cls_doc = QtGui.QStandardItem(cls_doc)
                    parent.appendRow([branch, value, unit, cls_name, cls_doc])
                    self.generate(_attr, parent=branch)

                # float, int, str attributes
                elif isinstance(_attr, (float, int, str)):
                    attribute = QtGui.QStandardItem(attr)
                    attribute.setEditable(False)
                    value = QtGui.QStandardItem(str(getattr(data, attr)))
                    value.setEditable(False)
                    unit = QtGui.QStandardItem("na")
                    cls_name = QtGui.QStandardItem(type(_attr).__name__)
                    cls_doc = getattr(
                        type(data), attr
                    ).__doc__  # tc.__class__.prop.__doc__
                    cls_doc = QtGui.QStandardItem(cls_doc)
                    parent.appendRow([attribute, value, unit, cls_name, cls_doc])

                # todo: list, dict, ndarray attributes
                else:
                    pass

