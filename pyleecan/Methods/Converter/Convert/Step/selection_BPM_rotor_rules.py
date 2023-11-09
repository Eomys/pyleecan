def selection_BPM_rotor_rules(self):
    """selection step to add rules for slot

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """
    BPM_rotor = self.other_dict["[Design_Options]"]["BPM_Rotor"]

    if BPM_rotor == "Surface_Radial":
        pass
    elif BPM_rotor == "Surface_Parallel":
        pass
    elif BPM_rotor == "Surface_Breadloaf":
        pass
    elif BPM_rotor == "Inset_Radial":
        pass
    elif BPM_rotor == "Inset_Parallel":
        pass
    elif BPM_rotor == "Inset_Breadloaf":
        pass
    elif BPM_rotor == "Embedded_Radial":
        pass
    elif BPM_rotor == "Embedded_Parallel":
        pass
    elif BPM_rotor == "Embedded_Breadloaf":
        pass
    elif BPM_rotor == "Interior_Flat(web)":
        pass
    elif BPM_rotor == "Interior_Flat(simple)":
        pass
    elif BPM_rotor == "Interior_U-Shape":
        pass
    elif BPM_rotor == "Spoke":
        pass

    return self.rules_list
