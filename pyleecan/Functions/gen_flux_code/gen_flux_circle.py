# -*- coding: utf-8 -*-
"""@package

@date Created on Fri Feb 12 10:16:41 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

# from pyleecan.Functions.gen_flux_code.gen_flux_arc import gen_flux_arc
# from pyleecan.Functions.gen_flux_code.gen_flux_point import gen_flux_point

from gen_flux_code.gen_flux_arc import gen_flux_arc
from gen_flux_code.gen_flux_point import gen_flux_point


def gen_flux_circle(code="", obj_cpt={"Point": 0, "Line": 0}, Zc=0, R=1, color="WHITE"):
    """Generate the code needed to create a Line in Flux

    Parameters
    ----------
    code :
        Current state of the code to expand (Default value = "")
    obj_cpt :
        Object counter (Default value = {"Point": 0), "Line": 0}
    Zc :
        Complex coordinate of the certer of the circle (Default value = 0)
    R :
        Radius of the circle (Default value = 1)
    color :
        Color of the Arcs (default white)

    Returns
    -------
    string, dict
        code,obj_cpt: The code needed to create the circle and the
        object counter

    """

    # A circle is define by two point and two arc
    code += gen_flux_point(obj_cpt["Point"] + 1, Zc - R)
    obj_cpt["Point"] += 1

    code += gen_flux_point(obj_cpt["Point"] + 1, Zc + R)
    obj_cpt["Point"] += 1

    code += gen_flux_arc(
        obj_cpt["Line"] + 1, R, obj_cpt["Point"], obj_cpt["Point"] - 1, color
    )
    obj_cpt["Line"] += 1

    code += gen_flux_arc(
        obj_cpt["Line"] + 1, R, obj_cpt["Point"] - 1, obj_cpt["Point"], color
    )
    obj_cpt["Line"] += 1

    return code, obj_cpt
