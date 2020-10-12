# -*- coding: utf-8 -*-

import femm


def create_FEMM_bar(is_mmfr, rho, materials):
    """Create the property for LamSquirrel cage on the rotor

    Parameters
    ----------
    is_mmfr : bool
        1 to compute the rotor magnetomotive force / rotor magnetic field
    rho : float
        the Resistivity at 20°C
    materials : list
        List of materials already created in FEMM

    Returns
    -------
    (str, list)
        material name "Rotor Bar", updated materials

    """

    if is_mmfr:
        if "Rotor Bar" not in materials:
            femm.mi_addmaterial(
                "Rotor Bar", 1, 1, 0, 0, 1e-6 / rho, 0, 0, 1, 0, 0, 0, 0, 0
            )
            materials.append("Rotor Bar")
    else:
        if "Rotor Bar" not in materials:
            # replacing the rotor bars by air
            femm.mi_addmaterial("Rotor Bar", 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0)
            materials.append("Rotor Bar")

    return "Rotor Bar", materials
