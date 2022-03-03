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

    if R1_ref is None:
        # Compute at correct temperature
        R1_ref = machine.stator.comp_resistance_wind(T=self.Tsta)
    elif T_ref is None:
        # Assume that the reference match EEC temperature (should not happend)
        pass
    else:  # Adpat the temperature
        # Get stator conductor
        machine = self.get_machine_from_parent()
        CondS = machine.stator.winding.conductor

        # Compute temperature effect on stator side
        Tfact1 = CondS.comp_temperature_effect(T_op=self.Tsta, T_ref=T_ref)
        R1_ref = R1_ref * Tfact1
    # Stator resistance
    self.R1 = R1_ref * self.Xkr_skinS
