def get_hole_list(self):
    """Return the list of all the holes (North and South)

    Parameters
    ----------
    self : LamHoleNS
        A LamHoleNS object

    Returns
    -------
    hole_list : [Hole]
        List of all the holes (North and South)
    """
    hole_list = list()
    hole_list.extend(self.hole_north)
    hole_list.extend(self.hole_south)

    return hole_list
