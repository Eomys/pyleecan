from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.Notch import Notch
from pyleecan.Classes.NotchEvenDist import NotchEvenDist
from pyleecan.Classes.SlotM19 import SlotM19


def selection_lamination_rules(self, is_stator):
    """selection step to add rules for lamination

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """
    if is_stator == True:
        lam_name = "Stator"
    else:
        lam_name = "Rotor"

    # sélection of number and type layers
    if not self.is_P_to_other:
        try:
            type_duct = self.other_dict["[Through_Vent]"][f"{lam_name}DuctType"]
        except:
            type_duct = 0

        if type_duct != 0:
            self.convert_duct_type_P(is_stator)

        else:
            print(f"not axial cooling duct at {lam_name}")

        if is_stator == False:
            try:
                Notch_depth = self.other_dict["[Dimensions]"]["PoleNotchDepth"]
            except:
                Notch_depth = 0

            if Notch_depth != 0:
                self.machine.rotor.notch.append(Notch())
                self.machine.rotor.notch[0] = NotchEvenDist()
                self.machine.rotor.notch[0].notch_shape = SlotM19()

                self.add_rule_notch(is_stator)

                self.get_logger().info("approximation of notch for slotM19")

        else:
            self.get_logger().info(
                "Motor-CAD have not possibility to add notch in stator"
            )
