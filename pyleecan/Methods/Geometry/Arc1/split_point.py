from numpy import exp, angle, abs as np_abs

DELTA = 1e-9  # To remove computing noise


def split_point(self, Z1, is_begin=True):
    """Cut the Arc according to a point on the arc

    Parameters
    ----------
    self : Arc1
        An Arc1 object
    Z1 : complex
        Cutting point on the line
    is_begin : bool
        True to keep the part begin=>Z1, False for the part Z1=>end

    Returns
    -------
    """

    if not self.is_on_line(Z1):
        raise Exception("Point is not on the line")

    # Check that the center is the same
    Zc = self.get_center()

    if is_begin:
        self.end = Z1
    else:
        self.begin = Z1

    # Correct center if needed
    if abs(Zc - self.get_center()) > 1e-6:
        self.radius = -1 * self.radius
