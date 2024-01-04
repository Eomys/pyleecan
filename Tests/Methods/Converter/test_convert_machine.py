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

        # machineP = load(
        #    "/Users\LAP17\AppData\Roaming\pyleecan/Machine/Renault_Zoe.json"
        # )
        #
        # machineP2 = load("/Users\LAP17\AppData\Roaming\pyleecan/Machine/Benchmark.json")
        #
        # machineP3 = load(
        #    "/Users\LAP17\AppData\Roaming\pyleecan/Machine/SCIM_5kw_Zaheer.json"
        # )
        # machineP3 = load(
        #    "/Users\LAP17\AppData\Roaming\pyleecan/Machine/Toyota_Prius_test_skew.json"
        # )

        """
            "EMD240_v16",
            "VF_Manatee_Hairpin_winding",
            
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
            
        """

        """
        "Audi_etron_SCIM_Parallel_tooth_parallel_tooth",
        "Benchmark_SPMSM_tapered_slot_surface_radial",
        "IPMSM_B_parallel_tooth_interior_V_web",
        "WRSM_parallel_tooth",
        "WRSM_parallel_slot",
        "WRSM_salient_pole",
        "WRSM_parallel_tooth_salient_pole",
        
        "skew",
        
            "parallel_tooth_interior_U_Shape_mat",
        "interor_V(web)_mat",
        """
        path_list = [
            "tapered_slot_slot_corner_radius",
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
