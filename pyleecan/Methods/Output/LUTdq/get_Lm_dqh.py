import numpy as np


def get_Lm_dqh(self, Id, Iq, Phi_dqh=None):
    """Get the magnetizing dqh inductance

    Parameters
    ----------
    self : LUTdq
        a LUTdq object
    Id : float
        current Id
    Iq : float
        current Iq
    Phi_dqh: ndarray
        Stator winding dqh flux

    Returns
    ----------
    Lmdqh : ndarray
        magnetizing dqh inductance
    """

    if Phi_dqh is None:
        Phi_dqh = self.interp_Phi_dqh(Id=Id, Iq=Iq)

    # Get dqh flux linkage (without currents, only due to PM)
    Phi_dqh_mag = self.get_Phi_dqh_mag_mean()[:, None]

    # Init dqh current
    if np.isscalar(Id) and np.isscalar(Iq):
        n_OP = 1
    else:
        n_OP = Id.size
    I_dqh = np.zeros((3, n_OP))
    I_dqh[0] = Id
    I_dqh[1] = Iq
    I_dqh[2] = 1

    # Divide flux by current to get inductance
    Lmdqh = (Phi_dqh - Phi_dqh_mag) / I_dqh

    return Lmdqh
