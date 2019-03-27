# -*- coding: utf-8 -*-
"""@package set_FEMM_boundary_conditions
@date Created on août 20 14:50 2018
@author franco_i
"""


import femm


def create_FEMM_boundary_conditions(sym, is_antisyma):
    """Create the boundary conditions in FEMM

    Parameters
    ----------
    sym :
        integer for symmetry
    is_antisyma :
    
    Returns
    -------
    None
    """
    if sym == 1:
        is_antisyma = False

    # anti periodic boundary conditions
    if is_antisyma:
        BdPr = 5
    # even number of rotor poles /slots -> periodic boundary conditions
    else:
        BdPr = 4  # Dirichlet (no flux going out)
    femm.mi_addboundprop("bc_A0", 0, 0, 0, 0, 0, 0, 0, 0, 0)
    # periodic and anti periodic conditions
    femm.mi_addboundprop("bc_ag2", 0, 0, 0, 0, 0, 0, 0, 0, BdPr + 2)
    if sym > 1:
        femm.mi_addboundprop("bc_s1", 0, 0, 0, 0, 0, 0, 0, 0, BdPr)
        femm.mi_addboundprop("bc_ag1", 0, 0, 0, 0, 0, 0, 0, 0, BdPr)
        femm.mi_addboundprop("bc_ag3", 0, 0, 0, 0, 0, 0, 0, 0, BdPr)
        femm.mi_addboundprop("bc_r1", 0, 0, 0, 0, 0, 0, 0, 0, BdPr)
        femm.mi_addboundprop("bc_r2", 0, 0, 0, 0, 0, 0, 0, 0, BdPr)
