def comp_R2(self, R2_ref=None, T_ref=None):
    """Compute and set the rotor phase resistance for the equivalent electrical circuit

    Parameters
    ----------
    self : EEC_SCIM
        an EEC_SCIM object
    R2_ref : float
        reference resistance
    T_ref : float
        reference temperature

    """

    if R2_ref is None:
        # Compute at correct temperature
        machine = self.get_machine_from_parent()
        R2_ref = machine.rotor.comp_resistance_wind(T=self.Trot)
        # putting resistance on stator side in EEC
        if self.K21Z is None:
            self.comp_K21()
        R2_ref = R2_ref * self.K21Z
    elif T_ref is None:
        # Assume that the reference match EEC temperature (should not happend)
        pass
    else:  # Adpat the temperature
        # Get rotor conductor
        machine = self.get_machine_from_parent()
        CondR = machine.rotor.winding.conductor

        # Compute temperature effect on stator side
        Tfact2 = CondR.comp_temperature_effect(T_op=self.Trot, T_ref=T_ref)
        R2_ref = R2_ref * Tfact2
    # Stator resistance
    self.R2 = R2_ref * self.Xkr_skinR
