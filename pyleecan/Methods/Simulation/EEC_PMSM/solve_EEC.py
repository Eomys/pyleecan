# -*- coding: utf-8 -*-

from ....Functions.Electrical.coordinate_transformation import dq2n

from numpy import array, pi, zeros
from numpy.linalg import solve

def solve_EEC(self, output):
    """Compute the parameters dict for the equivalent electrical circuit

    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    output : Output
        an Output object
    """
    
    qs = output.simu.machine.stator.winding.qs
    p = output.simu.machine.stator.winding.p
    freq0 = 0

    ws = 2*pi*freq0
    
    # Prepare linear system
    XU = array([self.parameters["Ud"], self.parameters["Uq"]])
    XR = array([[self.parameters["R20"], -ws*self.parameters["Lq"]],
                [self.parameters["R20"], ws*self.parameters["Ld"]]])
    XE = array([0, self.parameters["BEMF"]])
    
    # Solve linear system XU = XR.Idq + XE
    Idq = solve(XR, XU-XE[:,None])
    
    # Transform from d/q axes to phases
    output.elec.Is = dq2n(Idq, p*mmf_angle, n=qs)
    output.elec.Ir = zeros(output.elec.Is.shape)