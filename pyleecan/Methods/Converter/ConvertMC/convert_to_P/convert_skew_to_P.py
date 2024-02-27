from .....Classes.Skew import Skew


def convert_skew_to_P(self):
    """Selects correct skew and implements it in obj machine

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    # conversion to pyleecan
    if "SkewType" in self.other_dict["[Magnetics]"]:
        skew_type = self.other_dict["[Magnetics]"]["SkewType"]
    else:
        skew_type = 0

    if skew_type == 2:
        # initialisation to set the skew in rotor
        self.machine.rotor.skew = Skew()

        self.get_logger().info(f"Conversion skew ")
