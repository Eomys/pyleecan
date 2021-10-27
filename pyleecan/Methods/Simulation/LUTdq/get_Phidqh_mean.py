from numpy import zeros

from ....Functions.Electrical.dqh_transformation import n2dqh_DataTime


def get_Phidqh_mean(self):
    """Get the total d-axis inductance
    Parameters
    ----------
    self : LUTdq
        a LUTdq object

    Returns
    ----------
    Phi_dqh_mean : ndarray
        mean flux linkage in dqh frame (N_dq, 3)
    """

    if self.Phi_dqh_mean is None:

        Phi_dqh_mean = zeros((len(self.Phi_wind), 3))

        for i, Phi_wind in enumerate(self.Phi_wind):
            # dqh transform
            Phi_dqh = n2dqh_DataTime(
                Phi_wind,
                is_dqh_rms=True,
            )
            # mean over time axis
            Phi_dqh_mean[i, :] = Phi_dqh.get_along("time=mean", "phase")[Phi_dqh.symbol]

        # Store for next call
        self.Phi_dqh_mean = Phi_dqh_mean

    return self.Phi_dqh_mean
