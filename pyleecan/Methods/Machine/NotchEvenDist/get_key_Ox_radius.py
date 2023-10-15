def get_key_Ox_radius(self):
    """Return the Key max/min radius on Ox to close the sliding band in FEMM

    Parameters
    ----------
    self : NotchEvenDist
        A NotchEvenDist object

    Returns
    -------
    ROx : Float
        Radius to use to close  the sliding band [m] (None=no intersection)
    """

    # Get all surfaces
    surf_list = self.build_geometry_key(sym=1)

    # Cut to find a surface on Ox
    Z_list = list()
    for surf in surf_list:
        Z_list.extend(surf.intersect_line(0, 100))

    # No intersection => Return default radius
    if len(Z_list) == 0:
        return None

    # Get the min/max intersection on the right of Ox only
    Rright = [Z.real for Z in Z_list if Z.real > 0]
    if len(Rright) == 0:
        return None
    elif self.is_outwards():  # Outer lamination
        return min(Rright)
    else:
        return max(Rright)
