from h5py import File, Group
from numpy import bool_, int32, int64, string_, array
from cloudpickle import loads


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
        dictionary to instanciate Pyleecan obj
    """
    with File(file_path, "r") as file:
        # file is a group
        obj_dict = construct_dict_from_group(file)

    return file_path, obj_dict


def construct_dict_from_group(group):
    """
    construct_dict_from_group create a dictionary and extract datasets and groups from the group

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
                elif isinstance(value, bool_):  # bool
                    value = bool(value)
                elif isinstance(value, int64):  # float
                    value = float(value)
                elif isinstance(value, int32):  # int
                    value = int(value)
                elif isinstance(value, (string_, bytes)):  # String
                    value = value.decode("ISO-8859-2")
                    # None is not available in H5 => we use a string
                    if value == "NoneValue":
                        value = None

                list_.append(value)
        return list_
    else:
        for key, val in group.items():
            # Check if key is an int
            if is_int(key):
                key = int(key)
            # Convert key in case of "/"
            if isinstance(key, str):
                key = key.replace("\\x2F", "/")
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
                elif isinstance(value, int32):  # int
                    value = int(value)
                elif isinstance(value, (string_, bytes)):  # String
                    value = value.decode("ISO-8859-2")
                    # None is not available in H5 => we use a string
                    if value == "NoneValue":
                        value = None
                dict_[key] = value
        return dict_


def is_int(inputString):
    """Check if a string is an int"""
    # first check if string contains numbers
    if any(char.isdigit() for char in inputString):
        try:
            int(inputString)
            return True
        except:
            pass
    return False
