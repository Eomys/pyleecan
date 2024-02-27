# -*- coding: utf-8 -*-

from os import chdir, getcwd, walk
from os.path import isdir, join, splitext

from .Load.import_class import import_class
from .Load.load_hdf5 import load_hdf5
from .Load.load_json import load_json
from .Load.load_pkl import load_pkl
from .Load.retrocompatibility import convert_init_dict

# Matlib Keys
LIB_KEY = "RefMatLib"
MACH_KEY = "MachineMatLib"
PATH_KEY = "MATLIB_PATH"


def load(file_path):
    """Load a pyleecan object from a json file

    Parameters
    ----------
    file_path: str
        path to the file to load
    """
    if file_path.endswith(".pkl"):
        return load_pkl(file_path)
    file_path, init_dict = load_init_dict(file_path)

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

    # Retrocompatibility
    convert_init_dict(init_dict)

    return init_data(init_dict, file_path)


def load_init_dict(file_path):
    """load the init_dict from a h5 or json file"""
    if file_path.endswith("hdf5") or file_path.endswith("h5"):
        return load_hdf5(file_path)
    elif file_path.endswith((".json", ".json.gz")) or isdir(file_path):
        return load_json(file_path)
    else:
        raise Exception(
            "Load error: Only hdf5, h5, mot and json format supported: " + file_path
        )


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
            class_obj = import_class("pyleecan.Classes", obj.get("__class__"), "")
            if folder_path != "":
                wd = getcwd()
                chdir(folder_path)
                new_obj = class_obj(init_dict=obj)
                chdir(wd)
                return new_obj
            else:
                return class_obj(init_dict=obj)

        # --- 'normal' dict ---
        data = dict()
        for key in obj:
            data[key] = init_data(obj[key], file_path)
        return data

    # --- other type ---
    # keep all other (json) types as they are
    else:
        return obj


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

    return init_data(obj, file_path)


def load_list(file_path):
    return _load(file_path, "list")


def load_dict(file_path):
    return _load(file_path, "dict")


def load_matlib_folder(matlib_path):
    """Load all the Material json file from a folder and subfolder

    Parameters
    ----------
    matlib_path: str
        path to the file to load

    Returns
    -------
    material_list: list
        List of Material object from the Library
    """

    # Check that the dir exist
    if not isdir(matlib_path):
        raise LoadMissingFolderError(
            "The following given path doesn't lead to a directory: " + matlib_path
        )

    # Get and Read all the file to create a list dictionary : variable name <=> value
    material_list = list()
    Material = import_class("pyleecan.Classes", "Material")
    for dirpath, _, filenames in walk(matlib_path):
        for file_name in filenames:
            # For all json file in the folder and subfolder
            if file_name.endswith(".json") or file_name.endswith(".h5"):
                file_path = join(dirpath, file_name).replace("\\", "/")
                try:
                    mat = load(file_path)
                    # Update the object property
                    mat.name = splitext(file_name)[0]
                    mat.path = file_path
                    # Keep only the materials
                    if isinstance(mat, Material):
                        material_list.append(mat)
                except Exception:
                    print("When loading matlib, unable to load file: " + file_path)
    return material_list


def load_machine_materials(material_dict, machine):
    """Add the material from a machine that are different from the library one

    Parameters
    ----------
    material_dict: dict
        Materials dictionary (library + machine)
    machine : Machine
        Machine object to use the materials from
    """
    # Remove previous machine materials
    material_dict[MACH_KEY] = list()
    # Get machine materials (assume unique by name)
    mach_mat_dict = machine.get_material_dict()
    mach_mat_list = list(mach_mat_dict.values())

    # Compare material with matlib (ignores name and path)
    mat_lib_name = [mat.name for mat in material_dict[LIB_KEY]]
    name_list = list()  # Machine materials name
    for mach_mat in mach_mat_list:
        if mach_mat.name in mat_lib_name:
            # Machine material have a matching name in Library
            lib_mat = material_dict[LIB_KEY][mat_lib_name.index(mach_mat.name)]
            if mach_mat.compare(lib_mat, ignore_list=["self.name", "self.path"]):
                # Machine material is different from library one : rename + add to list
                mach_mat.name = mach_mat.name + "_old"
                if mach_mat.name not in name_list:
                    material_dict[MACH_KEY].append(mach_mat)
                    name_list.append(mach_mat.name)
        elif mach_mat.name not in name_list:  # Machine material not in Library
            material_dict[MACH_KEY].append(mach_mat)
            name_list.append(mach_mat.name)


def load_matlib(matlib_path=None, machine=None):
    """Load the Material library and the machine materials

    Parameters
    ----------
    matlib_path: str
        path to the Matlib folder to load
    machine : Machine
        Machine object to use the materials from

    Returns
    -------
    material_dict: dict
        Materials dictionary (library + machine)
    """
    material_dict = {LIB_KEY: list(), MACH_KEY: list(), PATH_KEY: matlib_path}
    if matlib_path is not None:
        material_dict[LIB_KEY] = load_matlib_folder(matlib_path)
    if machine is not None:
        load_machine_materials(material_dict, machine)
    return material_dict


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
