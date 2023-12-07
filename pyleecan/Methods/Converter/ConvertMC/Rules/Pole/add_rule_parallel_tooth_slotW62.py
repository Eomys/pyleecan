from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_parallel_tooth_slotW62(self, hole_id):
    """Create and adapt all the rules related to Hole
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", f"Pole_Depth"],
            P_obj_path=f"machine.rotor.pole.H0",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", f"Rotor_Pole_Angle"],
            P_obj_path=f"machine.rotor.pole.H1",
            unit_type="deg",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    # je ne connais pas le paramètre utilisé dans MC
    """ 
    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", f"Rotor_Coil_Width"],
            P_obj_path=f"machine.rotor.pole.W2",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )"""

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", f"Pole_Tip_Depth"],
            P_obj_path=f"machine.rotor.pole.H2",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", f"Pole_Width"],
            P_obj_path=f"machine.rotor.pole.W0",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleEquation(
            param=[
                {
                    "src": "other",
                    "path": ["[Dimensions]", "Pole_Tip_Width"],
                    "variable": "y",
                },
                {
                    "src": "other",
                    "path": ["[Dimensions]", "Pole_Width"],
                    "variable": "a",
                },
                {
                    "src": "pyleecan",
                    "path": f"machine.rotor.pole.W1",
                    "variable": "x",
                },
            ],
            unit_type="m",
            equation="2*y + a = x",
            file_name=__file__,
        )
    )
