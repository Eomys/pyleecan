import re
from os.path import isfile, join


def importName(modulename, name, ignore_error=False):
    """Import a named object from a module in the context of this function."""
    try:
        module = __import__(modulename, globals(), locals(), [name])
        return vars(module)[name]
    except Exception:
        if ignore_error:
            return None
        else:
            raise ImportError(
                f"ERROR: wildcard <{name}> could not be imported "
                + f"from module {modulename}"
            )


def rel_file_path(file_path, wildcard):
    """try to generate relative file path with given wildcard"""
    root_path = importName("..definitions", wildcard, ignore_error=True)
    if root_path:
        root_path = normpath(abspath(root_path))
        file_ = normpath(abspath(file_path))
        idx = len(root_path)
        # print(f"rel_file_path: {root_path}, <{wildcard}>")
        # print(f"file:          {file_[:idx]}")
        if file_[:idx].lower() == root_path.lower():
            file_path = f"<{wildcard}>" + file_[idx:]

    return file_path


def abs_file_path(file_path, is_check=True):
    """check a file path for a wildcard and replace it to get the abs path"""
    file_path = file_path.replace("\\", "/")
    if "<" in file_path and ">" in file_path:
        wildcard = re.search(r"\<([A-Za-z0-9_]+)\>", file_path).group(1)
        root_path = importName("pyleecan.definitions", wildcard)
        file_path = file_path.replace("<" + wildcard + ">/", "")
        file_path = join(root_path, file_path).replace("\\", "/")

    if not isfile(file_path) and is_check:
        raise FileError("ERROR: The file doesn't exist " + file_path)

    return file_path


class FileError(Exception):
    """Raised when the file does not exists"""

    pass


class ImportError(Exception):
    """Raised when the path could not be imported"""

    pass


if __name__ == "__main__":
    import sys
    from os.path import dirname, abspath, normpath, join

    ROOT_DIR = normpath(abspath(join(dirname(__file__), "..", "..")))

    sys.path.insert(0, ROOT_DIR)

    from ..definitions import MATLIB_DIR

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
