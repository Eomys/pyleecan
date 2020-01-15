# -*- coding: utf-8 -*-
"""
@date Created on Fri Mar 08 14:58:51 2018
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from json import dump
from os.path import join, basename, isdir


def fix_file_name(save_path, obj):
    if isdir(save_path) or not save_path:
        file_path = join(save_path, type(obj).__name__ + ".json")
    elif "." not in basename(save_path):
        file_path = save_path + ".json"
    else:
        file_path = save_path
    return file_path


def is_json_serializable(obj):
    if isinstance(obj, (bool, float, int, str)):
        return True
    else:
        return False


def has_as_dict(obj):
    """Check if object has 'as_dict' method.
    """
    return hasattr(obj, "as_dict") and callable(getattr(obj, "as_dict", None))


def build_data(obj):
    """
    Build a json serializable data structure of lists, dicts and pyleecan objects.
    Data that can not be serialized will be set to None. Tuples will also be None.

    Parameters
    ----------
    obj : 
        An object to serialize
    
    Returns
    -------
    data :
        A serializable data structure
    """
    # lists
    if isinstance(obj, list):
        data = []
        for elem in obj:
            data.append(build_data(elem))
        return data
    # dicts
    if isinstance(obj, dict):
        data = {}
        for key in obj:
            data[key] = build_data(obj[key])
        return data
    # tuples (excluded)
    if isinstance(obj, tuple):
        return None
    # pyleecan classes, i.e. instances with as_dict method
    if has_as_dict(obj):
        return obj.as_dict()
    #
    if is_json_serializable(obj):
        return obj
    else:
        return None


def save_data(obj, save_path=""):
    """Save the object to the save_path

    Parameters
    ----------
    self : 
        A pyleecan object
    save_path: str
        path to the folder to save the object
    """
    # correct file name if needed
    file_path = fix_file_name(save_path, obj)

    # save
    obj = build_data(obj)
    with open(file_path, "w") as json_file:
        dump(obj, json_file, sort_keys=True, indent=4, separators=(",", ": "))


def save(self, save_path=""):
    """Save the object to the save_path

    Parameters
    ----------
    self : 
        A pyleecan object
    save_path: str
        path to the folder to save the object
    """
    save_data(self, save_path=save_path)
