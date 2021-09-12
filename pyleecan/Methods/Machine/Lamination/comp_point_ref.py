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
    if self.is_internal:
        Rref = self.get_Ryoke() + (self.comp_height_yoke() / 2)
    else:
        Rref = self.get_Ryoke() - (self.comp_height_yoke() / 2)
    # TODO adapt Rref to avoid ventilations

    if self.yoke_notch in [None, list()]:
        angle = pi / sym
    else:
        yoke_desc, _ = self.get_yoke_desc(sym=sym, is_reversed=False)
        # Find an Arc without notches
        ii = 0
        while ii < len(yoke_desc) and not (
            isinstance(yoke_desc[ii]["obj"], Arc)
            and (yoke_desc[ii]["begin_angle"] < yoke_desc[ii]["end_angle"])
        ):
            ii += 1
        angle = (yoke_desc[ii]["begin_angle"] + yoke_desc[ii]["end_angle"]) / 2

    return Rref * exp(1j * angle)
