# -*- coding: utf-8 -*-
from io import StringIO
from ..Section import File

# some constants definition
WHITESPACE = " "
INDENT = 2 * WHITESPACE
COMMENT = "! "
NEWLINE = "\n"
END = "End"


def write(self, stream=None):
    """Write the Elmer SIF section to a stream. If no stream is given, the method
    will return a StringIO.
    """
    if not stream:
        stream = StringIO()

    # if section has an 'id' write a numbered sections
    if self.id:
        nbr = str(self.id)
    else:
        nbr = ""

    # write section header
    stream.write(NEWLINE)
    if self.comment:
        stream.write("! " + self.comment)
    stream.write(self.section + " " + nbr)

    # write section entries
    for key in self.keys():
        n = ""
        value, comment = self[key]
        if isinstance(value, list) and len(value) > 1:
            n = "(" + str(len(value)) + ")"
        stream.write(NEWLINE + INDENT)
        stream.write(key + n + " = " + _convert(value))
        if comment:
            stream.write(INDENT + "! " + comment)

    # end section
    stream.write(NEWLINE + END + NEWLINE)

    return stream


def _convert(value, get_type=True):
    """internal method to convert the data corresponding to Elmer SIF needs"""
    if isinstance(value, File):  # check before str due to inheretance
        return "File " * get_type + f'"{value}"'

    if isinstance(value, str):
        return "String " * get_type + f'"{value}"'

    if isinstance(value, float):
        return "Real " * get_type + f"{value}"

    if isinstance(value, bool):
        return "Logical " * get_type + f"{value}"

    if isinstance(value, int):
        return "Integer " * get_type + f"{value}"

    if isinstance(value, list):
        val_str = ""
        for idx, val in enumerate(value):
            get_type = True if idx == 0 else False
            val_str += _convert(val, get_type=get_type) + " "
        return val_str
