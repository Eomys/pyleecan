from ....Methods.Slot.SlotW16 import S16OutterError, S16AlphaT
from numpy import pi, arcsin


def check(self):
    """Check that the SlotW16 object is correct

    Parameters
    ----------
    self : SlotW16
        A SlotW16 object

    Returns
    -------
    None

    Raises
    -------
    S16OutterError
        Slot 16 must be on internal lamination only
    """
    if self.is_outwards():
        raise S16OutterError("Slot 16 must be on internal lamination only")

    # Check W3 at min radius
    Rbo = self.get_Rbo()
    sp = 2 * pi / self.Zs  # slot pitch
    alphaT = 2 * arcsin(self.W3 * 0.5 / (Rbo - self.H0 - self.H2))

    if alphaT >= sp:
        raise S16AlphaT(
            "Tooth is larger than the slot pitch angle: reduce W3, H2 or Zs"
        )
