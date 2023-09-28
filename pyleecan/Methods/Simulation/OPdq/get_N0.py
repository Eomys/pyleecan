from ....Methods.Simulation.Input import InputError


def get_N0(self, p=None):
    """Returns the Rotor speed

    Parameters
    ----------
    self : OPdq
        An OPdq object
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
        raise InputError("OPdq object can't have felec and N0 both None")

    if p is None:
        machine = self.get_machine_from_parent()
        if machine is None:
            raise InputError("OPdq object can't find machine parent to compute N0")
        p = machine.get_pole_pair_number()

    self.N0 = self.felec * 60 / p

    return self.N0
