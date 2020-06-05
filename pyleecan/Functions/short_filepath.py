# -*- coding: utf-8 -*-
import os


def short_filepath(filepath, length=40):
    """ 
    truncate a filepath string to the specified length
    but at least returns the filename
    """
    filepath = filepath.replace("/", "\\")
    if len(filepath) < length:
        return filepath
    else:
        filename = os.path.split(filepath)[1]
        path = os.path.split(filepath)[0]
        length = length - len(filename) - 3
        path = "" if length < 0 else str(path)[-length:] + "\\"
        path = path.split("\\", 1)[-1]
        filepath = "..\\" + path + filename
    return filepath
