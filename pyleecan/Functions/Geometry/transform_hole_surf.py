from numpy import pi, exp
from ...Functions.labels import (
    update_RTS_index,
    decode_label,
    BOUNDARY_PROP_LAB,
    YSR_LAB,
    YSL_LAB,
)


def transform_hole_surf(hole_surf_list, Zh, sym, alpha, delta, is_split=False):
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
    is_split : bool
        When sym>1, call surf.split_line to cut the surfaces

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
            new_surf = surf.copy()
            new_surf.rotate(ii * 2 * pi / Zh)
            # Update label like "Rotor-0_HoleVoid_R0-T0-S0"
            new_surf.label = update_RTS_index(label=new_surf.label, S_id=ii)
            surf_list.append(new_surf)

    # Split the surfaces for symmetry
    if is_split and sym > 1:
        # Add an extra surface for each cut (alpha0 > 0)
        for surf in hole_surf_list:
            last_surf = surf.copy()
            last_surf.rotate((ii + 1) * 2 * pi / Zh)
            # Update label like "Rotor-0_HoleVoid_R0-T0-S0"
            last_surf.label = update_RTS_index(label=last_surf.label, S_id=ii + 1)
            surf_list.append(last_surf)

            first_surf = surf.copy()
            first_surf.rotate((Zh - 1) * 2 * pi / Zh)
            # Update label like "Rotor-0_HoleVoid_R0-T0-S0"
            first_surf.label = update_RTS_index(label=first_surf.label, S_id=Zh - 1)
            surf_list.append(first_surf)

        cut_list = list()
        lam_label = decode_label(new_surf.label)["lam_label"]
        for surf in surf_list:
            # Cut Ox axis
            top, _ = surf.split_line(
                0,
                100,
                is_join=True,
                prop_dict_join={BOUNDARY_PROP_LAB: lam_label + "_" + YSR_LAB},
            )
            if top is not None and sym > 2:
                # Cut O-"sym angle" axis
                _, bot = top.split_line(
                    0,
                    100 * exp(1j * 2 * pi / sym),
                    is_join=True,
                    prop_dict_join={BOUNDARY_PROP_LAB: lam_label + "_" + YSL_LAB},
                )
                if bot is not None:
                    cut_list.append(bot)
            elif top is not None:  # Half the machine => Only one cut required
                cut_list.append(top)
        surf_list = cut_list

    return surf_list
