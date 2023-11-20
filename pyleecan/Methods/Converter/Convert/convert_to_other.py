def convert_to_other(self, machine):
    """conversion obj machine in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    machine : Machine
        A pyleecan machine

    Returns
    ---------
    other_dict : dict
        A dict with the conversion obj machine
    """
    self.machine = machine
    self.is_P_to_other = True
    self.other_dict = {}
    self.rules_list = []

    self.init_other_unit()

    self.get_logger().info(f"Pyleecan version : 1.5.2")
    self.get_logger().info("Conversion obj machine into dict")
    # conversion machine in dict
    self.convert()

    self.get_logger().info("End of conversion, dict is create")

    self.get_logger()

    return self.other_dict
