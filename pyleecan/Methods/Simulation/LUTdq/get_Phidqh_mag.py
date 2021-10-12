from ....Functions.Electrical.coordinate_transformation import n2dqh_DataTime


def get_Phidqh_mag(self):
    """Get the total d-axis inductance
    Parameters
    ----------
    self : LUTdq
        a LUTdq object

    Returns
    ----------
    Phi_dqh_mag : DataND
        magnets flux linkage in dqh frame (Nt_tot, 3)
    """

    if self.Phi_dqh_mag is None:

        # Find Id=Iq=0
        OP_list = self.OP_matrix[:, 1:3].tolist()
        if [0, 0] in OP_list:
            ii = OP_list.index([0, 0])
        else:
            raise Exception("Operating Point Id=Iq=0 is required to compute LUT")

        Time = self.Phi_wind[ii].get_axes("time")[0]
        # dqh transform
        Phi_dqh_mag = n2dqh_DataTime(
            self.Phi_wind[ii],
            is_dqh_rms=True,
        )

        # Store for next call
        self.Phi_dqh_mag = Phi_dqh_mag

    return self.Phi_dqh_mag
