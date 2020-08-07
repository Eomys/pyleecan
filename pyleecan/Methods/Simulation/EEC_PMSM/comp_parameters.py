# -*- coding: utf-8 -*-

from numpy import pi, sqrt


def comp_parameters(self, output):
    """Compute the parameters dict for the equivalent electrical circuit:
    resistance, inductance and back electromotive force
    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    output : Output
        an Output object
    """

    phi = self.fluxlink.comp_fluxlinkage(output)
    
    if "R20" not in self.parameters:
        self.parameters["R20"] = output.simu.machine.stator.comp_resistance_wind()
    if "Ld" not in self.parameters:
        (Lmd, Lmq) = self.indmag.comp_inductance(output)
        self.parameters["Ld"] = Lmd - phi
        self.parameters["Lq"] = Lmq
    if "BEMF" not in self.parameters:
        felec = output.elec.felec
        self.parameters["BEMF"] = 2 * pi * felec * phi
