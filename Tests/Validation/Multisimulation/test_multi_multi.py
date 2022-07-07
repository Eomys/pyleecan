from os.path import dirname, join

import matplotlib.pyplot as plt
import numpy as np
import pytest
from numpy import exp, linspace, ones, pi, sqrt, zeros
from pyleecan.Classes.DataKeeper import DataKeeper
from pyleecan.Classes.DriveWave import DriveWave
from pyleecan.Classes.EEC_PMSM import EEC_PMSM
from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.ImportGenMatrixSin import ImportGenMatrixSin
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportGenVectSin import ImportGenVectSin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Output import Output
from pyleecan.Classes.ParamExplorerInterval import ParamExplorerInterval
from pyleecan.Classes.ParamExplorerSet import ParamExplorerSet
from pyleecan.Classes.PostFunction import PostFunction
from pyleecan.Classes.PostPlot import PostPlot
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent
from pyleecan.Classes.VarParam import VarParam
from pyleecan.definitions import DATA_DIR
from pyleecan.Functions.load import load
from Tests import save_validation_path as save_path

# Prius MTPA
N0_MTPA = [
    500,
    894.736842105263,
    1289.47368421053,
    1684.21052631579,
    2078.94736842105,
    2473.68421052632,
    2868.42105263158,
    3263.15789473684,
    3657.89473684211,
    4052.63157894737,
    4447.36842105263,
    4842.10526315790,
    5236.84210526316,
    5631.57894736842,
    6026.31578947368,
    6421.05263157895,
    6815.78947368421,
    7210.52631578947,
    7605.26315789474,
    8000,
]
Id_MTPA = [
    -135.671342685371,
    -135.671342685371,
    -135.671342685371,
    -155.310621242485,
    -151.803607214429,
    -128.657314629259,
    -123.046092184369,
    -113.927855711423,
    -104.108216432866,
    -99.8997995991984,
    -94.9899799599199,
    -94.9899799599199,
    -92.1843687374750,
    -92.1843687374750,
    -88.6773547094188,
    -87.2745490981964,
    -87.2745490981964,
    -88.6773547094188,
    -84.4689378757515,
    -88.6773547094188,
]
Iq_MTPA = [
    113.226452905812,
    113.226452905812,
    113.226452905812,
    83.6673346693387,
    54.6092184368737,
    45.0901803607214,
    36.0721442885772,
    30.5611222444890,
    28.0561122244489,
    25.5511022044088,
    23.5470941883768,
    21.5430861723447,
    20.0400801603206,
    18.5370741482966,
    17.5350701402806,
    16.5330661322645,
    15.5310621242485,
    14.5290581162325,
    14.0280561122245,
    13.0260521042084,
]


@pytest.mark.MagFEMM
@pytest.mark.ForceMT
@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.IPMSM
@pytest.mark.VarLoadCurrent
@pytest.mark.VarParam
@pytest.mark.periodicity
def test_multi_multi():
    """Run a multi-simulation of multi-simulation"""

    # Main loop parameters
    Nt_tot = 96  # Number of time step for each FEMM simulation
    nb_worker = 3  # To parallelize FEMM

    Nspeed = 7  # Number of speed for the Variable speed linspace

    N1 = 4  # Number of parameters for first sensitivity parameter
    # N2 = 2  # Number of parameters for second sensitivity parameter

    # Reference simulation definition
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    simu = Simu1(
        name="test_multi_multi",
        machine=Toyota_Prius,
        path_result=join(save_path, "test_multi_multi"),
        layer_log_warn=2,
    )

    # Enforced sinusoïdal current (Maximum Torque Per Amp)
    simu.input = InputCurrent(
        Is=None,
        Ir=None,  # No winding on the rotor
        OP=OPdq(N0=N0_MTPA[0], Id_ref=Id_MTPA[0], Iq_ref=Iq_MTPA[0]),
        Nt_tot=Nt_tot,
        Na_tot=2048,
    )

    # Definition of the magnetic simulation
    simu.mag = MagFEMM(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_a=True,
        is_periodicity_t=True,
        Kgeo_fineness=0.2,
        Kmesh_fineness=0.2,
        nb_worker=nb_worker,
    )
    simu.force = ForceMT(is_periodicity_a=True, is_periodicity_t=True,)

    # VarSpeed Definition
    varload = VarLoadCurrent(is_reuse_femm_file=True)
    # Matrix N0, Id, Iq
    OP_matrix = zeros((Nspeed, 3))
    OP_matrix[:, 0] = N0_MTPA[:Nspeed]
    OP_matrix[:, 1] = Id_MTPA[:Nspeed]
    OP_matrix[:, 2] = Iq_MTPA[:Nspeed]
    varload.datakeeper_list = [
        DataKeeper(
            name="Average Torque",
            unit="N.m",
            symbol="Tem_av",
            keeper="lambda output: output.mag.Tem_av",
            error_keeper="lambda simu: np.nan",
        ),
        DataKeeper(
            name="6f Harmonic",
            unit="N.m^2",
            symbol="6fs",
            keeper="lambda output: output.force.AGSF.components['radial'].get_magnitude_along('freqs->elec_order=6','wavenumber=0')['AGSF_r']",
            error_keeper="lambda simu: np.nan",
        ),
        DataKeeper(
            name="12f Harmonic",
            unit="N.m^2",
            symbol="12fs",
            keeper="lambda output: output.force.AGSF.components['radial'].get_magnitude_along('freqs->elec_order=12','wavenumber=0')['AGSF_r']",
            error_keeper="lambda simu: np.nan",
        ),
    ]
    varload.is_keep_all_output = False

    # Multi-simulation to change machine parameters
    multisim = VarParam(stop_if_error=True, is_reuse_femm_file=False,)

    simu.var_simu = multisim

    # List of ParamExplorer to define multisimulation input values
    paramexplorer_list = [
        ParamExplorerInterval(
            name="Stator slot opening",
            symbol="W0s",
            unit="m",
            setter="simu.machine.stator.slot.W0",
            getter="simu.machine.stator.slot.W0",
            min_value=0.1 * Toyota_Prius.stator.slot.W0,
            max_value=Toyota_Prius.stator.slot.W0,
            N=N1,
        )
    ]
    assert (
        paramexplorer_list[0].get_desc(simu)
        == "W0s: " + str(N1) + " values from 0.000193 to 0.00193 (ref=0.00193) [m]"
    )
    multisim.paramexplorer_list = paramexplorer_list
    multisim.is_keep_all_output = True

    # List of DataKeeper to store results
    datakeeper_list = [
        DataKeeper(
            name="Max Variable speed Torque",
            unit="N.m",
            symbol="Max_Tem_av",
            keeper="lambda output: max(output.xoutput_dict['Tem_av'].result)",
            error_keeper="lambda simu: np.nan",
        ),
        DataKeeper(
            name="Max f6",
            unit="N.m^2",
            symbol="max(6fs)",
            keeper="lambda output: max(output.xoutput_dict['6fs'].result)",
            error_keeper="lambda simu: np.nan",
        ),
        DataKeeper(
            name="Max f12",
            unit="N.m^2",
            symbol="max(12fs)",
            keeper="lambda output: max(output.xoutput_dict['12fs'].result)",
            error_keeper="lambda simu: np.nan",
        ),
    ]
    multisim.datakeeper_list = datakeeper_list
    multisim.var_simu = varload  # Setup Multisim of Multi_sim
    varload.set_OP_array(OP_matrix, "N0", "Id", "Iq")

    # Post-process
    Post1 = PostFunction(join(dirname(__file__), "plot_save.py"))
    simu.postproc_list = [Post1]  # For all simulation save a png
    # Plot Max(f6) = f(W0)
    Post2 = PostPlot(
        method="plot_multi",
        param_list=["W0s", "max(6fs)"],
        param_dict={
            "save_path": join(save_path, "multi_multi", "Max_6fs.png"),
            "is_show_fig": False,
        },
    )
    # Plot Max(f12) = f(W0)
    Post3 = PostPlot(
        method="plot_multi",
        param_list=["W0s", "max(12fs)"],
        param_dict={
            "save_path": join(save_path, "multi_multi", "Max_12fs.png"),
            "is_show_fig": False,
        },
    )
    # Generate gif once all the simulation are done
    Post4 = PostFunction(join(dirname(__file__), "make_gif.py"))
    simu.var_simu.postproc_list = [Post2, Post3, Post4]
    # Execute every simulation
    results = simu.run()
    assert len(simu.var_simu.datakeeper_list) == 5
    assert len(simu.var_simu.var_simu.datakeeper_list) == 9


if __name__ == "__main__":
    test_multi_multi()
