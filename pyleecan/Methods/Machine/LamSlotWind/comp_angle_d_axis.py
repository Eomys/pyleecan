from numpy import argmax, cos, abs as np_abs, angle as np_angle


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

    MMF, _ = self.comp_mmf_unit(Nt=1, Na=400 * p)

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
    magmax = np_abs(mmf_ft[indr_fund])

    # Reconstruct fundamental MMF wave
    mmf_waveform = magmax * cos(p * angle_stator + phimax)

    # Get the first angle where mmf is max
    d_angle = angle_stator[argmax(mmf_waveform)]

    if is_plot:
        import matplotlib.pyplot as plt
        from numpy import squeeze

        fig, ax = plt.subplots()
        ax.plot(
            angle_stator, squeeze(MMF.get_along("angle[oneperiod]")[MMF.symbol]), "k"
        )
        ax.plot(angle_stator, mmf_waveform, "r")
        ax.plot([d_angle, d_angle], [-magmax, magmax], "--k")
        plt.show()

    return d_angle
