# https://gis.stackexchange.com/questions/350148/qcombobox-multiple-selection-pyqt5

from qtpy.QtWidgets import QComboBox, QStyledItemDelegate, QApplication
from qtpy.QtGui import QPalette, QStandardItem, QFontMetrics
from qtpy.QtCore import QEvent, Qt, Signal


class CheckableComboBox(QComboBox):
    selectionChanged = Signal()

    # Subclass Delegate to increase item height
    class Delegate(QStyledItemDelegate):
        def sizeHint(self, option, index):
            size = super().sizeHint(option, index)
            size.setHeight(20)
            return size

    def __init__(
        self, *args, label=None, singleSelection=False, allowNoSelection=True, **kwargs
    ):
        super().__init__(*args, **kwargs)

        self._label = label
        self._singleSelection = singleSelection
        self._allowNoSelection = allowNoSelection
        self._selectionChanged = False

        # Make the combo editable to set a custom text, but readonly
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        # Make the lineedit the same color as QPushButton
        palette = QApplication.palette()
        palette.setBrush(QPalette.Base, palette.button())
        self.lineEdit().setPalette(palette)

        # Use custom delegate
        self.setItemDelegate(CheckableComboBox.Delegate())

        # Update the text when an item is toggled
        self.model().dataChanged.connect(self.onDataChanged)

        # Hide and show popup when clicking the line edit
        self.lineEdit().installEventFilter(self)
        self.closeOnLineEditClick = False

        # Prevent popup from closing when clicking on an item
        self.view().viewport().installEventFilter(self)

    def resizeEvent(self, event):
        # Recompute text to elide as needed
        self.updateText()
        super().resizeEvent(event)

    def eventFilter(self, object, event):
        if object == self.lineEdit():
            if event.type() == QEvent.MouseButtonRelease:
                if self.closeOnLineEditClick:
                    self.hidePopup()
                else:
                    self.showPopup()
                return True
            return False

        if object == self.view().viewport():
            if event.type() == QEvent.MouseButtonRelease:
                index = self.view().indexAt(event.pos())
                item = self.model().item(index.row())

                if item.checkState() == Qt.Checked:
                    item.setCheckState(Qt.Unchecked)
                else:
                    item.setCheckState(Qt.Checked)
                return True
        return False

    def showPopup(self):
        super().showPopup()
        # When the popup is displayed, a click on the lineedit should close it
        self.closeOnLineEditClick = True

    def hidePopup(self):
        super().hidePopup()
        # Used to prevent immediate reopening when clicking on the lineEdit
        self.startTimer(100)
        # Refresh the display text when closing
        self.updateText()
        if self._selectionChanged:
            self.selectionChanged.emit()
            self._selectionChanged = False

    def timerEvent(self, event):
        # After timeout, kill timer, and reenable click on line edit
        self.killTimer(event.timerId())
        self.closeOnLineEditClick = False

    def onDataChanged(self, topLeft=None, bottomRight=None):
        current = self.currentData()

        item = None
        if topLeft is not None and topLeft.isValid():
            item = self.model().itemFromIndex(topLeft)

        if not self._allowNoSelection:
            if not current and self.model().rowCount() > 0:
                self.model().item(0).setCheckState(Qt.Checked)

        if self._singleSelection:
            if item is not None and item.data(Qt.CheckStateRole) == Qt.Checked:
                text = item.text()
                for i in range(self.model().rowCount()):
                    others = self.model().item(i)
                    if others.checkState() == Qt.Checked and others.text() != text:
                        self.model().item(i).setCheckState(Qt.Unchecked)

        self._selectionChanged = True
        self.updateText()

    def updateText(self):
        texts = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.Checked:
                texts.append(self.model().item(i).text())
        text = self._label + ": " if self._label else ""
        text += ", ".join(texts)

        # Compute elided text (with "...")
        # metrics = QFontMetrics(self.lineEdit().font())
        # elidedText = metrics.elidedText(text, Qt.ElideRight, self.lineEdit().width())
        # self.lineEdit().setText(elidedText)

        self.lineEdit().setText(text)  # no elided text for now

    def addItem(self, text, data=None):
        item = QStandardItem()
        item.setText(text)
        if data is None:
            item.setData(text)
        else:
            item.setData(data)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        item.setData(Qt.Unchecked, Qt.CheckStateRole)
        self.model().appendRow(item)
        self.onDataChanged()

    def addItems(self, texts, datalist=None):
        for i, text in enumerate(texts):
            try:
                data = datalist[i]
            except (TypeError, IndexError):
                data = None
            self.addItem(text, data)
        self.onDataChanged()

    def currentData(self):
        # Return the list of selected items data
        res = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.Checked:
                res.append(self.model().item(i).data())
        return res
