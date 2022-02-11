def build_geometry(self):
    """Compute the curve (Line) needed to plot the object.
    The ending point of a curve is the starting point of the next curve
    in the list

    Parameters
    ----------
    self : SlotW11
        A SlotW11 object

    Returns
    -------
    curve_list: list
        A list of 7 Segment and 2 Arc1

    """

    line_list = self._comp_line_list()
    # Last line is closing Arc
    return [line for line in line_list[:-1] if line is not None]
