from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.Classes.HoleM57 import HoleM57
from pyleecan.Classes.HoleM60 import HoleM60
from pyleecan.Classes.HoleM61 import HoleM61
from pyleecan.Classes.HoleM62 import HoleM62
from pyleecan.Classes.HoleM63 import HoleM63


def selection_hole_rules(self, is_stator):
    """selection step to add rules for hole and add hole into obj machine

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
        if (
            isinstance(self.machine.rotor.hole[hole_id], HoleM62)
            and self.machine.rotor.hole[hole_id].W0_is_rad == False
        ):
            self.add_rule_embedded_parallel_holeM62(is_stator, hole_id)

        elif (
            isinstance(self.machine.rotor.hole[hole_id], HoleM62)
            and self.machine.rotor.hole[hole_id].W0_is_rad == True
        ):
            self.add_rule_embedded_radial_holeM62(is_stator, hole_id)

        elif (
            isinstance(self.machine.rotor.hole[hole_id], HoleM63)
            and self.machine.rotor.hole[hole_id].top_flat == True
        ):
            self.add_rule_interior_flat_simple_holeM63(is_stator, hole_id)

        elif (
            isinstance(self.machine.rotor.hole[hole_id], HoleM63)
            and self.machine.rotor.hole[hole_id].top_flat == False
        ):
            self.add_rule_embedded_breadleoaf_holeM63(is_stator, hole_id)

        elif isinstance(self.machine.rotor.hole[hole_id], HoleM61):
            self.add_rule_interior_U_shape_holeM61(is_stator, hole_id)

        elif isinstance(self.machine.rotor.hole[hole_id], HoleM52):
            self.add_rule_interior_flat_wed_holeM52(is_stator, hole_id)

        elif isinstance(self.machine.rotor.hole[hole_id], HoleM60):
            self.add_rule_interior_V_simple_holeM60(is_stator, hole_id)

        elif isinstance(self.machine.rotor.hole[hole_id], HoleM57):
            self.add_rule_interior_V_web_holeM57(is_stator, hole_id)
