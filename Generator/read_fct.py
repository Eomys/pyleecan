# -*- coding: utf-8 -*-
"""Created on Mon Nov 17 11:18:59 2014
@author: pierre_b
"""
from os import walk
from os.path import isfile, join

from csv import reader

from pyleecan.Generator import PYTHON_TYPE

# Constante for csv reading
NAME_COL = 0  # Number of the Name column
EN_DESC_COL = 2  # Number of the English description column
TYPE_COL = 5  # Number of the Type column
DEF_VAL_COL = 6  # Number of the default value column
MIN_VAL_COL = 7  # Number of the minimum value column
MAX_VAL_COL = 8  # Number of the maximum value column

PACK_COL = 12  # Number of the Package column
HER_COL = 13  # Number of the mother class name column
METH_COL = 14  # Number of the Methods list column
CST_NAME_COL = 15  # Number of the Methods list column
CST_VAL_COL = 16  # Number of the Methods list column
CLASS_DEF_COL = 17  # Number of the Methods list column
DAUG_COL = 18  # Number of the daughter class list column


def read_all(path):
    """Read every csv files in a directory and subdirectory and create a structure for the
    code generation

    Parameters
    ----------
    path : str
        path to the root folder with the csv files

    Returns
    -------
    gen_dict : dict
        Dict with key = class name and value = class dict (name, package, properties, methods...)
    """
    gen_dict = dict()

    for (dirpath, dirnames, filenames) in walk(path):
        for file_name in filenames:
            if file_name[-4:] == ".csv" and file_name[:2] != "~$":
                # For all .csv file in the folder and subfolder ...
                gen_dict[file_name[:-4]] = read_file(join(dirpath, file_name))

    return gen_dict


def read_file(path):
    """Read a csv file and create a dict for the class code generation

    Parameters
    ----------
    path : str
        path to the class csv file to read


    Returns
    -------
    class_dict : dict
        Dict containing all the class informations (properties, package, methods...)
    """
    class_dict = dict()

    # Open the module doc
    if not isfile(path):
        raise NotAFile("File not found")

    # The class name is the csv file name
    class_dict["name"] = path.split("\\")[-1][:-4]

    with open(path, mode="r") as csv_file:
        class_csv = reader(csv_file, delimiter=";")
        class_csv = list(class_csv)
        # Get all the properties of the class
        properties = list()
        Nline = len(class_csv)
        for rx in range(1, Nline):  # Skip the first line (title of column)
            name = class_csv[rx][NAME_COL]
            if name != "":
                prop_dict = dict()
                prop_dict["name"] = name
                prop_dict["type"] = class_csv[rx][TYPE_COL]
                prop_dict["min"] = class_csv[rx][MIN_VAL_COL].replace(",", ".")
                prop_dict["max"] = class_csv[rx][MAX_VAL_COL].replace(",", ".")
                prop_dict["value"] = class_csv[rx][DEF_VAL_COL]
                if prop_dict["type"] == "float":
                    prop_dict["value"] = prop_dict["value"].replace(",", ".")
                if prop_dict["value"] != "" and prop_dict["type"] != "str":
                    prop_dict["value"] = eval(prop_dict["value"])
                desc = class_csv[rx][EN_DESC_COL]
                prop_dict["desc"] = desc.replace("\\\\", "\\")
                properties.append(prop_dict)
        class_dict["properties"] = properties

        # Get all the constants
        cste = list()
        for rx in range(1, Nline):  # Skip the first line (title of column)
            name = class_csv[rx][CST_NAME_COL]
            if name != "":
                cste_dict = dict()
                cste_dict["name"] = name
                cste_dict["value"] = class_csv[rx][CST_VAL_COL]
                cste.append(cste_dict)
        class_dict["constants"] = cste

        # Get all the methods
        class_dict["methods"] = list()
        for rx in range(1, Nline):  # Skip the first line (title of column)
            meth = class_csv[rx][METH_COL]
            if meth != "":
                class_dict["methods"].append(meth)

        # Get all the daughters
        class_dict["daughters"] = list()
        for rx in range(1, Nline):  # Skip the first line (title of column)
            daughter = class_csv[rx][DAUG_COL]
            if daughter != "":
                class_dict["daughters"].append(daughter)

    class_dict["package"] = class_csv[1][PACK_COL]
    class_dict["desc"] = class_csv[1][CLASS_DEF_COL]
    class_dict["mother"] = class_csv[1][HER_COL]

    return class_dict


def get_value_str(value, type_val):
    """Convert the value from the csv file to the correct str according to the type

    Parameters
    ----------
    value : str
        value to convert

    type_val : str
        Type to convert to

    Returns
    -------
    value : str
        Value updated to match the type
    """

    if value in ["None", None]:
        return "None"
    elif type_val == "str":
        # For str add " "
        return '"' + str(value) + '"'
    elif type_val == "int":
        # For int convert to avoid ".0"
        return str(int(value))
    elif type_val == "dict":
        return "{}"
    elif type_val == "bool":
        # change 1 or 0 to True and False
        return str(bool(int(value)))
    else:
        return str(value)


def find_import_type(gen_dict, class_dict, pyleecan_type=[]):
    """Find all the Pyleecan type used by the class of class_dict

    Parameters
    ----------
    gen_dict : dict
        Dict with key = class name and value = class_dict

    class_dict : dict
        Dict of the class to find the import

    pyleecan_type : list
        Existing type to import (Default value = [])

    Returns
    -------
    type_list : list
        List of pyleecan type (as str) to import
    """

    # Get all properties including mother ones
    prop_list = list(class_dict["properties"])
    while class_dict["mother"] != "":
        class_dict = gen_dict[class_dict["mother"]]
        prop_list.extend(class_dict["properties"])

    # Find every property type of the class
    for prop in prop_list:
        # Detect list of pyleecan type
        if is_list_pyleecan_type(prop["type"]):
            prop_type = prop["type"][1:-1]
        else:
            prop_type = prop["type"]
        # Store the non python type once and avoid empty line
        if prop_type not in PYTHON_TYPE and prop_type not in pyleecan_type:
            pyleecan_type.append(prop_type)
    return pyleecan_type


def is_list_pyleecan_type(type_name):
    """Check if the type is a list of Pyleecan type ([name])

    Parameters
    ----------
    type_name : str
        Type of the property

    Returns
    -------
    is_list : bool
        True if the type is a list of pyleecan type
    """
    return type_name[0] == "[" and type_name[-1] == "]"


class NotAFile(Exception):
    """Raised when the code generator is call on a wrong path
    """

    pass
