# -*- coding: utf-8 -*-
"""@package build_geometry
@date Created on août 10 10:42 2018
@author franco_i
"""


def build_geometry(self, sym=1, alpha=0, delta=0, is_simplified=False):
    """Build geometry of the LamSquirrelCage

    Parameters
    ----------
    self : 
        LamSquirrelCage Object
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation
    is_simplified: bool
        True to avoid line superposition

    Returns
    -------
    list
        surf_list: list of surfaces
    
    """
    surf_list = super(type(self), self).build_geometry(
        sym=sym, is_simplified=is_simplified, alpha=alpha, delta=delta
    )

    # Adapt the label
    for surf in surf_list:
        if "Wind" in surf.label:
            surf.label = surf.label.replace("Wind", "Bare")

    return surf_list
