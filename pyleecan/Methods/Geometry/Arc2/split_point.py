from numpy import exp, angle, abs as np_abs

DELTA = 1e-9  # To remove computing noise


def split_point(self, Z1, is_begin=True):
    """Cut the Arc according to a point on the arc

    Parameters
    ----------
    self : Arc2
        An Arc2 object
    Z1 : complex
        Cutting point on the line
    is_begin : bool
        True to keep the part begin=>Z1, False for the part Z1=>end

    Returns
    -------
    """

    if not self.is_on_line(Z1):
        raise Exception("Point is not on the line")

    Zc = self.get_center()

    if is_begin:
        self.angle = angle((Z1 - Zc) * exp(-1j * angle(self.begin)))
    else:
        self.angle = angle((self.get_end() - Zc) * exp(-1j * angle(Z1)))
        self.begin = Z1
