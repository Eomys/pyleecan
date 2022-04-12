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
        ang_rot = ang * ii + self.alpha
        # find intersection points of lines with bore
        inter1, inter2 = list(), list()
        for line in bore_lines:
            line = line.copy()
            line.rotate(-ang_rot)
            Zi1 = line.intersect_line(line1.get_begin(), line1.get_end())
            Zi2 = line.intersect_line(line2.get_begin(), line2.get_end())
            inter1.extend([z for z in Zi1 if z.real > 0])
            inter2.extend([z for z in Zi2 if z.real > 0])

        if len(inter1) != 1 or len(inter2) != 1:
            raise ValueError("Error placing Notch on Bore")  # TODO: proper err.

        # translate notch
        dZ1 = inter1[0] - line1.end
        dZ2 = inter2[0] - line2.end
        dZ = dZ1 if abs(dZ1) > abs(dZ2) else dZ2

        _notch = list()
        for line in notch:
            line = line.copy()
            line.translate(dZ)
            line.rotate(ang_rot)
            _notch.append(line)

        # add line to complete notch
        if abs(dZ1) > abs(dZ2):
            _notch.append(
                Segment(begin=_notch[-1].get_end(), end=inter2[0] * exp(1j * ang_rot))
            )
        elif abs(dZ1) < abs(dZ2):
            _notch.insert(
                0,
                Segment(begin=inter1[0] * exp(1j * ang_rot), end=_notch[0].get_begin()),
            )

        # add notch to list
        notch_dict = dict()
        notch_dict["begin_angle"] = angle(_notch[0].get_begin())
        notch_dict["end_angle"] = angle(_notch[-1].get_end())
        notch_dict["obj"] = _notch
        notch_list.append(notch_dict)

    return notch_list
