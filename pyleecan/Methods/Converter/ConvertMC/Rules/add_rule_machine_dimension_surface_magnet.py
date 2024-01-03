from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation


def add_rule_machine_dimension_surface_magnet(self):
    """Create and adapt all the rules related to machine dimensions (lam radius,...)
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Stator_Bore"],
            P_obj_path="machine.stator.Rint",
            unit_type="m",
            scaling_to_P=0.5,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Stator_Lam_Dia"],
            P_obj_path="machine.stator.Rext",
            unit_type="m",
            scaling_to_P=0.5,
            file_name=__file__,
        )
    )

    # shaft
    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Shaft_Dia"],
            P_obj_path="machine.rotor.Rint",
            unit_type="m",
            scaling_to_P=0.5,
            file_name=__file__,
        )
    )
    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Shaft_Dia"],
            P_obj_path="machine.shaft.Drsh",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    if self.is_P_to_other == True:
        self.rules_list.append(
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
                equation="y= b-a-c ",
                file_name=__file__,
            )
        )

    if not self.is_P_to_other:
        self.rules_list.append(
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
                equation="y/2-a-b= x ",
                file_name=__file__,
            )
        )
    else:
        self.rules_list.append(
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
                equation="y/2-a-b= x ",
                file_name=__file__,
            )
        )

    # frame
    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Motor_Length"],
            P_obj_path="machine.frame.Lfra",
            unit_type="m",
            scaling_to_P=0.5,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Stator_Lam_Dia"],
            P_obj_path="machine.frame.Rint",
            unit_type="m",
            scaling_to_P=0.5,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Housing_Dia"],
            P_obj_path="machine.frame.Rext",
            unit_type="m",
            scaling_to_P=0.5,
            file_name=__file__,
        )
    )
