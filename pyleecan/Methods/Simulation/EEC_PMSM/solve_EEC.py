# -*- coding: utf-8 -*-

from numpy import array, pi
from scipy.linalg import solve


def solve_EEC(self):
    """Compute the parameters dict for the equivalent electrical circuit
    cf "Advanced Electrical Drives, analysis, modeling, control"
    Rik de doncker, Duco W.J. Pulle, Andre Veltman, Springer edition

                 <---                               --->
     -----R-----wsLqIq----              -----R-----wsLdId----
    |                     |            |                     |
    |                     |            |                    BEMF
    |                     |            |                     |
     ---------Id----------              ---------Iq----------

             --->                               --->
              Ud                                 Uq

    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    Return
    ------
    out_dict : dict
        Dict containing all magnetic quantities that have been calculated in EEC
    """

    felec = self.freq0
    ws = 2 * pi * felec

    out_dict = dict()

    if "Ud" in self.parameters:  # Voltage driven
        # Prepare linear system
        XR = array(
            [
                [self.parameters["R20"], -ws * self.parameters["Lq"]],
                [ws * self.parameters["Ld"], self.parameters["R20"]],
            ]
        )
        XE = array([0, ws * self.parameters["phi"]])
        XU = array([self.parameters["Ud"], self.parameters["Uq"]])
        # Solve system
        XI = solve(XR, XU - XE)
        out_dict["Id"] = XI[0]
        out_dict["Iq"] = XI[1]
        out_dict["Ud"] = self.parameters["Ud"]
        out_dict["Uq"] = self.parameters["Uq"]
    else:  # Current Driven
        Ud = (
            self.parameters["R20"] * self.parameters["Id"]
            - ws * self.parameters["Phiq"]
        )
        Uq = (
            self.parameters["R20"] * self.parameters["Iq"]
            + ws * self.parameters["Phid"]
        )
        out_dict["Ud"] = Ud
        out_dict["Uq"] = Uq
        out_dict["Id"] = self.parameters["Id"]
        out_dict["Iq"] = self.parameters["Iq"]

    return out_dict
