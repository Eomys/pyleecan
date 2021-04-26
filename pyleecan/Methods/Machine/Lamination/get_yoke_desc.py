from numpy import exp, pi

from ....Classes.Arc1 import Arc1
from ....Classes.Arc3 import Arc3
from ....Functions.Geometry.merge_notch_list import merge_notch_list


def get_yoke_desc(self, sym=1, is_reversed=False, line_label=None):
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
    line_label : str
        Label to apply on the lines
    Returns
    -------
    yoke_desc : list
        list of dictionary with key: "begin_angle", "end_angle", "obj"
    yoke_lines : list
        List of Lines to draw the yoke
    """

    Ryoke = self.get_Ryoke()

    if self.yoke_notch is None or len(self.yoke_notch) == 0:
        # No notches
        if sym == 1:
            yoke_desc = list()
            yoke_desc.append(
                {
                    "obj": Arc3(begin=Ryoke, end=-Ryoke, is_trigo_direction=True),
                    "begin_angle": 0,
                    "end_angle": pi,
                }
            )
            yoke_desc.append(
                {
                    "obj": Arc3(begin=-Ryoke, end=Ryoke, is_trigo_direction=True),
                    "begin_angle": 0,
                    "end_angle": pi,
                }
            )
        else:
            yoke_desc = [
                {
                    "obj": Arc1(
                        begin=Ryoke,
                        end=Ryoke * exp(1j * 2 * pi / sym),
                        radius=Ryoke,
                        is_trigo_direction=True,
                    ),
                    "begin_angle": 0,
                    "end_angle": 2 * pi / sym,
                }
            ]
    else:
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
        if sym == 1 and len(notch_list) > 0:
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

    # Reverse the lines
    if is_reversed:
        yoke_lines = yoke_lines[::-1]
        for line in yoke_lines:
            line.reverse()

    # Set line label
    if line_label is not None:
        for line in yoke_lines:
            line.label = line_label

    return yoke_desc, yoke_lines
