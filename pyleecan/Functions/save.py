# -*- coding: utf-8 -*-
from .Save.save_json import save_json
from .Save.save_hdf5 import save_hdf5


class FormatError(Exception):
    pass


def save(self, save_path="", is_folder=False):
    """Save the object to the save_path

    Parameters
    ----------
    self : 
        A pyleecan object
    save_path: str
        path to the folder to save the object
    is_folder: bool
        to split the object in different files: separate simulation machine and materials 
    """
    # Save in the object.path if it exist and save_path is empty
    if save_path == "" and hasattr(self, "path") and getattr(self, "path") != None:
        save_path = self.path
    print(save_path, save_path.endswith("h5"))
    if (
        not save_path.endswith("json")
        and not save_path.endswith("h5")
        and not is_folder
    ):
        save_path += ".json"  # Default format

    # Save in json
    if save_path.endswith(".json") or is_folder:
        save_json(self, save_path=save_path, is_folder=is_folder)

    elif save_path.endswith(".h5"):
        print("YEAH")
        save_hdf5(self, save_path=save_path)
