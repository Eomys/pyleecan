# -*- coding: utf-8 -*-

from codecs import open as open_co
from imp import load_source
from os import walk, system
from os.path import abspath, join, isfile
from re import match
from subprocess import PIPE, Popen
from json import load as jload
import subprocess
from ..definitions import (
    GEN_DIR,
    GUI_DIR,
    RES_NAME,
    RES_PATH,
    PACKAGE_NAME,
    DEFAULT_FONT,
)
from ..Generator import TAB, TAB2, TAB3
from ..Functions.short_filepath import short_filepath

# SpinBox Must have min and max value, if not provided in csv use these one
MIN_SPIN = -999999
MAX_SPIN = 999999


def generate_gui_single_file(ui_name, ui_folder_path, gen_dict):
    """Generate all the needed file (Gen_, Ui_) for a single Ui file

    Parameters
    ----------
    ui_name : str
        Name of the ui file to convert
    ui_folder_path : str
        Path to the folder to scan recursively to find the ui file
    gen_dict : dict
        Dict with key = class name and value = class_dict
    """

    # Get all the ui files
    file_list = find_ui_files(ui_folder_path=ui_folder_path)
    for file_tuple in file_list:
        # Convert only a particular file
        if file_tuple[1] == ui_name:
            ui_to_py(file_tuple[0], file_tuple[1])

            # Create the "Gen_" classes from the gen_list.json file (if needed)
            gen_path = join(file_tuple[0], "gen_list.json")
            if isfile(gen_path):
                # If needed add a "Gen_" class to edit widget with csv values
                with open(gen_path, "r") as load_file:
                    gen_list = jload(load_file)
                    gen_gui_edit_file(
                        file_tuple[0], file_tuple[1][:-3], gen_dict, gen_list
                    )


def generate_gui(ui_folder_path, gen_dict, IS_SDT=False):
    """Generate all the needed file for the GUI

    Parameters
    ----------
    ui_folder_path : str
        Path to the folder to scan recursively for ui files
    gen_dict : dict
        Dict with key = class name and value = class_dict
    """

    # Get all the ui files
    file_list = find_ui_files(ui_folder_path=ui_folder_path)
    for file_tuple in file_list:
        # Convert every ui file to py
        ui_to_py(file_tuple[0], file_tuple[1])

        # Create the "Gen_" classes from the gen_list.json file (if needed)
        gen_path = join(file_tuple[0], "gen_list.json")
        if isfile(gen_path):
            # If needed add a "Gen_" class to edit widget with csv values
            with open(gen_path, "r") as load_file:
                gen_list = jload(load_file)
                gen_gui_edit_file(file_tuple[0], file_tuple[1][:-3], gen_dict, gen_list)
    # Generate the resources


def generate_GUI_resources():
    """Generate the GUI resources .py file from the .qrc file"""
    print("Generate GUI resources...")
    qrc_to_py(RES_PATH, RES_NAME)


def gen_gui_edit_file(path, class_name, gen_dict, gen_list):
    """Generate the "Gen_" class for editing the gui according to gen_list

    Parameters
    ----------
    path : str
        Path to the class folder

    class_name : str
        Name of the class to generate

    gen_dict : dict
        Dict with key = class name and value = class_dict

    gen_list : list
        List of widget to edit

    Returns
    -------

    """

    # gen_str contains the code that will be written in the generated file
    gen_str = "# -*- coding: utf-8 -*-\n"
    gen_str += '"""File generated according to ' + class_name + "/gen_list.json\n"
    gen_str += 'WARNING! All changes made in this file will be lost!\n"""\n'

    # Generate the import path
    # from "C:\\Users...\\GUI\\Dialog..." to ["C:", "Users",..., "GUI",
    # "Dialog",...]
    path = path.replace("\\", "/")
    split_path = path.split("/")  # Split the path arount the /
    # The import path start at "GUI", we remove everything before GUI in
    # split_path list
    # from ["C:", "Users",..., "GUI", "Dialog",...] to ["GUI", "Dialog"...]
    split_path.reverse()
    split_path = split_path[: split_path.index(PACKAGE_NAME) + 1]
    split_path.reverse()
    # from ["GUI", "Dialog", ...] to GUI.Dialog...
    import_path = ".".join(split_path)

    gen_str += (
        "from "
        + import_path
        + ".Ui_"
        + class_name
        + " import Ui_"
        + class_name
        + "\n\n\n"
    )
    gen_str += "class Gen_" + class_name + "(Ui_" + class_name + "):\n"

    # We use polymorphism to add some code lines to setupUi
    gen_str += TAB + "def setupUi(self, " + class_name + "):\n"
    gen_str += (
        TAB2 + '"""Abstract class to update the widget according to the csv doc\n'
    )
    gen_str += TAB2 + '"""\n'
    gen_str += TAB2 + "Ui_" + class_name + ".setupUi(self, " + class_name + ")\n"

    # We generate the corresponding lines for every needed widget
    for edit in gen_list:
        # data contains description, min, max of the variable according to Doc
        # excel files
        data = find_prop(gen_dict[edit["cls"]]["properties"], edit["name"])

        # widget can contain either a list or a string
        if isinstance(edit["widget"], list):
            # generate the code lines for every widget in the list (label and
            # corresponding input most of the time)
            for widget in edit["widget"]:
                gen_str += gen_edit_widget_code(widget, data)
        else:
            # generate the code lines for the widget
            gen_str += gen_edit_widget_code(edit["widget"], data)

    # Write the file with the generated code lines
    gen_file = open_co(join(path, "Gen_" + class_name + ".py"), "w", "utf-8")
    gen_file.write(gen_str[:-1])
    gen_file.close()


def gen_gui_class_file(path, class_name, gen_dict, gen_list):
    """Generate the Main class file according to the gen_list (should be run
    only once)

    Parameters
    ----------
    path : str
        Path to the class folder

    class_name : str
        Name of the class to generate

    gen_dict : dict
        Dict with key = class name and value = class_dict

    gen_list : list
        List of widget to edit

    Returns
    -------

    """
    gen_str = "# -*- coding: utf-8 -*-\n\n"

    # Generate the import path
    # from "C:\\Users...\\GUI\\Dialog..." to ["C:", "Users",..., "GUI",
    # "Dialog",...]
    split_path = path.split("\\")  # Split the path arount the \\
    # The import path start at "GUI", we remove everything before GUI in
    # split_path list
    # from ["C:", "Users",..., "GUI", "Dialog",...] to ["GUI", "Dialog"...]
    split_path.reverse()
    split_path = split_path[: split_path.index(PACKAGE_NAME) + 1]
    split_path.reverse()
    # from ["GUI", "Dialog", ...] to GUI.Dialog...
    import_path = ".".join(split_path)

    gen_str += "from PySide2.QtGui import QDialog\n"
    gen_str += "from PySide2.QtCore import SIGNAL, Qt\n\n"
    gen_str += (
        "from "
        + import_path
        + ".Gen_"
        + class_name
        + " import Gen_"
        + class_name
        + "\n\n"
    )
    gen_str += "class " + class_name + " (Gen_" + class_name + ", QDialog):\n"
    gen_str += TAB + "def __init__ (self,in_obj):\n"
    gen_str += TAB2 + "#Build the interface according to the .ui file\n"
    gen_str += TAB2 + "QDialog.__init__(self)\n"
    gen_str += TAB2 + "self.setupUi(self)\n\n"
    gen_str += TAB2 + "#Copy to set the modification only if validated\n"
    gen_str += TAB2 + "#self.fault = Fault(init_dict=fault.as_dict())\n\n"

    init_str = ""  # For loading the value from input
    connect_str = ""  # Connect slot and signal
    slot_str = ""  # Slot

    for edit in gen_list:
        data = find_prop(gen_dict[edit["xls"]][edit["cls"]]["properties"], edit["name"])
        if data["type"] == "int" and "type" in edit["name"]:
            init_str += (
                TAB2
                + "self.c_"
                + edit["name"]
                + ".setCurrentIndex(in_obj."
                + edit["name"]
                + ")\n"
            )
            connect_str += (
                TAB2
                + "self.connect(self.c_"
                + edit["name"]
                + ', SIGNAL("currentIndexChanged(int)"),self.set_'
                + edit["name"]
                + ")\n"
            )
            slot_str += TAB + "def set_" + edit["name"] + " (self,index):\n"
            slot_str += (
                TAB2
                + '"""Signal to update the value of '
                + edit["name"]
                + " according to the combobox\n"
            )
            slot_str += TAB2 + "@param[in] self A " + class_name + " object\n"
            slot_str += (
                TAB2
                + "@param[in] index Current index of the combobox\n"
                + TAB2
                + '"""\n'
            )
            slot_str += TAB2 + "self.obj." + edit["name"] + " = index\n\n"
        elif data["type"] == "int":
            init_str += (
                TAB2
                + "self.si_"
                + edit["name"]
                + ".setValue(in_obj."
                + edit["name"]
                + ")\n"
            )
            connect_str += (
                TAB2
                + "self.connect(self.si_"
                + edit["name"]
                + ', SIGNAL("editingFinished()"),self.set_'
                + edit["name"]
                + ")\n"
            )
            slot_str += TAB + "def set_" + edit["name"] + " (self):\n"
            slot_str += (
                TAB2
                + '"""Signal to update the value of '
                + edit["name"]
                + " according to the line edit\n"
            )
            slot_str += (
                TAB2 + "@param[in] self A " + class_name + " object\n" + TAB2 + '"""\n'
            )
            slot_str += (
                TAB2
                + "self.obj."
                + edit["name"]
                + " = self.si_"
                + edit["name"]
                + ".value()\n\n"
            )
        elif data["type"] == "float":
            init_str += (
                TAB2
                + "self.lf_"
                + edit["name"]
                + ".setValue(in_obj."
                + edit["name"]
                + ")\n"
            )
            connect_str += (
                TAB2
                + "self.connect(self.lf_"
                + edit["name"]
                + ', SIGNAL("editingFinished()"),self.set_'
                + edit["name"]
                + ")\n"
            )
            slot_str += TAB + "def set_" + edit["name"] + " (self):\n"
            slot_str += (
                TAB2
                + '"""Signal to update the value of '
                + edit["name"]
                + " according to the line edit\n"
            )
            slot_str += (
                TAB2 + "@param[in] self A " + class_name + " object\n" + TAB2 + '"""\n'
            )
            slot_str += (
                TAB2
                + "self.obj."
                + edit["name"]
                + " = self.lf_"
                + edit["name"]
                + ".value()\n\n"
            )
        elif data["type"] == "bool":
            init_str += TAB2 + "if in_obj." + edit["name"] + " :\n"
            init_str += TAB3 + "self." + edit["name"] + ".setCheckState(Qt.Checked)\n"
            init_str += TAB2 + "else :\n"
            init_str += TAB3 + "self." + edit["name"] + ".setCheckState(Qt.Unchecked)\n"
            connect_str += (
                TAB2
                + "self.connect(self."
                + edit["name"]
                + ', SIGNAL("toggled(bool)"),self.set_'
                + edit["name"]
                + ")\n"
            )
            slot_str += TAB + "def set_" + edit["name"] + " (self, is_checked):\n"
            slot_str += (
                TAB2
                + '"""Signal to update the value of '
                + edit["name"]
                + " according to the checkbox\n"
            )
            slot_str += TAB2 + "@param[in] self A " + class_name + " object\n"
            slot_str += (
                TAB2 + "@param[in] is_checked State of the checkbox\n" + TAB2 + '"""\n'
            )
            slot_str += TAB2 + "self.obj." + edit["name"] + " = is_checked\n\n"
        elif data["type"] == "str":
            init_str += (
                TAB2
                + "self.le_"
                + edit["name"]
                + ".setText(in_obj."
                + edit["name"]
                + ")\n"
            )
            connect_str += (
                TAB2
                + "self.connect(self.le_"
                + edit["name"]
                + ', SIGNAL("editingFinished()"),self.set_'
                + edit["name"]
                + ")\n"
            )
            slot_str += TAB + "def set_" + edit["name"] + " (self):\n"
            slot_str += (
                TAB2
                + '"""Signal to update the value of '
                + edit["name"]
                + " according to the line edit\n"
            )
            slot_str += (
                TAB2 + "@param[in] self A " + class_name + " object\n" + TAB2 + '"""\n'
            )
            slot_str += (
                TAB2
                + "self.obj."
                + edit["name"]
                + " = str(self.le_"
                + edit["name"]
                + ".text())\n\n"
            )

    # Concatenate all (and remove last \n)
    gen_str += init_str + "\n" + connect_str + "\n" + slot_str[:-1]
    # Write the file with the generated code lines
    gen_file = open_co(join(path, class_name + ".py"), "w", "utf-8")
    gen_file.write(gen_str)
    gen_file.close()


def gen_edit_widget_code(widget_name, data):
    """Generate the code lines to setup the widget according to data
    Parameters
    ----------
    widget_name : str
        Name of the widget to edit

    data : dict
        A dict with the main information about the corresponding variable

    Returns
    -------
    gen_str : str
        The generated code lines
    """

    gen_str = ""  # Will contain the generated code

    # All widget are named according to <type>_<name>
    widget_type = widget_name.split("_")[0]
    gen_str += TAB2 + "# Setup of " + widget_name + "\n"
    if widget_type == "si":  # SpinBox
        # Set the minimum
        if data["min"] == "":  # If no minimum use the default one
            data["min"] = MIN_SPIN
        gen_str += (
            TAB2 + "self." + widget_name + ".setMinimum(" + str(data["min"]) + ")\n"
        )

        # Set the maximum
        if data["max"] == "":  # If no maximum use the default one
            data["max"] = MAX_SPIN
        gen_str += (
            TAB2 + "self." + widget_name + ".setMaximum(" + str(data["max"]) + ")\n"
        )
    elif widget_type == "lf":  # FloatEdit
        if data["min"] != "":
            gen_str += (
                TAB2
                + "self."
                + widget_name
                + ".validator().setBottom("
                + str(data["min"])
                + ")\n"
            )
        if data["max"] != "":
            gen_str += (
                TAB2
                + "self."
                + widget_name
                + ".validator().setTop("
                + str(data["max"])
                + ")\n"
            )

    # Add the help text
    gen_str += TAB2 + 'txt = self.tr(u"""' + data["desc"] + '""")\n'
    gen_str += TAB2 + "self." + widget_name + ".setWhatsThis(txt)\n"
    gen_str += TAB2 + "self." + widget_name + ".setToolTip(txt)\n\n"

    return gen_str


def gen_whats_this(data):
    """Generate the "What's this" text for the variable discribed in data
    @param[in] data A dictionary with the caracteristics of the variable
    @param[out] WhatThis String with the "What's this" texte from data
    """

    return data["desc"]


def gen_tooltips(data):
    """Generate the Tooltips text for the variable discribed in data
    @param[in] data A dictionary with the caracteristics of the variable
    @param[out] Tooltips String with the Tooltips texte from data
    """
    return data["desc"]


def find_prop(prop_list, prop_name):
    """Find the property "prop_name" in the list "prop_list"
    @param[in] prop_list List of properties
    @param[in] prop_name Name of the property we're looking for
    @param[out] prop_dict Dictionary of the property (description, max, min...)
    """

    for prop in prop_list:
        if prop["name"] == prop_name:
            return prop

    # The property must be in the list otherwise either the doc or the
    # gen_list is wrong
    raise NotFoundError(prop_name + " was not found")


class NotFoundError(Exception):
    """Raised when a property can't be found in the property list in which it
    must be
    """

    pass


def qrc_to_py(path, file_name):
    """Convert a .qrc file in a .py file
    @param[in] path Path to the file folder
    @param[in] file_name Name of the file to convert
    """

    path_in = join(path, file_name)  # Input file
    path_out = join(path, file_name[:-4] + "_rc.py")  # Output file

    # Run the windows command "pyrcc5" for converting files
    p = Popen(
        'pyside2-rcc "' + path_in + '" -o "' + path_out + '"', stdout=PIPE, shell=True
    )
    (output, err) = p.communicate()

    # Print the name of the converted file for check
    if output != b"":
        print("Error while generating the Ressources:")
        print(output)
    else:
        print(file_name[:-4] + " resources added in " + path_out)


def ui_to_py(path, file_name):
    """Convert a .ui file in a .py file
    @param[in] path Path to the file folder
    @param[in] file_name Name of the file to convert
    """

    path_in = join(path, file_name)  # Input file
    path_out = join(path, "Ui_" + file_name[:-3] + ".py")  # Output file

    print(
        "pyside2-uic "
        + short_filepath(path_in, length=40)
        + '" -o "'
        + short_filepath(path_out, length=40)
        + '"'
    )
    # system("pyside2-uic " + path_in + '" -o "' + path_out + '"')
    subprocess.call(["pyside2-uic", path_in, "-o", path_out])
    # Remove header part of the generated file (to avoid "commit noise")
    with open(path_out, "r") as py_file:
        data = py_file.read().splitlines(True)

    # Set the good imports in the generated files
    if PACKAGE_NAME != "pyleecan":
        for idx, line in enumerate(data):
            if line.startswith("from pyleecan"):
                data[idx] = line.replace("from pyleecan", "from " + PACKAGE_NAME)
    prev_index = 0
    while "import pyleecan_rc\n" in data:
        index = data.index("import pyleecan_rc\n")
        if prev_index == 0:
            data[index] = data[index].replace(
                "import", "from " + PACKAGE_NAME + ".GUI.Resources import"
            )
        else:
            data[index] = ""
        prev_index = index

    while "import SDT_rc\n" in data:
        index = data.index("import SDT_rc\n")
        if prev_index == 0:
            data[index] = data[index].replace(
                "import", "from SciDataTool.GUI.Resources import"
            )
        else:
            data[index] = ""
        prev_index = index

    # Use correct font in QTextEdit
    for idx, line in enumerate(data):
        new_line = line.replace("MS Shell Dlg 2", DEFAULT_FONT)
        new_line = new_line.replace(
            """span style=\\" font-size""",
            """span style=\\" font-family:'""" + DEFAULT_FONT + """'; font-size""",
        )
        data[idx] = new_line

    with open(path_out, "w") as py_file:
        py_file.write(data[0])
        py_file.write("\n# File generated according to " + file_name + "\n")
        py_file.write("# WARNING! All changes made in this file will be lost!\n")
        py_file.writelines(data[7:])


#    #Run the windows command "pyuic5" for converting files
#    p = subprocess.Popen("pyuic5 "+path_in+" -o "+path_out,
#                         stdout=subprocess.PIPE, shell=True)
#
#    (output, err) = p.communicate()

# Print the name of the converted file for check
# print file_name[:-3]+" converted"


def find_ui_files(ui_folder_path):
    """Find all the .ui files in a directory

    Parameters
    ----------
    ui_folder_path : str
        Path to the folder to scan recursively for ui file

    Returns
    -------
    file_list : list
        List of tuple (folder_path, file_name.ui)
    """

    file_list = list()
    for dirpath, dirnames, filenames in walk(ui_folder_path):
        for file_name in filenames:
            # If the file name end by .ui, add it to the list
            if match(".*\.ui$", file_name):
                file_list.append((dirpath, file_name))

    return file_list


def find_py_files():
    """Find all the .py files (except __init__) in a directory
    @param[out] file_list List of tuple (path, file_name.py)
    """

    file_list = list()
    for dirpath, dirnames, filenames in walk(GUI_DIR):
        for file_name in filenames:
            # If the file name end by .ui, add it to the list
            if match(".*\.py$", file_name) and file_name != "__init__.py":
                file_list.append(join(dirpath, file_name))

    return file_list


def gen_pro_file():
    file_list = find_py_files()

    file_path = join(GUI_DIR, "all.pro")
    # Write the file with the generated lines
    with open(file_path, "w") as pro_file:
        for file_name in file_list:
            pro_file.write("SOURCES += " + file_name + "\n")
        pro_file.write("\nTRANSLATIONS += i18n\\pyleecan_cn.ts")
    print("pylupdate5 all.pro")
