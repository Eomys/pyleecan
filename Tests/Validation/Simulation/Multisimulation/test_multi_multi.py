# Multisimulation objects
from pyleecan.Classes.VarParam import VarParam
from pyleecan.Classes.ParamExplorerSet import ParamExplorerSet
from pyleecan.Classes.DataKeeper import DataKeeper
import numpy as np

## Reference simulation
from pyleecan.Classes.Simu1 import Simu1
from numpy import pi, ones, zeros, linspace, sqrt, exp
from os.path import join, dirname
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
from pyleecan.Classes.PostFunction import PostFunction
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

    # Main loop parameters
    Nt_tot = 96  # Number of time step for each FEMM simulation
    nb_worker = 3  # To parallelize FEMM

    Nspeed = 5  # Number of speed for the Variable speed linspace

    N1 = 4  # Number of parameters for first sensitivity parameter
    # N2 = 2  # Number of parameters for second sensitivity parameter

    # Reference simulation definition
    IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))
    simu = Simu1(name="multi_multi", machine=IPMSM_A)

    # Enforced sinusoïdal current (Maximum Torque Per Amp)
    I0_rms = 250 / sqrt(2)
    Phi0 = 140 * pi / 180
    Id_ref = (I0_rms * exp(1j * Phi0)).real
    Iq_ref = (I0_rms * exp(1j * Phi0)).imag
    simu.input = InputCurrent(
        Is=None,
        Ir=None,  # No winding on the rotor
        N0=2500,
        Id_ref=Id_ref,
        Iq_ref=Iq_ref,
        angle_rotor=None,  # Will be computed
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
    simu.force = ForceMT(
        is_periodicity_a=True,
        is_periodicity_t=True,
    )

    # VarSpeed Definition
    varload = VarLoadCurrent(is_reuse_femm_file=True, ref_simu_index=0)
    varload.type_OP_matrix = 1  # Matrix N0, Id, Iq

    OP_matrix = zeros((Nspeed, 3))
    OP_matrix[:, 0] = linspace(100, 5000, Nspeed)
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
    multisim = VarParam(
        stop_if_error=True,
        is_reuse_femm_file=False,
        ref_simu_index=N1 - 1,
    )

    simu.var_simu = multisim

    # List of ParamExplorer to define multisimulation input values
    paramexplorer_list = [
        ParamExplorerSet(
            name="Stator slot opening",
            symbol="W0s",
            unit="m",
            setter="simu.machine.stator.slot.W0",
            value=(
                IPMSM_A.stator.slot.W0 * linspace(0.1, 1, N1, endpoint=True)
            ).tolist(),
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
    multisim.var_simu = varload  # Setup Multisim of Multi_sim

    # Post-process
    Post1 = PostFunction(join(dirname(__file__), "plot_save.py"))
    simu.postproc_list = [Post1]  # For all simulation save a png
    # Generate gif once all the simulation are done
    Post2 = PostFunction(join(dirname(__file__), "make_gif.py"))
    simu.var_simu.postproc_list = [Post2]
    # Execute every simulation
    results = simu.run()


if __name__ == "__main__":
    test_multi_multi()
