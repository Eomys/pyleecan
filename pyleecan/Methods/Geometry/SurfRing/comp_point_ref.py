from numpy import array, sum


def comp_point_ref(self, is_set=False):
    """Compute the point ref of the Surface

    Parameters
    ----------
    self : SurfRing
        A SurfRing object
    is_set: bool
        True to update the point_ref property

    Returns
    -------
    point_ref : complex
        the reference point of the surface
    """

    point_list = list()
    out_lines = self.out_surf.get_lines()
    in_lines = self.in_surf.get_lines()
    # Compute the ref point as the barycenter of half the lines
    for line in out_lines[: len(out_lines) / 2]:
        point_list.append(line.get_middle())
    for line in in_lines[: len(in_lines) / 2]:
        point_list.append(line.get_middle())
    point_ref = sum(array(point_list)) / len(point_list)

    if is_set:
        self.point_ref = point_ref
    return point_ref
