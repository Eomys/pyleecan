
from ....Methods.Slot.SlotW16 import S16OutterError


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
