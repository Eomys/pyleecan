import numpy as np
import h5py


def pyleecan_dict_to_hdf5(file, obj):
    """
    Save a dict from a pyleecan object in the hdf5 file

    Parameters
    ----------
    file: hdf5 file
    obj: Pyleecan object
        object to save
    """
    obj_dict = obj.as_dict()
    for key, val in obj_dict.items():
        # Object that need groups
        if isinstance(val, dict) or isinstance(val, list):
            variable_to_hdf5(file, "", val, key)
        # Dataset
        elif val == None:
            file[key] = "NoneValue"
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
    #

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
        grp = file[group_name]

        grp[name] = array_list
        # Add an attribute to load correctly
        grp[name].attrs["array_list"] = True


def dict_to_hdf5(file, prefix, dict_to_save):
    """
    Save a list in the hdf5 file 
    """
    for key, value in dict_to_save.items():
        variable_to_hdf5(file, prefix, value, key)


def variable_to_hdf5(file, prefix, variable, name):
    # Pyleecan object dict
    if isinstance(variable, dict):
        # Create group
        group_name = prefix + "/" + name
        file.create_group(group_name)

        # Call function to create groups and datasets recursively
        dict_to_hdf5(file, group_name, variable)

    # List
    elif isinstance(variable, list):
        # Create group

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
            grp[name] = np.string_(variable.encode("ISO-8859-2"))
    # None
    elif None == variable:
        # Create dataset
        grp = file[prefix]
        grp[name] = "NoneValue"
    else:
        # Create dataset
        grp = file[prefix]
        grp[name] = variable


def save_hdf5(obj, save_path):
    """
    Save a pyleecan obj in hdf5 format
    
    Parameters
    ----------
    obj: Pyleecan object 
        object to save
    save_path: str
        file path
    """

    try:
        file = h5py.File(save_path, "w")
        pyleecan_dict_to_hdf5(file, obj)
        file.close()
    except Exception as err:
        file.close()
        raise (err)
