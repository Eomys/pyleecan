from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1


def _comp_line_dict(self):
    """Define a dictionnary of the lines to draw the slot
    If a line has begin==end, it is replaced by "None" (dict has always the same number of keys)

    Parameters
    ----------
    self : SlotCirc
        A SlotCirc object

    Returns
    -------
    line_dict: dict
        Dictionnary of the slot lines (key: line name, value: line object)
    """

    point_dict = self._comp_point_coordinate()
    R0 = self._comp_R0()

    if self.H0 < self.W0 / 2:
        sign = -1
    else:
        sign = 1
    # Creation of curve
    if self.is_outwards():
        full_arc = Arc1(
            begin=point_dict["Z1"],
            end=point_dict["Z2"],
            radius=-R0*sign,
            is_trigo_direction=True,
        )
    else:
        full_arc = Arc1(
            begin=point_dict["Z1"],
            end=point_dict["Z2"],
            radius=R0*sign,
            is_trigo_direction=False,
        )

    line_dict = dict()
    line_dict["1-2"] = full_arc
    # Split arc to avoid angle > 180 deg (for FEMM)
    line_dict["1-M"] = full_arc.copy()
    line_dict["1-M"].split_half(is_begin=True)
    line_dict["M-2"] = full_arc.copy()
    line_dict["M-2"].split_half(is_begin=False)
    # Closing arc
    line_dict["2-1"] = Arc1(
        point_dict["Z2"], point_dict["Z1"], -self.get_Rbo(), is_trigo_direction=False
    )

    return line_dict
