import sys
from os.path import dirname, abspath, normpath, join

sys.path.insert(0, normpath(abspath(join(dirname(__file__), ".."))))

from os import mkdir
from os.path import isdir
from sys import argv, exit

from PyQt5.QtCore import QTranslator
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from pyleecan.GUI import DATA_DIR
from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup
from pyleecan.GUI.Dialog.DMatLib.DMatLib import DMatLib
from pyleecan.GUI.Dialog.DMatLib.WMatSelect.WMatSelect import WMatSelect

from pyleecan.GUI.Tools.SidebarWindow import SidebarWindow
from pyleecan.GUI.Tools.MachinePlotWidget import MachinePlotWidget
from pyleecan.GUI._Internal.FEAnoloadWidget import FEAnoloadWidget

EXT_GUI = True

if __name__ == "__main__":
    # Default material data path
    matlib_path = join(DATA_DIR, "Material")

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
    c = DMachineSetup(machine_path=join(DATA_DIR, "Machine"), matlib_path=matlib_path)

    if EXT_GUI:
        # Setup extended GUI with sub windows
        icon = dirname(__file__) + "/GUI/Resources/images/icon/pyleecan_64.png"
        window = SidebarWindow()
        window.setWindowIcon(QIcon(icon))

        update_step = lambda : c.set_nav(c.nav_step.currentRow())
        window.addSubWindow("Design", c, update_step)
        window.DesignWidget = c

        plt_widget = MachinePlotWidget(window)
        window.addSubWindow("Plot", plt_widget, plt_widget.update)

        mat_widget = DMatLib(window.DesignWidget.matlib, selected=0)
        window.addSubWindow("MatLib", mat_widget, mat_widget.update_mat_list)

        test = FEAnoloadWidget(c, 'Leerlauf FEA')
        window.addSubWindow("noload FEA", test)
        
        
        

        window.show()

    else:
        # "Normal" GUI
        c.show()

    exit(a.exec_())
