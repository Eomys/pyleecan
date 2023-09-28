from numpy import exp, pi, angle

from ....Classes.Arc1 import Arc1
from ....Classes.Arc3 import Arc3
from ....Functions.Geometry.merge_notch_list import merge_notch_list


def build_radius_desc(self, is_bore, sym=1):
    """This method returns an ordered description of the slot/notch
    that defines the bore/yoke radius of the lamination
    (Bore/Yoke shape not taken into account by this method, cf build_radius_lines)

    Parameters
    ----------
    self : Lamination
        A Lamination object
    is_bore : bool
        True generate description of bore, else yoke
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)

    Returns
    -------
    radius_desc : list
        trigo ordered list of dictionary with key:
            "begin_angle" : float [rad]
            "end_angle" : float [rad]
            "obj" : Slot or None
            "lines : lines corresponding to the radius part
            "label" : Radius/Notch/Slot
    """

    # For readibility
    is_notch = self.has_notch(is_bore=is_bore)
    is_slot = self.has_slot(is_bore=is_bore)
    if is_bore:
        R = self.get_Rbo()
    else:
        R = self.get_Ryoke()

    radius_desc = list()
    if not is_notch and not is_slot:
        radius_lines = list()
        if sym == 1:  # Two arcs to avoid angle > 180 deg
            arc1 = Arc3(begin=R, end=-R, is_trigo_direction=True)
            arc2 = Arc3(begin=-R, end=R, is_trigo_direction=True)
            end_angle = 0
            radius_lines.append(arc1)
            radius_lines.append(arc2)
        else:
            end_angle = 2 * pi / sym
            rot = exp(1j * end_angle)
            arc = Arc1(begin=R, end=R * rot, radius=R, is_trigo_direction=True)
            radius_lines.append(arc)
        radius_desc.append(
            {
                "begin_angle": 0,
                "end_angle": end_angle,
                "obj": None,
                "lines": radius_lines,
                "label": "Radius",
            }
        )
        return radius_desc

    # Notch/Slot case
    if is_notch:
        # Get all the notch on the selected radius
        notch_list = [
            notch for notch in self.notch if notch.notch_shape.is_bore == is_bore
        ]
        # Get description of first notch
        notch_desc_list = notch_list[0].get_notch_desc_list(sym=sym)
        # If more than one notch, we need to merge and order the description
        for ii in range(len(notch_list) - 1):
            notch_desc_list = merge_notch_list(
                notch_desc_list, notch_list[ii + 1].get_notch_desc_list(sym=sym)
            )
    else:
        notch_desc_list = list()
    # Get slot description
    if is_slot:
        slot_desc_list = self.get_slot_desc_list(sym=sym, is_bore=is_bore)
    else:
        slot_desc_list = list()
    all_desc_list = merge_notch_list(notch_desc_list, slot_desc_list)

    # Add the radius between each notch/slot
    for ii in range(len(all_desc_list) - 1):
        radius_desc.append(all_desc_list[ii])
        begin = all_desc_list[ii]["end_angle"]
        end = all_desc_list[ii + 1]["begin_angle"]
        if begin != end:  # begin = end for "full slot / no tooth"
            radius_desc.append(
                {
                    "begin_angle": begin,
                    "end_angle": end,
                    "obj": None,
                    "lines": [
                        Arc1(
                            begin=R * exp(1j * begin),
                            end=R * exp(1j * end),
                            radius=R,
                            is_trigo_direction=True,
                        )
                    ],
                    "label": "Radius",
                }
            )
    # Add last notch/slot
    radius_desc.append(all_desc_list[-1])
    # Add first and last radius line if required
    if all_desc_list[0]["begin_angle"] > 0:
        if sym == 1 and all_desc_list[-1]["end_angle"] > 2 * pi:
            # Alpha >0, last notch cross Ox
            begin = all_desc_list[-1]["end_angle"] - 2 * pi
            radius_desc.insert(
                0,
                {
                    "begin_angle": begin,
                    "end_angle": all_desc_list[0]["begin_angle"],
                    "obj": None,
                    "lines": [
                        Arc1(
                            begin=R * exp(1j * begin),
                            end=R * exp(1j * all_desc_list[0]["begin_angle"]),
                            radius=R,
                            is_trigo_direction=True,
                        )
                    ],
                    "label": "Radius",
                },
            )
        else:  # Add radius from Ox to first notch
            radius_desc.insert(
                0,
                {
                    "begin_angle": 0,
                    "end_angle": all_desc_list[0]["begin_angle"],
                    "obj": None,
                    "lines": [
                        Arc1(
                            begin=R * exp(1j * 0),
                            end=R * exp(1j * all_desc_list[0]["begin_angle"]),
                            radius=R,
                            is_trigo_direction=True,
                        )
                    ],
                    "label": "Radius",
                },
            )
    if all_desc_list[-1]["end_angle"] < 2 * pi / sym:
        if all_desc_list[0]["begin_angle"] < 0 and sym == 1:
            # Full lamination with slot/notch on Ox
            radius_desc.append(
                {
                    "begin_angle": all_desc_list[-1]["end_angle"],
                    "end_angle": 2 * pi + all_desc_list[0]["begin_angle"],
                    "obj": None,
                    "lines": [
                        Arc1(
                            begin=R * exp(1j * all_desc_list[-1]["end_angle"]),
                            end=R
                            * exp(1j * (2 * pi + all_desc_list[0]["begin_angle"])),
                            radius=R,
                            is_trigo_direction=True,
                        )
                    ],
                    "label": "Radius",
                }
            )
        else:
            radius_desc.append(
                {
                    "begin_angle": all_desc_list[-1]["end_angle"],
                    "end_angle": 2 * pi / sym,
                    "obj": None,
                    "lines": [
                        Arc1(
                            begin=R * exp(1j * all_desc_list[-1]["end_angle"]),
                            end=R * exp(1j * 2 * pi / sym),
                            radius=R,
                            is_trigo_direction=True,
                        )
                    ],
                    "label": "Radius",
                }
            )
    return radius_desc
