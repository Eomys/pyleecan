from .....Classes.CondType12 import CondType12
from .....Classes.CondType11 import CondType11


def convert_conductor_to_other(self):
    """selects step to add rules for conductor in stator

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    conductor_type = self.machine.stator.winding.conductor

    if isinstance(conductor_type, CondType12):
        conductor_name = "AWG_Table"

    elif isinstance(conductor_type, CondType11):
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
