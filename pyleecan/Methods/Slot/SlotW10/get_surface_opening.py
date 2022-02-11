from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1
from ....Classes.SurfLine import SurfLine
from ....Functions.labels import SOP_LAB


def get_surface_opening(self, alpha=0, delta=0):
    """Return the list of surfaces defining the opening area of the Slot

    Parameters
    ----------
    self : SlotW10
        A SlotW10 object
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_list : list
        list of surfaces objects
    """

    # Create curve list
    line_list = self._comp_line_list()
    curve_list = line_list[0:3] + line_list[-4:]
    curve_list = [line for line in curve_list if line is not None]

    # Create surface
    H1 = self.get_H1()
    if self.is_outwards():
        Zmid = self.get_Rbo() + (self.H0 + H1) / 2
    else:
        Zmid = self.get_Rbo() - (self.H0 + H1) / 2
    label = self.parent.get_label() + "_" + SOP_LAB + "_R0-T0-S0"
    surface = SurfLine(line_list=curve_list, label=label, point_ref=Zmid)

    # Apply transformation
    surface.rotate(alpha)
    surface.translate(delta)

    return [surface]
