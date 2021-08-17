from ....Functions.Geometry.merge_notch_list import merge_notch_list
from ....Classes.Arc1 import Arc1
from ....Classes.Arc3 import Arc3
from numpy import exp, pi


def get_bore_desc(self, sym=1, line_label=None):
    """This method returns an ordered description of the elements
    that defines the bore radius of the lamination

    Parameters
    ----------
    self : Lamination
        A Lamination object
    line_label : str
        Label to apply on the lines

    Returns
    -------
    bore_desc : list
        list of dictionary with key: "begin_angle", "end_angle", "obj"
    bore_line : list
        list of line to draw the bore radius

    """

    Rbo = self.get_Rbo()

    if self.bore is not None and self.notch in [None, list()] and sym == 1:
        return None, self.bore.get_bore_line(label=line_label)
    elif self.notch is None or len(self.notch) == 0:
        # No notches
        if sym == 1:
            bore_desc = list()
            bore_desc.append(
                {
                    "obj": Arc3(begin=Rbo, end=-Rbo, is_trigo_direction=True),
                    "begin_angle": 0,
                    "end_angle": pi,
                }
            )
            bore_desc.append(
                {
                    "obj": Arc3(begin=-Rbo, end=Rbo, is_trigo_direction=True),
                    "begin_angle": 0,
                    "end_angle": pi,
                }
            )
        else:
            bore_desc = [
                {
                    "obj": Arc1(
                        begin=Rbo,
                        end=Rbo * exp(1j * 2 * pi / sym),
                        radius=Rbo,
                        is_trigo_direction=True,
                    ),
                    "begin_angle": 0,
                    "end_angle": 2 * pi / sym,
                }
            ]
    else:
        # Get the notches
        notch_list = self.get_notch_list(sym=sym)

        # Add all the bore lines
        bore_desc = list()
        for ii, desc in enumerate(notch_list):
            bore_desc.append(desc)
            if ii != len(notch_list) - 1:
                bore_dict = dict()
                bore_dict["begin_angle"] = notch_list[ii]["end_angle"]
                bore_dict["end_angle"] = notch_list[ii + 1]["begin_angle"]
                bore_dict["obj"] = Arc1(
                    begin=Rbo * exp(1j * bore_dict["begin_angle"]),
                    end=Rbo * exp(1j * bore_dict["end_angle"]),
                    radius=Rbo,
                    is_trigo_direction=True,
                )
                bore_desc.append(bore_dict)

        # Add last bore line
        if sym == 1:
            bore_dict = dict()
            bore_dict["begin_angle"] = notch_list[-1]["end_angle"]
            bore_dict["end_angle"] = notch_list[0]["begin_angle"]
            bore_dict["obj"] = Arc1(
                begin=Rbo * exp(1j * bore_dict["begin_angle"]),
                end=Rbo * exp(1j * bore_dict["end_angle"]),
                radius=Rbo,
                is_trigo_direction=True,
            )
            if notch_list[0]["begin_angle"] < 0:
                # First element is an slot or notch
                bore_desc.append(bore_dict)
            else:
                # First element is a bore line
                bore_desc.insert(0, bore_dict)
        elif sym != 1:  # With symmetry
            # Add last bore line
            bore_dict = dict()
            bore_dict["begin_angle"] = notch_list[-1]["end_angle"]
            bore_dict["end_angle"] = 2 * pi / sym
            bore_dict["obj"] = Arc1(
                begin=Rbo * exp(1j * bore_dict["begin_angle"]),
                end=Rbo * exp(1j * bore_dict["end_angle"]),
                radius=Rbo,
                is_trigo_direction=True,
            )
            bore_desc.append(bore_dict)

            # Add first bore line
            bore_dict = dict()
            bore_dict["begin_angle"] = 0
            bore_dict["end_angle"] = notch_list[0]["begin_angle"]
            bore_dict["obj"] = Arc1(
                begin=Rbo * exp(1j * bore_dict["begin_angle"]),
                end=Rbo * exp(1j * bore_dict["end_angle"]),
                radius=Rbo,
                is_trigo_direction=True,
            )
            bore_desc.insert(0, bore_dict)

    # Convert the description to lines
    bore_lines = list()
    for bore in bore_desc:
        if isinstance(bore["obj"], (Arc1, Arc3)):
            bore_lines.append(bore["obj"])
        elif "lines" in bore:  # Duplicated slot
            for line in bore["lines"]:
                bore_lines.append(line.copy())
                bore_lines[-1].rotate((bore["begin_angle"] + bore["end_angle"]) / 2)
        else:  # Notches
            lines = bore["obj"].build_geometry()
            for line in lines:
                bore_lines.append(line.copy())
                bore_lines[-1].rotate((bore["begin_angle"] + bore["end_angle"]) / 2)

    # Set line label
    if line_label is not None:
        for line in bore_lines:
            line.label = line_label

    return bore_desc, bore_lines
