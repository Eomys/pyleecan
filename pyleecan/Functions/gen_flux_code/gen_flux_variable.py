# -*- coding: utf-8 -*-
"""@package

@date Created on Thu Apr 07 13:47:58 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def gen_flux_variable(code, name, desc, formula):
    """Create a Flux Physical variable according to formula

    Parameters
    ----------
    code :
        Code to expand
    name :
        Name of the parameter to create
    desc :
        Description of the parameter
    formula :
        Formula to compute the parameter value (str)

    Returns
    -------
    string
        code: New state of the code

    """

    code += (
        "VariationParameterFormula(name='"
        + name
        + " : "
        + desc
        + "',formula='"
        + formula
        + "')\n"
    )

    return code
