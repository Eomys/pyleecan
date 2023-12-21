from ....Classes.MachineIPMSM import MachineIPMSM
from ....Classes.MachineSIPMSM import MachineSIPMSM
from ....Classes.MachineSCIM import MachineSCIM
from ....Classes.MachineWRSM import MachineWRSM


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
    # add machine rule. Independante of the machine type and of the conversion direction
    self.add_rule_machine_type()

    # selection motor_type
    if isinstance(self.machine, MachineSIPMSM):
        # particularity for SIPMSM with airgap, rule to change machine dimension
        self.select_SIPMSM_machine_dimension()
        self.select_SIPMSM_rules()

    elif isinstance(self.machine, MachineIPMSM):
        self.add_rule_machine_dimension()
        self.select_IPMSM_rules()

    elif isinstance(self.machine, MachineSCIM):
        self.add_rule_machine_dimension()
        self.select_SCIM_rules()

    elif isinstance(self.machine, MachineWRSM):
        self.add_rule_machine_dimension()
        self.select_WRSM_rules()

    else:
        raise NotImplementedError("machine is not implemented yet")

    self.select_material_rules("machine.shaft.mat_type")
    self.select_material_rules("machine.frame.mat_type")
