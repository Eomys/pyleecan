from numpy import pi
from ....Functions.labels import HOLEV_LAB, HOLEM_LAB, LAM_LAB


def build_geometry(self, alpha=0, delta=0, is_simplified=False):
    """Compute the curve (Segment) needed to plot the Hole.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : HoleUD
        A HoleUD object
    alpha : float
        Angle to rotate the slot (Default value = 0) [rad]
    delta : complex
        Complex to translate the slot (Default value = 0)
    is_simplified : bool
        True to avoid line superposition (not used)

    Returns
    -------
    surf_list: list
        List of SurfLine needed to draw the Hole
    """

    surf_list = [surf.copy() for surf in self.surf_list]

    # Get correct label for surfaces
    if self.parent is not None:
        lam_label = self.parent.get_label()
    else:
        lam_label = LAM_LAB
    R_id, surf_type = self.get_R_id()
    vent_label = lam_label + "_" + surf_type + "_R" + str(R_id) + "-T"
    mag_label = lam_label + "_" + HOLEM_LAB + "_R" + str(R_id) + "-T"

    # Update surface labels
    hole_id = 0
    mag_id = 0
    for surf in surf_list:
        if HOLEM_LAB in surf.label:
            key = "magnet_" + str(mag_id)
            if key in self.magnet_dict and self.magnet_dict[key] is not None:
                surf.label = mag_label + str(mag_id) + "-S0"
                mag_id += 1
            else:  # Magnet disabled or not defined
                surf.label = vent_label + str(hole_id) + "-S0"
                hole_id += 1
        elif HOLEV_LAB in surf.label:
            surf.label = vent_label + str(hole_id) + "-S0"
            hole_id += 1

    # Apply the transformations
    # Modulo on Alpha0 for sym
    Alpha0 = self.Alpha0 % (2 * pi / self.Zh)
    for surf in surf_list:
        surf.rotate(alpha + Alpha0)
        surf.translate(delta)

    return surf_list
