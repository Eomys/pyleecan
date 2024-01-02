from .....Classes.Skew import Skew


def convert_skew_to_P(self):
    """Selects correct skew and implements it in obj machine

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    # conversion to pyleecan
    skew_type = self.other_dict["[Magnetics]"]["SkewType"]

    if skew_type == 2:
        # initialisation to set the skew in rotor
        self.machine.rotor.skew = Skew()

        self.get_logger().info(f"Conversion skew ")
