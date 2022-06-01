from numpy import exp, pi

from ....Classes.Arc1 import Arc1
from ....Classes.Arc3 import Arc3
from ....Functions.Geometry.merge_notch_list import merge_notch_list


def get_yoke_desc(self, sym=1, is_reversed=False, prop_dict=None):
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
    prop_dict : dict
        Property dictionary to apply on the lines
    Returns
    -------
    yoke_desc : list
        list of dictionary with key: "begin_angle", "end_angle", "obj"
    yoke_lines : list
        List of Lines to draw the yoke
    """

    Ryoke = self.get_Ryoke()
    is_notch = self.has_notch(is_bore=False)

    if not is_notch:
        # No notches
        if sym == 1:
            yoke_desc = list()
            arc = Arc3(begin=Ryoke, end=-Ryoke, is_trigo_direction=True)
            yoke_desc.append({"obj": arc, "begin_angle": 0, "end_angle": pi})
            arc = Arc3(begin=-Ryoke, end=Ryoke, is_trigo_direction=True)
            yoke_desc.append({"obj": arc, "begin_angle": 0, "end_angle": pi})
        else:
            rot = exp(1j * 2 * pi / sym)
            arc = Arc1(
                begin=Ryoke, end=Ryoke * rot, radius=Ryoke, is_trigo_direction=True
            )
            yoke_desc = [{"obj": arc, "begin_angle": 0, "end_angle": 2 * pi / sym}]
    else:
        # Get the notches
        notch_list = self.get_notch_list(sym=1, is_bore=False)

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

    # Convert the description to lines
    yoke_lines = list()
    for yoke in yoke_desc:
        if isinstance(yoke["obj"], (Arc1, Arc3)):
            yoke_lines.append(yoke["obj"])
        elif "lines" in yoke:  # Duplicated slot
            for line in yoke["lines"]:
                yoke_lines.append(line.copy())
                yoke_lines[-1].rotate((yoke["begin_angle"] + yoke["end_angle"]) / 2)
        else:  # Notches
            self.is_internal = not self.is_internal  # To draw slot on yoke
            lines = yoke["obj"].build_geometry()
            self.is_internal = not self.is_internal  # To draw slot on yoke
            for line in lines:
                line.rotate((yoke["begin_angle"] + yoke["end_angle"]) / 2)
            yoke_lines.extend(lines)

    # Cut lines if sym and Notches
    if sym != 1 and self.notch not in [None, list()]:
        # First cut Ox
        first_cut = list()
        for line in yoke_lines:
            top, _ = line.split_line(-1.2 * self.Rext, 1.2 * self.Rext)
            first_cut.extend(top)
        if sym > 2:
            # Second cut 0Sym
            yoke_lines = list()
            for line in first_cut:
                top, _ = line.split_line(1.2 * self.Rext * exp(1j * 2 * pi / sym), 0)
                yoke_lines.extend(top)
        else:  # Cutting lamination in half
            yoke_lines = first_cut

    # Reverse the lines
    if is_reversed:
        yoke_lines = yoke_lines[::-1]
        for line in yoke_lines:
            line.reverse()

    # Set line properties
    if prop_dict is not None:
        for line in yoke_lines:
            if line.prop_dict is None:
                line.prop_dict = prop_dict
            else:
                line.prop_dict.update(prop_dict)

    return yoke_desc, yoke_lines
