from numpy import diff, zeros, newaxis


def comp_emf(self):
    """Compute the Electromotive force [V]

    Parameters
    ----------
    self : OutMag
        an OutMag object

    """

    # Get stator winding flux
    Phi_wind = self.Phi_wind_stator
    phi_wind = Phi_wind.get_along("time[smallestperiod]", "phase")[Phi_wind.symbol]

    # Get time axis
    for axe in Phi_wind.axes:
        if axe.name == "time":
            Time = axe

    # Get time values on the smallest period
    _, is_antiper_t = Time.get_periodicity()
    time = Time.get_values(
        is_oneperiod=True,
        is_antiperiod=is_antiper_t,
    )

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

        EMF = Phi_wind.copy()
        EMF.values = emf
        EMF.name = "Stator Winding Electromotive Force"
        EMF.unit = "V"
        EMF.symbol = "EMF"

        self.emf = EMF
