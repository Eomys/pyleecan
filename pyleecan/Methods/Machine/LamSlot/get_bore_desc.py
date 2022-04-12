from ....Functions.Geometry.merge_notch_list import merge_notch_list
from ....Classes.Arc1 import Arc1
from numpy import exp, pi
from ....Classes.Lamination import Lamination


def get_bore_desc(self, sym=1, prop_dict=None):
    """This method returns an ordered description of the elements
    that defines the bore radius of the lamination

    Parameters
    ----------
    self : LamSlot
        A LamSlot object
    prop_dict : dict
        Property dictionary to apply on the lines

    Returns
    -------
    bore_desc : list
        list of dictionary with key: "begin_angle", "end_angle", "obj"
    bore_line : list
        list of lines to draw the bore radius
    """

    if self.slot is None:  # No slot
        return Lamination.get_bore_desc(self, sym=sym, prop_dict=prop_dict)

    Rbo = self.get_Rbo()
    slot_list = list()
    slot = self.slot
    Zs = self.slot.Zs
    op = slot.comp_angle_opening()
    # To avoid calling build_geometry for all the slot
    lines = slot.build_geometry()
    # First add all the slots
    for ii in range(Zs // sym):
        bore_dict = dict()
        bore_dict["begin_angle"] = (2 * pi / Zs * ii - op / 2 + pi / Zs) % (2 * pi)
        bore_dict["end_angle"] = (2 * pi / Zs * ii + op / 2 + pi / Zs) % (2 * pi)
        bore_dict["obj"] = slot
        bore_dict["lines"] = lines
        slot_list.append(bore_dict)

    # Get the notches and set range for 0 to 2pi
    notch_list = self.get_notch_list(sym=sym)
    for notch in notch_list:
        notch["begin_angle"] = notch["begin_angle"] % (2 * pi)
        notch["end_angle"] = notch["end_angle"] % (2 * pi)

    # sort lists in the range from 0 to 2pi for later merge
    slot_list = sorted(slot_list, key=lambda k: k["begin_angle"] % (2 * pi))
    notch_list = sorted(notch_list, key=lambda k: k["begin_angle"] % (2 * pi))

    # Merge Slot and Notches
    merged_list = merge_notch_list(slot_list, notch_list)

    # move line that crosses x axis to first position otherwise split will not work
    if merged_list[-1]["begin_angle"] > merged_list[-1]["end_angle"]:
        merged_list.insert(0, merged_list.pop(-1))
        merged_list[0]["begin_angle"] = merged_list[0]["begin_angle"] - 2 * pi

    # Add all the bore lines
    bore_desc = list()
    for ii, desc in enumerate(merged_list):
        bore_desc.append(desc)
        if ii != len(merged_list) - 1 and abs(op - 2 * pi / Zs) > 1e-6:
            bore_dict = dict()
            bore_dict["begin_angle"] = merged_list[ii]["end_angle"]
            bore_dict["end_angle"] = merged_list[ii + 1]["begin_angle"]
            bore_dict["obj"] = Arc1(
                begin=Rbo * exp(1j * bore_dict["begin_angle"]),
                end=Rbo * exp(1j * bore_dict["end_angle"]),
                radius=Rbo,
            )
            bore_desc.append(bore_dict)

    # Add last bore line
    if sym != 1 and len(notch_list) > 0:
        # Notch and symetry => Generate full and cut
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
                top, _ = line.split_line(1.2 * self.Rext * exp(1j * 2 * pi / sym), 0)
                bore_lines.extend(top)
        else:  # Cutting lamination in half
            bore_lines = first_cut
        return bore_desc, bore_lines
    elif sym == 1 and abs(op - 2 * pi / Zs) > 1e-6:
        bore_dict = dict()
        bore_dict["begin_angle"] = merged_list[-1]["end_angle"]
        bore_dict["end_angle"] = merged_list[0]["begin_angle"]
        bore_dict["obj"] = Arc1(
            begin=Rbo * exp(1j * bore_dict["begin_angle"]),
            end=Rbo * exp(1j * bore_dict["end_angle"]),
            radius=Rbo,
        )
        if merged_list[0]["begin_angle"] < 0:
            # First element is an slot or notch
            bore_desc.append(bore_dict)
        else:
            # First element is a bore line
            bore_desc.insert(0, bore_dict)
    elif sym != 1 and abs(op - 2 * pi / Zs) > 1e-6:  # With symmetry
        # Add last bore line
        bore_dict = dict()
        bore_dict["begin_angle"] = merged_list[-1]["end_angle"]
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
        bore_dict["end_angle"] = merged_list[0]["begin_angle"]
        bore_dict["obj"] = Arc1(
            begin=Rbo * exp(1j * bore_dict["begin_angle"]),
            end=Rbo * exp(1j * bore_dict["end_angle"]),
            radius=Rbo,
        )
        bore_desc.insert(0, bore_dict)

    # Convert the description to lines
    bore_lines = list()
    for bore in bore_desc:
        if isinstance(bore["obj"], Arc1):
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
            bore_lines.extend(bore["obj"])

    return bore_desc, bore_lines
