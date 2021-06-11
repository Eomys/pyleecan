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
        return Lamination.get_bore_desc(self, sym=sym, line_label=line_label)

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
        bore_dict["begin_angle"] = 2 * pi / Zs * ii - op / 2 + pi / Zs
        bore_dict["end_angle"] = 2 * pi / Zs * ii + op / 2 + pi / Zs
        bore_dict["obj"] = slot
        bore_dict["lines"] = lines
        slot_list.append(bore_dict)

    # Get the notches
    notch_list = self.get_notch_list(sym=sym)

    # Merge Slot and Notches
    merged_list = merge_notch_list(slot_list, notch_list)

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
                is_trigo_direction=True,
            )
            bore_desc.append(bore_dict)

    # Add last bore line
    if sym == 1 and abs(op - 2 * pi / Zs) > 1e-6:
        bore_dict = dict()
        bore_dict["begin_angle"] = merged_list[-1]["end_angle"]
        bore_dict["end_angle"] = merged_list[0]["begin_angle"]
        bore_dict["obj"] = Arc1(
            begin=Rbo * exp(1j * bore_dict["begin_angle"]),
            end=Rbo * exp(1j * bore_dict["end_angle"]),
            radius=Rbo,
            is_trigo_direction=True,
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
            is_trigo_direction=True,
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
            is_trigo_direction=True,
        )
        bore_desc.insert(0, bore_dict)

    # Convert the description to lines
    bore_lines = list()
    for bore in bore_desc:
        if isinstance(bore["obj"], Arc1):
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

    # Set line properties
    if prop_dict is not None:
        for line in bore_lines:
            if line.prop_dict is None:
                line.prop_dict = prop_dict
            else:
                line.prop_dict.update(prop_dict)

    return bore_desc, bore_lines
