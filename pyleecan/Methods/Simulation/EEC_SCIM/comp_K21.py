def comp_K21(self):
    """Compute and set winding transformation ratios

    Parameters
    ----------
    self : EEC_SCIM
        An EEC_SCIM objects
    """

    machine = self.get_machine_from_parent()
    Zr = machine.rotor.slot.Zs
    qs = machine.stator.winding.qs
    # change from rotor frame to stator frame
    xi = machine.stator.winding.comp_winding_factor()
    Ntspc = machine.stator.winding.comp_Ntsp()

    # winding transformation ratios
    K21 = (xi[0] * Ntspc) / (1 * 0.5)  # (xi1[0] * Ntspc1) / (xi2[0] * Ntspc2)  for DFIM
    # transformation ratio from secondary (2, rotor) to primary (1, stator) for impedance in SCIM case
    self.K21Z = (qs / Zr) * K21**2
    # transformation ratio from secondary (2, rotor) to primary (1, stator) for current  in SCIM case
    self.K21I = (qs / Zr) * K21
