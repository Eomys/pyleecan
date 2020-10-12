# -*- coding: utf-8 -*-
"""@package Functions.gen_flux_code.gen_flux_param
Generate the flux code to create a Geometry Parameter
@date Created on Tue Mar 15 11:19:18 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def gen_flux_param(code, name, desc, value):
    """Generate the flux code to create a Geometry Parameter

    Parameters
    ----------
    code :
        Current state of the code
    name :
        Name of the Parameter to create
    desc :
        Description of the Parameter to create
    value :
        Value of the Parameter (str to allow the use of
        expression)

    Returns
    -------
    string
        code: Expanded Code

    """

    code += (
        "lastInstance = ParameterGeom(name='"
        + name
        + " : "
        + desc
        + "',expression='"
        + str(value)
        + "')\n"
    )
    return code
