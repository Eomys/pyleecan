from os.path import join, isfile

import pytest

from numpy import zeros, squeeze, abs as np_abs, array, pi, sum as np_sum, cos

import matplotlib.pyplot as plt

from Tests import save_validation_path as save_path

from pyleecan.Classes.Electrical import Electrical
from pyleecan.Classes.EEC_SCIM import EEC_SCIM
from pyleecan.Classes.LUTslip import LUTslip
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.InputVoltage import InputVoltage
from pyleecan.Classes.Output import Output
from pyleecan.Classes.Simu1 import Simu1

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
from pyleecan.Classes.ImportMatlab import ImportMatlab
from pyleecan.definitions import config_dict
from pyleecan.Functions.Plot import dict_2D, dict_3D

from SciDataTool import Data1D, DataLinspace, DataTime, DataFreq, VectorField, Norm_ref

color_list = config_dict["PLOT"]["COLOR_DICT"]["CURVE_COLORS"]

NAS_path = "//192.168.1.168/eomys/IT_data/Validation_data/Manatee_v2/"

is_show_fig = False


@pytest.mark.SCIM
@pytest.mark.Electrical
@pytest.mark.skip(reason="Work in progress")
def test_EEC_ELUT_SCIM_001():
    """Validation of the structural/acoustic module for default_machine machine
    Comparison with MANATEE V1 results"""

    #%%    Load MANATEE V1 results
    # matlab_path = (
    #     NAS_path + "Manatee_v1_results/default_proj_nl/default_proj_nl_results.mat"
    # )
    # matlab_path = "D:/Manatee_V1_trunk/Manatee_1.0/Results/default_proj_nl/default_proj_nl_results.mat"
    # matlab_path = "D:/Manatee_V1_trunk/Manatee_1.0/ELUT_SCIM_001.mat"
    matlab_path = "//192.168.1.168/eomys/IT_data/Validation_data/Manatee_v2/test_EEC_SCIM_001/ELUT_SCIM_001.mat"

    assert isfile(matlab_path)

    param_dict = dict()
    param_list = [
        "slip",
        "N0",
        "Im",
        "Lm",
        "R10",
        "R20",
        "R1_20",
        "R2_20",
        "L10",
        "L20",
        "I10",
        "U0",
        "I20",
        "Tswind",
        "Trwind",
    ]

    for param in param_list:
        value = ImportMatlab(file_path=matlab_path, var_name=param).get_data()
        if value.size == 1:
            if value.dtype == complex:
                param_dict[param] = complex(value)
            else:
                param_dict[param] = float(value)
        else:
            param_dict[param] = value

    # add Rfe
    # param_dict["Rfe"] = 1e12

    # Prepare simulation
    SCIM_001 = load(join(DATA_DIR, "Machine", "SCIM_001.json"))

    # change SCIM data that is different from ManateeV1
    # (#TODO check also difference of rotor bar section)
    # alpha = 1 big bug in Pyleecan to be corrected
    SCIM_001.rotor.winding.conductor.cond_mat.elec.alpha = 0.003
    SCIM_001.rotor.winding.conductor.cond_mat.elec.rho = 2.2e-8
    SCIM_001.rotor.ring_mat.elec.alpha = 0.003
    SCIM_001.rotor.ring_mat.elec.rho = 2.2e-8

    simu = Simu1(name="test_EEC_ELUT_SCIM_001", machine=SCIM_001)

    simu.input = InputVoltage(
        U0_ref=param_dict["U0"],
        Na_tot=2016,
        Nt_tot=2016,
        N0=param_dict["N0"],
        slip_ref=param_dict["slip"],
    )

    ELUT_SCIM_001 = LUTslip(
        R1=param_dict["R1_20"],
        L1=param_dict["L10"],
        T1_ref=20,
        R2=param_dict["R2_20"],
        L2=param_dict["L20"],
        T2_ref=20,
        Phi_m=np_abs(param_dict["Lm"] * param_dict["Im"]),
        I_m=np_abs(param_dict["Im"]),
    )

    # Configure simulation
    simu.elec = Electrical(
        ELUT_enforced=ELUT_SCIM_001,
        Tsta=param_dict["Tswind"],
        Trot=param_dict["Trwind"],
    )

    # Run simulation
    #%%
    out = simu.run()
    #%%

    # #%%   Prepare MANATEE V1 data for comparisons
    # Angle = Data1D(
    #     name="angle",
    #     unit="rad",
    #     values=angle,
    # )
    # MMF_space = DataTime(
    #     symbol="MMF",
    #     unit="At",
    #     values=MMF_space_v1,
    #     axes=[Angle],
    # )

    # Per_space = DataTime(
    #     symbol="Per",
    #     unit="H/m^2",
    #     values=Per_space_v1,
    #     axes=[Angle],
    # )
    # Br_space = DataTime(
    #     symbol="B_r",
    #     unit="T",
    #     values=B_r_space,
    #     axes=[Angle],
    # )
    # B_space = VectorField(components={"radial": Br_space})
    # AGSFr_space = DataTime(
    #     symbol="AGSF_r",
    #     unit="N/m^2",
    #     values=AGSF_space_v1,
    #     axes=[Angle],
    # )
    # AGSF_space = VectorField(components={"radial": AGSFr_space})

    # Time = Data1D(
    #     name="time",
    #     unit="s",
    #     values=time,
    #     normalizations={"elec_order": Norm_ref(ref=1188 / 60 * 3)},
    # )
    # MMF_time = DataTime(
    #     symbol="MMF",
    #     unit="At",
    #     values=MMF_time_v1,
    #     axes=[Time],
    # )

    # Per_time = DataTime(
    #     symbol="Per",
    #     unit="H/m^2",
    #     values=Per_time_v1,
    #     axes=[Time],
    # )
    # Br_time = DataTime(
    #     symbol="B_r",
    #     unit="T",
    #     values=B_r_time,
    #     axes=[Time],
    # )
    # B_time = VectorField(components={"radial": Br_time})

    # # Plots
    # if is_show_fig:
    #     legend_list = ["Manatee v2", "Manatee v1"]
    #     out.mag.MMF.plot_2D_Data(
    #         "angle{°}",
    #         data_list=[MMF_space],
    #         legend_list=legend_list,
    #         save_path=join(save_path, "plot_MMF_angle"),
    #         linestyles=["solid", "dashed"],
    #         is_show_fig=is_show_fig,
    #         **dict_2D
    #     )
    #     out.mag.MMF.plot_2D_Data(
    #         "time",
    #         data_list=[MMF_time],
    #         legend_list=legend_list,
    #         save_path=join(save_path, "plot_MMF_time"),
    #         is_show_fig=is_show_fig,
    #         linestyles=["solid", "dashed"],
    #         **dict_2D
    #     )
    #     out.mag.Per.plot_2D_Data(
    #         "angle{°}",
    #         data_list=[Per_space],
    #         legend_list=legend_list,
    #         save_path=join(save_path, "plot_Per_angle"),
    #         is_show_fig=is_show_fig,
    #         linestyles=["solid", "dashed"],
    #         **dict_2D
    #     )
    #     out.mag.Per.plot_2D_Data(
    #         "time",
    #         data_list=[Per_time],
    #         legend_list=legend_list,
    #         save_path=join(save_path, "plot_Per_time"),
    #         is_show_fig=is_show_fig,
    #         **dict_2D
    #     )
    #     out.mag.B.plot_2D_Data(
    #         "angle{°}",
    #         component_list=["radial"],
    #         data_list=[B_space],
    #         legend_list=legend_list,
    #         save_path=join(save_path, "plot_Br_angle"),
    #         is_show_fig=is_show_fig,
    #         **dict_2D
    #     )

    return out


if __name__ == "__main__":

    out = test_EEC_ELUT_SCIM_001()
