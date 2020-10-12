# -*- coding: utf-8 -*-
"""@package

@date Created on Thu Apr 07 11:51:50 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def gen_flux_application(code):
    """Create an application Magneto statique 3D for flux

    Parameters
    ----------
    code :
        Code to expand

    Returns
    -------
    string
        code: New state of the code

    """

    code += "#Creating Application Magneto Statique 3D\n"
    code += (
        "lastInstance = ApplicationMagneticDC3D("
        "formulationModel=MagneticDC3DAutomatic(),\n\
                        scalarVariableOrder=ScalarVariableAutomaticOrder(),\n\
                        vectorNodalVariableOrder=VectorNodalVariableAutomaticOrder(),\n\
                        coilCoefficient=CoilCoefficientAutomatic())\n"
    )
    return code
