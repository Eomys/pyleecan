# -*- coding: utf-8 -*-


from femm import mi_addboundprop


def create_FEMM_boundary_conditions(sym, is_antiper):
    """Create the boundary conditions in FEMM

    Parameters
    ----------
    sym : int
        Symmetry factor of the machine
    is_antiper : bool
        True if an anti-periodicity is considered

    Returns
    -------
    None
    """
    if sym == 1:
        is_antiper = False

    # anti periodic boundary conditions
    if is_antiper:
        BdPr = 5
    # even number of rotor poles /slots -> periodic boundary conditions
    else:
        BdPr = 4

    # Dirichlet (no flux going out)
    mi_addboundprop("bc_A0", 0, 0, 0, 0, 0, 0, 0, 0, 0)
    # periodic and anti periodic conditions
    mi_addboundprop("bc_ag2", 0, 0, 0, 0, 0, 0, 0, 0, BdPr + 2)
    if sym > 1:
        mi_addboundprop("bc_s1", 0, 0, 0, 0, 0, 0, 0, 0, BdPr)
        mi_addboundprop("bc_ag1", 0, 0, 0, 0, 0, 0, 0, 0, BdPr)
        mi_addboundprop("bc_ag3", 0, 0, 0, 0, 0, 0, 0, 0, BdPr)
        mi_addboundprop("bc_r1", 0, 0, 0, 0, 0, 0, 0, 0, BdPr)
        mi_addboundprop("bc_r2", 0, 0, 0, 0, 0, 0, 0, 0, BdPr)
