from .....Classes.CondType12 import CondType12
from .....Classes.CondType11 import CondType11


def select_conductor_rules(self, is_stator):
    """selects step to add rules for conductor

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """

    # select slot type and add it to obj machine or in dict
    if self.is_P_to_other:
        self.convert_conductor_to_other(is_stator)
    else:
        self.convert_conductor_to_P(is_stator)

    if is_stator:
        conductor = self.machine.stator.winding.conductor
    else:
        conductor = self.machine.rotor.winding.conductor

    # add the correct rule depending on the rotor
    if isinstance(conductor, CondType12):
        self.add_rule_condtype12(is_stator)

    elif isinstance(conductor, CondType11):
        self.add_rule_condtype11(is_stator)

    else:
        raise TypeError("Error type of conductor doesn't exist")

    if is_stator:
        self.select_material_rules("machine.stator.winding.conductor.cond_mat")
        self.get_logger().info("Insulator material, Not Implemented")
        # self.select_material_rules("machine.stator.winding.conductor.ins_mat")

    else:
        self.select_material_rules("machine.rotor.winding.conductor.cond_mat")
        # self.select_material_rules("machine.rotor.winding.conductor.ins_mat")
        self.get_logger().info("Insulator material, Not Implemented")
