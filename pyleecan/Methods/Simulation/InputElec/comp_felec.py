from ....Classes.Simulation import Simulation
from ....Methods.Simulation.Input import InputError


def comp_felec(self):
    """Compute the electrical frequency

    Parameters
    ----------
    felec : float
        Electrical frequency [Hz]
    """
    if self.felec is not None:
        return self.felec
    elif self.N0 is not None:
        # Get the phase number for verifications
        if self.parent is None:
            raise InputError(
                "ERROR: InputCurrent object should be inside a Simulation object"
            )
        # get the simulation
        if isinstance(self.parent, Simulation):
            simu = self.parent
        elif isinstance(self.parent.parent, Simulation):
            simu = self.parent.parent
        else:
            raise InputError("Cannot find InputCurrent simulation.")

        zp = simu.machine.get_pole_pair_number()
        if zp is None:
            return self.N0 / 60
        else:
            return zp * self.N0 / 60
    else:
        return 50
