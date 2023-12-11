from ....Classes.MachineIPMSM import MachineIPMSM
from ....Classes.MachineSIPMSM import MachineSIPMSM


def select_machine_rules(self):
    """select the correct machine to add rules
    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    # selection machine type, with implementation in obj machine or in dict
    if self.is_P_to_other:
        self.convert_machine_to_other()
    else:
        self.convert_machine_to_P()
    # add rule present in all machine
    self.add_rule_machine_type()

    # selection motor_type
    if isinstance(self.machine, MachineSIPMSM):
        # particularity for SIPMSM with airgap, changement rule machine dimension
        self.select_SIPMSM_machine_dimension()
        self.select_SIPMSM_rules()

    elif isinstance(self.machine, MachineIPMSM):
        self.add_rule_machine_dimension()
        self.select_IPMSM_rules()
    else:
        raise NotImplementedError("machine is not implemented yet")
