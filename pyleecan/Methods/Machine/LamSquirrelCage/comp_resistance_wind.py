from numpy import pi, sin


def comp_resistance_wind(self, T=20):
    """Computation of the equivalent rotor resistance per phase of a cage winding with 'qs' number of phases

    Parameters
    ----------
    self : LamSquirrelCage
        A LamSquirrelCage object
    T : float
        mean winding temperature [°C], default value is 20°C

    Returns
    -------
    Rrot: float
        resistance of the rotor [Ohm]
    """
    # calculate resistance ring at T degC
    rho = self.ring_mat.elec.get_resistivity(T_op=T, T_ref=20)

    Sring = self.comp_surface_ring()
    lring = self.comp_length_ring()
    Zr = self.get_Zs()
    P = self.get_pole_pair_number()
    # total ring resistance (not yet divided by Zr to take average resistance seen by one bar)
    Rring = rho * lring / Sring

    # calculate resistance rod at T degC
    rho = self.winding.conductor.cond_mat.elec.get_resistivity(T_op=T, T_ref=20)

    # active surface inside slot
    Srod = self.winding.conductor.comp_surface_active()
    # total bar length inside lamination + outside lamination before end ring (#TODO Lewout should be 0 for molded cage, #TODO comp_length() should account for skew shape)
    lrod = self.comp_length() + 2 * self.winding.Lewout
    # bar resistance
    Rrod = rho * lrod / Srod

    # average physical resistance per rotor bar (not yet transfered on stator side, per stator phase)
    Rtot = Rrod + Rring / Zr / (2 * sin(pi * P / Zr) ** 2)

    return Rtot
