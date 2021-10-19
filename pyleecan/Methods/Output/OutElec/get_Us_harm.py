from ....Functions.Electrical.coordinate_transformation import n2dqh_DataTime


def get_Us_harm(self, is_dqh=True):
    """Return the harmonic stator voltage

    Parameters
    ----------
    self : OutElec
        an OutElec object
    is_dqh : bool
        True to rotate in DQH frame

    Returns
    -------
    Us_harm
        harmonic stator voltage
    """
    if self.Us_PWM is None:
        raise Exception("No PWM voltage was defined in the simulation")
    else:
        # Rotate to DQH frame
        if is_dqh:
            U = n2dqh_DataTime(self.Us_PWM, is_dqh_rms=True)
        else:
            U = self.Us_PWM
        # fft
        Us_fft = U.time_to_freq()
        # Remove f=0 (/!\ for DC machines)
        Us_harm = Us_fft.get_data_along("freqs>" + str(self.OP.get_felec()), "phase")
        return Us_harm
