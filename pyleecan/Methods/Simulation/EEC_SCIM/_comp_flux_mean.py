from numpy import zeros, sqrt, isnan

from ....Functions.Electrical.dqh_transformation import n2abc
from ....Functions.labels import STATOR_LAB, ROTOR_LAB


def _comp_flux_mean(self, out):
    # TODO add fix for single time value
    # TODO add option to calculate RMS instead of mean fluxlinkage

    # some readability
    logger = self.get_logger()
    machine = out.simu.machine
    p = machine.rotor.winding.p
    qsr = machine.rotor.winding.qs
    sym, is_anti_per = machine.comp_periodicity_spatial()

    # get the fluxlinkages
    Phi = out.mag.Phi_wind[ROTOR_LAB + "-0"].get_along("time", "phase")["Phi_{wind}"]

    # reconstruct fluxlinkage in case of (anti) periodicity
    if out.simu.mag.is_periodicity_a:
        # reconstruct anti periodicity
        if is_anti_per:
            qsr_eff = qsr // (sym * (1 + is_anti_per))
            for ii in range(qsr_eff):
                if not all(isnan(Phi[:, ii + qsr_eff]).tolist()):
                    logger.warning(
                        f"{type(self).__name__}: "
                        + f"Rotor fluxlinkage of bar {ii + qsr_eff} will be overridden."
                    )
                Phi[:, ii + qsr_eff] = -Phi[:, ii]
        # reconstruct periodicity
        if sym != 1:
            qsr_eff = qsr // sym
            if not all(isnan(Phi[:, qsr_eff:]).tolist()):
                logger.warning(
                    f"{type(self).__name__}: "
                    + f"Rotor fluxlinkage of bar "
                    + "starting with {qsr_eff} will be overridden."
                )
            for ii in range(sym - 1):
                id0 = qsr_eff * (ii + 1)
                id1 = qsr_eff * (ii + 2)
                Phi[:, id0:id1] = Phi[:, :qsr_eff]

        # rescale
        Phi = Phi / (sym * (1 + is_anti_per))

    # compute mean value of periodic bar flux linkage
    Phi_ab = zeros([Phi.shape[0], 2])
    if (qsr % p) == 0:
        qsr_per_pole = qsr // p
        for ii in range(p):
            id0 = qsr_per_pole * ii
            id1 = qsr_per_pole * (ii + 1)
            Phi_ab += n2abc(Phi[:, id0:id1], n=qsr_per_pole) / p
    else:
        logger.warning(f"{type(self).__name__}: " + "Not Implemented Yet")

    # compute rotor and stator flux linkage
    Phi_r = abs(Phi_ab[:, 0] + 1j * Phi_ab[:, 1]).mean() / sqrt(2)
    Phi_ab = n2abc(
        out.mag.Phi_wind[STATOR_LAB + "-0"].get_along("time", "phase")["Phi_{wind}"]
    )
    Phi_s = abs(Phi_ab[:, 0] + 1j * Phi_ab[:, 1]).mean() / sqrt(2)

    return Phi_s, Phi_r
