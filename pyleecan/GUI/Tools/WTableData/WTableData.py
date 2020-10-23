from numpy import zeros
from PySide2.QtWidgets import QTableView, QDialog, QVBoxLayout
from PySide2.QtCore import Qt, QAbstractTableModel


class DTableData(QDialog):
    def __init__(self, data=zeros((1, 1))):
        super(DTableData, self).__init__()
        self.data = data

        self.main_layout = QVBoxLayout(self)
        self.tab = WTableData(data)
        self.main_layout.addWidget(self.tab)


class WTableData(QTableView):
    def __init__(self, data=zeros((1, 1))):
        super(WTableData, self).__init__()
        self.data = data

        self.data_model = TableModelNumpy(self.data)
        self.setModel(self.data_model)


class TableModelNumpy(QAbstractTableModel):
    def __init__(self, data):
        super(TableModelNumpy, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # Note: self._data[index.row()][index.column()] will also work
            value = self._data[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]
