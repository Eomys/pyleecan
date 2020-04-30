def split_half(self, is_begin=True):
    """Cut the line in half (modify the object)

    Parameters
    ----------
    self : Arc2
        An Arc2 object
    is_begin : bool
        True to keep the part begin=>middle, False for the part middle=>end

    Returns
    -------
    """

    if not is_begin:
        self.begin = self.get_middle()
    self.angle = self.angle / 2
