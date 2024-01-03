# -*- coding: utf-8 -*-
from os import walk
from os.path import isfile, join, basename, isdir

from csv import reader

from ..Generator import PYTHON_TYPE
from ..definitions import PACKAGE_NAME

# Constants for csv reading, i.e. column number of data
NAME_COL = 0  # attribue name
UNIT_COL = 1  # value unit
EN_DESC_COL = 2  # english description
SIZE_COL = 3  # size
TYPE_COL = 4  # type
DEF_VAL_COL = 5  # default value
MIN_VAL_COL = 6  # minimum value
MAX_VAL_COL = 7  # maximum value
AS_DICT_COL = 8  # To change as_dict/copy behavior

# Index in side by side
PACK_COL = 9  # package
HER_COL = 10  # mother class name
METH_COL = 11  # methods list
CST_NAME_COL = 12  # constants name list
CST_VAL_COL = 13  # constants value list
CLASS_DEF_COL = 14  # class description

# Offset for column csv (to convert side by side index to column)
COLUMN_OFFSET = PACK_COL


def read_all(
    path,
    is_internal=False,
    in_path="",
    soft_name=PACKAGE_NAME,
    is_update_mother_of_mother=True,
):
    """Read every csv files in a directory and subdirectory and create a structure for the
    code generation

    Parameters
    ----------
    path : str
        path to the root folder with the csv files
    is_internal : bool
        True to overwrite the open source csv files by internal ones
    soft_name : str
        Name of the generated software
    is_update_mother_of_mother: bool
        True to update mother of mother in update_all_daughters

    Returns
    -------
    gen_dict : dict
        Dict with key = class name and value = class dict (name, package, properties, methods...)
    """
    gen_dict = dict()

    if not isdir(path):
        raise Exception(
            "Error while scanning csv files, " + path + " is not a folder !"
        )
    # Read the open source doc
    for dirpath, _, filenames in walk(path):
        for file_name in filenames:
            if file_name[-4:] == ".csv" and file_name[:2] != "~$":
                # For all .csv file in the folder and subfolder ...
                gen_dict[file_name[:-4]] = read_file(
                    join(dirpath, file_name), soft_name=soft_name
                )
                gen_dict[file_name[:-4]]["is_internal"] = False

    # Read the Internal doc to adapt the classes (if needed)
    if is_internal:
        for dirpath, _, filenames in walk(in_path):
            for file_name in filenames:
                if file_name[-4:] == ".csv" and file_name[:2] != "~$":
                    # For all .csv file in the folder and subfolder ...
                    print("Using internal version for: " + file_name[:-4])
                    gen_dict[file_name[:-4]] = read_file(
                        join(dirpath, file_name), soft_name=soft_name
                    )
                    gen_dict[file_name[:-4]]["is_internal"] = True

    # Update all the "daughters" key according to "mother" key
    update_all_daughters(gen_dict, is_update_mother_of_mother=is_update_mother_of_mother)

    return gen_dict


def read_file(file_path, soft_name=PACKAGE_NAME):
    """Read a csv file and create a dict for the class code generation

    Parameters
    ----------
    file_path : str
        path to the class csv file to read

    Returns
    -------
    class_dict : dict
        Dict containing all the class informations (properties, package, methods...)
    """
    class_dict = dict()
    # Open the module doc
    if not isfile(file_path):
        raise NotAFile("File not found")

    # The class name is the csv file name
    class_dict["name"] = basename(file_path)[:-4]
    try:  # Cleanup path to avoid "commit noise"
        class_dict["path"] = file_path[file_path.rfind(soft_name) :]
    except ValueError:  # Path doesn't contain pyleecan
        class_dict["path"] = file_path
    # Cleanup \ to avoid errors
    class_dict["path"] = class_dict["path"].replace("\\", "/")
    with open(file_path, mode="r") as csv_file:
        class_csv = reader(csv_file, delimiter=",")
        class_csv = list(class_csv)
        # Check format of the csv (two tables side by side or in column)
        is_side_by_side = True
        header_index = None
        Nline = len(class_csv)
        for rx in range(1, Nline):  # Skip the first line (title of column)
            if class_csv[rx][0] == "Package" and class_csv[rx][1] == "Inherit":
                is_side_by_side = False
                header_index = rx
                break
        if is_side_by_side:
            get_dict_from_side_by_side(class_csv, class_dict)
        else:
            get_dict_from_columns(class_csv, class_dict, header_index)
    return class_dict


def get_dict_from_side_by_side(class_csv, class_dict):
    # Get all the properties of the class
    properties = list()
    Nline = len(class_csv)
    for rx in range(1, Nline):  # Skip the first line (title of column)
        name = class_csv[rx][NAME_COL]
        if name != "":
            prop_dict = dict()
            prop_dict["name"] = name
            prop_dict["unit"] = class_csv[rx][UNIT_COL]
            prop_dict["type"] = class_csv[rx][TYPE_COL]
            prop_dict["min"] = class_csv[rx][MIN_VAL_COL].replace(",", ".")
            prop_dict["max"] = class_csv[rx][MAX_VAL_COL].replace(",", ".")
            prop_dict["value"] = class_csv[rx][DEF_VAL_COL]
            prop_dict["as_dict"] = class_csv[rx][AS_DICT_COL]
            if prop_dict["type"] == "float":
                prop_dict["value"] = prop_dict["value"].replace(",", ".")
            if (
                prop_dict["value"] != ""
                and prop_dict["type"] != "str"
                and "." not in prop_dict["type"]
                and "()" not in prop_dict["value"]
            ):
                prop_dict["value"] = eval(prop_dict["value"])
            desc = class_csv[rx][EN_DESC_COL]
            prop_dict["desc"] = desc.replace("\\\\", "\\")
            properties.append(prop_dict)
    class_dict["properties"] = properties

    # Get all the constants
    cste = list()
    for rx in range(1, Nline):
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

    # The daughters are automatically detected in read_all
    class_dict["daughters"] = list()

    class_dict["package"] = class_csv[1][PACK_COL]
    class_dict["desc"] = class_csv[1][CLASS_DEF_COL]
    class_dict["mother"] = class_csv[1][HER_COL]
    if class_dict["mother"] == class_dict["name"]:
        raise InheritError(
            "ERROR: the class " + class_dict["name"] + " inherit from itself"
        )


def get_dict_from_columns(class_csv, class_dict, header_index):
    # Get all the properties of the class
    properties = list()
    Nline = len(class_csv)
    # Skip the first line (title of column), stop before second tables
    for rx in range(1, header_index - 1):
        name = class_csv[rx][NAME_COL]
        if name != "":
            prop_dict = dict()
            prop_dict["name"] = name
            prop_dict["unit"] = class_csv[rx][UNIT_COL]
            prop_dict["size"] = class_csv[rx][SIZE_COL]
            prop_dict["type"] = class_csv[rx][TYPE_COL]
            prop_dict["min"] = class_csv[rx][MIN_VAL_COL].replace(",", ".")
            prop_dict["max"] = class_csv[rx][MAX_VAL_COL].replace(",", ".")
            prop_dict["value"] = class_csv[rx][DEF_VAL_COL]
            if len(class_csv[rx]) == AS_DICT_COL + 1:  # Not mandatory columns
                prop_dict["as_dict"] = class_csv[rx][AS_DICT_COL]
            else:
                prop_dict["as_dict"] = ""

            if prop_dict["type"] == "float":
                prop_dict["value"] = prop_dict["value"].replace(",", ".")
            if (
                prop_dict["value"] != ""
                and prop_dict["type"] != "str"
                and "." not in prop_dict["type"]
                and "()" not in prop_dict["value"]
            ):
                prop_dict["value"] = eval(prop_dict["value"])
            desc = class_csv[rx][EN_DESC_COL]
            prop_dict["desc"] = desc.replace("\\\\", "\\")
            properties.append(prop_dict)
    class_dict["properties"] = properties

    # Get all the constants
    cste = list()
    for rx in range(header_index + 1, Nline):  # Read only second table
        name = class_csv[rx][CST_NAME_COL - COLUMN_OFFSET]
        if name != "":
            cste_dict = dict()
            cste_dict["name"] = name
            cste_dict["value"] = class_csv[rx][CST_VAL_COL - COLUMN_OFFSET]
            cste.append(cste_dict)
    class_dict["constants"] = cste

    # Get all the methods
    class_dict["methods"] = list()
    for rx in range(header_index + 1, Nline):  # Read only second table
        meth = class_csv[rx][METH_COL - COLUMN_OFFSET]
        if meth != "":
            class_dict["methods"].append(meth)

    # The daughters are automatically detected in read_all
    class_dict["daughters"] = list()

    class_dict["package"] = class_csv[header_index + 1][PACK_COL - COLUMN_OFFSET]
    class_dict["desc"] = class_csv[header_index + 1][CLASS_DEF_COL - COLUMN_OFFSET]
    class_dict["mother"] = class_csv[header_index + 1][HER_COL - COLUMN_OFFSET]
    if class_dict["mother"] == class_dict["name"]:
        raise InheritError(
            "ERROR: the class " + class_dict["name"] + " inherit from itself"
        )


def update_all_daughters(gen_dict, is_update_mother_of_mother=True):
    """This function update all the "daughters" key according to the "mother" key

    Parameters
    ----------
    gen_dict : dict
        gen_dict with no daughter set
    is_update_mother_of_mother: bool
        True to update mother of mother in update_all_daughters
    """

    # list of classes that have a mother
    daughter_dict = {
        class_name: class_dict
        for class_name, class_dict in gen_dict.items()
        if class_dict["mother"] not in ["", None] and "." not in class_dict["mother"]
    }

    # Update the daughter (sorted to avoid "commit noise")
    for name, daughter in iter(sorted(list(daughter_dict.items()))):
        # Update the mother
        mother = gen_dict[daughter["mother"]]
        if name not in mother["daughters"]:
            mother["daughters"].append(name)
        # Update all the mother of the mother
        if is_update_mother_of_mother:
            while mother["mother"] not in ["", None]:
                mother = gen_dict[mother["mother"]]
                if name not in mother["daughters"]:
                    mother["daughters"].append(name)


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
        return "-1"
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
    while class_dict["mother"] != "" and "." not in class_dict["mother"]:
        class_dict = gen_dict[class_dict["mother"]]
        prop_list.extend(class_dict["properties"])

    # Find every property type of the class
    for prop in prop_list:
        # Detect list of pyleecan type
        if is_list_pyleecan_type(prop["type"]) or is_dict_pyleecan_type(prop["type"]):
            prop_type = prop["type"][1:-1]
        else:
            prop_type = prop["type"]
        # Store the non python type once and avoid empty line
        if prop_type not in PYTHON_TYPE and prop_type not in pyleecan_type:
            pyleecan_type.append(prop_type)
        # Default value as pyleecan type
        if (
            type(prop["value"]) is str
            and "()" in prop["value"]
            and prop["value"][:-2] not in pyleecan_type
        ):
            pyleecan_type.append(prop["value"][:-2])
    return pyleecan_type


def is_dict_list_pyleecan_type(type_name):
    """Check if the type is a dict of list of Pyleecan type ({[name]})

    Parameters
    ----------
    type_name : str
        Type of the property

    Returns
    -------
    is_dict_list : bool
        True if the type is a dict of list of pyleecan type
    """
    return (
        type_name not in ["", None]
        and type_name[0] == "{"
        and type_name[-1] == "}"
        and type_name[1] == "["
        and type_name[-2] == "]"
        and ("." not in type_name or "SciDataTool" in type_name)
    )


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
    return (
        type_name not in ["", None]
        and len(type_name) > 2  # No "[]" = List of Unknow type
        and type_name[0] == "["
        and type_name[-1] == "]"
        and type_name != "[ndarray]"
        and ("." not in type_name or "SciDataTool" in type_name)
    )


def is_dict_pyleecan_type(type_name):
    """Check if the type is a dict of Pyleecan type ({name})

    Parameters
    ----------
    type_name : str
        Type of the property

    Returns
    -------
    is_list : bool
        True if the type is a dict of pyleecan type
    """

    return (
        type_name not in ["", None]
        and type_name[0] == "{"
        and type_name[-1] == "}"
        and type_name != "{ndarray}"
        and ("." not in type_name or "SciDataTool" in type_name)
    )


def is_list_unknow_type(type_name):
    """Check if the type is a list of unknow type (Frozen or ndarray or python) "[]"

    Parameters
    ----------
    type_name : str
        Type of the property

    Returns
    -------
    is_list : bool
        True if the type is a list of unknow type
    """
    return type_name == "[]"


class NotAFile(Exception):
    """Raised when the code generator is call on a wrong path"""

    pass


class InheritError(Exception):
    """Raised when a class has a wrong mother defined"""

    pass
