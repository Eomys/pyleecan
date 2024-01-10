from ....Functions.Converter.Utils.ConvertionError import ConvertionError
from .... import __version__
from os import path


def convert_to_P(self, file_path):
    """Convert a "other" file to a Pyleecan machine

    Parameters
    ----------
    self : Convert
        A Convert object
    file_path : str
        A path to "other" file to convert

    Returns
    ---------
    machine : Machine
        The converted pyleecan machine
    """
    self.is_P_to_other = False  # Select rules direction

    # add log
    self.get_logger().info(f"Pyleecan version : {__version__}")
    self.get_logger().info(f"Path file use to convert : {file_path}")
    # conversion file in dict
    self.get_logger().info("Conversion file .mot into dict")
    self.convert_other_to_dict(file_path)

    # To be sure rules_list is empty
    self.rules_list = []

    self.get_logger().info("Conversion dict into obj machine")

    # conversion dict into machine
    self.select_machine_rules()

    comp = 0
    # rule consersion into obj machine
    for rule in self.rules_list:
        try:
            # Uses polymorphism to choose type rule
            self.machine = rule.convert_to_P(
                self.other_dict, self.machine, self.other_unit_dict
            )
        except Exception as e:
            self.get_logger().info(f"Error while running rule {rule.get_name()}:\n{e}")
            # raise ConvertionError(f"Error while running rule {rule.get_name()}:\n{e}")
        comp += 1
    # Get machine name from the .mot file name
    # Example :
    #   file_path = \path\to\your\mot\file\SCIM.mot
    #   => self.machine.name = SCIM
    file_name_extension = path.basename(file_path)
    self.machine.name = path.splitext(file_name_extension)[0]

    self.get_logger().info("End of conversion, obj machine is create\n\n\n")

    return self.machine
