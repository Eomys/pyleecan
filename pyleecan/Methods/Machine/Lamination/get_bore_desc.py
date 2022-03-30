from numpy import exp, pi

from ....Classes.Arc1 import Arc1
from ....Classes.Arc3 import Arc3


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
        list of lines to draw the bore radius
    """

    Rbo = self.get_Rbo()
    is_notch = not self.notch in [None, list()]

    if not is_notch and self.bore and sym == 1:
        return None, self.bore.get_bore_line(prop_dict=prop_dict)

    bore_desc = list()
    if not is_notch:  # ... and (not self.bore or sym != 1):
        # No notches
        if sym == 1:
            arc1 = Arc3(begin=Rbo, end=-Rbo)
            arc2 = Arc3(begin=-Rbo, end=Rbo)
            bore_desc.append({"obj": arc1, "begin_angle": 0, "end_angle": pi})
            bore_desc.append({"obj": arc2, "begin_angle": 0, "end_angle": pi})
        else:
            arc = Arc1(begin=Rbo, end=Rbo * exp(1j * 2 * pi / sym), radius=Rbo)
            bore_desc = [{"obj": arc, "begin_angle": 0, "end_angle": 2 * pi / sym}]
    else:  # Notches => Generate Full lines and cut (if needed)
        # Get the notches
        notch_list = self.get_notch_list(sym=sym)

        # Add all the bore lines
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
                )
                bore_desc.append(bore_dict)

        # Add last bore line
        if sym != 1 and len(notch_list) > 0:
            # Notche and symetry => Generate full and cut
            bore_desc, bore_lines = self.get_bore_desc(sym=1, prop_dict=prop_dict)
            # First cut Ox
            first_cut = list()
            for line in bore_lines:
                top, _ = line.split_line(-1.2 * self.Rext, 1.2 * self.Rext)
                first_cut.extend(top)
            if sym > 2:
                # Second cut 0Sym
                bore_lines = list()
                for line in first_cut:
                    top, _ = line.split_line(
                        1.2 * self.Rext * exp(1j * 2 * pi / sym), 0
                    )
                    bore_lines.extend(top)
            else:  # Cutting lamination in half
                bore_lines = first_cut
            return bore_desc, bore_lines
        elif sym == 1:
            bore_dict["begin_angle"] = notch_list[-1]["end_angle"]
            bore_dict["end_angle"] = notch_list[0]["begin_angle"]
            bore_dict["obj"] = Arc1(
                begin=Rbo * exp(1j * bore_dict["begin_angle"]),
                end=Rbo * exp(1j * bore_dict["end_angle"]),
                radius=Rbo,
            )
            if notch_list[0]["begin_angle"] < 0:
                # First element is a slot or notch
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
            )
            bore_desc.insert(0, bore_dict)

    # Convert the description to lines
    bore_lines = list()
    for bore in bore_desc:
        if isinstance(bore["obj"], (Arc1, Arc3)):
            # Set bore line properties
            if bore["obj"].prop_dict is None:
                bore["obj"].prop_dict = prop_dict
            else:
                bore["obj"].prop_dict.update(prop_dict)
            bore_lines.append(bore["obj"])
        elif "lines" in bore:  # Duplicated slot
            for line in bore["lines"]:
                bore_lines.append(line.copy())
                bore_lines[-1].rotate((bore["begin_angle"] + bore["end_angle"]) / 2)
        else:  # Notches
            lines = bore["obj"].build_geometry()
            for line in lines:
                line.rotate((bore["begin_angle"] + bore["end_angle"]) / 2)
            bore_lines.extend(lines)

    return bore_desc, bore_lines
