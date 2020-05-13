# -*- coding: utf-8 -*-

from json import dump, load
from os.path import join, basename, isdir, isfile
from os import mkdir
from datetime import datetime
from logging import getLogger
from ..Classes._frozen import FrozenClass


def create_folder(logger, save_path):
    """
    Create the folder: "YYYY_mm_dd HH_MM_SS save_path"
    """
    # datetime object containing current date and time
    now = datetime.now()
    dt_string = now.strftime("%Y_%m_%d %Hh%Mmin%Ss ")
    path = dt_string + save_path

    # Check if the directory exists
    while isdir(path):
        now = datetime.now()
        dt_string = now.strftime("%Y_%m_%d %Hh%Mmin%Ss ")
        path = dt_string + save_path

    logger.info("Creating folder " + path + " to save the object.")
    mkdir(path)

    return path


def fix_file_name(save_path, obj, is_folder, logger):
    """
    Check save_path and modify it according to is_folder
    
    Parameters
    ----------
    save_path: str
        File/Folder path
    obj: 
        Pyleecan object to save
    is_folder: bool
        object is saved if folder mode (splitting Materials, Machine, Simulation in different files)
    """
    if not save_path:
        if is_folder:  # Create the folder
            save_path = create_folder(logger, type(obj).__name__)
        else:
            save_path = join(save_path, type(obj).__name__ + ".json")
    elif ".json" != basename(save_path)[-5:] and not is_folder:
        save_path = save_path + ".json"
    elif is_folder:
        if save_path.endswith(".json"):
            save_path = save_path[:-5]
        if not isdir(save_path):
            mkdir(save_path)
    else:
        save_path = save_path

    return save_path


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


def save_separated_obj(classes_list, obj_dict, folder_path, logger):
    """
    Save classes_list objects contained in obj_dict in separated files and modify obj_dict
    """

    for key, val in obj_dict.items():
        if isinstance(val, dict):
            if "__class__" in val.keys() and val["__class__"] in classes_list:
                # Call save_separated_obj to save the obj
                save_separated_obj(classes_list, val, folder_path, logger)

                if "name" in val.keys() and val["name"] != "" and val["name"] != None:
                    name = val["name"] + ".json"
                    if not isfile(join(folder_path, name)):
                        with open(join(folder_path, name), "w") as json_file:
                            logger.info(
                                "Saving "+ val["name"] + " in " + join(folder_path, name)
                            )
                            dump(
                                val,
                                json_file,
                                sort_keys=True,
                                indent=4,
                                separators=(",", ": "),
                            )
                else:
                    zeros = "0000"
                    num = 1
                    prefix = zeros[: -len(str(num))] + str(num)
                    name = val["__class__"] + prefix

                    # Define the file name
                    while isfile(join(folder_path, name + ".json")):
                        num += 1
                        prefix = zeros[: -len(str(num))] + str(num)
                        name = val["__class__"] + prefix

                    # Save the file
                    name += ".json"
                    logger.info(
                        "Saving unamed object of class",
                        val["__class__"],
                        "in",
                        join(folder_path, name),
                    )
                    with open(join(folder_path, name), "w") as json_file:
                        dump(
                            val,
                            json_file,
                            sort_keys=True,
                            indent=4,
                            separators=(",", ": "),
                        )

                obj_dict[key] = name  # Set the name to load the file

            else:
                obj_dict[key] = save_separated_obj(
                    classes_list, val, folder_path, logger
                )

    return obj_dict


def save_data(obj, save_path="", is_folder=False):
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
    if isinstance(obj, FrozenClass):  # Pyleecan obj
        # Get the object logger
        logger = obj.get_logger()
    else:
        logger = getLogger("Pyleecan")

    # correct file name if needed
    save_path = fix_file_name(save_path, obj, is_folder, logger)

    # save
    obj = build_data(obj)
    if isinstance(obj, dict) and is_folder:
        # List containing classes to save separately
        class_to_split = ["Machine", "Material"]

        # Add the classes daughters
        class_to_add = []
        with open(
            __file__[: __file__.rfind("Functions")] + "Classes/Class_Dict.json"
        ) as class_dict_file:
            class_dict = load(class_dict_file)

        for class_name in class_to_split:
            class_to_add.extend(class_dict[class_name]["daughters"])

        class_to_split.extend(class_to_add)

        # Call ref_objects to save the objects separately
        obj = save_separated_obj(class_to_split, obj, save_path, logger)

        i = max(save_path.rfind("/"), save_path.rfind("\\"))
        if i != -1:
            save_path += save_path[i:]
        else:
            save_path += "/" + save_path
    if is_folder:
        save_path += ".json"

    logger.info("Saving in " + save_path)
    with open(save_path, "w") as json_file:
        dump(obj, json_file, sort_keys=True, indent=4, separators=(",", ": "))

    return obj


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

    save_data(self, save_path=save_path, is_folder=is_folder)
