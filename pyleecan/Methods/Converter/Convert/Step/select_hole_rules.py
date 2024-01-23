from .....Classes.HoleM52 import HoleM52
from .....Classes.HoleM57 import HoleM57
from .....Classes.HoleM60 import HoleM60
from .....Classes.HoleM61 import HoleM61
from .....Classes.HoleM62 import HoleM62
from .....Classes.HoleM63 import HoleM63


def select_hole_rules(self, is_stator):
    """selects step to add rules for hole and adds hole into obj machine

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """

    # In Pyleecan :
    #   Multiple set of notch
    #   Multiple type of notch
    # In Motor-Cad :
    #   Multi set of notch  (Only for some type)
    #   Single type of notch

    if is_stator:
        raise ValueError("Hole are just in rotor")

    if self.is_P_to_other:
        self.convert_hole_to_other()
    else:
        self.convert_hole_to_P()

    # Number of magnet in Hole
    dict_nb_magnet = {
        "HoleM52": 1,
        "HoleM57": 2,
        "HoleM60": 2,
        "HoleM61": 4,
        "HoleM62": 1,
        "HoleM63": 1,
    }

    # The counter solve the case where self.machine.rotor.hole = [HoleM62, HoleM57, HoleM62]
    hole_id = 0
    for hole in self.machine.rotor.hole:
        # Ensure that all the added rules are for the same slot type
        if not isinstance(hole, self.machine.rotor.hole[0].__class__):
            continue

        number_magnet = dict_nb_magnet[self.machine.rotor.hole[0].__class__.__name__]

        # add the correct rule depending on the hole
        if isinstance(hole, HoleM62):
            self.add_rule_holeM62(hole_id)

        elif isinstance(hole, HoleM63):
            self.add_rule_holeM63(hole_id)

        elif isinstance(hole, HoleM61):
            self.add_rule_holeM61(hole_id)

        elif isinstance(hole, HoleM52):
            self.add_rule_holeM52(hole_id)

        elif isinstance(hole, HoleM57):
            self.add_rule_holeM57(hole_id)

        elif isinstance(hole, HoleM60):
            self.add_rule_holeM60(hole_id)

        for number in range(number_magnet):
            self.select_material_rules(
                f"machine.rotor.hole[{hole_id}].magnet_{number}.mat_type"
            )

            # set type_magnetization at parallel (type_magnetization = 1)
            path = f"self.machine.rotor.hole[{hole_id}].magnet_{number}"
            setattr(
                eval(path),
                "type_magnetization",
                1,
            )

        hole_id += 1
