from h5py import File, Group
from numpy import bool_, int64, string_, array
from cloudpickle import loads


def construct_dict_from_group(group):
    """
    construct_dict_from_group create a dictionnary and extract datasets and groups from the group

    Parameters
    ----------
    group: h5py.Group
        group to browse

    Returns
    -------
    dict_ : dict
        created dict containing the group data
    """
    dict_ = {}

    # List split to load
    if "length_list" in group.attrs.keys():
        list_ = []

        for i in range(group.attrs["length_list"]):
            if hasattr(group["list_" + str(i)], "items"):  # Group in list
                list_.append(construct_dict_from_group(group["list_" + str(i)]))
            else:  # Dataset
                dataset = group["list_" + str(i)]
                value = dataset[()]
                if "array_list" in dataset.attrs.keys():  # List saved as an array
                    value = value.tolist()
                elif value == "NoneValue":  # Handle None values
                    value = None
                elif isinstance(value, bool_):  # bool
                    value = bool(value)
                elif isinstance(value, int64):  # float
                    value = float(value)
                elif isinstance(value, string_):  # String
                    value = value.decode("ISO-8859-2")

                list_.append(value)
        return list_
    else:
        for key, val in group.items():
            # Check if val is a group or a dataset
            if isinstance(val, Group):  # Group
                # Call the function recursively to load group
                dict_[key] = construct_dict_from_group(val)
            else:  # Dataset
                value = val[()]
                if "array_list" in val.attrs.keys():  # List saved as an array
                    value = value.tolist()
                elif value == "NoneValue":  # Handle None values
                    value = None
                elif isinstance(value, bool_):  # bool
                    value = bool(value)
                elif isinstance(value, int64):  # float
                    value = float(value)
                elif isinstance(value, string_):  # String
                    value = value.decode("ISO-8859-2")
                dict_[key] = value
        return dict_


def load_hdf5(file_path):
    """
    Load pyleecan object from h5 file

    Parameters
    ----------

    file_path: str
        file path

    Returns
    -------

    file_path: str
    obj_dict: dict
        dictionnary to instanciate Pyleecan obj
    """
    with File(file_path, "r") as file:
        # file is a group
        obj_dict = construct_dict_from_group(file)

    return file_path, obj_dict
