# -*- coding: utf-8 -*-


class ObjectItem:
    """TreeEditModel item class."""

    def __init__(self, obj, name, index=None, parent=None):
        self._parent = parent
        self._obj = obj
        self._name = name
        self._index = index
        self._children = []

        self._columns = 1

        if parent is not None:
            parent.appendChild(self)

    def parent(self):
        return self._parent

    def children(self):
        return self._children

    def child(self, row):
        if row >= self.childCount():
            return None
        return self._children[row]

    def childCount(self):
        return len(self._children)

    def row(self):
        if self._parent is not None:
            children = self._parent.children()
            return children.index(self) if self in children else None

    def columnCount(self):
        return self._columns

    def object(self):
        return self._obj

    def name(self):
        return self._name

    def appendChild(self, item):
        self._children.append(item)
        item._parent = self

    def clearChildren(self):
        self._children = []

    def setObject(self, obj):
        self._obj = obj

    def data(self, role=None):
        return None

    def index(self):
        return self._index


class UnknownItem(ObjectItem):
    """Convienence class for unknown (not implemented yet) objects."""

    pass
