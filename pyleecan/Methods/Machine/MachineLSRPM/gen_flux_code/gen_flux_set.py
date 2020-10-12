# -*- coding: utf-8 -*-
"""@package

@date Created on Thu Apr 07 13:21:38 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def gen_flux_set(code):
    """Create the rotor and stator mechanical set

    Parameters
    ----------
    code :
        Code to expand

    Returns
    -------
    string
        code: New state of the code

    """

    code += "#Rotor Mechanical set\n"
    code += (
        "lastInstance = MechanicalSetRotation1Axis(name='ROTOR_SET',\n\
                               kinematics=RotatingMultiStatic(),\n\
                               rotationAxis=RotationZAxis(coordSys=CoordSys["
        "'XYZ1'],\n\
                                                          pivot=['0','0',"
        "'0']))\n"
    )
    code += "#Stator Mechanical set\n"
    code += "lastInstance = MechanicalSetFixed(name='STATOR_SET')\n\n"

    return code
