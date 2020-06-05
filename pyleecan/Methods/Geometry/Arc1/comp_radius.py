# -*- coding: utf-8 -*-


def comp_radius(self):
    """Compute the Radius of the Arc1 (for unification with other arc objects)

    Parameters
    ----------
    self : Arc1
        An Arc1 object

    Returns
    -------
    radius: float
        radius of the arc
    """

    self.check()

    return abs(self.radius)  # Radius of the arc
