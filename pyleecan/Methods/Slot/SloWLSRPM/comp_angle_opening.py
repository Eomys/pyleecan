
from numpy import arcsin, exp, pi, sqrt, sin, cos
def comp_angle_opening(self):
    """Compute the average opening angle of the Slot

    Parameters
    ----------
    self : SlotWLSRPM：
        A SlotWLSRPM： object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """
    Rbo = self.get_Rbo()
    return 2*(pi / self.Zs-arcsin(self.W3/2/Rbo))
