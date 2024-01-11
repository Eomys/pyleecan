# -*- coding: utf-8 -*-

import pytest
from pyleecan.Classes.ConvertMC import ConvertMC
from pyleecan.Functions.load import load


class Test_converter_machine(object):
    def test_convert_machine(self):
        """check if machine convert and machine save is equal"""
        # cleaning log file
        f = open("/Users\LAP17\AppData\Roaming\pyleecan/Pyleecan.log", "w")
        f.close()

        path_list = [
            "Form_wound_inset_paraellel_cicular_duct_stator",
            "Parallel_Slot_inset_radial_rectangular_duct_stator",
            "Parallel_tooth_embedded_breadloaf",
            "Parallel_tooth_embedded_parallel_skew",
            "Parallel_tooth_embedded_radial",
            "Parallel_tooth_interior_flat_simple",
            "Parallel_tooth_interior_flat_web",
            "Parallel_tooth_interior_V_web",
            "Parallel_tooth_parallel_slot_WRSM",
            "Parallel_tooth_parallel_tooth",
            "Parallel_tooth_parallel_tooth_WRSM",
            "Parallel_tooth_Pear",
            "Parallel_tooth_Rectangular",
            "Parallel_tooth_Round",
            "Parallel_tooth_salient_pole",
            "Parallel_tooth_SqB_surface_breadloaf_arc_duct_stator",
            "Parallel_tooth_surface_parallel_circular_duct_stator",
            "Parallel_tooth_surface_radial",
            "Tapered_slot_inset_breadloaf_rectangular_duct_stator",
            "tapered_slot_slot_corner_radius",
            "VF_Manatee_Hairpin_winding_interior_V_web",
        ]

        for path in path_list:
            conv = ConvertMC()
            machine = conv.convert_to_P(
                f"/Users\LAP17\Documents/Machine/Motor-cad/{path}.mot"
            )

            # 2 possibility plot machine, or regenerate all .json to load machine without pass by plot
            machine.plot()
            # machine.save(f"/Users/LAP17/Documents/Machine/Pyleecan/{machine.name}")

            machine2 = load(
                f"/Users\LAP17\Documents/Machine/Pyleecan/{machine.name}.json"
            )

            l = machine.compare(machine2)

            if len(l) != 0:
                raise ValueError("Machine isn't equivalent")

        print("Done")


if __name__ == "__main__":
    a = Test_converter_machine()
    a.test_convert_machine()
    print("Test Done")
