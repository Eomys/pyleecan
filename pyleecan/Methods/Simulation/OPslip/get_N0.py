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

    if self.slip_ref is None:
        raise InputError("OPslip object can't have felec and slip_ref both None")

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

    if self.slip_ref == 1 and self.N0 not in [0, None]:
        raise InputError(
            "Speed and slip values are not consistent: slip_ref=1 and N0 not in [0, None]"
        )
    if self.N0 == 0 and self.slip_ref not in [1, None]:
        raise InputError(
            "Speed and slip values are not consistent: N0=0 and slip_ref not in [1, None]"
        )

    self.N0 = 60 * (1 - self.slip_ref) * self.felec / p

    return self.N0
