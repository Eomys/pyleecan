from numpy import array, sum, exp, angle, min as np_min, max as np_max, argmin


def comp_point_ref(self, is_set=False):
    """Compute the point ref of the Surface

    Parameters
    ----------
    self : SurfLine
        A SurfLine object
    is_set: bool
        True to update the point_ref property

    Returns
    -------
    point_ref : complex
        the reference point of the surface
    """

    middle_array = array([line.get_middle() for line in self.get_lines()])
    point_ref = sum(middle_array) / middle_array.size

    # Use another method if the point is not is the surface
    if not self.is_inside(Z=point_ref, if_online=False):
        middle_array_abs = abs(middle_array)
        # Find "min abs" middle
        mid_id = argmin(middle_array_abs)
        Zmid = middle_array[mid_id]
        H = (np_min(middle_array_abs) + np_max(middle_array_abs)) / 2

        point_ref = (abs(Zmid) + H / 100) * exp(1j * angle(Zmid))

    if is_set:
        self.point_ref = point_ref
    return point_ref
