# -*- coding: utf-8 -*-
import sys
from os.path import dirname, join
from sys import argv, exit

from PyQt5.QtCore import QTranslator
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

try:  # Import if pyleecan is installed with pip
    from .definitions import ROOT_DIR, DATA_DIR, MATLIB_DIR, PACKAGE_NAME
    from .GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
    from .GUI.Dialog.DMatLib.DMatLib import DMatLib
    from .GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect
    from .GUI.Tools.SidebarWindow import SidebarWindow
    from .GUI.Tools.MachinePlotWidget import MachinePlotWidget
    from .GUI.Tools.TreeView import TreeView

except ImportError:  # Import for dev version
    from definitions import PACKAGE_NAME, DATA_DIR, MATLIB_DIR, ROOT_DIR

    exec(
        "from "
        + PACKAGE_NAME
        + ".GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup"
    )
    exec("from " + PACKAGE_NAME + ".GUI.Dialog.DMatLib.DMatLib import DMatLib")
    exec(
        "from "
        + PACKAGE_NAME
        + ".GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect"
    )
    exec("from " + PACKAGE_NAME + ".GUI.Tools.SidebarWindow import SidebarWindow")
    exec(
        "from " + PACKAGE_NAME + ".GUI.Tools.MachinePlotWidget import MachinePlotWidget"
    )
    exec("from " + PACKAGE_NAME + ".GUI.Tools.TreeView import TreeView")

    sys.path.insert(0, ROOT_DIR)

EXT_GUI = True


def run_GUI(argv):
    # Default material data path

    # Script to be used to test in dev
    a = QApplication(argv)

    # Set CSS
    # a.setStyleSheet("QLineEdit { background-color: yellow }")

    # Setup the translation
    translationFile = "pyleecan_fr.qm"
    translator = QTranslator()
    translator.load(translationFile, "GUI//i18n")
    a.installTranslator(translator)

    # Machine Setup Widget
    c = DMachineSetup(machine_path=join(DATA_DIR, "Machine"), matlib_path=MATLIB_DIR)

    if EXT_GUI:
        # Setup extended GUI with sub windows
        icon = dirname(__file__) + "/GUI/Resources/images/icon/pyleecan_64.png"
        window = SidebarWindow()
        window.setWindowIcon(QIcon(icon))

        update_step = lambda: c.set_nav(c.nav_step.currentRow())
        window.addSubWindow("Design", c, update_step)
        window.DesignWidget = c

        plt_widget = MachinePlotWidget(window)
        window.addSubWindow("Plot", plt_widget, plt_widget.update)

        mat_widget = DMatLib(window.DesignWidget.matlib, selected=0)
        mat_widget.installEventFilter(window)
        window.addSubWindow("MatLib", mat_widget, mat_widget.update_mat_list)

        tree = TreeView()
        tree_fcn = lambda: tree.generate(getattr(c, "machine"))
        window.addSubWindow("TreeView", tree, tree_fcn)

        window.show()

    else:
        # "Normal" GUI
        c.show()

    exit(a.exec_())


if __name__ == "__main__":
    run_GUI(argv)
