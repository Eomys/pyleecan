from json import load as jload
from os.path import isfile, isdir
from re import match


def load_json(file_path):
    """Load a json file

    Parameters
    ----------
    file_path: str
        path to the file to load

    Returns
    -------
    file_path: str
        edited path to the file to load
    json_data: json decoded data type
        data of the json file
    """
    if isdir(file_path):
        i = max(file_path.rfind("\\"), file_path.rfind("/"))
        if i != -1:
            file_path += file_path[i:] + ".json"
        else:
            file_path += "/" + file_path + ".json"

    # The file_name must end with .json
    elif not match(".*\.json", file_path):
        file_path += ".json"  # If it doesn't, we add .json at the end

    # The file (and the folder) should exist
    if not isfile(file_path):
        raise LoadMissingFileError(str(file_path) + " doesn't exist")

    # Get the data dictionary
    with open(file_path, "r") as load_file:
        json_data = jload(load_file)

    return file_path, json_data


class LoadMissingFileError(Exception):
    """ """

    pass
