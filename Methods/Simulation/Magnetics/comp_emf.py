from numpy import diff, zeros, newaxis

from pyleecan.Methods.Simulation.Input import InputError


def comp_emf(self):
    """Compute the Electromotive force [V]
    """
    if self.parent is None:
        raise InputError(
            "ERROR: The Magnetic object must be in a Simulation object to run"
        )
    if self.parent.parent is None:
        raise InputError(
            "ERROR: The Simulation object must be in an Output object to run"
        )

    output = self.parent.parent
    Phi_wind = output.mag.Phi_wind_stator
    time = output.mag.time
    Nt_tot = output.mag.Nt_tot
    qs = output.simu.machine.stator.winding.qs

    if Nt_tot > 1:
        emf = zeros((Nt_tot, qs))
        emf[:-1, :] = diff(Phi_wind, 1, 0) / diff(time, 1, 0)[:, newaxis]
        # We approximate the Phi_wind to be periodic to compute the last value
        # And we assume time to be a linspace
        emf[-1] = (Phi_wind[0] - Phi_wind[-1]) / (time[1] - time[0])
    else:
        emf = None

    output.mag.emf = emf
