from ....Methods.Simulation.Input import InputError


def get_felec(self, p=None):
    """Returns the electrical frequency

    Parameters
    ----------
    self : OPslip
        An OPslip object
    p: int
        pole pair number

    Returns
    -------
    felec : float
        Electrical Frequency [Hz]
    """

    if self.slip_ref is None:
        raise InputError("OPslip object can't have felec and slip_ref both None")

    if p is None and (self.felec is None or self.N0 is None):
        machine = self.get_machine_from_parent()
        if machine is None:
            raise InputError("OPslip object can't find machine parent to compute felec")

        p = machine.get_pole_pair_number()

    if self.felec is not None:
        return self.felec

    # Compute felec if possible
    if self.N0 is None:
        raise InputError("OPslip object can't have felec and N0 both None")

    if self.slip_ref != 1:
        self.felec = self.N0 * p / (60 * (1 - self.slip_ref))
    else:
        raise InputError(
            "Cannot calculate felec if slip_ref=1, felec must be enforced and N0 set to None or 0s"
        )

    return self.felec
