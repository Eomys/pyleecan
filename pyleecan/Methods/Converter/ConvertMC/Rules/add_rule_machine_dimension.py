from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_machine_dimension(rules_list):
    rules_list.append(
        RuleSimple(
            other=["[Dimensions]", "Stator_Bore"],
            pyleecan="machine.stator.Rint",
            unit_type="m",
            scaling_to_P=0.5,
        )
    )

    rules_list.append(
        RuleSimple(
            other=["[Dimensions]", "Stator_Lam_Dia"],
            pyleecan="machine.stator.Rext",
            unit_type="m",
            scaling_to_P=0.5,
        )
    )

    rules_list.append(
        RuleEquation(
            param_other=[
                {
                    "src": "MC",
                    "path": ["[Dimensions]", "Stator_Bore"],
                    "variable": "y",
                },
                {
                    "src": "MC",
                    "path": ["[Dimensions]", "Airgap"],
                    "variable": "a",
                },
            ],
            param_pyleecan=[
                {
                    "src": "pyleecan",
                    "path": "machine.rotor.Rext",
                    "variable": "x",
                }
            ],
            unit_type="m",
            scaling_to_P="y/2+a= x ",
        )
    )

    # shaft
    rules_list.append(
        RuleSimple(
            other=["[Dimensions]", "Shaft_Dia"],
            pyleecan="machine.rotor.Rint",
            unit_type="m",
            scaling_to_P=0.5,
        )
    )

    # frame
    rules_list.append(
        RuleSimple(
            other=["[Dimensions]", "Motor_Length"],
            pyleecan="machine.frame.Lfra",
            unit_type="m",
            scaling_to_P=0.5,
        )
    )

    rules_list.append(
        RuleSimple(
            other=["[Dimensions]", "Stator_Lam_Dia"],
            pyleecan="machine.frame.Rint",
            unit_type="m",
            scaling_to_P=0.5,
        )
    )

    rules_list.append(
        RuleSimple(
            other=["[Dimensions]", "Housing_Dia"],
            pyleecan="machine.frame.Rext",
            unit_type="m",
            scaling_to_P=0.5,
        )
    )

    return rules_list
