from numpy import pi, exp, angle

from ....Classes.Segment import Segment


def get_notch_desc_list(self, sym=1):
    """Returns an ordered description of the notches

    Parameters
    ----------
    self : NotchEvenDist
        A NotchEvenDist object
    sym: int
        Number of symmetry

    Returns
    -------
    notch_desc : list
        trigo ordered list of dictionary with key:
            "begin_angle" : float [rad]
            "end_angle" : float [rad]
            "obj" : Slot (for notch_shape) / None for Radius
            "lines : lines corresponding to the radius part
            "label" : Radius/Notch/Slot
    """

    notch_list = list()
    op = self.notch_shape.comp_angle_opening()
    Zs = self.notch_shape.Zs
    # No need to rotate more than a notch pitch
    alpha = self.alpha % (2 * pi / Zs)

    for ii in range(Zs // sym):
        notch_dict = dict()
        notch_dict["begin_angle"] = 2 * pi / Zs * ii + alpha - op / 2
        notch_dict["end_angle"] = 2 * pi / Zs * ii + alpha + op / 2
        notch_dict["obj"] = self.notch_shape
        notch_dict["lines"] = self.notch_shape.build_geometry()
        # Apply rotation
        for line in notch_dict["lines"]:
            line.rotate((notch_dict["begin_angle"] + notch_dict["end_angle"]) / 2)
        notch_dict["label"] = "Notch"
        notch_list.append(notch_dict)

    # If first notch is on Ox, then sym+1 notch are required (half on both yoke side)
    if notch_list[0]["begin_angle"] < 0 and sym != 1:
        notch_dict = dict()
        notch_dict["begin_angle"] = 2 * pi / Zs * (ii + 1) + alpha - op / 2
        notch_dict["end_angle"] = 2 * pi / Zs * (ii + 1) + alpha + op / 2
        notch_dict["obj"] = self.notch_shape
        notch_dict["lines"] = self.notch_shape.build_geometry()
        # Apply rotation
        for line in notch_dict["lines"]:
            line.rotate((notch_dict["begin_angle"] + notch_dict["end_angle"]) / 2)
        notch_dict["label"] = "Notch"
        notch_list.append(notch_dict)

    return notch_list
