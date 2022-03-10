def comp_resistance_wind(self, T=20):
    """Compute the DC winding resistance per phase without skin effect at average temperature T degC

    Parameters
    ----------
    self : LamSlotWind
        a LamSlotWind object
    T : float
        mean winding temperature [°C], default value is 20°C

    Returns
    -------
    R : float
        DC winding resistance per phase without skin effect [Ohm]
    """

    Zs = self.slot.Zs
    Ntspc = self.winding.comp_Ntsp(Zs)
    # length of the stack including ventilation ducts
    L1vd = self.comp_length()

    # end-winding length on one side for a half-turn
    # TODO implement endwinding length (return Enforced endwinding length)
    Lew = self.winding.comp_length_endwinding()

    # average length of a lamination winding half-turn (one "go" conductor
    # without "return" conductor)
    Lwht = L1vd + 2 * Lew

    # Active surface of conductor
    Sact = self.winding.conductor.comp_surface_active()

    # temperature coefficient and electrical conductivity
    rhow = self.winding.conductor.cond_mat.elec.get_resistivity(T_op=T, T_ref=20)

    # DC winding resistance per phase at specified temperature
    R = (1.0 / self.winding.Npcp) * rhow * (Ntspc * 2 * Lwht) / (Sact)

    return R
