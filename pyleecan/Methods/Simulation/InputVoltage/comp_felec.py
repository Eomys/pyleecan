from ....Methods.Simulation.Input import InputError


def comp_felec(self):
    """Compute the electrical frequency

    Parameters
    ----------
    self : InputVoltage
        An InputVoltage object
    """

    name = self.__class__.__name__

    if self.parent is None:
        raise InputError(name + " object should be inside a Simulation object")

    # get the pole pair number
    if hasattr(self.parent, "machine"):
        p = self.parent.machine.stator.get_pole_pair_number()
    elif hasattr(self.parent.parent, "machine"):
        p = self.parent.parent.machine.stator.get_pole_pair_number()
    else:
        logger = self.get_logger()
        logger.warning("Input.comp_felec(): Machine was not found.")
        p = 1

    if hasattr(self, "felec") and self.felec is not None:
        if self.N0 is None:
            self.N0 = 60 * (1 - self.slip_ref) * self.felec / p
        else:
            assert self.felec == self.N0 * p / (
                60 * (1 - self.slip_ref)
            ), "Input speed and frequency are not consistent regarding N0=60*(1-slip)*f_elec/p"

        return self.felec

    elif self.N0 is not None:
        # Get the phase number for verifications
        return self.N0 * p / (60 * (1 - self.slip_ref))
    else:
        raise InputError(name + " object can't have felec and N0 at None")
