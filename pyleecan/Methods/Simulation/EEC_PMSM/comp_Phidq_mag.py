from lib2to3.pgen2.token import OP


def comp_Phidq_mag(self):
    """Compute and set the stator winding flux in open-circuit for the EEC

    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object

    """
    OP_oc = self.OP.copy()
    OP_oc.Id_ref = 0
    OP_oc.Iq_ref = 0

    Phi_dqh_mag_mean = self.comp_fluxlinkage(OP=OP_oc)[0]

    self.Phid_mag = float(Phi_dqh_mag_mean[0])
    self.Phiq_mag = float(Phi_dqh_mag_mean[1])
