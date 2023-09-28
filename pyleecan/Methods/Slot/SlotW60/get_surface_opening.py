from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1
from ....Classes.SurfLine import SurfLine
from ....Functions.labels import SOP_LAB, DRAW_PROP_LAB


def get_surface_opening(self, alpha=0, delta=0):
    """Return the list of surfaces defining the opening area of the Slot

    Parameters
    ----------
    self : SlotW60
        A SlotW60 object
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
    line_dict = self._comp_line_dict()
    curve_list = [
        line_dict["1-2"],
        line_dict["2-3"],
    ]
    if self.H3 > 0:
        curve_list.extend([line_dict["3-4"], line_dict["4-w1"], line_dict["w1-w4"]])
    elif self.W3 > 0:
        curve_list.append(line_dict["3-w4"])
    curve_list.append(line_dict["w4-w3"])
    if self.H4 > 0:
        curve_list.extend([line_dict["w3-w2"], line_dict["w2-5"], line_dict["5-6"]])
    else:
        curve_list.append(line_dict["w3-6"])
    #  second winding
    if self.H4 > 0:
        curve_list.extend([line_dict["6-7"], line_dict["7-w2s"], line_dict["w2s-w3s"]])
    else:
        curve_list.append(line_dict["6-w3s"])
    curve_list.append(line_dict["w3s-w4s"])
    if self.H3 > 0:
        curve_list.extend([line_dict["w4s-w1s"], line_dict["w1s-8"], line_dict["8-9"]])
    elif self.W3 > 0:
        curve_list.append(line_dict["w4s-9"])
    curve_list.extend([line_dict["9-10"], line_dict["10-11"], line_dict["11-1"]])

    curve_list = [line for line in curve_list if line is not None]

    # Only the closing arc (11-1) needs to be drawn (in FEMM)
    for curve in curve_list[:-1]:
        if curve.prop_dict is None:
            curve.prop_dict = dict()
        curve.prop_dict.update({DRAW_PROP_LAB: False})

    # Create surface
    Z10 = line_dict["10-11"].get_begin()
    Z2 = line_dict["1-2"].get_end()
    Zmid = (Z10 + Z2) / 2
    label = self.parent.get_label() + "_" + SOP_LAB + "_R0-T0-S0"
    surface = SurfLine(line_list=curve_list, label=label, point_ref=Zmid)

    # Apply transformation
    if alpha != 0:
        surface.rotate(alpha)
    if delta != 0:
        surface.translate(delta)

    return [surface]
