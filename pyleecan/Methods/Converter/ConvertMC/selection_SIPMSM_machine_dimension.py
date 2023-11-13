def selection_SIPMSM_machine_dimension(self):
    if self.is_P_to_other:
        magnet_name = type(self.machine.rotor.slot).__name__
        if (
            magnet_name in ["SlotM11", "SlotM13", "SlotM15"]
            and self.machine.rotor.slot.H0 == 0
        ):
            self.add_rule_machine_dimension_surface_magnet()
        else:
            self.add_rule_machine_dimension()

    else:
        magnet_name = self.other_dict["[Design_Options]"]["BPM_Rotor"]
        if magnet_name in [
            "Surface_Radial",
            "Surface_Parallel",
            "Surface_Breadloaf",
        ]:
            self.add_rule_machine_dimension_surface_magnet()
        else:
            self.add_rule_machine_dimension()
