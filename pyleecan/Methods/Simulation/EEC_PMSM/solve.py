from numpy import array, pi
import numpy.linalg as np_lin


def solve(self, out_dict=None):
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

    par = self.parameters

    ws = 2 * pi * par["felec"]

    if out_dict is None:
        out_dict = dict()

    if "Ud" in par and par["Ud"] is not None:
        # Voltage driven
        # Impedance matrix
        XR = array(
            [
                [par["R1"], -ws * par["Lq"]],
                [ws * par["Ld"], par["R1"]],
            ]
        )
        # Back emf array
        if "Phid_mag" in par:
            XE = array([-ws * par["Phiq_mag"], ws * par["Phid_mag"]])
        else:
            XE = array([0, 0])
        # Voltage array
        XU = array([par["Ud"], par["Uq"]])
        # Solve system to get current array
        XI = np_lin.solve(XR, XU - XE)

        # Store values in out_dict
        out_dict["Id"] = XI[0]
        out_dict["Iq"] = XI[1]
        out_dict["Ud"] = par["Ud"]
        out_dict["Uq"] = par["Uq"]

    elif "Id" in par and par["Id"] is not None:
        # Current Driven
        Ud = par["R1"] * par["Id"] - ws * par["Phiq"]
        Uq = par["R1"] * par["Iq"] + ws * par["Phid"]
        out_dict["Ud"] = Ud
        out_dict["Uq"] = Uq
        out_dict["Id"] = par["Id"]
        out_dict["Iq"] = par["Iq"]

    else:
        raise Exception("Cannot solve EEC if both voltage or current are not given")

    return out_dict
