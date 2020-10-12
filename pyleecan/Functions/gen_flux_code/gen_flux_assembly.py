# -*- coding: utf-8 -*-
"""@package

@date Created on Mon Apr 04 16:29:08 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def gen_flux_assembly(code, name, blank, obj_list):
    """

    Parameters
    ----------
    code :

    name :

    blank :

    obj_list :


    Returns
    -------

    """
    code += (
        "lastInstance = BooleanAssembly(name='Assembly_"
        + name
        + "',\n\
                    coordSys=CoordSys['XYZ1'],\n\
                    blank=ModelerObject['OBJ_EXTRUDE_"
        + blank
        + "'],\n\
                    tools=["
    )
    for obj in obj_list:
        code += "ModelerObject['OBJ_EXTRUDE_" + obj + "'],"
    code = code[:-1] + "],\n"  # Remove last ","
    code += "                    visibility=Visibility['VISIBLE'])\n"

    return code
