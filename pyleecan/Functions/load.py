# -*- coding: utf-8 -*-

from json import load as jload
from os.path import isfile, isdir, join
from os import walk
from re import match
from ..Functions.load_switch import load_switch
from ..Classes.Material import Material


def load_json(file_path):
    """Load a json file

    Parameters
    ----------
    file_path: str
        path to the file to load

    Returns
    -------
    json_data: json decoded data type
        data of the json file
    """
    # The file_name must end with .json
    if not match(".*\.json", file_path):
        file_path += ".json"  # If it doesn't, we add .json at the end

    # The file (and the folder) should exist
    if not isfile(file_path):
        raise LoadMissingFileError(str(file_path) + " doesn't exist")

    # Get the data dictionary
    with open(file_path, "r") as load_file:
        json_data = jload(load_file)

    return json_data


def init_data(obj):
    """ 
    Initialize pyleecan objects (by init_dict) within list and/or dict data structure.
    Non pyleecan, list or dict type data will be kept as they are.

    Parameters
    ----------
    obj: object
        list/dict containing pyleecan init_dict data

    Returns
    -------
    data: 
        initialized pyleecan objects within a list or dict
    """
    # --- list type ---
    if isinstance(obj, list):
        data = []
        for elem in obj:
            data.append(init_data(elem))
        return data
    # --- dict type ---
    if isinstance(obj, dict):
        # --- pyleecan class (has to be checked befor 'normal' dict) ---
        # Check if the dictionay has a "__class__" key
        if "__class__" in obj:
            # Check if data is a pyleecan class
            if obj["__class__"] in load_switch:
                return load_switch[obj["__class__"]](init_dict=obj)

        # --- 'normal' dict ---
        data = dict()
        for key in obj:
            data[key] = init_data(obj[key])
        return data

    # --- other type ---
    # keep all other (json) types as they are
    else:
        return obj


def load(file_path):
    """Load a pyleecan object from a json file

    Parameters
    ----------
    file_path: str
        path to the file to load
    """
    init_dict = load_json(file_path)

    # Check that loaded data are of type dict
    if not isinstance(init_dict, dict):
        raise LoadWrongTypeError(
            'Loaded file is of type "'
            + type(init_dict).__name__
            + '", type "dict" expected.'
        )
    # Check that the dictionay has a "__class__" key
    if "__class__" not in init_dict:
        raise LoadWrongDictClassError('Key "__class__" missing in loaded file')
    # Check that data is a pyleecan class
    if init_dict["__class__"] not in load_switch:
        raise LoadWrongDictClassError(
            init_dict["__class__"] + " is not a pyleecan class"
        )

    return init_data(init_dict)


def _load(file_path, cls_type=None):
    """Load a list of pyleecan objects from a json file

    Parameters
    ----------
    file_path: str
        path to the file to load
    """
    obj = load_json(file_path)

    # check the initial object's type if set
    if cls_type is not None:
        if type(obj).__name__ != cls_type:
            raise LoadWrongTypeError(
                'Object is of type "'
                + type(obj).__name__
                + '", type "'
                + cls_type
                + '" expected.'
            )

    # check that load_switch does not contain 'dict' or 'list' for init_data to work
    if ("list" in load_switch) or ("dict" in load_switch):
        raise LoadSwitchError("'list' or 'dict' should not be in load_switch dict.")

    return init_data(obj)


def load_list(file_path):
    return _load(file_path, "list")


def load_dict(file_path):
    return _load(file_path, "dict")


def load_matlib(mat_path):
    """Load all the Material json file from a folder and subfolder

    Parameters
    ----------
    mat_path: str
        path to the file to load

    Returns
    -------
    matlib: list
        List of Material object
    """

    # Check that the dir exist
    if not isdir(mat_path):
        raise LoadMissingFolderError("The given path doesn't lead to a directory")

    # Get and Read all the file to create a list dictionary : variable name <=> value
    matlib = list()
    for (dirpath, dirnames, filenames) in walk(mat_path):
        for file_name in filenames:
            # For all json file in the folder and subfolder
            if file_name[-5:] == ".json":
                file_path = join(dirpath, file_name)
                try:
                    mat = load(file_path)
                    # Update the object property
                    mat.name = file_name[:-5]
                    mat.path = file_path
                    # Keep only the materials
                    if isinstance(mat, Material):
                        matlib.append(mat)
                except Exception:
                    print("When loading matlib, unable to load file: " + file_path)
    return matlib


class LoadMissingFileError(Exception):
    """ """

    pass


class LoadMissingFolderError(Exception):
    """ """

    pass


class LoadWrongDictClassError(Exception):
    """ """

    pass


class LoadWrongTypeError(Exception):
    """ """

    pass


class LoadSwitchError(Exception):
    """ """

    pass
