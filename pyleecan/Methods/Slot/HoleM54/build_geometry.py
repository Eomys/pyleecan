from numpy import pi, exp

from ....Classes.Arc1 import Arc1
from ....Classes.Arc3 import Arc3
from ....Classes.SurfLine import SurfLine
from ....Functions.labels import HOLEV_LAB, HOLEM_LAB


def build_geometry(self, alpha=0, delta=0, is_simplified=False):
    """Compute the curve (Arc) needed to plot the Hole.
    The ending point of a curve is the starting point of the next curve in the
    list

    Parameters
    ----------
    self : HoleM54
        A HoleM54 object
    alpha : float
        Angle to rotate the slot (Default value = 0) [rad]
    delta : complex
        Complex to translate the slot (Default value = 0)
    is_simplified : bool
       True to avoid line superposition

    Returns
    -------
    surf_list : list
        List of Air Surface on the slot

    """

    # Get correct label for surfaces
    lam_label = self.parent.get_label()
    R_id, surf_type = self.get_R_id()
    vent_label = lam_label + "_" + surf_type + "_R" + str(R_id) + "-"

    Rext = self.get_Rext()
    # Get all the points
    point_dict = self._comp_point_coordinate()
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]

    surf_list = list()
    curve_list = list()
    curve_list.append(Arc1(begin=Z1, end=Z2, radius=-self.R1, is_trigo_direction=False))
    curve_list.append(Arc3(begin=Z2, end=Z3, is_trigo_direction=True))
    curve_list.append(Arc1(begin=Z3, end=Z4, radius=self.R1 + self.H1))
    curve_list.append(Arc3(begin=Z4, end=Z1, is_trigo_direction=True))

    Zref = Rext - self.H0 - self.H1 / 2
    surf_list.append(
        SurfLine(line_list=curve_list, label=vent_label + "T0-S0", point_ref=Zref)
    )

    # Apply the transformations
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
