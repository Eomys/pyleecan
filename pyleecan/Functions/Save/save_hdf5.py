import h5py
import numpy as np
from h5py import File as FileH5
from ...definitions import PACKAGE_NAME
from ... import __version__
from datetime import datetime


def save_hdf5(obj, save_path, obj_dict=None):
    """
    Save a pyleecan obj in hdf5 format

    Parameters
    ----------
    obj: Pyleecan object
        object to save
    save_path: str
        file path
    obj_dict : dict
        obj.as_dict to save (optionnal to skip call to as_dict)
    """

    file5 = None
    try:
        file5 = FileH5(save_path, "w")
        pyleecan_dict_to_hdf5(file5, obj, obj_dict=obj_dict)
        file5.close()
    except Exception as err:
        if file5:
            file5.close()
        raise (err)


def pyleecan_dict_to_hdf5(file, obj, obj_dict=None):
    """
    Save a dict from a pyleecan object in the hdf5 file

    Parameters
    ----------
    file:
        hdf5 file
    obj: Pyleecan object
        object to save
    obj_dict : dict
        obj.as_dict to save (optionnal to skip call to as_dict)
    """
    if obj_dict is not None:
        pass
    elif isinstance(obj, dict):
        obj_dict = dict()
        for key, val in obj.items():
            obj_dict[key] = val.as_dict(type_handle_ndarray=2)
    else:
        obj_dict = obj.as_dict(type_handle_ndarray=2)
    now = datetime.now()
    obj_dict["__save_date__"] = now.strftime("%Y_%m_%d %Hh%Mmin%Ss ")
    obj_dict["__version__"] = PACKAGE_NAME + "_" + __version__
    for key, val in obj_dict.items():
        # Object that need groups
        if isinstance(val, dict) or isinstance(val, list):
            variable_to_hdf5(file, "", val, key)
        # Dataset
        elif isinstance(val, np.ndarray):
            file[key] = val
        elif val == None:
            # None is not available in H5 => we use a string
            file[key] = np.string_("NoneValue".encode("ISO-8859-2"))
        elif isinstance(val, str):
            file[key] = np.string_(val.encode("ISO-8859-2"))
        else:
            file[key] = val


def list_to_hdf5(file, group_name, name, list_to_save):
    """
    Save a list in the hdf5 file : save it as a ndarray if possible

    Parameters
    ----------
    file: HDF5 file
        file to save the data
    group_name: str
        name of the group
    name: str
        name to extend the group or to contain the dataset
    list_to_save: list
        list to save

    """

    np.warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

    # Convert into array
    array_list = np.array(list_to_save)

    # Check the type to split or save as an array
    if array_list.dtype.kind in ["O", "U"]:
        # Split the list into several datasets
        # Create a new group to contain every dataset
        group_name = group_name + "/" + name
        grp = file.create_group(group_name)

        # Add an attribute to load correctly
        grp.attrs["length_list"] = len(list_to_save)

        # Save every element of the list
        for i, element in enumerate(list_to_save):
            variable_to_hdf5(file, group_name, element, "list_{}".format(i))

    else:  # Save as an array
        if group_name == "":
            file[name] = array_list
            file[name].attrs["array_list"] = True
        else:
            grp = file[group_name]
            grp[name] = array_list
            # Add an attribute to load correctly
            grp[name].attrs["array_list"] = True


def dict_to_hdf5(file, prefix, dict_to_save):
    """
    Save a list in the hdf5 file
    """
    for key, value in dict_to_save.items():
        if isinstance(key, int):
            key = str(key)
        variable_to_hdf5(file, prefix, value, key)


def variable_to_hdf5(file, prefix, variable, name):
    # Unable to save matrix of string (U=unicode) => Convert to list
    if isinstance(variable, np.ndarray) and "U" in str(variable.dtype):
        variable = variable.tolist()
    # Pyleecan object dict
    if isinstance(variable, dict):
        # Create group
        group_name = prefix + "/" + name
        file.create_group(group_name)

        # Call function to create groups and datasets recursively
        dict_to_hdf5(file, group_name, variable)

    # List
    elif isinstance(variable, list):

        # Call function to create groups and datasets recursively
        list_to_hdf5(file, prefix, name, variable)
    # Str
    elif isinstance(variable, str):
        if len(variable) == 0:
            grp = file[prefix]
            grp[name] = variable
        else:
            grp = file[prefix]
            # Create a fixed-width ASCII string according
            # to http://docs.h5py.org/en/stable/strings.html#exceptions-for-python-3
            try:
                grp[name] = np.string_(variable.encode("ISO-8859-2"))
            except Exception as e:
                raise Exception(
                    "Error while h5 saving variable " + name + ":\n" + str(e)
                )
    # None
    elif variable is None:
        # Create dataset
        grp = file[prefix]
        grp[name] = "NoneValue"
    else:
        # Create dataset
        grp = file[prefix]
        grp[name] = variable
