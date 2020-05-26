# -*- coding: utf-8 -*-

from numpy import pi

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
    
    freq0 = self.freq0

    self.parameters["R20"] = output.simu.machine.stator.comp_resistance_wind()
    phi = self.fluxlink.comp_fluxlinkage(output)
    (Lmd, Lmq) = self.indmag.comp_inductance(output)
    self.parameters["Ld"] = Lmd - phi
    self.parameters["Lq"] = Lmq
    self.parameters["BEMF"] = 2*pi*freq0 * phi