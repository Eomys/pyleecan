def selection_machine_rules(self):
    """
    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object

    self.is_P_to_other : bool
        True conversion pyleecan to other, False conversion other to pyleecan
    self.rules_list : list
        list with all rules,
    self.other_dict : dict
        A dict with all parameters motor_cad used to conversion or implementation after conversion obj machine
    self.machine : Machine
        A Machine with all parameters pyleecan used to conversion or implementation after conversion dict
    self.file_path : str
        path file use to convert
    """
    # selection machine type, with implementation in obj machine or in dict
    self.convert_machine_type()
    motor_type = type(self.machine).__name__
    # add rule present in all machine
    self.add_rule_machine_type()

    # selecion motor_type
    if motor_type == "MachineSIPMSM":
        self.add_rule_machine_dimension()
        # particularity for BPM with airgap, changemen rule machine dimension
        self.selection_SIPMSM_rules()

    elif motor_type == "MachineIPMSM":
        self.add_rule_machine_dimension()
        self.selection_IM_rules()
