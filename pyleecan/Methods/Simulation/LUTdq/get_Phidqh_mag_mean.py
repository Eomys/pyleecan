def get_Phidqh_mag_mean(self):
    """Get the total d-axis inductance
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
    OP_list = self.OP_matrix[:, 1:3].tolist()
    if [0, 0] in OP_list:
        ii = OP_list.index([0, 0])
    else:
        raise Exception("Operating Point Id=Iq=0 is required to compute LUT")

    return self.get_Phidqh_mean()[ii, :]
