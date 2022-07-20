import gzip
from datetime import datetime
from json import dump
from logging import getLogger
from os import makedirs, remove, listdir
from os.path import isdir, isfile, join, split
from shutil import move
from numpy import int32

from ... import __version__
from ...Classes import get_class_dict
from ...Classes._frozen import FrozenClass
from ...definitions import PACKAGE_NAME


def save_json(
    obj,
    save_path="",
    is_folder=False,
    type_handle_old=2,
    type_compression=0,
    class_to_split=("Simulation", "Machine", "Material", "HoleUD", "SlotUD", "SlotUD2"),
):
    """Save the object to the save_path

    Parameters
    ----------
    obj :
        A pyleecan object to save
    save_path: str
        path to the folder to save the object
    is_folder: bool
        to split the object in different files
    type_handle_old : int
        How to handle old file in folder mode (0:Nothing, 1:Delete, 2:Move to "Backup" folder)
    type_compression: int
        0: no compression, 1: gzip
    class_to_split: list
        list of classes (and daughter classes) that should be split
        only for is_folder == True
    """
    if isinstance(obj, FrozenClass):  # Pyleecan obj
        # Get the object logger
        logger = obj.get_logger()
    else:
        logger = getLogger("Pyleecan")

    # init
    file_ext = ".json"
    if type_compression == 1:
        file_ext += ".gz"

    # create path and name for the base file
    file_path, base_name = setup_save_path(
        save_path,
        obj,
        is_folder=is_folder,
        type_handle_old=type_handle_old,
        file_ext=file_ext,
        logger=logger,
    )

    # prepare data for dumping and split if needed
    obj = build_data(obj, logger)
    now = datetime.now()
    obj["__save_date__"] = now.strftime("%Y_%m_%d %Hh%Mmin%Ss ")
    obj["__version__"] = PACKAGE_NAME + "_" + __version__

    split_list = [{base_name: obj}]

    if is_folder:
        # Add the classes daughters
        class_to_add = []
        class_dict = get_class_dict()

        for class_name in class_to_split:
            class_to_add.extend(class_dict[class_name]["daughters"])

        class_to_split += tuple(class_to_add)
        split_obj_dict(class_to_split, obj, file_path, split_list, file_ext, logger)

    # logging
    cls_name = obj["__class__"]
    if is_folder:
        msg = f"Saving {cls_name} to folder '{file_path}' ({len(split_list)} files)."
    else:
        msg = f"Saving {cls_name} to file '{join(file_path, base_name)}'."
    logger.info(msg)
    print(msg)

    # save all objects from the split list
    for elem in split_list:
        file_name = list(elem.keys())[0]
        save_obj = elem[file_name]
        json_kwargs = dict(sort_keys=True, indent=2, separators=(",", ": "))
        json_file = join(file_path, file_name)

        if type_compression == 1:
            with gzip.open(json_file, mode="wt", encoding="utf-8") as fp:
                dump(save_obj, fp, **json_kwargs)
        else:
            with open(json_file, "w") as fp:
                dump(save_obj, fp, **json_kwargs)

    return obj


def setup_save_path(save_path, obj, is_folder, type_handle_old, file_ext, logger):
    """
    Check save_path and modify or create it if needed, i.e. add or remove
    file extension .json or create new name based on class name.

    Parameters
    ----------
    save_path: str
        File/Folder path
    obj:
        Pyleecan object to save
    is_folder: bool
        object is saved if folder mode
    type_handle_old : int
        How to handle old file in folder mode (0:Nothing, 1:Delete, 2:Move to "Backup" folder)
    file_ext: str
        File extension e.g. ".json"
    logger :
        Logger to use
    """
    # generate or correct file and path if needed
    if not save_path:  # generate
        if is_folder:
            file_path = create_folder(type(obj).__name__, logger)
            file_name = file_path + file_ext
        else:
            file_path = ""
            file_name = get_filename(obj, file_path, [], file_ext, logger)

    else:  # correct
        # remove old extension in case
        if save_path.endswith(".json"):
            save_path = save_path[:-5]
            if is_folder:
                logger.warning(
                    f"Removed '.json' from save_path '{save_path}' in folder mode."
                )

        # file mode
        if not is_folder:
            if not save_path.endswith(file_ext):
                save_path += file_ext
            file_path, file_name = split(save_path)

        # folder mode
        else:
            file_path, file_name = split(save_path)
            file_path = join(file_path, file_name)
            file_name += file_ext
            # Remove old files from old folder
            if isdir(file_path) and type_handle_old != 0:
                for name in listdir(file_path):
                    if name[-5:] == ".json":
                        path = join(file_path, name)
                        if type_handle_old == 1:
                            logger.debug("Removing old file :" + path)
                            try:
                                remove(path)
                            except Exception as e:
                                logger.error(
                                    "Unable to remove old file ("
                                    + path
                                    + ") while saving:\n"
                                    + str(e)
                                )
                        elif type_handle_old == 2:
                            logger.debug("Moving old file to Backup folder:" + path)
                            back_path = join(file_path, "Backup")
                            try:
                                if not isdir(back_path):
                                    makedirs(back_path)
                                move(path, back_path)
                            except Exception as e:
                                logger.error(
                                    "Unable to move old file ("
                                    + path
                                    + ") while saving:\n"
                                    + str(e)
                                )

    if file_path and not isdir(file_path):
        makedirs(file_path)

    return file_path, file_name


def build_data(obj, logger):
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
            data.append(build_data(elem, logger))
        return data
    # dicts
    if isinstance(obj, dict):
        data = {}
        for key in obj:
            data[key] = build_data(obj[key], logger)
        return data
    # pyleecan classes, i.e. instances with as_dict method
    if hasattr(obj, "as_dict") and callable(getattr(obj, "as_dict", None)):
        return build_data(obj.as_dict(), logger)
    if isinstance(obj, int32):  # int
        return int(obj)
    # other allowed types
    if is_json_serializable(obj):
        return obj
    # tuples (excluded)
    if isinstance(obj, tuple):
        pass  # TODO Do we need tuples? If we do, add pyleecan tuple helper class.

    if obj is not None:
        logger.warning(
            f"build_data(): Objects of type {type(obj).__name__} can not be "
            + "serialized for now and will be saved as None."
        )

    return None


def split_obj_dict(cls_tupel, obj_dict, folder, split_list, file_ext, logger):
    """
    Store classes_tuple objects contained in obj_dict in split_list and modify
    the obj_dict.

    Parameters
    ----------

    classes_tuple: tuple
        tuple containing the classe names to save separately

    obj_dict: dict
        object dictionary to save

    folder_path: str
        directory to save all the files

    logger: logging.Logger
        logger to display information

    Returns
    -------
    obj_dict : dict
        object dictionnary to save
    """
    if isinstance(obj_dict, dict):
        for key, val in obj_dict.items():
            obj_dict[key] = split_obj_dict(
                cls_tupel, val, folder, split_list, file_ext, logger
            )

        if (
            "__class__" in obj_dict.keys()
            and obj_dict["__class__"] in cls_tupel
            and (
                ("name" in obj_dict.keys() and obj_dict["name"] not in ["", None])
                or "name" not in obj_dict.keys()
            )
        ):
            # and also add it to the list of objects to be saved
            name = get_filename(obj_dict, folder, split_list, file_ext, logger)
            split_list.append({name: obj_dict})
            return name

    elif isinstance(obj_dict, list):
        for idx, list_val in enumerate(obj_dict):
            obj_dict[idx] = split_obj_dict(
                cls_tupel, list_val, folder, split_list, file_ext, logger
            )

    return obj_dict


def create_folder(name, logger):
    """Create a new non existing the folder: "YYYY_mm_dd-HH_MM_SS-name"."""
    # datetime object containing current date and time
    now = datetime.now()
    dt_string = now.strftime("%Y_%m_%d-%Hh%Mmin%Ss-")
    path = dt_string + name

    # Check if the directory exists
    while isdir(path):
        now = datetime.now()
        dt_string = now.strftime("%Y_%m_%d-%Hh%Mmin%Ss-")
        path = dt_string + name

    logger.info("Creating folder " + path + " to save the object.")
    makedirs(path)

    return path


def is_json_serializable(obj):
    if isinstance(obj, (bool, float, int, str)):
        return True
    else:
        return False


def get_filename(obj, folder, split_list, file_ext, logger):
    """
    Get a filename for the object that doesn't exists.

    Parameters
    ----------

    obj: dict
        object dictionary to save

    folder_path: str
        directory to save all the files

    split_list: list
        list of objects to be saved seperately

    logger: logging.Logger
        logger to display information

    Returns
    -------
    name : str
        name of the file containing the object
    """
    # Define the file name
    if "name" in obj.keys() and obj["name"] not in ["", None]:
        name = obj["name"]
        msg = f"Saving {name} in "
    else:
        name = obj["__class__"]
        msg = f"Saving unnamed object of class {name} in "

    # get list of names that will be created with this save to folder
    name_list = []
    for elem in split_list:
        name_list.append(list(elem.keys())[0])

    # Add prefix to get a file name that doesn't exists
    num = 0
    new_name = name + file_ext
    while isfile(join(folder, new_name)) or new_name in name_list:
        num += 1
        new_name = name + "_{:05d}".format(num) + file_ext

    # logging
    file_path = join(folder, new_name)
    logger.info(msg + file_path)

    return new_name  # Set the name to load the file
