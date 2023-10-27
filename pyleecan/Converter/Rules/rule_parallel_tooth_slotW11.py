from pyleecan.Classes.Rules_simple import Rules_simple
from pyleecan.Classes.Rules_equation import Rules_equation


def add_rule_parallel_tooth_slotW11(rules, is_stator):
    print("parallel_tooth_slotW11")

    if is_stator == True:
        select_stator = "stator"
    else:
        select_stator = "rotor"

    rules.append(
        Rules_simple(
            other="Parallel_Tooth",
            pyleecan=f"machine.{select_stator}.slot",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rules.append(
        Rules_simple(
            other="Slot_Opening",
            pyleecan=f"machine.{select_stator}.slot.W0",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rules.append(
        Rules_simple(
            other="Tooth_Width",
            pyleecan=f"machine.{select_stator}.slot.W3",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rules.append(
        Rules_simple(
            other="Tooth_Tip_Depth",
            pyleecan=f"machine.{select_stator}.slot.H0",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rules.append(
        Rules_simple(
            other="Slot_Corner_Radius",
            pyleecan=f"machine.{select_stator}.slot.R1",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rules.append(
        Rules_simple(
            other="Tooth_Tip_Angle",
            pyleecan=f"machine.{select_stator}.slot.H1",
            unit_type="rad",
            scaling_to_P=1,
        )
    )

    rules.append(
        Rules_equation(
            param_other={
                "src": "motor-cad",
                "path": "Slot_Depth",
                "varaible": "y",
            },
            param_pyleecan={
                "src": "pyleecan",
                "path": f"machine.{select_stator}.slot.H2",
                "varaible": "x",
                "src": "pyleecan",
                "path": f"machine.{select_stator}.slot.H1",
                "varaible": "a",
            },
            unit_type="m",
            scaling_to_P="y = a+x",
        )
    )

    return rules
