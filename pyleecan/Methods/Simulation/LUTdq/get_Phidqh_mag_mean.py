from ....Classes.OPdq import OPdq

from ....Functions.Electrical.dqh_transformation import n2dqh_DataTime


def get_Phidqh_mag_mean(self):
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
    OP_list = self.OP_matrix[:, 1:3].tolist()
    if [0, 0] in OP_list:
        ii = OP_list.index([0, 0])
    else:
        raise Exception("Operating Point Id=Iq=0 is required to compute LUT")

    if self.is_interp_along_curve:
        # Create open-circuit operating point
        OP = OPdq(N0=1000, Id_ref=0, Iq_ref=0)

        # Interpolate stator winding flux using LUT
        Phi_wind = self.interp_Phi_wind(OP=OP)

        # dqh transform
        Phi_dqh = n2dqh_DataTime(
            Phi_wind, is_dqh_rms=True, phase_dir=self.get_phase_dir()
        )

        # Get Phi_dqh_mean
        Phi_dqh_mag_mean = Phi_dqh.get_along("time=mean", "phase")[Phi_dqh.symbol]

    else:
        Phi_dqh_mag_mean = self.get_Phidqh_mean()[ii, :]

    return Phi_dqh_mag_mean
