from numpy import argmax, cos, abs as np_abs, angle as np_angle


def comp_angle_d_axis(self):
    """Compute the angle between the X axis and the first d+ axis
    By convention a "Tooth" is centered on the X axis

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object

    Returns
    -------
    d_angle : float
        angle between the X axis and the first d+ axis
    """

    MMF = self.comp_mmf_unit()
    p = self.get_pole_pair_number()

    # Get the unit mmf FFT and angle values
    results = MMF.get_along("angle")
    angle_rotor = results["angle"]
    results = MMF.get_along("wavenumber")
    wavenumber = results["wavenumber"]
    mmf_ft = results[MMF.symbol]

    # Find the angle where the FFT is max
    indr_fund = np_abs(wavenumber - p).argmin()
    phimax = np_angle(mmf_ft[indr_fund])
    magmax = np_abs(mmf_ft[indr_fund])
    mmf_waveform = magmax * cos(p * angle_rotor + phimax)
    ind_max = argmax(mmf_waveform)
    return angle_rotor[ind_max]
