from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment


def _comp_line_dict(self):
    """Define a dictionnary of the lines to draw the slot
    If a line has begin==end, it is replaced by "None" (dict has always the same number of keys)

    Parameters
    ----------
    self : SlotW16
        A SlotW16 object

    Returns
    -------
    line_dict: dict
        Dictionnary of the slot lines (key: line name, value: line object)
    """

    Rbo = self.get_Rbo()

    point_dict = self._comp_point_coordinate()
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]
    Z5 = point_dict["Z5"]
    Z6 = point_dict["Z6"]
    Z7 = point_dict["Z7"]
    Z8 = point_dict["Z8"]
    Z9 = point_dict["Z9"]
    Z10 = point_dict["Z10"]

    # Creation of curve
    line_dict = dict()
    line_dict["1-2"] = Segment(Z1, Z2)
    line_dict["2-3"] = Arc1(Z2, Z3, -Rbo + self.H0, is_trigo_direction=False)
    line_dict["3-4"] = Arc1(Z3, Z4, -self.R1, is_trigo_direction=False)
    line_dict["4-5"] = Segment(Z4, Z5)
    line_dict["5-6"] = Arc1(Z5, Z6, Rbo - self.H0 - self.H2, is_trigo_direction=True)
    line_dict["6-7"] = Segment(Z6, Z7)
    line_dict["7-8"] = Arc1(Z7, Z8, -self.R1, is_trigo_direction=False)
    line_dict["8-9"] = Arc1(Z8, Z9, -Rbo + self.H0, is_trigo_direction=False)
    line_dict["9-10"] = Segment(Z9, Z10)

    # Closing Arc (Rbo)
    line_dict["10-1"] = Arc1(Z10, Z1, -self.get_Rbo(), is_trigo_direction=False)

    # Closing Active part
    line_dict["9-2"] = Arc1(
        begin=Z9,
        end=Z2,
        radius=-abs(Z9),
        is_trigo_direction=False,
    )
    line_dict["2-9"] = Arc1(
        begin=Z2,
        end=Z9,
        radius=abs(Z9),
        is_trigo_direction=True,
    )

    return line_dict
