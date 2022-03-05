from numpy import isscalar


def comp_parameters(self):
    """Compute the parameters dict for the equivalent electrical circuit:
    resistance, inductance and back electromotive force

    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object

    """

    # Check that OP and temperature are set
    assert self.OP is not None
    assert self.Tsta is not None

    # Update skin effect
    self.comp_skin_effect()

    # Compute stator winding resistance
    if self.R1 is None:
        self.comp_R1()

    # Compute stator winding flux in open-circuit
    if self.Phid_mag is None or self.Phiq_mag is None:
        self.comp_Phidq_mag()

    # Compute stator winding flux
    if self.Phid is None or self.Phiq is None:
        self.comp_Phidq()

    # Compute stator winding inductance along d-axis
    if self.Ld is None:
        self.comp_Ld()

    # Compute stator winding inductance along q-axis
    if self.Lq is None:
        self.comp_Lq()
