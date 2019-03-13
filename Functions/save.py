# -*- coding: utf-8 -*-
"""
@date Created on Fri Mar 08 14:58:51 2018
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from json import dump
from os.path import join, basename, isdir


def save(self, save_path=""):
    """Save the object to the save_path

    Parameters
    ----------
    self : 
        A pyleecan object
    save_path: str
        path to the folder to save the object
    """

    obj_dict = self.as_dict()
    if isdir(save_path):
        file_path = join(save_path, type(self).__name__ + ".json")
    elif "." not in basename(save_path):
        file_path = save_path + ".json"
    else:
        file_path = save_path
    with open(file_path, "w") as json_file:
        dump(obj_dict, json_file, sort_keys=True, indent=4, separators=(",", ": "))
