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
    self.get_logger().info(f"Pyleecan version : 1.5.2")
    self.get_logger().info(f"Path file use to convert : {file_path}")
    # conversion file in dict
    self.get_logger().info("Conversion file .mot into dict")
    self.convert_other_to_dict(file_path)

    # To be sure rules_list is empty
    self.rules_list = []

    self.get_logger().info("Conversion dict into obj machine")
    # conversion dict into machine
    self.convert()

    # add name for machine
    list_path = file_path.split(".")
    name = list_path[-2].split("/")
    self.machine.name = name[-1]

    self.get_logger().info("End of conversion, obj machine is create\n\n\n")

    return self.machine
