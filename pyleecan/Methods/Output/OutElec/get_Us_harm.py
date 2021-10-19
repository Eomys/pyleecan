from ....Functions.Electrical.coordinate_transformation import n2dqh_DataTime


def get_Us_harm(self):
    """Return the harmonic stator voltage in dqh frame"""
    if self.Us_PWM is None:
        raise Exception("No PWM voltage was defined in the simulation")
    else:
        # Rotate to DQH frame
        Udqh = n2dqh_DataTime(self.Us_PWM, is_dqh_rms=True)
        # fft
        Udqh_freq = Udqh.time_to_freq()
        # Remove f=0 (/!\ for DC machines)
        Us_harm = Udqh_freq.get_data_along("freqs>" + str(self.OP.get_felec()), "phase")
        return Us_harm
