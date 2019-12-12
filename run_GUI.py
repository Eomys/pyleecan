from os.path import abspath, dirname, join, realpath, split
from sys import argv, exit, path

path.append(split(dirname(realpath(__file__)))[0])

from PyQt5.QtCore import QTranslator
from PyQt5.QtWidgets import QApplication
from pyleecan.GUI import DATA_DIR
from pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup import DMachineSetup

if __name__ == "__main__":

    # Script to be used to test in dev
    a = QApplication(argv)

    # Set CSS
    # a.setStyleSheet("QLineEdit { background-color: yellow }")

    # Setup the translation
    translationFile = "pyleecan_fr.qm"
    translator = QTranslator()
    translator.load(translationFile, "GUI//i18n")
    a.installTranslator(translator)

    c = DMachineSetup(
        machine_path=join(DATA_DIR, "Machine"), matlib_path=join(DATA_DIR, "Material")
    )
    c.show()

    exit(a.exec_())
