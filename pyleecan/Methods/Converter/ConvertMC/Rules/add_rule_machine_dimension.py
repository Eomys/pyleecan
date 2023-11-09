from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_machine_dimension(self):
    """Create and adapt all the rules related to machine dimensions (lam radius,...)
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """

    rules_list = self.rules_list
    rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Stator_Bore"],
            P_obj_path="machine.stator.Rint",
            unit_type="m",
            scaling_to_P=0.5,
        )
    )

    rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Stator_Lam_Dia"],
            P_obj_path="machine.stator.Rext",
            unit_type="m",
            scaling_to_P=0.5,
        )
    )

    # shaft
    rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Shaft_Dia"],
            P_obj_path="machine.rotor.Rint",
            unit_type="m",
            scaling_to_P=0.5,
        )
    )

    if self.is_P_to_other == True:
        rules_list.append(
            RuleEquation(
                param=[
                    {
                        "src": "other",
                        "path": ["[Dimensions]", "Airgap"],
                        "variable": "y",
                    },
                    {
                        "src": "pyleecan",
                        "path": "machine.rotor.Rext",
                        "variable": "a",
                    },
                    {
                        "src": "pyleecan",
                        "path": "machine.stator.Rint",
                        "variable": "b",
                    },
                    {
                        "src": "pyleecan",
                        "path": "machine.rotor.slot.H1",
                        "variable": "c",
                    },
                ],
                unit_type="m",
                scaling_to_P="y= b-a-c ",
            )
        )

    if self.is_P_to_other == False:
        rules_list.append(
            RuleEquation(
                param=[
                    {
                        "src": "other",
                        "path": ["[Dimensions]", "Stator_Bore"],
                        "variable": "y",
                    },
                    {
                        "src": "other",
                        "path": ["[Dimensions]", "Airgap"],
                        "variable": "a",
                    },
                    {
                        "src": "other",
                        "path": ["[Dimensions]", "Magnet_Thickness"],
                        "variable": "b",
                    },
                    {
                        "src": "pyleecan",
                        "path": "machine.rotor.Rext",
                        "variable": "x",
                    },
                ],
                unit_type="m",
                scaling_to_P="y/2-a-b= x ",
            )
        )
    else:
        rules_list.append(
            RuleEquation(
                param=[
                    {
                        "src": "other",
                        "path": ["[Dimensions]", "Stator_Bore"],
                        "variable": "y",
                    },
                    {
                        "src": "other",
                        "path": ["[Dimensions]", "Airgap"],
                        "variable": "a",
                    },
                    {
                        "src": "pyleecan",
                        "path": "machine.rotor.slot.H1",
                        "variable": "b",
                    },
                    {
                        "src": "pyleecan",
                        "path": "machine.rotor.Rext",
                        "variable": "x",
                    },
                ],
                unit_type="m",
                scaling_to_P="y/2-a-b= x ",
            )
        )

    # frame
    rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Motor_Length"],
            P_obj_path="machine.frame.Lfra",
            unit_type="m",
            scaling_to_P=0.5,
        )
    )

    rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Stator_Lam_Dia"],
            P_obj_path="machine.frame.Rint",
            unit_type="m",
            scaling_to_P=0.5,
        )
    )

    rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Housing_Dia"],
            P_obj_path="machine.frame.Rext",
            unit_type="m",
            scaling_to_P=0.5,
        )
    )
