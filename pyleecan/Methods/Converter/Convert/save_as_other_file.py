import json
from os import path

"""
def selection_file():
    print("Enter path file other : ")
    path = input()

    return path
"""
# !!! not use


def save_as_other_file(path_save, other_dict):
    """save a dict

    Parameters
    ----------
    path_save : str
        Path of fuure file
    other_dict : dict
        dict use to convert in the conrrect version
    """
    with open(path.join("Tests", "Methods", "Converter", path_save), "x") as file:
        json.dump(other_dict, file)
