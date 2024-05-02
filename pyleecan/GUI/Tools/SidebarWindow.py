import sys
from qtpy import QtWidgets, QtGui, QtCore

"""
def _setColor(widget):
    widget.setAutoFillBackground(True)
    p = widget.palette()
    p.setColor(widget.backgroundRole(), QtCore.Qt.red)
    widget.setPalette(p)
"""


class SidebarWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # === App-Init ===
        super(SidebarWindow, self).__init__()
        self._title = "Pyleecan"
        self.setWindowTitle(self._title)
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)

        # === Main Widgets ===
        # Navigation Panel with Button Group
        self.nav_panel = QtWidgets.QFrame()

        self.nav_btn_grp = QtWidgets.QButtonGroup()
        self.nav_btn_grp.setExclusive(True)
        self.nav_btn_grp.buttonClicked[int].connect(self.switch_stack)
        self.btn_grp_fct = []

        self.nav_layout = QtWidgets.QVBoxLayout(self.nav_panel)
        self.nav_layout.setContentsMargins(2, 2, 2, 2)
        self.nav_layout.addStretch(1)  # add stretch first

        # Sub Window Stack
        self.io_stack = QtWidgets.QStackedWidget(self)

        # Seperator Line
        line = QtWidgets.QFrame()
        line.setStyleSheet("QFrame { background-color: rgb(200, 200, 200) }")
        line.setFixedWidth(2)

        # === Main Layout ===
        main_layout = QtWidgets.QHBoxLayout()
        main_layout.addWidget(self.nav_panel)
        main_layout.addWidget(line)
        main_layout.addWidget(self.io_stack)

        self._main.setLayout(main_layout)

        self.show()
        self.centerOnScreen()

    def close_application(self):
        sys.exit()

    def switch_stack(self, btn):
        # print('Button Nbr. %2d pressed' % btn)
        self.io_stack.setCurrentIndex(btn)  # set stack
        if self.btn_grp_fct[btn] is not None:  # execute user function
            self.btn_grp_fct[btn]()

    def centerOnScreen(self):
        """centerOnScreen() - Centers the window on the screen."""
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        frame = self.frameSize()
        self.move(
            (resolution.width() / 2) - (frame.width() / 2),
            (resolution.height() / 2) - (frame.height() / 2),
        )

    def addSubWindow(self, name, widget, btn_fct=None):
        """add a new sub window to the stack including the coresponding button"""
        # Button
        btn = QtWidgets.QPushButton(name)
        btn.setFixedSize(100, 40)
        btn.setCheckable(True)

        self.nav_btn_grp.addButton(btn, self.io_stack.count())
        self.nav_layout.insertWidget(self.io_stack.count(), btn)
        self.btn_grp_fct.insert(self.io_stack.count(), btn_fct)

        # Stack
        self.io_stack.addWidget(widget)

    def eventFilter(self, obj, event):
        """
        Event Filter to disable 'Esc'-Key in a Widgets.
        To install eventFilter on a Widget:
            widget.installEventFilter(instance_of_main_window)
        """
        if event.type() == QtCore.QEvent.KeyPress:
            if event.key() in (QtCore.Qt.Key_Escape,):
                return True
        return super(SidebarWindow, self).eventFilter(obj, event)

    def closeEvent(self, event):
        """Overload the methode to call DesignWidget.closeEvent"""
        self.DesignWidget.closeEvent(event)
