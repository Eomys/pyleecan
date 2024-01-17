from os.path import isfile
from sys import argv, exit

from PySide2.QtWidgets import QApplication

try:  # Import if pyleecan is installed with pip
    from ..GUI.Dialog.DClassGenerator.DClassGenerator import DClassGenerator
except ImportError:  # Import for dev version
    exec(
        "from pyleecan.GUI.Dialog.DClassGenerator.DClassGenerator import DClassGenerator"
    )

## UPDATE paths to prefered applications
# Path to prefered application to edit python files
PATH_EDITOR_PY = "notepad.exe"
# Path to prefered application to edit csv files
PATH_EDITOR_CSV = "notepad.exe"


def run_class_generator(argv):
    # Script to be used to test in dev
    a = QApplication(argv)

    # Machine Setup Widget
    c = DClassGenerator(path_editor_py=PATH_EDITOR_PY, path_editor_csv=PATH_EDITOR_CSV)

    c.show()

    exit(a.exec_())


if __name__ == "__main__":
    run_class_generator(argv)
