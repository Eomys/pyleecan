def update_from_ref(self, EEC_ref):
    """Compute the stator winding inductance along d-axis for the equivalent electrical circuit

    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    EEC_ref : EEC_PMSM
        reference EEC_PMSM object

    """

    # Update skin effect
    self.comp_skin_effect()

    # Update stator winding resistance
    R1_ref = EEC_ref.R1 / EEC_ref.Xkr_skinS
    self.comp_R1(R1_ref=R1_ref, T_ref=EEC_ref.Tsta)

    # Update stator winding flux in open-circuit
    self.comp_Phidq_mag()

    # Compute stator winding flux
    self.comp_Phidq()

    # Compute stator winding inductance along d-axis
    self.comp_Ld()

    # Compute stator winding inductance along q-axis
    self.comp_Lq()
