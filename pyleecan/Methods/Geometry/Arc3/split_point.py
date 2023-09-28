from ....Classes.Arc1 import Arc1
from numpy import pi, abs as np_abs

DELTA = 1e-9  # To remove computing noise


def split_point(self, Z1, is_begin=True):
    """Cut the Arc according to a point on the arc

    Parameters
    ----------
    self : Arc3
        An Arc3 object
    Z1 : complex
        Cutting point on the line
    is_begin : bool
        True to keep the part begin=>Z1, False for the part Z1=>end

    Returns
    -------
    """

    # Check if the point is on the circle
    Zc = self.get_center()
    R = self.comp_radius()
    if abs(np_abs(Z1 - Zc) - R) > 1e-6:
        raise Exception("Point is not on the line")

    if is_begin:
        arc = Arc1(
            begin=self.begin,
            end=Z1,
            radius=R,
            is_trigo_direction=self.is_trigo_direction,
        )
    else:
        arc = Arc1(
            begin=Z1,
            end=self.end,
            radius=R,
            is_trigo_direction=self.is_trigo_direction,
        )
    # Correct radius sign if needed
    if arc.get_angle() > pi:
        arc.radius *= -1

    # Change the object type from Arc3 => Arc1
    self.__class__ = Arc1
    self.__dict__.update(arc.__dict__)
