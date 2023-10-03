# -*- coding: utf-8 -*-
from PySide2 import QtWidgets, QtGui, QtCore
from matplotlib.backends.backend_qt5agg import (
    FigureCanvas,
)  # needed for proper exe gen.

import sys
from os.path import dirname, join, isfile
from sys import argv, exit

from PySide2.QtCore import QTranslator
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QIcon

try:  # Import if pyleecan is installed with pip
    from .definitions import ROOT_DIR, PACKAGE_NAME, config_dict
    from .GUI.Dialog.DClassGenerator.DClassGenerator import DClassGenerator
    from .GUI.Dialog.DMatLib.DMatLib import DMatLib
    from .GUI.Tools.SidebarWindow import SidebarWindow
    from .GUI.Tools.MachinePlotWidget import MachinePlotWidget
    from .GUI.Tools.WTreeEdit.WTreeEdit import WTreeEdit
    from .GUI.Tools.GuiOption.WGuiOption import WGuiOption
    from .Functions.load import load_matlib
    from .GUI.Resources import pixmap_dict

except ImportError:  # Import for dev version
    exec(
        "from pyleecan.GUI.Dialog.DClassGenerator.DClassGenerator import DClassGenerator"
    )
    exec("from pyleecan.GUI.Dialog.DMatLib.DMatLib import DMatLib")
    exec("from pyleecan.GUI.Tools.SidebarWindow import SidebarWindow")
    exec("from pyleecan.GUI.Tools.MachinePlotWidget import MachinePlotWidget")
    exec("from pyleecan.GUI.Tools.WTreeEdit.WTreeEdit import WTreeEdit")
    exec("from pyleecan.GUI.Tools.GuiOption.WGuiOption import WGuiOption")
    exec("from pyleecan.Functions.load import load_matlib")
    exec("from pyleecan.definitions import PACKAGE_NAME, ROOT_DIR, config_dict")
    exec("from pyleecan.GUI.Resources import pixmap_dict")

EXT_GUI = True


def run_class_generator(argv):
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

    # Machine Setup Widget
    c = DClassGenerator()

    # Setup extended GUI with sub windows
    icon = pixmap_dict["soft_icon"]
    c.setWindowIcon(QIcon(icon))

    # tree = WTreeEdit(c.machine)
    # tree_fcn = lambda: tree.update(getattr(c, "machine"))
    # window.addSubWindow("TreeEdit", tree, tree_fcn)

    # option = WGuiOption(machine_setup=c, matlib=mat_widget)
    # window.addSubWindow("Option", option)

    # c.treeView.resizeColumnToContents(0)

    c.show()

    exit(a.exec_())


if __name__ == "__main__":
    run_class_generator(argv)
