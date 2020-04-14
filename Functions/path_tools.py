# -*- coding: utf-8 -*-
"""
@date Created on Sat Feb 22 21:37:30 2020
@author sebastian_g
"""
from os.path import isfile, join, normpath, abspath
import re


def importName(modulename, name, ignore_error=False):
    """ Import a named object from a module in the context of this function.
    """
    try:
        module = __import__(modulename, globals(), locals(), [name])
        return vars(module)[name]
    except:
        if ignore_error:
            return None
        else:
            raise ImportError(
                f"ERROR: wildcard <{name}> could not be imported "
                + f"from module {modulename}"
            )


def rel_file_path(file, wildcard):
    """ try to generate relative file path with given wildcard
    """
    root_path = importName("pyleecan.definitions", wildcard, ignore_error=True)
    if root_path:
        root_path = normpath(abspath(root_path))
        file_ = normpath(abspath(file))
        idx = len(root_path)
        # print(f"rel_file_path: {root_path}, <{wildcard}>")
        # print(f"file:          {file_[:idx]}")
        if file_[:idx].lower() == root_path.lower():
            file = f"<{wildcard}>" + file_[idx:]

    return file


def abs_file_path(file, is_check=True):
    """ check a file path for a wildcard and replace it to get the abs path
    """
    if "<" in file and ">\\" in file:
        wildcard = re.search(r"\<([A-Za-z0-9_]+)\>", file).group(1)
        root_path = importName("pyleecan.definitions", wildcard)
        file = join(root_path, file.replace(f"<{wildcard}>\\", ""))

    if not isfile(file) and is_check:
        raise FileError("ERROR: The file doesn't exist " + file)

    return file


class FileError(Exception):
    """Raised when the file does not exists
    """

    pass


class ImportError(Exception):
    """Raised when the path could not be imported
    """

    pass


if __name__ == "__main__":
    import sys
    from os.path import dirname, abspath, normpath, join

    ROOT_DIR = normpath(abspath(join(dirname(__file__), "..", "..")))

    sys.path.insert(0, ROOT_DIR)

    from pyleecan.definitions import MATLIB_DIR

    file = "<MATLIB_DIR>\Magnet1.json"
    print(abs_file_path(file, is_check=False))

    file = "MATLIB_DIR>\Magnet1.json"
    print(abs_file_path(file, is_check=False))

    file = join(MATLIB_DIR, "test.json")
    print(rel_file_path(file, "MATLIB_DIR"))

    file = "c:/test.json"
    print(rel_file_path(file, "MATLIB_DIR"))

    file = join(MATLIB_DIR, "test.json")
    print(rel_file_path(file, "invalid_DIR"))
