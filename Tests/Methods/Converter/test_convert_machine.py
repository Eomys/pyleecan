# -*- coding: utf-8 -*-

import pytest
from pyleecan.Classes.ConvertMC import ConvertMC
from pyleecan.Classes.CondType12 import CondType12
from pyleecan.Functions.load import load
from pyleecan.Classes.CondType11 import CondType11


class Test_converter_machine(object):
    def test_convert_machine(self):
        """check if machine convert and machine save is equal"""
        # cleaning log file
        f = open("/Users\LAP17\AppData\Roaming\pyleecan/Pyleecan.log", "w")
        f.close()

        # machineP = load(
        #    "/Users\LAP17\AppData\Roaming\pyleecan/Machine/Renault_Zoe.json"
        # )
        #
        # machineP2 = load("/Users\LAP17\AppData\Roaming\pyleecan/Machine/Benchmark.json")
        #
        # machineP3 = load(
        #    "/Users\LAP17\AppData\Roaming\pyleecan/Machine/SCIM_5kw_Zaheer.json"
        # )
        """
            "EMD240_v16",
            "VF_Manatee_Hairpin_winding",
        
            
        """

        path_list = [
            "interor_V(web)",
            "form_wound_inset_parallel_arc_duct",
            "parallel_slot_surface_breadloaf",
            "parallel_tooth_embedded_breadloaf",
            "parallel_tooth_embedded_parallel_rectanguler_duct_stator",
            "parallel_tooth_embedded_radial_notch_circular_duct_sator",
            "parallel_tooth_inset_beadloaf_circular_duct",
            "parallel_tooth_interior_flat(simple)",
            "parallel_tooth_interior_flat(web)",
            "parallel_tooth_interior_V(web)",
            "parallel_tooth_interior_V_simple",
            "parallel_tooth_SqB_Surface_radial",
            "tapered_slot_inset_radial_2_rectangular_duct",
            "Matlab_Test_2",
            "SCIM_parallel_tooth",
            "SCIM_pear",
            "SCIM_rectangular",
            "SCIM_round",
            "WRSM_parallel_tooth",
            "WRSM_parallel_slot",
            "WRSM_salient_pole",
        ]

        for path in path_list:
            conv = ConvertMC()
            machine = conv.convert_to_P(
                f"/Users\LAP17\Documents/machine_MC_P/file_mot/{path}.mot"
            )

            machine.plot()
            machine.save(
                f"/Users/LAP17/Documents/machine_MC_P/file_json/{machine.name}"
            )

            machine2 = load(
                f"/Users\LAP17\Documents/machine_MC_P/file_json/{machine.name}.json"
            )

            l = machine.compare(machine2)

            if len(l) != 0:
                raise ValueError("Machine isn't equivalent")

        print("Done")


if __name__ == "__main__":
    a = Test_converter_machine()
    a.test_convert_machine()
    print("Test Done")
