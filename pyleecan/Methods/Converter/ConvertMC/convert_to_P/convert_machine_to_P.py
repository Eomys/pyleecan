from .....Classes.MachineSIPMSM import MachineSIPMSM
from .....Classes.MachineIPMSM import MachineIPMSM
from .....Classes.MachineSCIM import MachineSCIM
from .....Classes.MachineWRSM import MachineWRSM


def convert_machine_to_P(self):
    """Update machine with the correct machine type

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    # conversion to Pyleecan
    motor_type = self.other_dict["[Calc_Options]"]["Motor_Type"]
    magnet_type = self.other_dict["[Design_Options]"]["BPM_Rotor"]

    # select machine type abd create it
    if motor_type == "BPM":
        if magnet_type in [
            "Surface_Radial",
            "Surface_Parallel",
            "Surface_Breadloaf",
            "Inset_Radial",
            "Inset_Parallel",
            "Inset_Breadloaf",
        ]:
            self.machine = MachineSIPMSM()
        else:
            # "Embedded_Parallel"
            # "Embedded_Radial"
            # "Embedded_Breadleaof"
            # "Interior_Flat(simple)"
            # "Interior_Flat(web)"
            # "Interior_V(simple)"
            # "Interior_V(web)"
            # "Interior_U-Shape"

            self.machine = MachineIPMSM()

    elif motor_type == "IM":
        self.machine = MachineSCIM()

    elif motor_type == "SYNC":
        self.machine = MachineWRSM()

    else:
        # exception if machine as not an equivalent in pyleecan
        raise NotImplementedError(
            f"Machine {motor_type} has not equivalent in pyleecan or has not been implementated"
        )

    self.get_logger().info(
        f"Conversion {motor_type} into {type(self.machine).__name__}"
    )
