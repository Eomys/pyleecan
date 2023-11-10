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
    self.convert_machine_type()
    # add rule present in all machine
    self.add_rule_machine_type()

    # selecion motor_type
    if isinstance(self.machine, MachineSIPMSM):
        self.convert_magnet_type()
        magnet_name = type(self.machine.rotor.slot).__name__

        if magnet_name in ["SlotM11", "SlotM15"] and self.machine.rotor.slot.H0 == 0:
            self.add_rule_machine_dimension_surface_magnet()
        else:
            self.add_rule_machine_dimension()
        # particularity for BPM with airgap, changemen rule machine dimension
        self.selection_SIPMSM_rules()

    elif isinstance(self.machine, MachineIPMSM):
        self.add_rule_machine_dimension()
        self.selection_IM_rules()
    else:
        raise Exception("Not implemented yet")
