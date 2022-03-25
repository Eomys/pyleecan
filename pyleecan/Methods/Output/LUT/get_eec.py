def get_eec(self):
    """Get the Electrical Equivalent Circuit

    Parameters
    ----------
    self : LUT
        a LUT object

    Returns
    ----------
    eec : EEC
        Electrical Equivalent Circuit
    """

    if self.simu is None:
        return None
    if self.simu.elec is None:
        return None
    return self.simu.elec.eec
