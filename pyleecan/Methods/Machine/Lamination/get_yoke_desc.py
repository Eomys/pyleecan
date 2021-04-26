from numpy import exp, pi

from ....Classes.Arc1 import Arc1
from ....Functions.Geometry.merge_notch_list import merge_notch_list


def get_yoke_desc(self, sym=1, is_reversed=False):
    """This method returns an ordered description of the elements
    that defines the yoke radius of the lamination

    Parameters
    ----------
    self : Lamination
        A Lamination object
    sym : int
        Symetry factor (2=half the lamination)
    is_reversed : bool
        True to return the line in clockwise oder
    Returns
    -------
    yoke_desc : list
        list of dictionary with key: "begin_angle", "end_angle", "obj"
    """

    Ryoke = self.get_Ryoke()

    # Get the notches
    notch_list = self.get_notch_list(sym=sym, is_yoke=True)

    # Add all the yoke lines
    yoke_desc = list()
    for ii, desc in enumerate(notch_list):
        yoke_desc.append(desc)
        if ii != len(notch_list) - 1:
            yoke_dict = dict()
            yoke_dict["begin_angle"] = notch_list[ii]["end_angle"]
            yoke_dict["end_angle"] = notch_list[ii + 1]["begin_angle"]
            yoke_dict["obj"] = Arc1(
                begin=Ryoke * exp(1j * yoke_dict["begin_angle"]),
                end=Ryoke * exp(1j * yoke_dict["end_angle"]),
                radius=Ryoke,
                is_trigo_direction=True,
            )
            yoke_desc.append(yoke_dict)

    # Add last yoke line
    if sym == 1:
        yoke_dict = dict()
        yoke_dict["begin_angle"] = notch_list[-1]["end_angle"]
        yoke_dict["end_angle"] = notch_list[0]["begin_angle"]
        yoke_dict["obj"] = Arc1(
            begin=Ryoke * exp(1j * yoke_dict["begin_angle"]),
            end=Ryoke * exp(1j * yoke_dict["end_angle"]),
            radius=Ryoke,
            is_trigo_direction=True,
        )
        if notch_list[0]["begin_angle"] < 0:
            # First element is an slot or notch
            yoke_desc.append(yoke_dict)
        else:
            # First element is a yoke line
            yoke_desc.insert(0, yoke_dict)
    elif sym != 1:  # With symmetry
        # Add last yoke line
        yoke_dict = dict()
        yoke_dict["begin_angle"] = notch_list[-1]["end_angle"]
        yoke_dict["end_angle"] = 2 * pi / sym
        yoke_dict["obj"] = Arc1(
            begin=Ryoke * exp(1j * yoke_dict["begin_angle"]),
            end=Ryoke * exp(1j * yoke_dict["end_angle"]),
            radius=Ryoke,
            is_trigo_direction=True,
        )
        yoke_desc.append(yoke_dict)

        # Add first yoke line
        yoke_dict = dict()
        yoke_dict["begin_angle"] = 0
        yoke_dict["end_angle"] = notch_list[0]["begin_angle"]
        yoke_dict["obj"] = Arc1(
            begin=Ryoke * exp(1j * yoke_dict["begin_angle"]),
            end=Ryoke * exp(1j * yoke_dict["end_angle"]),
            radius=Ryoke,
            is_trigo_direction=True,
        )
        yoke_desc.insert(0, yoke_dict)

    if is_reversed:
        yoke_desc = yoke_desc[::-1]
        for desc in yoke_desc:
            begin_trigo = desc["begin_angle"]
            end_trigo = desc["end_angle"]
            desc["begin_angle"] = end_trigo
            desc["end_angle"] = begin_trigo
    return yoke_desc
