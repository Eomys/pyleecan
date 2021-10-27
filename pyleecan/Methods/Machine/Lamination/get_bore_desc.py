from ....Functions.Geometry.merge_notch_list import merge_notch_list
from ....Classes.Arc1 import Arc1
from ....Classes.Arc3 import Arc3
from numpy import exp, pi


def get_bore_desc(self, sym=1, prop_dict=None):
    """This method returns an ordered description of the elements
    that defines the bore radius of the lamination

    Parameters
    ----------
    self : Lamination
        A Lamination object
    prop_dict : dict
        Property dictionary to apply on the lines


    Returns
    -------
    bore_desc : list
        list of dictionary with key: "begin_angle", "end_angle", "obj"
    bore_line : list
        list of line to draw the bore radius

    """

    Rbo = self.get_Rbo()

    if self.notch is None:
        self.notch = list()

    if self.bore is not None and self.notch in [None, list()] and sym == 1:
        return None, self.bore.get_bore_line(prop_dict=prop_dict)
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
    else:  # Notches => Generate Full lines and cut (if needed)
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

    # Cut lines if sym and Notches
    if sym != 1 and self.notch not in [None, list()]:
        # First cut Ox
        first_cut = list()
        for line in bore_lines:
            top, _ = line.split_line(-1.2 * self.Rext, 1.2 * self.Rext)
            first_cut.extend(top)
        if sym > 2:
            # Second cut 0Sym
            bore_lines = list()
            for line in first_cut:
                top, _ = line.split_line(1.2 * self.Rext * exp(1j * 2 * pi / sym), 0)
                bore_lines.extend(top)
        else:  # Cutting lamination in half
            bore_lines = first_cut

    # Set line properties
    if prop_dict is not None:
        for line in bore_lines:
            if line.prop_dict is None:
                line.prop_dict = prop_dict
            else:
                line.prop_dict.update(prop_dict)

    return bore_desc, bore_lines
