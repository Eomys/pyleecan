import gzip
from json import load as jload
from os.path import isdir, isfile, splitext


def load_json(file_path):
    """Load a json file

    Parameters
    ----------
    file_path: str
        path to the file or directory to load

    Returns
    -------
    file_path: str
        edited path to the file to load
    json_data: json decoded data type
        data of the json file
    """
    # remove tailing dir seperators
    while file_path.endswith(("\\", "/")):
        file_path = file_path[:-1]

    # if a path is given, add default file name to file_path
    if isdir(file_path):
        i = max(file_path.rfind("\\"), file_path.rfind("/"))
        if i != -1:
            file_path += file_path[i:]
        else:
            file_path += "/" + file_path

    # if there is no file extension, try some
    if not splitext(file_path)[1]:
        file_ext = ""
        for ext in [".json", ".json.gz"]:
            if isfile(file_path + ext):
                file_ext = ext
        file_path += file_ext

    # The file (and the folder) should exist
    if not isfile(file_path):
        raise LoadMissingFileError(str(file_path) + " doesn't exist")

    # Get the data dictionary
    if file_path.endswith(".json.gz"):
        with gzip.open(file_path, mode="rt", encoding="utf-8") as fp:
            json_data = jload(fp)
    else:
        with open(file_path, "r") as fp:
            json_data = jload(fp)

    return file_path, json_data


class LoadMissingFileError(Exception):
    """ """

    pass
