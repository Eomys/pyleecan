def get_Phi_dqh_mag_mean(self):
    """Get the mean magnets flux linkage in DQH frame

    Parameters
    ----------
    self : LUTdq
        a LUTdq object

    Returns
    ----------
    Phi_dqh_mag_mean : ndarray
        mean magnets flux linkage in dqh frame (3,)
    """

    # Find Id=Iq=0
    OP_list = self.get_OP_array("Id", "Iq").tolist()
    if [0, 0] in OP_list:
        ii = OP_list.index([0, 0])
    else:
        raise Exception("Operating Point Id=Iq=0 is required to compute LUT")

    Phi_dqh_mag_mean = self.get_Phi_dqh_mean()[ii, :]

    return Phi_dqh_mag_mean
