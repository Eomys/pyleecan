# -*- coding: utf-8 -*-
"""
@date Created on Fri Mar 08 14:58:51 2018
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from json import load as jload
from os.path import isfile, isdir, join
from os import walk
from re import match
from pyleecan.Functions.load_switch import load_switch
from pyleecan.Classes.Material import Material


def load(file_path):
    """Load a pyleecan object from a json file

    Parameters
    ----------
    file_path: str
        path to the file to load
    """
    # The file_name must end with .json
    if not match(".*\.json", file_path):
        file_path += ".json"  # If it doesn't, we add .json at the end

    # The file (and the folder) should exist
    if not isfile(file_path):
        raise LoadMissingFileError(str(file_path) + " doesn't exist")

    # Get the data dictionnary
    with open(file_path, "r") as load_file:
        init_dict = jload(load_file)

    # Check that the dictionnay have a "__class__" key
    if "__class__" not in init_dict:
        raise LoadWrongDictClassError('Key "__class__" missing in loaded file')
    if init_dict["__class__"] not in load_switch:
        raise LoadWrongDictClassError(
            init_dict["__class__"] + " is not a pyleecan class"
        )

    return load_switch[init_dict["__class__"]](init_dict=init_dict)


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
