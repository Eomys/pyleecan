from qtpy.QtWidgets import (
    QTableView,
    QLabel,
    QWidget,
    QVBoxLayout,
    QAbstractItemView,
)
from qtpy.QtCore import Signal, Qt

from .WTableParameterModel import WTableParameterModel

# TODO change to QTableWidget to enable Excel like editing ???
#      see. https://pohlondrej.com/qtableview-excel-like-editing/


class WTableParameterEdit(QWidget):
    dataChanged = Signal()

    def __init__(self, obj):
        super(WTableParameterEdit, self).__init__()
        self._obj = obj

        self._model = WTableParameterModel(self._obj)

        self._view = QTableView()
        self._view.setModel(self._model)

        self.setupUi()
        self.setNotEditableHidden(True)
        self.resizeToContent()

        self._model.dataChanged.connect(self.dataChanged.emit)

    def resizeToContent(self):
        """
        Resize all the columns (but the last) to fit the content or the minimum size.
        """
        rootIndex = self._view.rootIndex()
        for colId in range(self._model.columnCount() - 1):
            self._view.resizeColumnToContents(colId)

    def setNotEditableHidden(self, hidden):
        """Set the hide state of all rows that are not editable."""
        rootIndex = self._view.rootIndex()
        for rowId in range(self._model.rowCount()):
            isEditableRow = False
            for colId in range(self._model.columnCount()):
                flag = self._model.flags(self._model.index(rowId, colId, rootIndex))
                if flag & Qt.ItemIsEditable:
                    isEditableRow = True

            self._view.setRowHidden(rowId, not isEditableRow and hidden)

    def setupUi(self):
        header = QLabel(f"{type(self._obj).__name__}")
        font = header.font()
        font.setBold(True)
        header.setFont(font)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(header)

        if isinstance(self._obj, (list, dict)):
            label = f"The {type(self._obj).__name__} has {len(self._obj)} element"
            if len(self._obj) != 1:
                label += "s"
            self.mainLayout.addWidget(QLabel(label + "."))
            self.mainLayout.addStretch()
        elif self._obj is None:
            self.mainLayout.addWidget(QLabel("Not implemented yet."))
            self.mainLayout.addStretch()
        else:
            self.mainLayout.addWidget(self._view)

        self.setLayout(self.mainLayout)

        # === table settings ===
        # self._view.resizeColumnsToContents()
        self._view.verticalHeader().setVisible(False)
        self._view.setFocusPolicy(Qt.NoFocus)
        self._view.setSelectionMode(QAbstractItemView.SingleSelection)
        self._view.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self._view.horizontalHeader().setStretchLastSection(True)
        self._view.horizontalHeader().setSectionsClickable(False)
        # self._view.setMinimumWidth(650)

        self.setMinimumWidth(600)
