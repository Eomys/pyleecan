from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.Classes.HoleM57 import HoleM57
from pyleecan.Classes.HoleM60 import HoleM60
from pyleecan.Classes.HoleM61 import HoleM61
from pyleecan.Classes.HoleM62 import HoleM62
from pyleecan.Classes.HoleM63 import HoleM63


def select_hole_rules(self, is_stator):
    """select step to add rules for hole and add hole into obj machine

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """
    if is_stator:
        raise ValueError("Hole are just in rotor")

    if self.is_P_to_other:
        self.convert_hole_to_other()

    else:
        self.convert_hole_to_P()

    for hole_id, hole in enumerate(self.machine.rotor.hole):
        # add the correct rule depending on the hole
        if isinstance(hole, HoleM62) and not hole.W0_is_rad:
            self.add_rule_embedded_parallel_holeM62(hole_id)

        elif isinstance(hole, HoleM62) and hole.W0_is_rad:
            self.add_rule_embedded_radial_holeM62(hole_id)

        elif isinstance(hole, HoleM63) and hole.top_flat == True:
            self.add_rule_interior_flat_simple_holeM63(hole_id)

        elif isinstance(hole, HoleM63) and hole.top_flat == False:
            self.add_rule_embedded_breadleoaf_holeM63(hole_id)

        elif isinstance(hole, HoleM61):
            self.add_rule_interior_U_shape_holeM61(hole_id)

        elif isinstance(hole, HoleM52):
            self.add_rule_interior_flat_web_holeM52(hole_id)

        elif isinstance(hole, HoleM60):
            self.add_rule_interior_V_simple_holeM60(hole_id)

        elif isinstance(hole, HoleM57):
            self.add_rule_interior_V_web_holeM57(hole_id)
