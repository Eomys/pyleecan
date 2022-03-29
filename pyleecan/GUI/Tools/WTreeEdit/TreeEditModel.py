# -*- coding: utf-8 -*-

from ....Classes._ClassInfo import ClassInfo
from .TreeEditModelItems import ObjectItem, UnknownItem

from PySide2.QtCore import Qt, QAbstractItemModel, QModelIndex, Signal
from PySide2.QtGui import QColor, QBrush, QFont

""" from QAbstractItemModel doc: 
When subclassing QAbstractItemModel, at the very least you must implement index(), 
parent(), rowCount(), columnCount(), and data(). ... in all read-only models ...
"""


class TreeEditModel(QAbstractItemModel):

    objChanged = Signal(object)
    dataChanged = Signal(object, object)

    def __init__(self, obj, parent=None):
        super(TreeEditModel, self).__init__(parent)
        self._obj = obj
        self._class_dict = ClassInfo().get_dict()
        self._header = ["Object", "Size"]
        self.rootItem = None
        self._cache = []

        self.setRoot()
        self.setupModelData(obj)

        self.objChanged.connect(self.updateItem)

    def setRoot(self):
        self.rootItem = ObjectItem(None, "root", parent=None)

    def setupModelData(self, obj, name=None, index=None, parent=None, viewItem=None):
        """
        obj : an object (that should be modeled and shown)
        parent : a model item
        name : name of the property (or the parent that contains the object)
        id : list index or dict key if parent object is a list or a dict
        """
        if viewItem is None:
            if parent is None:
                parent = self.rootItem
                name = type(obj).__name__
            viewItem = ObjectItem(obj, name, index=index, parent=parent)

        # prepare the objects properties
        props = []
        typ = type(obj).__name__
        if typ in self._class_dict:
            cls_props = self._class_dict[typ]["prop_dict"]
            for prop_name, prop_info in cls_props.items():
                prop = getattr(obj, prop_name)
                props.append([prop, prop_name, prop_info["type"], None])
        elif hasattr(obj, "as_dict"):
            obj_dict = obj.as_dict()
            for prop_name in obj_dict.keys():
                if not prop_name.startswith("_"):
                    prop = getattr(obj, prop_name)
                    prop_type = type(prop).__name__
                    props.append([prop, prop_name, prop_type, None])
        elif isinstance(obj, (list, dict)):
            iter = enumerate(obj) if isinstance(obj, list) else obj.items()
            for ii, item in iter:
                item_name = viewItem.name() + f"[{ii}]"
                item_type = type(item).__name__
                props.append([item, item_name, item_type, ii])

        # create the object properties
        for prop, prop_name, prop_type, index in props:

            # pyleecan type properties
            if prop_type in self._class_dict:
                self.setupModelData(prop, name=prop_name, index=index, parent=viewItem)

            # list or dict of pyleecan type
            elif self.isListType(prop_type) or self.isDictType(prop_type):
                child = ObjectItem(prop, name=prop_name, index=index, parent=viewItem)
                if prop is not None:
                    iter = enumerate(prop) if isinstance(prop, list) else prop.items()
                    for ii, item in iter:
                        it_name = prop_name + f"[{ii}]"
                        self.setupModelData(item, name=it_name, index=ii, parent=child)

            # base python types
            elif self.is_not_tree_type(prop, prop_type):
                pass  # don't show base types in the tree

            # numpy array # TODO only ndarrays with more than 2 dims
            elif prop_type == "ndarray":
                self.setupModelData(prop, name=prop_name, index=index, parent=viewItem)

            # 'normal' lists or dicts, i.e. list or dicts with no pyleecan type
            elif prop_type in ["list", "dict"] or isinstance(prop, (list, dict)):
                child = ObjectItem(prop, name=prop_name, index=index, parent=viewItem)
                if prop is not None:
                    iter = enumerate(prop) if isinstance(prop, list) else prop.items()
                    for ii, item in iter:
                        it_name = prop_name + f"[{ii}]"
                        self.setupModelData(item, name=it_name, index=ii, parent=child)

            # pyleecan compatible types
            elif prop is not None and hasattr(prop, "as_dict"):
                self.setupModelData(prop, name=prop_name, index=index, parent=viewItem)

            # not implemented types
            else:
                child = UnknownItem(prop, name=prop_name, index=index, parent=viewItem)

    def is_not_tree_type(self, prop, prop_type):
        if prop_type in ["float", "bool", "int", "str"]:
            return True
        if isinstance(prop, (float, bool, int, str)):
            return True
        return False

    def get_obj_info(self, item):
        """Get some information on the object in the context of its parent."""
        obj = item.object()
        parent = item.parent()
        parent_obj = parent.object()
        parent_typ = type(parent_obj).__name__

        name = item.name()
        index = item.index()

        # item must be the root if parent is None
        # if parent_obj is None:
        #     obj_info = dict()
        #     obj_info["obj"] = obj
        #     obj_info["parent"] = None
        #     obj_info["parent_typ"] = None
        #     obj_info["property"] = name
        #     obj_info["ref_typ"] = None
        #     obj_info["index"] = None

        # setup object information
        obj_info = dict()
        obj_info["obj"] = obj
        obj_info["parent"] = item.parent().object()
        obj_info["parent_typ"] = parent_typ
        obj_info["property"] = name
        obj_info["ref_typ"] = None
        obj_info["index"] = index  # list index of dict key in case parent is list/dict

        # add 'reference type' if parent is a pyleecan object
        if parent_typ in self._class_dict:
            props = self._class_dict[parent_typ]["prop_dict"]
            obj_info["ref_typ"] = props[name]["type"]

        # for lists/dicts get ref. type information from parent (due to model structure)
        elif isinstance(parent_obj, (list, dict)):
            parent_info = self.get_obj_info(parent)
            obj_info["property"] = parent_info["property"]
            ref_typ = parent_info["ref_typ"]
            if self.isListType(ref_typ) or self.isDictType(ref_typ):
                obj_info["ref_typ"] = ref_typ[1:-1]

        return obj_info

    def index(self, row, column, index=QModelIndex()):
        """Get the index of the item in the model."""
        if not self.hasIndex(row, column, index):
            return QModelIndex()

        if not index.isValid():
            item = self.rootItem
        else:
            item = self.item(index)

        child = item.child(row)
        if child:
            return self.createIndex(row, column, child)
        return QModelIndex()

    def item(self, index):
        """Get the item from the given index."""
        if not index.isValid():
            return None

        item = index.internalPointer()
        if isinstance(item, ObjectItem):
            return item
        else:
            print("TreeEditModel: Invalid index")

    # TODO add check to 'index' and 'parent' method / test rowcount etc.
    def parent(self, index):
        """Get the parent of the item with the given index. If the item has no parent,
        an invalid QModelIndex is returned.
        """
        if not index.isValid():
            return QModelIndex()

        item = self.item(index)
        if not item:
            return QModelIndex()

        parent = item.parent()
        if parent is self.rootItem or parent is None or parent.row() is None:
            return QModelIndex()

        return self.createIndex(parent.row(), 0, parent)

    def rowCount(self, index=QModelIndex()):
        """Get the number of rows of the item of the given index."""

        if index.isValid():
            item = self.item(index)
        else:
            item = self.rootItem
        return item.childCount()

    def columnCount(self, index=QModelIndex()):
        """Get the number of columns of the model."""
        if self.rootItem is not None:
            return self.rootItem.columnCount()
        return 0

    def data(self, index, role=None):
        """Get data of the given role for the item referred to by the index."""
        item = self.item(index)

        if role == Qt.DisplayRole:
            return item.name()
        elif role == Qt.FontRole:
            obj = item.object()
            is_empty = isinstance(obj, (list, dict)) and not obj
            if isinstance(item, UnknownItem) or is_empty or obj is None:
                font = QFont()
                font.setItalic(True)
                return font
        elif role == Qt.ForegroundRole:
            if isinstance(item, UnknownItem):
                return QBrush(QColor("#777777"))
        elif role is None:
            return item.object()
        else:
            return item.data(role=role)

        # check if object has changed and update in case
        if not self.isValid(item):
            self.objChanged.emit(index)

    def isValid(self, item):
        """Check if the view item still represent the respective object."""
        ref_obj = self._get_object(item)
        if isinstance(ref_obj, (list, dict)):
            nb_not_tree = 0
            iter = enumerate(ref_obj) if isinstance(ref_obj, list) else ref_obj.items()
            for ii, iter_item in iter:
                if self.is_not_tree_type(iter_item, type(iter_item).__name__):
                    nb_not_tree += 1
            return True if len(ref_obj) - nb_not_tree == item.childCount() else False
        return True if ref_obj is item.object() else False

    def updateItem(self, index):
        print("TreeEditModel: Updating.")
        self.layoutAboutToBeChanged.emit()
        item = self.item(index)
        new_obj = self._get_object(item)

        self.removeRows(0, self.item(index).childCount(), parent=index)

        # self.beginInsertRows(index, 0, item.childCount() - 1)
        item.setObject(new_obj)
        self.setupModelData(new_obj, viewItem=item)
        # self.endInsertRows()

        self.layoutChanged.emit()
        self.dataChanged.emit(QModelIndex(), QModelIndex())

    def removeRows(self, row, count, parent=QModelIndex()):
        """Remove the given rows from the model."""
        self._cache.clear()
        if not parent.isValid():
            return False
        item = self.item(parent)
        self.beginRemoveRows(parent, row, row + count - 1)
        # self.beginResetModel()

        children = item.children()
        for ii in reversed(range(row, row + count)):
            child = children.pop(ii)
            print(f"Cached removed child '{child.name()}'")
            # the object is cached for some time to avoid a crash when the views
            # try to get the object via the model index's internalPointer method
            self._cache.append(child)

        # self.endResetModel()
        self.endRemoveRows()
        return True

    def _get_object(self, item):
        """
        Get the object that is referenced by the 'item' indirecly, i.e. from its parent.
        """
        parent = item.parent().object()

        if item.parent().name() == "root":
            ref_obj = self._obj
        elif isinstance(parent, (list, dict)):
            ref_obj = parent[item.index()]
        else:
            ref_obj = getattr(parent, item.name())

        return ref_obj

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """Get the data for the given role and section in the header with the specified
        orientation.
        """
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._header[section]

    def isListType(self, typ):
        return (
            typ and typ[0] == "[" and typ[-1] == "]" and typ[1:-1] in self._class_dict
        )

    def isDictType(self, typ):
        return (
            typ and typ[0] == "{" and typ[-1] == "}" and typ[1:-1] in self._class_dict
        )
