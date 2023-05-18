from numpy import pi

from ....Classes.Arc2 import Arc2


def split_half(self, is_begin=True):
    """Cut the line in half (modify the object Arc3 => Arc2)

    Parameters
    ----------
    self : Arc3
        An Arc3 object
    is_begin : bool
        True to keep the part begin=>middle, False for the part middle=>end

    Returns
    -------
    """

    if self.is_trigo_direction:
        sign = 1
    else:
        sign = -1

    if is_begin:
        arc = Arc2(begin=self.begin, center=self.get_center(), angle=sign * pi / 2)
    else:
        arc = Arc2(
            begin=self.get_middle(), center=self.get_center(), angle=sign * pi / 2
        )
    # Change the object type from Arc3 => Arc2
    self.__class__ = Arc2
    self.__dict__.update(arc.__dict__)
