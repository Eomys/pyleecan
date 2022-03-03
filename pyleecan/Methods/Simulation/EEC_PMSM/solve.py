from numpy import array, pi
import numpy.linalg as np_lin


def solve(self, eec_param):
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

    out_dict = {"eec_param": eec_param}

    ws = 2 * pi * eec_param["felec"]

    if "Ud" in eec_param and eec_param["Ud"] is not None:
        # Voltage driven
        # Impedance matrix
        XR = array(
            [
                [eec_param["R1"], -ws * eec_param["Lq"]],
                [ws * eec_param["Ld"], eec_param["R1"]],
            ]
        )
        # Back emf array
        if "Phid_mag" in eec_param:
            XE = array([-ws * eec_param["Phiq_mag"], ws * eec_param["Phid_mag"]])
        else:
            XE = array([0, 0])
        # Voltage array
        XU = array([eec_param["Ud"], eec_param["Uq"]])
        # Solve system to get current array
        XI = np_lin.solve(XR, XU - XE)

        # Store values in out_dict
        out_dict["Id"] = XI[0]
        out_dict["Iq"] = XI[1]
        out_dict["Ud"] = eec_param["Ud"]
        out_dict["Uq"] = eec_param["Uq"]

    elif "Id" in eec_param and eec_param["Id"] is not None:
        # Current Driven
        Ud = eec_param["R1"] * eec_param["Id"] - ws * eec_param["Phiq"]
        Uq = eec_param["R1"] * eec_param["Iq"] + ws * eec_param["Phid"]
        out_dict["Ud"] = Ud
        out_dict["Uq"] = Uq
        out_dict["Id"] = eec_param["Id"]
        out_dict["Iq"] = eec_param["Iq"]

    else:
        raise Exception("Cannot solve EEC if both voltage or current are not given")

    return out_dict
