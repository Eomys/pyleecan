def split_half(self, is_begin=True):
    """Cut the line in half (modify the object)

    Parameters
    ----------
    self : Segment
        An Segment object
    is_begin : bool
        True to keep the part begin=>middle, False for the part middle=>end

    Returns
    -------
    """

    if is_begin:
        self.end = self.get_middle()
    else:
        self.begin = self.get_middle()
