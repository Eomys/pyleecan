def comp_point_ref(self, is_set=False):
    """Compute the point ref of the Surface

    Parameters
    ----------
    self : PolarArc
        A PolarArc object
    is_set: bool
        True to update the point_ref property

    Returns
    -------
    point_ref : complex
        the reference point of the surface
    """

    point_ref = self.point_ref
    if is_set:
        self.point_ref = point_ref
    return point_ref
