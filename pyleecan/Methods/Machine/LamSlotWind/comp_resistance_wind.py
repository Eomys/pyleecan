# -*- coding: utf-8 -*-


def comp_resistance_wind(self):
    """Compute the DC winding resistance per phase at 20°C without skin effect

    Parameters
    ----------
    self : LamSlotWind
        a LamSlotWind object

    Returns
    -------
    R20 : float
        DC winding resistance per phase at 20°C without skin effect
    """

    Zs = self.slot.Zs
    Ntspc = self.winding.comp_Ntspc(Zs)
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

    rhow20 = self.winding.conductor.cond_mat.elec.rho
    # DC winding resistance per phase at 20°C
    R20 = (1.0 / self.winding.Npcpp) * rhow20 * (Ntspc * 2 * Lwht) / (Sact)

    return R20
