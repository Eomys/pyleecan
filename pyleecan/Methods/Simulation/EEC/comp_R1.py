def comp_R1(self, R1_ref=None, T_ref=None):
    """Compute the stator phase resistance for the equivalent electrical circuit

    Parameters
    ----------
    self : EEC
        an EEC object
    R1_ref : float
        reference resistance
    T_ref : float
        reference temperature

    """

    if T_ref is None:
        T_ref = self.Tsta
    if R1_ref is None:
        R1_ref = machine.stator.comp_resistance_wind(T=self.Tsta)

    # Get stator conductor
    machine = self.get_machine_from_parent()
    CondS = machine.stator.winding.conductor

    # Compute temperature effect on stator side
    Tfact1 = CondS.comp_temperature_effect(T_op=self.Tsta, T_ref=T_ref)

    # Stator resistance
    self.R1 = R1_ref * Tfact1 * self.Xkr_skinS
