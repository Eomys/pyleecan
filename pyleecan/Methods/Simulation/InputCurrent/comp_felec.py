from ....Methods.Simulation.Input import InputError


def comp_felec(self):
    """Compute the electrical frequency

    Parameters
    ----------
    self : InputCurrent
        An InputCurrent object
    """

    if hasattr(self, "felec") and self.felec is not None:
        return self.felec  # TODO maybe add some checks?
    elif self.N0 is not None:
        # Get the phase number for verifications
        if self.parent is None:
            raise InputError("InputCurrent object should be inside a Simulation object")
        # get the pole pair number
        if hasattr(self.parent, "machine"):
            zp = self.parent.machine.get_pole_pair_number()
        elif hasattr(self.parent.parent, "machine"):
            zp = self.parent.parent.machine.get_pole_pair_number()
        else:
            logger = self.get_logger()
            logger.warning("Input.comp_felec(): Machine was not found.")
            zp = 1
        return self.N0 * zp / (60 * (1 - self.slip_ref))
    else:
        raise InputError("InputCurrent object can't have felec and N0 at None")