from ....Methods.Slot.SlotWLSRPM import SLSRPMOutterError


def check(self):
    """Check that the SlotW16 object is correct

    Parameters
    ----------
    self : SlotWLSRPM
        A SlotWLSRPM object

    Returns
    -------
    None

    Raises
    -------

    """

    if self.is_outwards():
        raise SLSRPMOutterError("Slot Type LSRPM can’t be used on outer lamination")
