# -*- coding: utf-8 -*-
"""@package

@date Created on Thu Feb 11 11:45:29 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def gen_flux_line(line_index, start_index, end_index):
    """Generate the code needed to create a Line in Flux

    Parameters
    ----------
    line_index :
        Index of the Line
    start_index :
        Index of the start point of the Line
    end_index :
        Index of the end point of the Line

    Returns
    -------
    string
        code: Needed code to add the Line

    """

    code = (
        "LineSegment(color=Color['White'],#Line["
        + str(line_index)
        + "]\n\
                visibility=Visibility['VISIBLE'],\n\
                defPoint=[Point["
        + str(start_index)
        + "],Point["
        + str(end_index)
        + "]],\n\
                nature=Nature['STANDARD'])\n"
    )
    return code
