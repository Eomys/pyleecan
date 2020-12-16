# -*- coding: utf-8 -*-

from distutils.spawn import find_executable
from os.path import split


def get_path_binary(binary_name, is_include_file=True):
    """Function to find path of the executable given by 'binary_name'

    Parameters
    ----------

    bindary_name : str
        name of the executable

    is_include_file : bool
        append the bindary_name to the path if set to True, default: True

    Return
    ------

    path : str
        path of the executable, return None if no executable is found

    """

    path_file = find_executable(binary_name)

    if not is_include_file and path_file:
        path_file, _ = split(path_file)

    return path_file


if __name__ == "__main__":
    print(get_path_binary("python"))
    print(get_path_binary("python", is_include_file=False))
