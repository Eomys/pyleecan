def convert(self, other_unit_dict):
    """convert the file .mot in machine pyleecan or vice versa
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

    self.selection_machine_rules()

    # conversion rules list
    if self.is_P_to_other == False:  # conversion to Pyleecan
        for rule in self.rules_list:
            # utilisation polymorphism to choose type rule
            self.machine = rule.convert_to_P(
                self.other_dict, self.machine, other_unit_dict
            )
        # self.machine.stator.plot()
        # self.machine.plot()
        print("Done")
        return self.machine

    else:  # conversion to other
        for rule in self.rules_list:
            self.other_dict = rule.convert_to_other(
                self.other_dict, self.machine, other_unit_dict
            )
        print("Done")
        return self.other_dict
