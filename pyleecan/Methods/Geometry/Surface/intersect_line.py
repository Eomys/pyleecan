def intersect_line(self, Z1, Z2):
    """Return all the intersection of a line with the surfaces

    Parameters
    ----------
    self : Surface
        A Surface object
    Z1 : complex
        First point to define the intersecting line
    Z2 : complex
        Second point to define the intersecting line

    Returns
    -------
    Z_list : [complex]
        List of intersection between the line and the surface
    """

    Z_list = list()

    for line in self.get_lines():
        Z_list.extend(line.intersect_line(Z1, Z2))

    return Z_list
