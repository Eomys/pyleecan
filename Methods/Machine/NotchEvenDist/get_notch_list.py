from numpy import pi


def get_notch_list(self, sym=1):
    """Returns an ordered description of the notches
    """

    notch_list = list()
    op = self.notch_shape.comp_angle_opening()
    for ii in range(self.notch_shape.Zs // sym):
        notch_dict = dict()
        notch_dict["begin_angle"] = (
            2 * pi / self.notch_shape.Zs * ii + self.alpha - op / 2
        )
        notch_dict["end_angle"] = (
            2 * pi / self.notch_shape.Zs * ii + self.alpha + op / 2
        )
        notch_dict["obj"] = self.notch_shape
        if notch_dict["begin_angle"] > 0 and notch_dict["end_angle"] < 2 * pi / sym:
            notch_list.append(notch_dict)

    return notch_list
