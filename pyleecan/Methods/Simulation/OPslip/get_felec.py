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

    if self.felec is not None:
        return self.felec

    # Compute felec if possible
    if self.N0 is None:
        raise InputError("OPslip object can't have felec and N0 both None")

    if p is None:
        machine = self.get_machine_from_parent()
        if machine is None:
            raise InputError("OPslip object can't find machine parent to compute felec")

        p = machine.get_pole_pair_number()

    self.felec = self.N0 * p / (60 * (1 - self.slip_ref))

    return self.felec
