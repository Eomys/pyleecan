from ....Classes.MachineIPMSM import MachineIPMSM
from ....Classes.MachineSIPMSM import MachineSIPMSM


def selection_machine_rules(self):
    """select the correct machine to add rules
    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    # selection machine type, with implementation in obj machine or in dict
    if self.is_P_to_other:
        self.convert_machine_type_MC()
    else:
        self.convert_machine_type_P()
    # add rule present in all machine
    self.add_rule_machine_type()

    # selecion motor_type
    if isinstance(self.machine, MachineSIPMSM):
        # particularity for SIPMSM with airgap, changement rule machine dimension
        self.selection_SIPMSM_machine_dimension()
        self.selection_SIPMSM_rules()

    elif isinstance(self.machine, MachineIPMSM):
        self.add_rule_machine_dimension()
        self.selection_IPMSM_rules()
    else:
        raise Exception("Not implemented yet")
