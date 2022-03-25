from ....Methods.Simulation.Input import InputError


def get_N0(self, p=None):
    """Returns the Rotor speed

    Parameters
    ----------
    self : OPslip
        An OPslip object
    p: int
        pole pair number

    Returns
    -------
    N0 : float
        Rotor speed [rpm]
    """

    if self.N0 is not None:
        return self.N0

    # Compute N0 if possible
    if self.felec is None:
        raise InputError("OPslip object can't have felec and N0 both None")

    if p is None:
        machine = self.get_machine_from_parent()
        if machine is None:
            raise InputError("OPslip object can't find machine parent to compute N0")

        p = machine.get_pole_pair_number()

    self.N0 = 60 * (1 - self.slip_ref) * self.felec / p

    return self.N0
