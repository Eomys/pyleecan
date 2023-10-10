import numpy as np
import pandas as pd

from os.path import realpath

MATCH_PROP_DICT = {
    "Variable name": "name",
    "Unit": "unit",
    "Description (EN)": "desc",
    "Size": "size",
    "Type": "type",
    "Default value": "value",
    "Minimum value": "min",
    "Maximum value": "max",
    "as_dict Type": "as_dict",
}

MATCH_META_DICT = {
    "Package": "package",
    "Inherit": "mother",
    "Class description": "desc",
    "Children": "daughters",
}

MATCH_CONST_DICT = {
    "Constant Name": ["constants", "name"],
    "Constant Value": ["constants", "value"],
}


def write_file(class_dict):
    """Write a csv file from a class dict

    Parameters
    ----------
    class_dict : dict
        Dict containing all the class informations (properties, package, methods...)

    """

    list_meta = list(MATCH_META_DICT.keys())
    list_prop = list(MATCH_PROP_DICT.keys())
    list_const = list(MATCH_CONST_DICT.keys())

    # Get csv path
    csv_path = realpath(class_dict["path"])

    # Copy and sort all class properties and values
    prop_list = list()
    for prop_dict in class_dict["properties"]:
        prop_dict_new = dict()
        for prop_name in list_prop:
            prop_dict_new[prop_name] = prop_dict[MATCH_PROP_DICT[prop_name]]
        prop_list.append(prop_dict_new)

    # Get the list of methods
    meth_list = class_dict["methods"]

    # Copy the list of meta data
    meta_dict = dict()
    for meta_name in list_meta:
        meta_prop = class_dict[MATCH_META_DICT[meta_name]]
        meta_dict[meta_name] = meta_prop

    # Copy the list of constants
    const_list = class_dict["constants"]
    cst_name_list = list()
    cst_val_list = list()
    for const_dict in const_list:
        for name, val in const_dict.items():
            if name == MATCH_CONST_DICT["Constant Name"][1]:
                cst_name_list.append(val)
            else:
                cst_val_list.append(val)

    # Number of properties
    Nprop = len(prop_list)
    # Number of methods
    Nmeth = len(meth_list)
    # Number of constants
    Nconst = len(cst_name_list)

    # Total number of rows in csv file
    Nrow = 1 + Nprop + 2 + max([1, Nmeth, Nconst])
    # Total number of columns in csv file
    Ncol = len(list_prop)

    # Init array containing all class information
    class_array = np.zeros(shape=(Nrow, Ncol), dtype=object)

    # Init empty row containing empty strings
    empty_row = np.array(["" for jj in range(Ncol)])

    # Fill first line with all property names
    class_array[0, :] = np.array(list_prop)

    # Fill next lines with all properties values
    if Nprop > 0:
        class_array[1 : Nprop + 1, :] = np.array(
            [list(val.values()) for val in prop_list]
        )

    # Empty row between properties and methods/metadata
    class_array[Nprop + 1, :] = empty_row

    # Fill line with methods, metadata names and constants
    # Package Inherit Methods Constant Name	Constant Value Class description
    list_meta_meth_const = [*list_meta[:2], "Methods", *list_const, list_meta[2]]
    for ii in range(len(list_meta_meth_const), Ncol, 1):
        list_meta_meth_const.append("")
    class_array[Nprop + 2 : Nprop + 3, :] = np.array(list_meta_meth_const)

    # Init last lines as empty rows
    for row in range(Nprop + 3, Nrow, 1):
        class_array[row, :] = empty_row

    # Fill values of metadata except for children
    for meta_name in list_meta[:-1]:
        col = list_meta_meth_const.index(meta_name)
        class_array[Nprop + 3, col] = meta_dict[meta_name]

    # Fill column of methods (3rd column)
    if Nmeth > 0:
        class_array[Nprop + 3 : Nprop + 3 + Nmeth, 2] = np.array(meth_list)

    # Fill column of constants names (4th column)
    class_array[Nprop + 3 : Nprop + 3 + Nconst, 3] = np.array(cst_name_list)

    # Fill column of constants values (5th column)
    class_array[Nprop + 3 : Nprop + 3 + Nconst :, 4] = np.array(cst_val_list)

    # Replace None with "None"
    class_array[class_array == None] = "None"

    # Save as .csv using Panda framework
    df = pd.DataFrame(class_array)
    print("Saving class " + class_dict["name"] + " to : " + csv_path)
    df.to_csv(csv_path, header=False, index=False)
