# -*- coding: utf-8 -*-

from os.path import isdir, join
from os import walk, getcwd, chdir
from ..Functions.load_switch import load_switch
from ..Classes.Material import Material
from .Load.load_json import load_json
from .Load.load_hdf5 import load_hdf5


def init_data(obj, file_path):
    """ 
    Initialize pyleecan objects (by init_dict) within list and/or dict data structure.
    Non pyleecan, list or dict type data will be kept as they are.

    Parameters
    ----------
    obj: object
        list/dict containing pyleecan init_dict data

    file_path: str
        path of the obj loaded
        
    Returns
    -------
    data: 
        initialized pyleecan objects within a list or dict
    """

    # Find the folder path
    idx = max(file_path.rfind("/"), file_path.rfind("\\"))
    if idx == -1:
        folder_path = ""
    else:
        folder_path = file_path[: idx + 1]

    # --- list type ---
    if isinstance(obj, list):
        data = []
        for elem in obj:
            data.append(init_data(elem, file_path))
        return data
    # --- dict type ---
    if isinstance(obj, dict):
        # --- pyleecan class (has to be checked befor 'normal' dict) ---
        # Check if the dictionay has a "__class__" key
        if "__class__" in obj:
            # Check if data is a pyleecan class
            if obj["__class__"] in load_switch:
                if "init_str" in obj:  # Load from file
                    return load_switch[obj["__class__"]](
                        init_str=folder_path + obj["init_str"]
                    )
                elif folder_path != "":
                    wd = getcwd()
                    chdir(folder_path)
                    new_obj = load_switch[obj["__class__"]](init_dict=obj)
                    chdir(wd)
                    return new_obj
                else:
                    return load_switch[obj["__class__"]](init_dict=obj)

        # --- 'normal' dict ---
        data = dict()
        for key in obj:
            data[key] = init_data(obj[key], file_path)
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

    if file_path.endswith("hdf5") or file_path.endswith("h5"):
        file_path, init_dict = load_hdf5(file_path)
    else:
        file_path, init_dict = load_json(file_path)

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

    return init_data(init_dict, file_path)


def _load(file_path, cls_type=None):
    """Load a list of pyleecan objects from a json file

    Parameters
    ----------
    file_path: str
        path to the file to load
    """
    _, obj = load_json(file_path)

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

    return init_data(obj, file_path)


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
        raise LoadMissingFolderError(
            "The following given path doesn't lead to a directory: " + mat_path
        )

    # Get and Read all the file to create a list dictionary : variable name <=> value
    matlib = list()
    for (dirpath, _, filenames) in walk(mat_path):
        for file_name in filenames:
            # For all json file in the folder and subfolder
            if file_name.endswith(".json") or file_name.endswith(".h5"):
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
