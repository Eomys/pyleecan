from numpy import pi, interp


def solve_elementary(self, Lm_init):
    """Compute the parameters dict for the equivalent electrical circuit
    TODO find ref. to cite
    cf "Title"
    Autor, Publisher

                  --->                     ---->
     -----Rs------XsIs---- --- -----Rr'----XrIr----
    |                     |   |                       |
    |                     par["Rfe"] Xm                      Rr*(s-1)/s
    |                     |   |                       |
     ---------Is---------- --- ---------Ir------------

             --->
              Us

    Parameters
    ----------



    Parameters
    ----------
    self : EEC_SCIM
        an EEC_SCIM object
    Lm_init: float
        Magnetizing inductance initial value [H]

    Returns
    ----------
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
    delta_Lm: float
        Magnetizing inductance [H]
    """

    par = self.parameters

    ws = 2 * pi * par["felec"]

    Xm = ws * Lm_init
    X1 = ws * par["L1"]
    X2 = ws * par["L2"]
    Zm = 1j * Xm
    # magnetizing branch impedance, including iron loss resistance
    Zmf = 1 / (1 / Zm + 1 / par["Rfe"])

    # rotor impedance
    Z2 = 1j * X2 + par["R2"] / par["slip"]

    # stator impedance
    Z1 = 1j * X1 + par["R1"]

    # total impedance
    if par["slip"] != 0:
        Ztot = Z1 + 1 / (1 / Zmf + 1 / Z2)
    else:
        Ztot = Z1 + Zmf

    I1 = (par["U0_ref"] + 1j * 0) / Ztot
    E = par["U0_ref"] - Z1 * I1
    Im = E / Zm
    If = E / par["Rfe"]
    I2 = I1 - (Im + If)

    # recalculating magnetizing inductance
    Phim = interp(abs(Im), par["I_m"], par["Phi_m"])

    Lm = Phim / abs(Im)

    # calculation of non linearity effect (should be ->0 when Lm(Im)=Lm_init)
    delta_Lm = abs((Lm - Lm_init) / Lm_init)

    # A = array(
    #         [
    #             # sum of (real and imaginary) voltages equals the input voltage Us
    #             [ 1,  0, Rs, -Xs,  0,   0,    0,    0,   0,   0, ],
    #             [ 0,  1, Xs,  Rs,  0,   0,    0,    0,   0,   0, ],
    #             # sum of (real and imaginary) currents are zeros
    #             [ 0,  0, -1,   0,  1,   0,    1,    0,   1,   0, ],
    #             [ 0,  0,  0,  -1,  0,   1,    0,    1,   0,   1, ],
    #             # j*Xm*Im = Um
    #             [-1,  0,  0,   0,  0, -Xm,    0,    0,   0,   0, ],
    #             [ 0, -1,  0,   0, Xm,   0,    0,    0,   0,   0, ],
    #             # (Rr'/s + j*Xr')*Ir' = Um
    #             [-1,  0,  0,   0,  0,   0, Rr_s,  -Xr,   0,   0, ],
    #             [ 0, -1,  0,   0,  0,   0,   Xr, Rr_s,   0,   0, ],
    #             # par["Rfe"]*Ife = Um
    #             [-1,  0,  0,   0,  0,   0,    0,    0, par["Rfe"],   0, ],
    #             [ 0, -1,  0,   0,  0,   0,    0,    0,   0, par["Rfe"], ],
    #         ]
    #     )
    #     # fmt: on
    #     # delete last row and column if par["Rfe"] is None
    #     if par["Rfe"] is None:
    #         A = A[:-2, :-2]
    #         b = b[:-2]

    #     # print(b)
    #     # print(A)
    #     X = solve(A.astype(float), b.astype(float))

    return I1, I2, Im, If, Lm, delta_Lm
