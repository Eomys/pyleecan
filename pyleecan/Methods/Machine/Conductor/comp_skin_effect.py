from numpy import pi, sqrt, sin


def comp_skin_effect(self, freq, T=20, type_skin_effect=1):
    """Compute the skin effect factor for the conductor

    Parameters
    ----------
    self : Conductor
        an Conductor object
    freq: float
        electrical frequency [Hz]
    T: float
        Conductor temperature [degC]
    type_skin_effect: int
        Model type for skin effect calculation:
        - 1: analytical model (default)

    Returns
    ----------
    Xkr_skinS : float
        skin effect coeff for resistance at freq
    Xke_skinS : float
        skin effect coeff for inductance at freq
    """

    rhosw20 = self.cond_mat.elec.rho
    alphasw = self.cond_mat.elec.alpha
    rho = rhosw20 * (1 + alphasw * (T - 20))
    sigmar = 1 / rho
    mu0 = 4 * pi * 1e-7
    ws = 2 * pi * freq
    Slot = self.parent.parent.slot
    # nsw = len(ws)

    # initialization
    Xkr_skinS = 1
    Xke_skinS = 1

    if type_skin_effect == 1:  # analytical calculations based on Pyrhonen
        # case of preformed rectangular wire CondType11
        if hasattr(self, "Wwire") and hasattr(self, "Hwire"):
            Hwire = self.Hwire
            Wwire = self.Wwire
            Nwppc_rad = self.Nwppc_rad
            Nwppc_tan = self.Nwppc_tan
            W2s = Slot.W2
            # ksi=Hwire*sqrt((1/2)*ws*mu0*sigmar*Nwppc_tan*Wwire/W2s)

            # case of round wire CondType12 - approximation based on rectangular wire formula
        elif hasattr(self, "Wwire") and not hasattr(self, "Hwire"):
            Hwire = self.Wwire
            Wwire = self.Wwire
            Nwppc_tan = self.Nwppc
            Nwppc_rad = self.Nwppc
            Alpha_wind = Slot.comp_angle_active_eq()
            R_wind = Slot.comp_radius_mid_active()
            W2s = 2 * R_wind * sin(Alpha_wind)

            # average resistance factor over the slot
            ksi = Hwire * sqrt((1 / 2) * ws * mu0 * sigmar * Nwppc_tan * Wwire / W2s)
            phi_skin = self.comp_phi_skin(ksi)
            psi_skin = self.comp_psi_skin(ksi)
            phip_skin = self.comp_phip_skin(ksi)
            psip_skin = self.comp_psip_skin(ksi)

            Xkr_skinS = phi_skin + ((Nwppc_rad ** 2 - 1) / 3) * psi_skin
            Xke_skinS = (1 / Nwppc_rad ** 2) * phip_skin + (
                1 - 1 / Nwppc_rad ** 2
            ) * psip_skin

    return Xkr_skinS, Xke_skinS
