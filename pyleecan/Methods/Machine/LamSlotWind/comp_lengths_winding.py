def comp_lengths_winding(self):
    """Compute the lengths of the Lamination's Winding.
    - Lwtot : total length of lamination winding incl. end-windings and
    radial ventilation ducts [m].
    - Lwact : active length of lamination winding excl. end-windings and
    radial ventilation ducts [m].
    - Lewt : total end-winding length [m].
    - Lew : end-winding length on one side for a half-turn
    - Lwvent : length of lamination winding in the radial ventilation ducts [m]
    Parameters
    ----------
    self: LamSlotWind
        a LamSlotWind object
    Returns
    -------
    L_dict: dict
        Dictionary of the length (Lwtot, Lwact, Lew, Lwvent)
    """

    # length of the stack including ventilation ducts
    L1vd = self.comp_length()

    # end-winding length on one side for a half-turn
    Lew = self.winding.comp_length()

    # total end-winding length
    Ntspc = self.winding.comp_Ntsp(self.get_Zs())
    qb = self.comp_number_phase_eq()
    Lewt = qb * Ntspc * self.winding.Npcp * 4 * Lew

    # average length of a lamination winding half-turn (one "go" conductor
    # without "return" conductor)
    Lwht = L1vd + 2 * Lew

    # total length of lamination winding incl. end windings [m]
    Lwtot = qb * Ntspc * self.winding.Npcp * 2 * Lwht

    # Active length of lamination winding excl. end windings and radial
    # ventilation duct [m]
    Lwact = qb * Ntspc * self.winding.Npcp * 2 * self.L1

    # length of lamination winding in the radial ventilation duct [m]
    if self.Nrvd is None or self.Wrvd is None:
        Lwvent = 0
    else:
        Lwvent = qb * Ntspc * self.winding.Npcp * 2 * self.Nrvd * self.Wrvd

    return {
        "Lwtot": Lwtot,
        "Lwht": Lwht,
        "Lwact": Lwact,
        "Lewt": Lewt,
        "Lwvent": Lwvent,
        "Lew": Lew,
    }
