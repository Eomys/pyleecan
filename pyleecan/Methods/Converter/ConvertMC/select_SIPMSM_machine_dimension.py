def select_SIPMSM_machine_dimension(self):
    """select the correct rule for machine dimension
    if the slot is in surface conversion to machine dimension is different

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    if self.is_P_to_other:
        magnet_name = type(self.machine.rotor.slot).__name__
        if (
            magnet_name in ["SlotM11", "SlotM13", "SlotM15"]
            and self.machine.rotor.slot.H0 == 0
        ):
            self.add_rule_machine_dimension_surface_magnet()
        else:
            # "HoleM62"
            # "HoleM63"
            # "HoleM52"
            # "HoleM60"
            # "HoleM57"
            # "HoleM61"
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
            # "Embedded_Parallel"
            # "Embedded_Radial"
            # "Embedded_Breadleaof"
            # "Interior_Flat(simple)"
            # "Interior_Flat(web)"
            # "Interior_V(simple)"
            # "Interior_V(web)"
            # "Interior_U-Shape"

            self.add_rule_machine_dimension()
