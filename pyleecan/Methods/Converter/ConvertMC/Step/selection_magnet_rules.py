from pyleecan.Methods.Converter.ConvertMC.Rules.Rotor_Magnet.add_rule_surface_radial_slotM11 import (
    add_rule_surface_radial_slotM11,
)


def selection_magnet_rules(self, is_stator):
    if self.is_P_to_other:
        magnet_type = type(self.machine.rotor.slot).__name__

    else:
        magnet_type = self.other_dict["[Design_Options]"]["BPM_Rotor"]

    # add the correct rule depending on the slot
    if magnet_type in ["Surface_Radial", "SlotM11"]:
        add_rule_surface_radial_slotM11(self, is_stator)
