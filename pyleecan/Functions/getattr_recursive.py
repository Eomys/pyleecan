# -*- coding: utf-8 -*-


def getattr_recursive(obj, attr_list):
    """
    Function to recursively get an attribute.

    Parameters
    ----------
    obj : object
        An object

    attr_list: list
        A list of strings that is the attribute 'tree'

    Returns
    -------
    attr: attribute
        An attribute

    """

    if len(attr_list) > 1:
        return getattr_recursive(getattr(obj, attr_list[0]), attr_list[1:])
    else:
        return getattr(obj, attr_list[0])
