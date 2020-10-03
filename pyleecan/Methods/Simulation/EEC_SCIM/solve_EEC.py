# -*- coding: utf-8 -*-

from numpy import array, pi
from scipy.linalg import solve


def solve_EEC(self, output):
    """Compute the parameters dict for the equivalent electrical circuit
    TODO find ref. to cite
    cf "Advanced Electrical Drives, analysis, modeling, control"
    Rik de doncker, Duco W.J. Pulle, Andre Veltman, Springer edition

                  <---                     ---->
     -----Rs------XsIs---- --- -----Rr'----Xr'Ir'----
    |                     |   |                       |
    |                     Rm  Xm                      Rr'*(s-1)/s
    |                     |   |                       |
     ---------Is---------- --- ---------Ir------------

             --->                               <---
              Us                                 Ur

    Parameters
    ----------
    self : EEC_SCIM
        an EEC_SCIM object
    output : Output
        an Output object
    """

    felec = output.elec.felec
    ws = 2 * pi * felec

    # Prepare linear system

    # Solve system
    if "Ud" in self.parameters:
        XR = array(
            [
                [self.parameters["R20"], -ws * self.parameters["Lq"]],
                [ws * self.parameters["Ld"], self.parameters["R20"]],
            ]
        )
        XE = array([0, ws * self.parameters["phi"]])
        XU = array([self.parameters["Ud"], self.parameters["Uq"]])
        XI = solve(XR, XU - XE)
        output.elec.Id_ref = XI[0]
        output.elec.Iq_ref = XI[1]
    else:
        output.elec.Ud_ref = (
            self.parameters["R20"] * self.parameters["Id"]
            - ws * self.parameters["Phiq"]
        )
        output.elec.Uq_ref = (
            self.parameters["R20"] * self.parameters["Iq"]
            + ws * self.parameters["Phid"]
        )

    # Compute currents
    output.elec.Is = None
    output.elec.Is = output.elec.get_Is()

    # Compute voltage
    output.elec.Us = None
    output.elec.Us = output.elec.get_Us()
