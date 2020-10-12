# -*- coding: utf-8 -*-
"""@package

@date Created on Thu Feb 11 13:33:11 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""
from pyleecan.Functions.gen_flux_code import REPERE_NAME


def gen_flux_arc(arc_index, R, start_index, end_index, color="WHITE"):
    """Generate the code needed to create a Line in Flux

    Parameters
    ----------
    arc_index :
        Index of the Arc
    Zcenter :
        Complex coordinate of the certer of the Arc
    start_index :
        Index of the start point of the Arc
    end_index :
        Index of the end point of the Arc
    color :
        Color of the arc (default white)
    R :
        Radius of the arc

    Returns
    -------
    string
        code: Needed code to add the Arc

    """

    if type(start_index) is int:
        start_index = "Point[" + str(start_index) + "]"
    if type(end_index) is int:
        end_index = "Point[" + str(end_index) + "]"

    code = (
        "LineArcRadius(color=Color['"
        + color
        + "'],#Line["
        + str(arc_index)
        + "]\n\
              visibility=Visibility['VISIBLE'],\n\
              coordSys=CoordSys['"
        + REPERE_NAME
        + "'],\n\
              radius='"
        + str(R)
        + "',\n\
              defPoint=["
        + str(start_index)
        + ","
        + str(end_index)
        + "],\n\
              nature=Nature['STANDARD'])\n"
    )

    return code
