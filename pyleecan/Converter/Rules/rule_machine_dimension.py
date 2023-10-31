from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_machine_dimension(rules):
    rules.append(
        RuleSimple(
            other=["[Dimensions]", "Stator_Bore"],
            pyleecan="machine.stator.Rint",
            unit_type="m",
            scaling_to_P=0.5,
        )
    )

    rules.append(
        RuleSimple(
            other=["[Dimensions]", "Stator_Lam_Dia"],
            pyleecan="machine.stator.Rext",
            unit_type="m",
            scaling_to_P=0.5,
        )
    )

    rules.append(
        RuleEquation(
            param_other=[
                {
                    "src": "motor-cad",
                    "path": "[Dimension]" "Stator_Bore",
                    "varaible": "y",
                },
                {
                    "src": "motor-cad",
                    "path": "[Dimension]" ".0",
                    "varaible": "a",
                },
            ],
            param_pyleecan=[
                {
                    "src": "pyleecan",
                    "path": "machine.rotor.Rext",
                    "varaible": "x",
                }
            ],
            unit_type="m",
            scaling_to_P="y/2+a = x",
        )
    )

    # shaft
    rules.append(
        RuleSimple(
            other=["[Dimensions]", "Shaft_Dia"],
            pyleecan="machine.rotor.Rint",
            unit_type="m",
            scaling_to_P=0.5,
        )
    )

    # frame
    rules.append(
        RuleSimple(
            other=["[Dimensions]", "Motor_Length"],
            pyleecan="machine.frame.Lfra",
            unit_type="m",
            scaling_to_P=0.5,
        )
    )

    rules.append(
        RuleSimple(
            other=["[Dimensions]", "Stator_Lam_Dia"],
            pyleecan="machine.frame.Rint",
            unit_type="m",
            scaling_to_P=0.5,
        )
    )

    rules.append(
        RuleSimple(
            other=["[Dimensions]", "Housing_Dia"],
            pyleecan="machine.frame.Rext",
            unit_type="m",
            scaling_to_P=0.5,
        )
    )

    return rules
