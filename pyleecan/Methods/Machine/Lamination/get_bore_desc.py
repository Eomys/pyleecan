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

    is_notch = self.notch and any([not notch.is_yoke for notch in self.notch])

    if not is_notch and self.bore:
        bore_lines = self.bore.get_bore_line(prop_dict=prop_dict)
        if sym == 1:
            return None, bore_lines
        else:
            # First cut Ox
            bore_lines_top = list()
            for line in bore_lines:
                top, _ = line.split_line(-1.2 * self.Rext, 1.2 * self.Rext)
                bore_lines_top.extend(top)
            if sym > 2:
                # Second cut 0Sym
                bore_lines_cut = list()
                for line in bore_lines_top:
                    top, _ = line.split_line(
                        1.2 * self.Rext * exp(1j * 2 * pi / sym), 0
                    )
                    bore_lines_cut.extend(top)
            else:  # Cutting lamination in half
                bore_lines_cut = bore_lines_top
            return None, bore_lines_cut

    bore_desc = list()
    if not is_notch and not self.bore:  # ... and (not self.bore or sym != 1):
        # No notches
        if sym == 1:
            arc1 = Arc3(begin=Rbo, end=-Rbo, is_trigo_direction=True)
            arc2 = Arc3(begin=-Rbo, end=Rbo, is_trigo_direction=True)
            bore_desc.append({"obj": arc1, "begin_angle": 0, "end_angle": pi})
            bore_desc.append({"obj": arc2, "begin_angle": 0, "end_angle": pi})
        else:
            rot = exp(1j * 2 * pi / sym)
            arc = Arc1(begin=Rbo, end=Rbo * rot, radius=Rbo, is_trigo_direction=True)
            bore_desc = [{"obj": arc, "begin_angle": 0, "end_angle": 2 * pi / sym}]

        return bore_desc, _convert_desc(bore_desc, prop_dict)

    if is_notch:  # Notches => Generate Full lines and cut (if needed)
        # Get all the notches
        notch_list = self.get_notch_list(sym=1, is_yoke=False)

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

        bore_dict["begin_angle"] = notch_list[-1]["end_angle"]
        bore_dict["end_angle"] = notch_list[0]["begin_angle"]
        bore_dict["obj"] = Arc1(
            begin=Rbo * exp(1j * bore_dict["begin_angle"]),
            end=Rbo * exp(1j * bore_dict["end_angle"]),
            radius=Rbo,
            is_trigo_direction=True,
        )
        if notch_list[0]["begin_angle"] < 0:
            # First element is a slot or notch
            bore_desc.append(bore_dict)
        else:
            # First element is a bore line
            bore_desc.insert(0, bore_dict)

        bore_lines = _convert_desc(bore_desc, prop_dict)

        # Cut the bore lines if needed
        if sym != 1:
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


def _convert_desc(bore_desc, prop_dict):
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
    return bore_lines