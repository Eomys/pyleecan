from numpy import pi


def split_half(self, is_begin=True):
    """Cut the line in half (modify the object)

    Parameters
    ----------
    self : Arc1
        An Arc1 object
    is_begin : bool
        True to keep the part begin=>middle, False for the part middle=>end

    Returns
    -------
    """

    # Check that the center is the same
    Zc = self.get_center()

    if is_begin:
        self.end = self.get_middle()
    else:
        self.begin = self.get_middle()

    # Correct center if needed
    if abs(Zc - self.get_center()) > 1e-6:
        self.radius = -1 * self.radius
