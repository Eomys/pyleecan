def update_from_ref(self, LUT_ref):
    """Update the equivalent circuit according to the LUT

    Parameters
    ----------
    self : EEC_SCIM
        an EEC_SCIM object
    LUT_ref : LUTslip
        reference LUTslip object
    """

    # Update skin effect to OP/T
    self.comp_skin_effect()
    self.comp_K21()

    eec_ref = LUT_ref.eec
    Tsta_ref, Trot_ref = eec_ref.Tsta, eec_ref.Trot
    Xkr_skinS_ref, Xke_skinS_ref = eec_ref.Xkr_skinS, eec_ref.Xke_skinS
    Xkr_skinR_ref, Xke_skinR_ref = eec_ref.Xkr_skinR, eec_ref.Xke_skinS

    # Compute stator winding resistance
    if eec_ref.R1 is None:
        self.comp_R1()
    else:
        self.comp_R1(R1_ref=eec_ref.R1 / Xkr_skinS_ref, T_ref=Tsta_ref)

    # Compute stator winding inductance
    if eec_ref.L1 is None:
        self.comp_L1()
    else:
        self.comp_L1(L1_ref=eec_ref.L1 / Xke_skinS_ref)

    # Iron loss resistance
    if self.Rfe is None:
        self.Rfe = 1e12  # TODO calculate (or estimate at least)

    # Compute rotor winding resistance
    if eec_ref.R2 is None:
        self.comp_R2()
    else:
        self.comp_R2(R2_ref=eec_ref.R2 / Xkr_skinR_ref, T_ref=Trot_ref)

    # Compute rotor winding inductance
    if eec_ref.L2 is None:
        self.comp_L2()
    else:
        self.comp_L2(L2_ref=eec_ref.L2 / Xke_skinR_ref)

    # Get Im/Lm tables from LUT
    if eec_ref.Lm_table is None or eec_ref.Im_table is None:
        raise Exception("LUT must contains Lm/Im tables to solve EEC_SCIM")
    self.Lm_table = eec_ref.Lm_table / Xke_skinS_ref * self.Xke_skinS
    self.Im_table = eec_ref.Im_table
