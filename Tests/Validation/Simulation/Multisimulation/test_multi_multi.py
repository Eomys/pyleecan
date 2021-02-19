# Multisimulation objects
from pyleecan.Classes.VarParam import VarParam
from pyleecan.Classes.ParamExplorerSet import ParamExplorerSet
from pyleecan.Classes.DataKeeper import DataKeeper
import numpy as np

## Reference simulation
from pyleecan.Classes.Simu1 import Simu1
from numpy import pi, ones, zeros, linspace, sqrt, exp
from os.path import join
import matplotlib.pyplot as plt
from Tests import save_validation_path as save_path

from pyleecan.Classes.Simu1 import Simu1

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportGenVectSin import ImportGenVectSin
from pyleecan.Classes.ImportGenMatrixSin import ImportGenMatrixSin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.EEC_PMSM import EEC_PMSM
from pyleecan.Classes.FluxLinkFEMM import FluxLinkFEMM
from pyleecan.Classes.IndMagFEMM import IndMagFEMM
from pyleecan.Classes.DriveWave import DriveWave
from pyleecan.Classes.Output import Output
from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent

# Load the machine
from os.path import join
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

import pytest


@pytest.mark.FEMM
@pytest.mark.long
def test_multi_multi():
    """Run a multi-simulation of multi-simulation"""
    IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))
    simu = Simu1(name="multi_multi", machine=IPMSM_A)

    # Definition of the enforced output of the electrical module
    I0_rms = 250 / sqrt(2)
    Phi0 = 140 * pi / 180  # Maximum Torque Per Amp

    Id_ref = (I0_rms * exp(1j * Phi0)).real
    Iq_ref = (I0_rms * exp(1j * Phi0)).imag
    simu.input = InputCurrent(
        Is=None,
        Ir=None,  # No winding on the rotor
        N0=2500,
        Id_ref=Id_ref,
        Iq_ref=Iq_ref,
        angle_rotor=None,  # Will be computed
        Nt_tot=2,
        Na_tot=2048,
    )

    # Definition of the magnetic simulation
    simu.mag = MagFEMM(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_a=True,
        Kgeo_fineness=0.2,
        Kmesh_fineness=0.2,
    )

    # Multi-simulation to variate the slot size
    multisim = VarParam(
        stop_if_error=True,
        is_reuse_femm_file=False,
        ref_simu_index=1,  # Reference simulation is set as the first simulation from var_simu
    )

    simu.var_simu = multisim

    def slot_scale(simu, scale_factor):
        """
        Edit stator slot size according to a percentage

        Parameters
        ----------
        simu: Simulation
            simulation to modify
        scale_factor: float
            stator slot scale factor
        """
        simu.machine.stator.slot.W0 *= scale_factor
        simu.machine.stator.slot.W1 *= scale_factor
        simu.machine.stator.slot.W2 *= scale_factor
        simu.machine.stator.slot.H0 *= scale_factor
        simu.machine.stator.slot.H1 *= scale_factor

    # List of ParamExplorer to define multisimulation input values
    paramexplorer_list = [
        ParamExplorerSet(
            name="Stator slot scale factor",
            symbol="stat_slot",
            unit="",
            setter=slot_scale,
            value=[0.5, 1, 1.1],
        )
    ]

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
            name="Variable speed Torque",
            unit="N.m",
            symbol="S_Tem_av",
            keeper="lambda output: output.xoutput_dict['Tem_av'].result",
            error_keeper="lambda simu: np.nan",
        ),
    ]
    multisim.datakeeper_list = datakeeper_list

    # Variable Speed Simulation
    varload = VarLoadCurrent(is_reuse_femm_file=True, ref_simu_index=0)
    varload.type_OP_matrix = 1  # Matrix N0, Id, Iq

    N_simu = 4
    OP_matrix = zeros((N_simu, 3))
    OP_matrix[:, 0] = linspace(100, 8000, N_simu)
    OP_matrix[:, 1] = Id_ref
    OP_matrix[:, 2] = Iq_ref
    varload.OP_matrix = OP_matrix
    varload.datakeeper_list = [
        DataKeeper(
            name="Average Torque",
            unit="N.m",
            symbol="Tem_av",
            keeper="lambda output: output.mag.Tem_av",
            error_keeper="lambda simu: np.nan",
        )
    ]
    varload.is_keep_all_output = False
    simu.var_simu.var_simu = varload

    # Execute every simulation
    results = simu.run()

    fig = results.plot_multi(
        x_symbol="stat_slot",
        y_symbol="Max_Tem_av",
        title="Average torque in function of the stator slot scale factor ",
    )
    fig.savefig(join(save_path, "test_slot_scale"))
    plt.close()
    for ii in range(3):
        plt.plot(
            linspace(100, 8000, N_simu), results.xoutput_dict["S_Tem_av"].result[ii]
        )
    plt.show()


if __name__ == "__main__":
    test_multi_multi()
