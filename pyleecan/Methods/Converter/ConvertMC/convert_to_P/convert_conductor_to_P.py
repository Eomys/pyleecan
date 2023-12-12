from .....Classes.CondType12 import CondType12
from .....Classes.CondType13 import CondType13


def convert_conductor_to_P(self):
    """selects step to add rules for conductor in stator

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    conductor_type = self.other_dict["[Winding_Design]"]["Wire_Type"]

    if conductor_type == "AWG_Table":
        self.machine.stator.winding.conductor = CondType12()

    elif conductor_type == "Rectangular":
        self.machine.stator.winding.conductor = CondType13()
    else:
        raise NotImplementedError(
            f"Type of conductor {conductor_type} has not equivalent or has not implement"
        )

    self.get_logger().info(
        f"Conversion {conductor_type} into {self.machine.stator.winding.conductor.__class__.__name__}"
    )
