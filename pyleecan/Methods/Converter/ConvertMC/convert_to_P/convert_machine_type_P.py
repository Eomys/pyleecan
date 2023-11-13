from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.MachineIPMSM import MachineIPMSM


def convert_machine_type_P(self):
    """Update other_dict or machine with the correct machine type

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    # conversion to Pyleecan
    motor_type = self.other_dict["[Calc_Options]"]["Motor_Type"]

    # selection type of machine and creation
    if motor_type == "BPM":
        self.machine = MachineSIPMSM()

    elif motor_type == "IM":
        self.machine = MachineIPMSM()

    # exepction if machine as not an equivalent in pyleecan
    else:
        raise Exception("Conversion of machine doesn't exist")
