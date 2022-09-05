# -*- coding: utf-8 -*-
from PySide2 import QtWidgets, QtGui, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvas # needed for proper exe gen.

import sys
from os.path import dirname, join, isfile
from sys import argv, exit

from PySide2.QtCore import QTranslator
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QIcon

try:  # Import if pyleecan is installed with pip
    from .definitions import ROOT_DIR, PACKAGE_NAME, config_dict
    from .GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
    from .GUI.Dialog.DMatLib.DMatLib import DMatLib
    from .GUI.Tools.SidebarWindow import SidebarWindow
    from .GUI.Tools.MachinePlotWidget import MachinePlotWidget
    from .GUI.Tools.WTreeEdit.WTreeEdit import WTreeEdit
    from .GUI.Tools.GuiOption.WGuiOption import WGuiOption
    from .Functions.load import load_matlib
    from .GUI.Resources import pixmap_dict
except ImportError:  # Import for dev version
    exec("from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup")
    exec("from pyleecan.GUI.Dialog.DMatLib.DMatLib import DMatLib")
    exec("from pyleecan.GUI.Tools.SidebarWindow import SidebarWindow")
    exec("from pyleecan.GUI.Tools.MachinePlotWidget import MachinePlotWidget")
    exec("from pyleecan.GUI.Tools.WTreeEdit.WTreeEdit import WTreeEdit")
    exec("from pyleecan.GUI.Tools.GuiOption.WGuiOption import WGuiOption")
    exec("from pyleecan.Functions.load import load_matlib")
    exec("from pyleecan.definitions import PACKAGE_NAME, ROOT_DIR, config_dict")
    exec("from pyleecan.GUI.Resources import pixmap_dict")

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
    if isfile(config_dict["GUI"]["CSS_PATH"]):
        with open(config_dict["GUI"]["CSS_PATH"], "r") as css_file:
            a.setStyleSheet(css_file.read())

    # Load Material Library
    material_dict = load_matlib(
        machine=None, matlib_path=config_dict["MAIN"]["MATLIB_DIR"]
    )

    # MatLib widget
    mat_widget = DMatLib(material_dict=material_dict)

    # Machine Setup Widget
    c = DMachineSetup(
        material_dict=material_dict, machine_path=config_dict["MAIN"]["MACHINE_DIR"]
    )

    if EXT_GUI:
        # Setup extended GUI with sub windows
        icon = pixmap_dict["soft_icon"]
        window = SidebarWindow()
        window.setWindowIcon(QIcon(icon))

        update_step = lambda: c.set_nav(c.nav_step.currentRow())
        window.addSubWindow("Design", c, update_step)
        window.DesignWidget = c

        plt_widget = MachinePlotWidget(window)
        window.addSubWindow("Plot", plt_widget, plt_widget.update)

        mat_widget.installEventFilter(window)
        window.addSubWindow("MatLib", mat_widget, mat_widget.update_treeview_material)

        tree = WTreeEdit(c.machine)
        tree_fcn = lambda: tree.update(getattr(c, "machine"))
        window.addSubWindow("TreeEdit", tree, tree_fcn)

        option = WGuiOption(machine_setup=c, matlib=mat_widget)
        window.addSubWindow("Option", option)
        window.show()

    else:
        # "Normal" GUI
        c.show()

    exit(a.exec_())


if __name__ == "__main__":
    run_GUI(argv)
