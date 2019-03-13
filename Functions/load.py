# -*- coding: utf-8 -*-
"""
@date Created on Fri Mar 08 14:58:51 2018
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from json import load as jload
from os.path import isfile
from re import match
from pyleecan.Functions.load_switch import load_switch


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


class LoadMissingFileError(Exception):
    """ """

    pass


class LoadWrongDictClassError(Exception):
    """ """

    pass
