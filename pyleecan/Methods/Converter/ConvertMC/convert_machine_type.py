from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.MachineIPMSM import MachineIPMSM


def convert_machine_type(self):
    """Update other_dict or machine with the correct machine type

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    # check the direction of conversion
    if self.is_P_to_other == True:  # conversion to MotorCAD
        motor_type = type(self.machine).__name__

        # selection type of machine
        if motor_type == "MachineSIPMSM":
            name_machine = "BPM"

        elif motor_type == "MachineIPMSM":
            name_machine = "IM"

        else:
            raise Exception("Conversion of machine doesn't exist")

        # writting in dict
        if "[Calc_Options]" not in self.other_dict:
            self.other_dict["[Calc_Options]"] = {"Motor_Type": name_machine}
        else:
            self.other_dict["[Calc_Options]"]["Motor_Type"] = name_machine

    else:  # conversion to Pyleecan
        motor_type = self.other_dict["[Calc_Options]"]["Motor_Type"]

        # selection type of machine and creation
        if motor_type == "BPM":
            self.machine = MachineSIPMSM()

        elif motor_type == "IM":
            self.machine = MachineIPMSM()

        # exepction if machine as not an equivalent in pyleecan
        else:
            raise Exception("Conversion of machine doesn't exist")
