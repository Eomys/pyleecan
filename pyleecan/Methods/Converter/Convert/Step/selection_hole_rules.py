from pyleecan.Classes.HoleM62 import HoleM62
from pyleecan.Classes.HoleM63 import HoleM63


def selection_hole_rules(self, is_stator):
    """selection step to add rules for slot

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """
    if self.is_P_to_other:
        number_hole = self.convert_hole_type_MC()

    else:
        number_hole = self.convert_hole_type_P()

    for hole_id in range(number_hole):
        # add the correct rule depending on the hole
        if isinstance(self.machine.rotor.hole[hole_id], HoleM62):
            self.add_rule(is_stator, hole_id)

        elif isinstance(self.machine.rotor.hole[hole_id], HoleM63):
            self.add_rule_(is_stator, hole_id)
