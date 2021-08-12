from numpy import pi
from ...Functions.labels import update_RTS_index


def transform_hole_surf(hole_surf_list, Zh, sym, alpha, delta):
    """Take a list of surface for a single hole and apply the
    transformation (rotate, translate, duplicate)

    Parameters
    ----------
    surf_list : list
        List of the surface to edit (single hole)
    sym : int
        Symetry to apply 2 = half the machine (Default value = 1 => full machine)
    alpha : float
        Angle for rotation (Default value = 0) [rad]
    delta : complex
        Complex for translation (Default value = 0)
    is_stator : bool
        True if ventilation is on the stator and 0 on the rotor (Default value = True)

    Returns
    -------
    surf_list: list
        A list of transformed surface
    """

    assert Zh % sym == 0

    # Rotate/translate
    if alpha != 0 or delta != 0:
        for surf in hole_surf_list:
            surf.rotate(alpha)
            surf.translate(delta)

    # Duplicate to have Zh/sym all the hole surfaces
    surf_list = list()
    for ii in range(Zh // sym):
        for surf in hole_surf_list:
            new_surf = type(surf)(init_dict=surf.as_dict())
            new_surf.rotate(ii * 2 * pi / Zh)
            # Update label like "Rotor-0_HoleVoid_R0-T0-S0"
            new_surf.label = update_RTS_index(label=new_surf.label, S_id=ii)
            surf_list.append(new_surf)
    return surf_list