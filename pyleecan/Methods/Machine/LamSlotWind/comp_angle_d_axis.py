from numpy import abs as np_abs, angle as np_angle, pi


def comp_angle_d_axis(self, is_plot=False):
    """Compute the angle between the X axis and the first d+ axis
    By convention a "Tooth" is centered on the X axis
    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object
    is_plot : bool
        True to plot d axis position regarding unit mmf
    Returns
    -------
    d_angle : float
        angle between the X axis and the first d+ axis
    """

    if self.winding is None or self.winding.qs == 0 or self.winding.conductor is None:
        return 0

    p = self.get_pole_pair_number()

    MMF, _ = self.comp_mmf_unit(Nt=100, Na=400 * p)

    # Get angle values
    results1 = MMF.get_along("angle[oneperiod]")
    angle_stator = results1["angle"]

    # Get the unit mmf FFT and wavenumbers
    results = MMF.get_along("wavenumber")
    wavenumber = results["wavenumber"]
    mmf_ft = results[MMF.symbol]

    # Find the fundamental harmonic of MMF
    indr_fund = np_abs(wavenumber - p).argmin()
    phimax = np_angle(mmf_ft[indr_fund])

    # Get the angle for which mmf is max
    # MMF_max = A*cos(p*d_angle + phimax) which is maximum for p*d_angle + phimax = 2*pi
    d_angle = ((2 * pi - phimax) / p) % (2 * pi / p)

    if is_plot:
        import matplotlib.pyplot as plt
        from numpy import squeeze, argmax, cos

        # Reconstruct fundamental MMF wave
        magmax = np_abs(mmf_ft[indr_fund])
        mmf_waveform = magmax * cos(p * angle_stator + phimax)

        # Get the first angle where mmf is max
        I_max = argmax(mmf_waveform)
        d_angle0 = angle_stator[I_max]  # d_angle0->d_angle when Na->inf

        fig, ax = plt.subplots()
        ax.plot(
            angle_stator, squeeze(MMF.get_along("angle[oneperiod]")[MMF.symbol]), "k"
        )
        ax.plot(angle_stator, mmf_waveform, "r")
        ax.plot([d_angle, d_angle], [-magmax, magmax], "--k")
        ax.plot([d_angle0, d_angle0], [-magmax, magmax], "--b")
        plt.show()

    return d_angle
