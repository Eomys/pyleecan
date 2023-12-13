from .....Classes.VentilationCirc import VentilationCirc
from .....Classes.VentilationPolar import VentilationPolar
from .....Classes.VentilationTrap import VentilationTrap


def select_duct_rules(self, is_stator):
    """selects step to add rules for duct

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
    #   Multi set of notch
    #   Single type of notch

    # selection of number and add in machine
    if self.is_P_to_other:
        self.convert_duct_to_other(is_stator)
    else:
        self.convert_duct_to_P(is_stator)

    if is_stator:
        axial_vent = self.machine.stator.axial_vent
    else:
        axial_vent = self.machine.rotor.axial_vent

    # add rules based on the number of duct in the machine
    duct_id = 0
    for duct in axial_vent:
        if not isinstance(duct, axial_vent[0].__class__):
            continue

        if isinstance(duct, VentilationCirc):
            self.add_rule_ventilationCirc(is_stator, duct_id)

        elif isinstance(duct, VentilationPolar):
            self.add_rule_ventilationPolar(is_stator, duct_id)

        elif isinstance(duct, VentilationTrap):
            self.add_rule_ventilationTrap(is_stator, duct_id)

        duct_id += 1
