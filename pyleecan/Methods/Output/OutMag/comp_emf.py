from numpy import diff, zeros, newaxis, pi

from ....Functions.Electrical.coordinate_transformation import n2dq


def comp_emf(self, is_dq=False):
    """Compute the Electromotive force [V]

    Parameters
    ----------
    self : OutMag
        an OutMag object
    is_dq : bool
        rotate to dq axes if true

    """

    # Get stator winding flux
    Phi_wind = self.Phi_wind_stator
    result = Phi_wind.get_along("time[smallestperiod]", "phase")
    phi_wind = result[Phi_wind.symbol]
    time = result["time"]

    # Get time axis
    for axe in Phi_wind.axes:
        if axe.name == "time":
            Time = axe

    # Get time values on the smallest period
    _, is_antiper_t = Time.get_periodicity()

    # Calculate EMF and store it in OutMag
    if time.size > 1:
        emf = zeros(phi_wind.shape)
        emf[:-1, :] = diff(phi_wind, 1, 0) / diff(time, 1, 0)[:, newaxis]
        # We assume phi_wind to be periodic to compute the last value
        # and we assume time to be a linspace
        if is_antiper_t:
            sign0 = (
                -1
            )  # The opposite of the first value of the anti-period is after the last value of the anti-period
        else:
            sign0 = (
                1  # The first value of the period is after the last value of the period
            )
        emf[-1, :] = (sign0 * phi_wind[0, :] - phi_wind[-1, :]) / (time[1] - time[0])

        if is_dq:
            output = self.parent
            qs = output.simu.machine.stator.winding.qs
            felec = output.elec.felec
            # Get rotation direction of the fundamental magnetic field created by the winding
            rot_dir = output.get_rot_dir()
            # Get stator current function of time
            emf = n2dq(
                emf, 2 * pi * felec * time, n=qs, rot_dir=rot_dir, is_dq_rms=True
            )

        EMF = Phi_wind.copy()
        EMF.values = emf
        EMF.name = "Stator Winding Electromotive Force"
        EMF.unit = "V"
        EMF.symbol = "EMF"

        self.emf = EMF
