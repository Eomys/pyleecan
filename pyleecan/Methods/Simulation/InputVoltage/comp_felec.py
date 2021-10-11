from ....Methods.Simulation.Input import InputError


def comp_felec(self, p=None):
    """Compute the electrical frequency

    Parameters
    ----------
    self : InputVoltage
        An InputVoltage object
    """

    name = self.__class__.__name__

    if p is None:
        if self.parent is None:
            raise InputError(name + " object should be inside a Simulation object")
        # get the pole pair number
        elif hasattr(self.parent, "machine"):
            p = self.parent.machine.get_pole_pair_number()
        elif hasattr(self.parent.parent, "machine"):
            p = self.parent.parent.machine.get_pole_pair_number()
        else:
            raise Exception("Cannot calculate pole pair number if machine is not found")

    if self.N0 is None and self.felec is None:
        raise InputError(name + " object can't have felec and N0 both None")

    if hasattr(self, "felec") and self.felec is not None:
        if self.N0 is None:
            self.N0 = 60 * (1 - self.slip_ref) * self.felec / p
        else:
            assert self.felec == self.N0 * p / (
                60 * (1 - self.slip_ref)
            ), "Input speed and frequency are not consistent regarding N0=60*(1-slip)*f_elec/p"

    elif self.N0 is not None:

        # Get the phase number for verifications
        return self.N0 * p / (60 * (1 - self.slip_ref))

    return self.felec
