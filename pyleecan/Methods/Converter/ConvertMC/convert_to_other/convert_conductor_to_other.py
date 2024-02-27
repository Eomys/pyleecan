from .....Classes.CondType12 import CondType12
from .....Classes.CondType13 import CondType13


def convert_conductor_to_other(self, is_stator):
    """selects step to add rules for conductor

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    # selection if conductor is in stator or rotor
    if is_stator:
        conductor_type = self.machine.stator.winding.conductor
    else:
        conductor_type = self.machine.rotor.winding.conductor

    if isinstance(conductor_type, CondType12):
        conductor_name = "AWG_Table"

    elif isinstance(conductor_type, CondType13):
        conductor_name = "Rectangular"
    else:
        raise NotImplementedError(
            f"Type of conductor {conductor_type.__class__.__name__} has not equivalent or has not implement"
        )

    # writting in dict
    if "[Winding_Design]" not in self.other_dict:
        self.other_dict["[Winding_Design]"] = {"Wire_Type": conductor_name}
    else:
        self.other_dict["[Winding_Design]"]["Wire_Type"] = conductor_name

    self.get_logger().info(
        f"Conversion {conductor_type.__class__.__name__} into {conductor_name}"
    )
