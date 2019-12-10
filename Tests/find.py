# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 10:04:21 2014

@author: pierre_b
"""

from numpy.random import random_sample, ranf

PYTHON_TYPE = ["float", "int", "str", "bool", "complex"]


def find_test_value(prop_dict, return_type):
    """Find a appropriate value to test the property of the return_type

    Parameters
    ----------
    prop_dict : dict
        Dictionary containing the property informations

    return_type : str
        type of the value for the test (can be different of the property one)

    Returns
    -------
    value: ?
        A "return_type" value for the test


    """
    assert return_type in PYTHON_TYPE or return_type == "ndarray"

    if return_type == "str":
        return "test with a string"

    if return_type == "bool":
        return True
    if return_type == "dict":
        return {"test": "Test for a dict", "test2": 5.2}

    if return_type == "int":
        if prop_dict["type"] in ["float", "int"]:
            return find_num_value(prop_dict, True)
        else:
            return 42
    if return_type == "complex":
        return random_sample() + 1j * random_sample()
    if return_type == "float":
        if prop_dict["type"] in ["float", "int"]:
            return find_num_value(prop_dict, False)
        else:
            return 2.0
    if return_type == "ndarray":
        return find_test_ndarray(prop_dict)


def find_test_ndarray(prop_dict):
    """Find a correct value to test ndarray

    Parameters
    ----------
    prop_dict : dict
        dictionary containing the information of the property to test


    Returns
    -------
    value: numpy.ndarray
        A value to test the property

    """
    assert prop_dict["type"] == "ndarray"

    var_min = prop_dict["min"]
    var_max = prop_dict["max"]

    # Adapt the value to the min/max
    if var_min == "" and var_max == "":  # No min and No max
        var_min = 0
        var_max = 100
    elif var_min == "" and var_max != "":  # No min but a max
        var_max = float(var_max)
        var_min = var_max - 100
    elif var_min != "" and var_max == "":  # No max but a min
        var_min = float(var_min)
        var_max = var_min + 100
    else:  # A min and a max
        var_min = float(var_min)
        var_max = float(var_max)

    # Random 4x4 float Matrix in [var_min, var_max]
    return ranf((4, 4)) * (var_max - var_min) + var_min


def find_num_value(prop_dict, is_int_return):
    """Find a value to test Double or Integer matching min/max

    Parameters
    ----------
    prop_dict : dict
        dictionary containing the information on the property to test

    is_int_return : bool
        To convert the value to int (if needed)

    Returns
    -------
    value : int/float
        value for the test

    """
    assert prop_dict["type"] in [
        "float",
        "int",
    ], "find_num_value is for numerical properties"
    assert type(is_int_return) is bool, "is_int_return must be a Boolean"

    var_min = prop_dict["min"]
    var_max = prop_dict["max"]

    # Adapt the value to the min/max
    if var_min == "" and var_max == "":  # No min and No max
        var_min = 0
        var_max = 100
    elif var_min == "" and var_max != "":  # No min but a max
        var_max = float(var_max)
        var_min = var_max - 100
    elif var_min != "" and var_max == "":  # No max but a min
        var_min = float(var_min)
        var_max = var_min + 100
    else:  # A min and a max
        var_min = float(var_min)
        var_max = float(var_max)

    # Random float in [var_min, var_max]
    test_value = random_sample() * (var_max - var_min) + var_min
    if is_int_return:  # We have to return an integer
        return int(test_value)
    else:
        return test_value


def is_type_list(type_name):
    """Check if the type_name is a list of pyleecan objects "[class_name]"

    Parameters
    ----------
    type_name : str
        name of the type to test

    Returns
    -------
    is_list : bool
        True if the type is a list of pyleecan objects

    """
    return type_name[0] == "[" and type_name[-1] == "]"


def is_type_dict(type_name):
    """Check if the type_name is a dict of pyleecan objects "{class_name}"

    Parameters
    ----------
    type_name : str
        name of the type to test

    Returns
    -------
    is_list : bool
        True if the type is a dict of pyleecan objects

    """
    return type_name[0] == "{" and type_name[-1] == "}"


class MissingTypeError(Exception):
    """ """

    pass
