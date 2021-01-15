from definitions import ROOT_DIR, DATA_DIR, MATLIB_DIR

import sys
from os.path import dirname, abspath, normpath, join

ROOT_DIR = normpath(abspath(join(dirname(__file__), "..")))

sys.path.insert(0, ROOT_DIR)

from pyleecan.Classes.Machine import Machine
from pyleecan.Functions.load import load
import tkinter as tk
from tkinter import filedialog


def load_dialog(filetypes=(("JSON Dateien", "*.json"),)):
    """load a machine from a .json file

    Parameters
    ----------

    """
    # Ask the user to select a .json file to load
    root = tk.Tk()
    root.withdraw()
    load_path = filedialog.askopenfilename(filetypes=filetypes)

    if load_path != "":
        try:
            # Load and check type of instance
            obj = load(load_path)
            return obj
        except Exception as e:
            print(e)
            return None


if __name__ == "__main__":
    obj = load_dialog()
