from numpy import array

from ....Classes.EEC_PMSM import EEC_PMSM
from ....Classes.Electrical import Electrical


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

    eec = self.get_eec()

    if eec is not None and eec.Phid_mag is not None and eec.Phiq_mag is not None:
        Phi_dqh_mag_mean = array([eec.Phid_mag, eec.Phiq_mag, 0])
    else:

        # Get stator winding flux due to magnets
        Phi_dqh_mag = self.get_Phi_dqh_mag()

        if Phi_dqh_mag is not None:
            # Get mean value
            Phi_dqh_mag_mean = Phi_dqh_mag.get_along("time=mean", "phase")[
                Phi_dqh_mag.symbol
            ]
            # Store in eec for further use
            if eec is None:
                eec = EEC_PMSM()
                if self.simu.elec is None:
                    self.simu.elec = Electrical()
                self.simu.elec.eec = eec
            eec.Phid_mag = float(Phi_dqh_mag_mean[0])
            eec.Phiq_mag = float(Phi_dqh_mag_mean[1])

        else:
            Phi_dqh_mag_mean = None

    return Phi_dqh_mag_mean
