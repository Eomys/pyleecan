from ....Classes.Arc1 import Arc1
from numpy import exp


def build_geometry(self):
    """Compute the curve (Line) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotCirc
        A SlotCirc object

    Returns
    -------
    curve_list: list
        A list of one Arc
    """
    Rbo = self.get_Rbo()
    alpha = self.comp_angle_opening()

    Z1 = Rbo * exp(-1j * alpha / 2)
    Z2 = Rbo * exp(1j * alpha / 2)

    # R0 is the radius of the circle
    # Pythagore in Triangle: Center, Z2, middle(Z1,Z2)
    # R0**2 = (W0/2)**2 + (H0-R0)**2
    R0 = ((self.W0 / 2) ** 2 + self.H0 ** 2) / (2 * self.H0)

    # Creation of curve
    curve_list = list()
    if self.is_outwards():
        curve_list.append(Arc1(begin=Z1, end=Z2, radius=-R0, is_trigo_direction=True))
    else:
        curve_list.append(Arc1(begin=Z1, end=Z2, radius=R0, is_trigo_direction=False))

    return curve_list
