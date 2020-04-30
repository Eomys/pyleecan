from numpy import array, sum


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

    point_list = list()
    for line in self.get_lines():
        point_list.append(line.get_middle())
    point_ref = sum(array(point_list)) / len(point_list)

    if is_set:
        self.point_ref = point_ref
    return point_ref
