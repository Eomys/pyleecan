def comp_L1(self, L1_ref=None):
    """Compute and set the Stator phase inductance for the equivalent electrical circuit

    Parameters
    ----------
    self : EEC_SCIM
        an EEC_SCIM object
    L1_ref : float
        reference inductance

    """

    if L1_ref is None:
        raise Exception("L1 parameter for EEC_SCIM must be enforced !")
        if self.type_comp_Lr == 1:
            # analytic calculation
            # L10 = machine.stator.slot.comp_inductance_leakage_ANL() #TODO
            pass
        else:
            # FEA calculation
            # L1 = machine.rotor.slot.comp_inductance_leakage_FEA() #TODO
            pass

    self.L1 = L1_ref * self.Xke_skinS
