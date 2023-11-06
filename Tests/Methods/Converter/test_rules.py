import pytest

from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex

from pyleecan.Methods.Converter.RuleSimple.convert_to_P import convert_to_P
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM


from pyleecan.Classes.ConvertMC import ConvertMC

rule_list = list()

rule_list.append(RuleComplex(fct_name="parallel_tooth_slotW11", src="pyleecan"))

rule_list.append(
    RuleSimple(
        other_key_list=["[Dimensions]", "Slot_Opening"],
        P_obj_path=f"machine.stator.slot.W0",
        unit_type="m",
        scaling_to_P=1,
    )
)


# add equation rules

other_dict = {}
other_dict["[Dimensions]"] = {}
other_dict["[Dimensions]"]["Slot_Opening"] = 12.5


class Test_converter_mot(object):
    def compare_simple_rule(self):
        machine = MachineSIPMSM()
        self = ConvertMC

        for rule in rule_list:
            machine = rule.convert_to_P(other_dict, self.is_P_to_other, machine=machine)

        assert type(machine.stator.slot).__name__ == "SlotW11"
        msg = machine.stator.slot
        assert abs(machine.stator.slot.W0) == pytest.approx(12.5), msg


if __name__ == "__main__":
    a = Test_converter_mot()
    a.compare_simple_rule()
    print("Done")
