from ....Functions.Converter.Utils.ConvertionError import ConvertionError
from .... import __version__


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

    self.get_logger().info(f"Pyleecan version : {__version__}")
    self.get_logger().info("Conversion obj machine into dict")

    # conversion machine in dict
    self.select_machine_rules()

    # conversion rule in dict
    for rule in self.rules_list:
        try:
            self.other_dict = rule.convert_to_other(
                self.other_dict, self.machine, self.other_unit_dict
            )
        except Exception as e:
            raise ConvertionError(f"Error while running rule {rule.get_name()}:\n{e}")

    self.get_logger().info("End of conversion, dict is create")

    self.get_logger()

    return self.other_dict
