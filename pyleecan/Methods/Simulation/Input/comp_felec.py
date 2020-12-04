from ....Methods.Simulation.Input import InputError


def comp_felec(self):
    """Compute the electrical frequency

    Parameters
    ----------
    felec : float
        Electrical frequency [Hz]
    """

    if hasattr(self, "felec") and self.felec is not None:
        return self.felec  # TODO maybe add some checks?
    elif self.N0 is not None:
        # Get the phase number for verifications
        if self.parent is None:
            raise InputError(
                "ERROR: InputCurrent object should be inside a Simulation object"
            )
        # get the simulation
        if self.parent is None:
            raise InputError("ERROR: Input object should be inside a Simulation object")
        simu = self.parent

        zp = simu.machine.stator.get_pole_pair_number()
        zp = zp if zp is not None else 1

        return self.N0 * zp / 60
    else:
        raise InputError("ERROR: InputCurrent object can't have felec and N0 at None")
