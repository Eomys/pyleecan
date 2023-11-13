from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.MachineSCIM import MachineSCIM


def convert_machine_type_P(self):
    """Update other_dict or machine with the correct machine type

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    # conversion to Pyleecan
    motor_type = self.other_dict["[Calc_Options]"]["Motor_Type"]
    magnet_type = self.other_dict["[Design_Options]"]["BPM_Rotor"]

    # selection type of machine and creation
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
            self.machine = MachineIPMSM()

    elif motor_type == "IM":
        self.machine = MachineSCIM()

    # exepction if machine as not an equivalent in pyleecan
    else:
        raise Exception("Conversion of machine doesn't exist")
