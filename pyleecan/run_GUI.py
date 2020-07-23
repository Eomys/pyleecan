# -*- coding: utf-8 -*-
import sys
from os.path import dirname, join, isfile
from sys import argv, exit

from PyQt5.QtCore import QTranslator
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

try:  # Import if pyleecan is installed with pip
    from .definitions import ROOT_DIR, PACKAGE_NAME, config_dict
    from .GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
    from .GUI.Dialog.DMatLib.DMatLib import DMatLib
    from .GUI.Dialog.DMatLib.MatLib import MatLib
    from .GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect
    from .GUI.Tools.SidebarWindow import SidebarWindow
    from .GUI.Tools.MachinePlotWidget import MachinePlotWidget
    from .GUI.Tools.TreeView import TreeView
    from .GUI.Tools.GuiOption.WGuiOption import WGuiOption

except ImportError:  # Import for dev version
    from definitions import PACKAGE_NAME, ROOT_DIR, config_dict

    exec(
        "from "
        + PACKAGE_NAME
        + ".GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup"
    )
    exec("from " + PACKAGE_NAME + ".GUI.Dialog.DMatLib.DMatLib import DMatLib")
    exec("from " + PACKAGE_NAME + ".GUI.Dialog.DMatLib.MatLib import MatLib")
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
    exec("from " + PACKAGE_NAME + ".GUI.Tools.GuiOption.WGuiOption import WGuiOption")


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

    # Setting the material library
    matlib = MatLib(config_dict["MAIN"]["MATLIB_DIR"])

    # MatLib widget
    mat_widget = DMatLib(matlib, selected=0)

    # Machine Setup Widget
    c = DMachineSetup(
        dmatlib=mat_widget, machine_path=config_dict["MAIN"]["MACHINE_DIR"]
    )

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

        mat_widget.installEventFilter(window)
        window.addSubWindow("MatLib", mat_widget, mat_widget.update_list_mat)

        tree = TreeView()
        tree_fcn = lambda: tree.generate(getattr(c, "machine"))
        window.addSubWindow("TreeView", tree, tree_fcn)

        option = WGuiOption(machine_setup=c, matlib=matlib)
        window.addSubWindow("Option", option)
        window.show()

    else:
        # "Normal" GUI
        c.show()

    exit(a.exec_())


if __name__ == "__main__":
    run_GUI(argv)
