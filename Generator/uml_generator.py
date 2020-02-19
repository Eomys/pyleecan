# -*- coding: utf-8 -*-
"""Created on 2020-02-18 18:11:50
@author: sebastian_g
"""
import sys
from os.path import dirname, abspath, normpath, join, isfile, split

from json import load as jload

TAB = " " * 8


def generate_uml(file_path, save_file=None, is_attributes=True, is_methods=True):

    # check if the file exist
    if not isfile(file_path):
        raise GenerateUMLMissingFileError(str(file_path) + " doesn't exist")

    # get the class dictionary
    with open(file_path, "r") as load_file:
        class_dict = jload(load_file)

    # generate dot language file header
    header = ""
    header += 0 * TAB + "digraph G {\n"
    header += 1 * TAB + 'fontname = "Bitstream Vera Sans"\n'
    header += 1 * TAB + "fontsize = 8\n\n"
    header += 1 * TAB + "node [\n"
    header += 2 * TAB + 'fontname = "Bitstream Vera Sans"\n'
    header += 2 * TAB + "fontsize = 8\n"
    header += 2 * TAB + 'shape = "record"\n'
    header += 1 * TAB + "]\n\n"
    header += 1 * TAB + "edge [\n"
    header += 2 * TAB + 'fontname = "Bitstream Vera Sans"\n'
    header += 2 * TAB + "fontsize = 8\n"
    header += 1 * TAB + "]\n\n"

    # content
    cls_str = ""
    rel_str = "\n\n"
    for cls_name, cls_dict in class_dict.items():
        cls_str += "\n"
        cls_str += 1 * TAB + cls_name + "_ [\n"
        cls_str += 2 * TAB + 'label = "{' + cls_name + "|"
        if is_attributes:
            for attr in cls_dict["properties"]:
                type_str = attr["type"]
                type_str = type_str.replace("]", ")")
                type_str = type_str.replace("}", ")")
                type_str = type_str.replace("[", "list(")
                type_str = type_str.replace("{", "dict(")
                cls_str += attr["name"] + " : " + type_str + "\\l"
        cls_str += "|"
        if is_methods:
            for mthd in cls_dict["methods"]:
                cls_str += mthd + "()\\l"

        cls_str += '}"\n'
        cls_str += 1 * TAB + "]"

        if cls_dict["mother"]:
            rel_str += 1 * TAB + cls_name + "_ -> " + cls_dict["mother"] + "_\n"

    # footer
    footer = "\n}"

    # write file
    if save_file is None:
        save_file = join(split(file_path)[0], "class_uml.gv")

    with open(save_file, "w") as fp:
        fp.write(header + cls_str + rel_str + footer)

    print('UML File "' + save_file + '" generated.')


class GenerateUMLMissingFileError(Exception):
    """ """

    pass


if __name__ == "__main__":
    root_path = normpath(abspath(join(dirname(__file__), "..", "..")))
    file_path = join(root_path, "pyleecan", "Classes", "class_dict.json")
    generate_uml(file_path)
