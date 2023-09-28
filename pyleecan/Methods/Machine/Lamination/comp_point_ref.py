from numpy import exp, pi
from ....Classes.Arc import Arc


def comp_point_ref(self, sym=1):
    """Compute coordinates of a point in the lamination
    to assign property in FEA software
    Account for slot, notches and ventilations (TODO)

    Parameters
    ----------
    self : Lamination
        Lamination Object
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)

    Returns
    point_ref : complex
        Reference point of the lamination

    """

    Rref = self.comp_radius_mid_yoke()

    # Find a radius that doesn't match any ventilation
    if self.axial_vent not in [None, list()]:
        R1, R2 = Rref, Rref
        for vent in self.axial_vent:
            (Rmin, Rmax) = vent.comp_radius()
            R1 = min(R1, Rmin)
            R2 = max(R2, Rmax)
        if self.is_internal:
            Rref = (self.Rint + R1) / 2
        else:
            Rref = (self.Rext + R2) / 2

    # Find an angle without notches on the yoke
    if not self.has_notch(is_bore=False):
        angle = pi / sym
    else:
        yoke_desc_list = self.build_radius_desc(sym=sym, is_bore=False)
        ii = 0
        while (
            ii < len(yoke_desc_list)
            and yoke_desc_list[ii]["label"] != "Radius"
            and (yoke_desc_list[ii]["begin_angle"] < yoke_desc_list[ii]["end_angle"])
        ):
            ii += 1
        angle = (
            yoke_desc_list[ii]["begin_angle"] + yoke_desc_list[ii]["end_angle"]
        ) / 2

    return Rref * exp(1j * angle)
