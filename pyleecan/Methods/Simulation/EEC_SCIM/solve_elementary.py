from numpy import pi, interp, inf, exp


def solve_elementary(self):
    """Compute the parameters dict for the equivalent electrical circuit

                  --->                     ---->
     -----Rs------XsIs---- --- -----Rr'----XrIr----
    |                     |   |                       |
    |                    Rfe  Xm                    Rr*(s-1)/s
    |                     |   |                       |
     ---------Is---------- --- ---------Ir------------

             --->
              Us

    Parameters
    ----------
    self : EEC_SCIM
        an EEC_SCIM object

    Returns
    ----------
    delta_Lm: float
        convergence criterion for magnetizing inductance calculation [H]
    """

    felec = self.OP.get_felec()
    slip = self.OP.get_slip()
    ws = 2 * pi * felec

    Xm = ws * self.Lm
    X1 = ws * self.L1
    X2 = ws * self.L2
    Zm = 1j * Xm
    # magnetizing branch impedance, including iron loss resistance
    Zmf = 1 / (1 / Zm + 1 / self.Rfe)

    # rotor impedance
    if slip == 0:
        Z2 = inf
    else:
        Z2 = 1j * X2 + self.R2 / slip

    # stator impedance
    Z1 = 1j * X1 + self.R1

    # total impedance
    Ztot = Z1 + 1 / (1 / Zmf + 1 / Z2)

    if self.OP.U0_ref is not None:  # Voltage driven
        UPhi0_ref = 0 if self.OP.UPhi0_ref is None else self.OP.UPhi0_ref
        U1 = self.OP.U0_ref * exp(1j * UPhi0_ref)
        I1 = (U1 + 1j * 0) / Ztot
        E = U1 - Z1 * I1
        Im = E / Zm
    elif self.OP.I0_ref is not None:  # Current driven
        IPhi0_ref = 0 if self.OP.IPhi0_ref is None else self.OP.IPhi0_ref
        I1 = self.OP.I0_ref * exp(1j * IPhi0_ref)
        Im = I1 / (1 + Zm / Z2 + Zm / self.Rfe)
        E = Zm * Im
        U1 = E + Z1 * I1
    else:
        raise Exception("Either U0_ref or I0_ref must be set to solve EEC_SCIM")

    If = E / self.Rfe
    I2 = I1 - (Im + If)

    # recalculating magnetizing inductance
    Lm = interp(abs(Im), self.Im_table, self.Lm_table)

    # calculation of non linearity effect (should be ->0 when Lm(Im)=self.Lm"])
    delta_Lm = abs((Lm - self.Lm) / self.Lm)

    # Update eec parameters
    self.I1 = I1
    self.I2 = I2
    self.Im = Im
    self.If = If
    self.U1 = U1
    self.U2 = E
    self.Lm = Lm

    return delta_Lm
