def set_FEMM_wind_material(femm, materials, cname, Jcus=0, Cduct=None, dwire=None):
    """Create or update the property of a winding material

    Parameters
    ----------
    femm : FEMMHandler
        client to send command to a FEMM instance
    materials: list
        list the name of all materials
    cname: str
        name of the material to create/update
    Jcus : float
        Applied source current density [A/mm^2]
    Cduct : float
        Electrical conductivity of the material [MS/m]
    dwire : float
        Diameter of each of the wire’s constituent strand [mm]

    Returns
    -------
    circuits : list
        list the name of the circuits in FEMM

    """
    if cname not in materials:
        # Create a new material
        femm.mi_addmaterial(
            cname,
            1,  # Relative permeability in the x- or r-direction
            1,  # Relative permeability in the y- or z-direction
            0,  # Permanent magnet coercivity [A/m]
            Jcus,
            Cduct,
            0,  # Lamination thickness [mm]
            0,  # Hysteresis lag angle [deg], (used for nonlinear BH curves)
            1,  # Fraction of the volume occupied per lamination that is actually filled withiron
            0,  # LamType (Not laminated)
            0,  # Hysteresis lag [deg] in the x-direction for linear problems
            0,  # Hysteresis lag [deg] in the y-direction for linear problems
            1,  # Number of strands in the wire build
            dwire,
        )
        materials.append(cname)

    return materials
