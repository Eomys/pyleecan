def comp_L2(self, L2_ref=None):
    """Compute and set the Rotor phase inductance for the equivalent electrical circuit

    Parameters
    ----------
    self : EEC_SCIM
        an EEC_SCIM object
    L2_ref : float
        reference inductance

    """

    if L2_ref is None:
        raise Exception("L2 parameter for EEC_SCIM must be enforced !")
        if self.type_comp_Lr == 1:
            # analytic calculation
            # L2 = machine.rotor.slot.comp_inductance_leakage_ANL() #TODO
            pass
        else:
            # FEA calculation
            # L2 = machine.rotor.slot.comp_inductance_leakage_FEA() #TODO
            pass

    self.L2 = L2_ref * self.Xke_skinR
