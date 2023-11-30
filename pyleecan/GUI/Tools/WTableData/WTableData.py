from numpy import zeros
from PySide2.QtWidgets import QTableView, QDialog, QVBoxLayout
from PySide2.QtCore import Qt, QAbstractTableModel, Signal


class DTableData(QDialog):
    def __init__(self, data=zeros((1, 1))):
        super(DTableData, self).__init__()
        self.data = data

        self.main_layout = QVBoxLayout(self)
        self.tab = WTableData(data)
        self.main_layout.addWidget(self.tab)


class WTableData(QTableView):
    dataChanged = Signal()

    def __init__(self, data=zeros((1, 1)), editable=False):
        super(WTableData, self).__init__()
        self.data = data

        if isinstance(data, list):
            self.data_model = TableModelList(self.data, editable=editable)
        else:
            self.data_model = TableModelNumpy(self.data, editable=editable)
        self.setModel(self.data_model)
        self.resizeColumnsToContents()

        self.data_model.dataChanged.connect(self.dataChanged.emit)


class TableModelNumpy(QAbstractTableModel):
    dataChanged = Signal()

    def __init__(self, data, editable=False):
        super(TableModelNumpy, self).__init__()
        self._data = data
        self._shape = data.shape
        self._ndims = len(self._shape)
        self._editable = editable

    def data(self, index, role=Qt.UserRole):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            # Note: self._data[index.row()][index.column()] will also work
            return str(self._data[self.dataIndex(index)])
        elif role == Qt.UserRole:
            return self._data[self.dataIndex(index)]

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            try:
                type(self.data(index))(value)
            except ValueError:
                return False
            self._data[self.dataIndex(index)] = value
            self.dataChanged.emit()
            return True
        return False

    def flags(self, index):
        if self._editable:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
        else:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled

    def rowCount(self, index):
        return self._shape[0]

    def columnCount(self, index):
        if self._ndims == 1:
            return 1
        else:
            return self._shape[1]

    def dataIndex(self, index):
        if self._ndims == 1:
            return index.row()
        else:
            return index.row(), index.column()


class TableModelList(QAbstractTableModel):
    dataChanged = Signal()

    def __init__(self, data, editable=False):
        super(TableModelList, self).__init__()
        self._data = data
        self._editable = editable

        self._rows = len(data)
        self._columns = len(data[0]) if isinstance(data[0], list) else 0
        self._valid = True
        for item in data:
            if isinstance(item, list) and len(item) != self._columns:
                self._valid = False
                self._editable = False

    def data(self, index, role=Qt.UserRole):
        # TODO typ check
        if role == Qt.DisplayRole or role == Qt.EditRole:
            # Note: self._data[index.row()][index.column()] will also work
            return str(self._get_data(index)) if self._valid else "unsupported size"
        elif role == Qt.UserRole:
            return self._get_data(index) if self._valid else None

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            try:
                value = type(self.data(index))(value)
                self._set_data(index, value)
            except ValueError:
                return False
            self.dataChanged.emit()
            return True
        return False

    def flags(self, index):
        if self._editable and self._valid:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
        else:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled

    def rowCount(self, index):
        return self._rows

    def columnCount(self, index):
        return self._columns if self._columns != 0 else 1

    def _get_data(self, index):
        if not self._valid:
            return None
        item = self._data[index.row()]
        if self._columns == 0:
            return item
        return item[index.column()]

    def _set_data(self, index, value):
        if not self._valid:
            return
        if self._columns == 0:
            self._data[index.row()] = value
        else:
            self._data[index.row()][index.column()] = value
