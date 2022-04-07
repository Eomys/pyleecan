from numpy import pi, exp, angle

from ....Classes.Segment import Segment


def get_notch_list(self, sym=1):
    """Returns an ordered description of the notches

    Parameters
    ----------
    self : NotchEvenDist
        A NotchEvenDist object
    sym: int
        Number of symmetry
    is_yoke : bool
        True if the notch is on the Yoke

    Returns
    -------
    notch_list : list
        list of dictionary with key: "begin_angle", "end_angle", "obj"
    """

    notch_list = list()
    op = self.notch_shape.comp_angle_opening()

    notch = self.notch_shape.build_geometry()
    mid = (notch[0].get_begin() + notch[-1].get_end()) / 2
    line1 = Segment(begin=notch[0].get_begin() - mid, end=notch[0].get_begin())
    line2 = Segment(begin=notch[-1].get_end() - mid, end=notch[-1].get_end())

    bore_lines = self.parent.get_bore_line()
    ang = 2 * pi / self.notch_shape.Zs

    for ii in range(self.notch_shape.Zs // sym):
        rot = exp(1j * ang * ii + +self.alpha)
        # find intersection of lines with bore
        inter1 = list()
        for line in bore_lines:
            inter1.extend(
                line.intersect_line(line1.get_begin() * rot, line1.get_end() * rot)
            )

        inter2 = list()
        for line in bore_lines:
            inter2.extend(
                line.intersect_line(line2.get_begin() * rot, line2.get_end() * rot)
            )

        if len(inter1) != 1 or len(inter2) != 1:
            raise ValueError("Error placing Notch on Bore")  # TODO: proper err.

        # translate notch
        dZ1 = line1.end - inter1[0]
        dZ2 = line2.end - inter2[0]
        dZ = dZ1 if abs(dZ1) < abs(dZ2) else dZ2

        _notch = list()
        for line in notch:
            _notch.append(line.copy().rotate(ang * ii + self.alpha).translate(dZ))

        # add line to complete notch
        if abs(dZ1) < abs(dZ2):
            _notch.append(Segment(begin=_notch[-1].get_end(), end=inter2[0]))

        # add notch to list
        notch_dict = dict()
        notch_dict["begin_angle"] = angle(_notch[0].get_begin())
        notch_dict["end_angle"] = angle(_notch[-1].get_end())
        notch_dict["obj"] = _notch
        notch_list.append(notch_dict)

    return notch_list
