from ....Functions.Geometry.inter_line_circle import inter_line_circle


def intersect_obj(self, other, is_on_line=True):
    """Find the intersection points between this line
    and another line object

    Parameters
    ----------
    self : Segment
        A Segment object
    other : Line
        The other line object to intersect
    is_on_line : bool
        True to return only points that are on both Line objects

    Returns
    -------
    Z_list: list
        Complex coordinates of the intersection (if any)
    """

    if other.is_arc():
        inter_list = inter_line_circle(
            Z1=self.begin,
            Z2=self.end,
            R=abs(other.comp_radius()),
            Zc=other.get_center(),
        )
    else:
        inter_list = self.intersect_line(Z1=other.get_begin(), Z2=other.get_end())

    if not is_on_line:
        return inter_list

    # Keep only points on both lines
    Z_list = list()
    for Z in inter_list:
        if self.is_on_line(Z) and other.is_on_line(Z):
            Z_list.append(Z)

    return Z_list
