# -*- coding: utf-8 -*-
"""@package

@date Created on Thu Feb 11 11:38:10 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from pyleecan.Functions.gen_flux_code import REPERE_NAME


def gen_flux_point(index, Z):
    """Generate the code needed to create a Point in Flux

    Parameters
    ----------
    index :
        Index of the point
    Z :
        Complex coordinate of the point

    Returns
    -------
    string
        code: Needed code to add the point

    """

    code = (
        "PointCoordinates(color=Color['White'],#Point["
        + str(index)
        + "]\n\
             visibility=Visibility['VISIBLE'],\n\
             coordSys=CoordSys['"
        + REPERE_NAME
        + "'],\n\
             uvw=['"
        + str(Z.real)
        + "','"
        + str(Z.imag)
        + "','0'],\n\
             nature=Nature['STANDARD'])\n"
    )

    return code
