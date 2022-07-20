from numpy import pi, interp, inf, exp
import scipy.interpolate as scp_int


def solve_elementary(self):
    """Solve the EEC, set the resulting currents and voltages and update the
    magnetizing inductance.

    Parameters
    ----------
    self : EEC_SCIM
        an EEC_SCIM object

    Returns
    ----------
    delta_Lm: float
        convergence criterion for magnetizing inductance calculation,
        i.e. relative difference between the recalculated magnetizing inductance
        and the current magnetizing inductance
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

    U_dict, I_dict = self.OP.get_U0_UPhi0(), self.OP.get_I0_Phi0()
    if U_dict["U0"] is not None:  # Voltage driven
        UPhi0_ref = 0 if U_dict["UPhi0"] is None else U_dict["UPhi0"]
        U1 = U_dict["U0"] * exp(1j * UPhi0_ref)
        I1 = (U1 + 1j * 0) / Ztot
        E = U1 - Z1 * I1
        Im = E / Zm
    elif I_dict["I0"] is not None:  # Current driven
        IPhi0_ref = 0 if I_dict["Phi0"] is None else I_dict["Phi0"]
        I1 = I_dict["I0"] * exp(1j * IPhi0_ref)
        Im = I1 / (1 + Zm / Z2 + Zm / self.Rfe)
        E = Zm * Im
        U1 = E + Z1 * I1
    else:
        raise Exception("Either U0_ref or I0_ref must be set to solve EEC_SCIM")

    If = E / self.Rfe
    I2 = I1 - (Im + If)

    # recalculating magnetizing inductance
    # linear interpolation with linear extrapolation if Im is outside Im_table
    Lm1 = scp_int.interp1d(
        self.Im_table, self.Lm_table, kind="linear", fill_value="extrapolate"
    )(abs(Im))
    # linear interpolation with nearest extrapolation if Im is outside Im_table
    Lm2 = interp(abs(Im), self.Im_table, self.Lm_table)
    # magnetizing inductance is the average of both to simulate the saturation increase
    Lm = 0.5 * (Lm1 + Lm2)

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
