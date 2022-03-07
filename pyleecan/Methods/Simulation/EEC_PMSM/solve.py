from numpy import array, pi
import numpy.linalg as np_lin


def solve(self):
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

    Returns
    ------
    out_dict : dict
        Dict containing all magnetic quantities that have been calculated in EEC
    """

    ws = 2 * pi * self.OP.get_felec()

    out_dict = dict()

    if self.OP.get_Ud_Uq()["Ud"] is not None:
        # Voltage driven
        # Impedance matrix
        XR = array(
            [
                [self.R1, -ws * self.Lq],
                [ws * self.Ld, self.R1],
            ]
        )
        # Back emf array
        if self.Phid_mag is not None:
            XE = array([-ws * self.Phiq_mag, ws * self.Phid_mag])
        else:
            XE = array([0, 0])
        # Voltage array
        XU = array([self.OP.get_Ud_Uq()["Ud"], self.OP.get_Ud_Uq()["Uq"]])
        # Solve system to get current array
        XI = np_lin.solve(XR, XU - XE)

        # Store values in out_dict
        out_dict["Id"] = XI[0]
        out_dict["Iq"] = XI[1]
        out_dict["Ud"] = self.OP.get_Ud_Uq()["Ud"]
        out_dict["Uq"] = self.OP.get_Ud_Uq()["Uq"]

    elif self.OP.get_Id_Iq()["Id"] is not None:
        # Current Driven
        Ud = self.R1 * self.OP.get_Id_Iq()["Id"] - ws * self.Phiq
        Uq = self.R1 * self.OP.get_Id_Iq()["Iq"] + ws * self.Phid
        out_dict["Ud"] = Ud
        out_dict["Uq"] = Uq
        out_dict["Id"] = self.OP.get_Id_Iq()["Id"]
        out_dict["Iq"] = self.OP.get_Id_Iq()["Iq"]

    else:
        raise Exception("Cannot solve EEC if both voltage or current are not given")

    return out_dict
