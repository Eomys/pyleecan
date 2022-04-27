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

    # Get stator winding flux due to magnets
    Phi_dqh_mag = self.get_Phi_dqh_mag()

    if Phi_dqh_mag is not None:
        # Get mean value
        Phi_dqh_mag_mean = Phi_dqh_mag.get_along("time=mean", "phase")[
            Phi_dqh_mag.symbol
        ]
    else:
        Phi_dqh_mag_mean = None

    return Phi_dqh_mag_mean
