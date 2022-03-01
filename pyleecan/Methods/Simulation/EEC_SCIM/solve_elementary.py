from numpy import pi, interp, inf


def solve_elementary(self, eec_param):
    """Compute the parameters dict for the equivalent electrical circuit

                  --->                     ---->
     -----Rs------XsIs---- --- -----Rr'----XrIr----
    |                     |   |                       |
    |             eec_param["Rfe"]  Xm                    Rr*(s-1)/s
    |                     |   |                       |
     ---------Is---------- --- ---------Ir------------

             --->
              Us

    Parameters
    ----------
    self : EEC_SCIM
        an EEC_SCIM object
    eec_param: dict
        dictionnary containing EEC parameters:
            I1: float
                Stator phase current [Arms]
            I2: float
                Rotor bar current [Arms]
            Im: float
                Magnetizing current [Arms]
            If: float
                Iron loss current [Arms]
            Lm: float
                Magnetizing inductance [H]
            U1: float
                Stator phase voltage [Vrms]
            E: float
                Rotor phase voltage [Vrms]
            Z1: float
                Stator phase impedance [Ohm]
            Z2: float
                Rotor phase impedance [Ohm]
            Rfe: float
                Iron loss resistance [Ohm]

    Returns
    ----------
    eec_param: dict
        dictionnary containing updated EEC parameters
    delta_Lm: float
        convergence criterion for magnetizing inductance calculation [H]
    """

    ws = 2 * pi * eec_param["felec"]

    Xm = ws * eec_param["Lm"]
    X1 = ws * eec_param["L1"]
    X2 = ws * eec_param["L2"]
    Zm = 1j * Xm
    # magnetizing branch impedance, including iron loss resistance
    Zmf = 1 / (1 / Zm + 1 / eec_param["Rfe"])

    # rotor impedance
    if eec_param["slip"] == 0:
        Z2 = inf
    else:
        Z2 = 1j * X2 + eec_param["R2"] / eec_param["slip"]

    # stator impedance
    Z1 = 1j * X1 + eec_param["R1"]

    # total impedance
    Ztot = Z1 + 1 / (1 / Zmf + 1 / Z2)

    if "U0_ref" in eec_param and eec_param["U0_ref"] is not None:
        U1 = eec_param["U0_ref"]
        I1 = (U1 + 1j * 0) / Ztot
        E = U1 - Z1 * I1
        Im = E / Zm
    else:
        I1 = eec_param["I0_ref"]
        Im = I1 / (1 + Zm / Z2 + Zm / eec_param["Rfe"])
        E = Zm * Im
        U1 = E + Z1 * I1

    If = E / eec_param["Rfe"]
    I2 = I1 - (Im + If)

    # recalculating magnetizing inductance
    Phim = interp(abs(Im), eec_param["I_m"], eec_param["Phi_m"])

    Lm = Phim / abs(Im)

    # calculation of non linearity effect (should be ->0 when Lm(Im)=eec_param["Lm"])
    delta_Lm = abs((Lm - eec_param["Lm"]) / eec_param["Lm"])

    # Update eec parameters
    eec_param["I1"] = I1
    eec_param["I2"] = I2
    eec_param["Im"] = Im
    eec_param["If"] = If
    eec_param["U1"] = U1
    eec_param["E"] = E
    eec_param["Z1"] = Z1
    eec_param["Z2"] = Z2
    eec_param["Lm"] = Lm

    return eec_param, delta_Lm
