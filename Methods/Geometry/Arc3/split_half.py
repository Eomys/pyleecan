from pyleecan.Classes.Arc1 import Arc1


def split_half(self, is_begin=True):
    """Cut the line in half (modify the object Arc3 => Arc1)

    Parameters
    ----------
    self : Arc3
        An Arc3 object
    is_begin : bool
        True to keep the part begin=>middle, False for the part middle=>end

    Returns
    -------
    """

    if is_begin:
        arc = Arc1(begin=self.begin, end=self.get_middle(), radius=self.comp_radius())
    else:
        arc = Arc1(end=self.end, begin=self.get_middle(), radius=self.comp_radius())
    # Change the object type from Arc3 => Arc1
    self.__class__ = Arc1
    self.__dict__.update(arc.__dict__)
