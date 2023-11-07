from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.MachineIPMSM import MachineIPMSM


def convert_machine_type(self):
    # check the direction of conversion
    if self.is_P_to_other == True:  # conversion to pyleecan
        motor_type = type(self.machine).__name__

        if motor_type == "MachineSIPMSM":
            name_machine = "BPM"

        elif motor_type == "MachineIPMSM":
            name_machine = "IM"

        else:
            raise Exception("Conversion of machine doesn't exist")

        if "[Calc_Options]" not in self.other_dict:
            self.other_dict["[Calc_Options]"] = {}
            temp_dict = self.other_dict["[Calc_Options]"]
        temp_dict["Motor_Type"] = name_machine

    else:
        motor_type = self.other_dict["[Calc_Options]"]["Motor_Type"]

        if motor_type == "BPM":
            self.machine = MachineSIPMSM()

        elif motor_type == "IM":
            self.machine = MachineIPMSM()

        else:
            raise Exception("Conversion of machine doesn't exist")
