# Multisimulation objects
from pyleecan.Classes.VarParam import VarParam
from pyleecan.Classes.ParamExplorerSet import ParamExplorerSet
from pyleecan.Classes.DataKeeper import DataKeeper
import numpy as np

## Reference simulation
from pyleecan.Classes.Simu1 import Simu1
from numpy import pi, ones, zeros, linspace
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

# Load the machine
from os.path import join
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

import pytest


@pytest.mark.FEMM
@pytest.mark.long
def test_slot_scale():
    IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))
    ref_simu = Simu1(name="E_IPMSM_FL_002", machine=IPMSM_A)

    # Definition of the enforced output of the electrical module
    Is_mat = zeros((1, 3))
    Is_mat[0, :] = np.array([0, 12.2474, -12.2474])
    Is = ImportMatrixVal(value=Is_mat)
    time = ImportGenVectLin(start=0, stop=0, num=1, endpoint=False)
    Na_tot = 2048

    ref_simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        N0=2504,
        angle_rotor=None,  # Will be computed
        time=time,
        Na_tot=Na_tot,
        angle_rotor_initial=0.86,
    )

    # Definition of the magnetic simulation
    ref_simu.mag = MagFEMM(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_a=True,
        Kgeo_fineness=0.2,
        Kmesh_fineness=0.2,
    )

    # Multi-simulation to variate the slot size
    multisim = VarParam(
        stop_if_error=True,
        ref_simu_index=0,  # Reference simulation is set as the first simulation from var_simu
    )

    ref_simu.var_simu = multisim

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
            value=linspace(0.1, 1.1, 11).tolist(),
        )
    ]

    multisim.paramexplorer_list = paramexplorer_list

    error_keeper_mag_flux = "lambda simu: np.nan * np.zeros(len(simu.mag.B.time.value), len(simu.mag.B.angle.value))"

    # List of DataKeeper to store results
    datakeeper_list = [
        DataKeeper(
            name="Average Torque",
            unit="N.m",
            symbol="Tem_av",
            keeper="lambda output: output.mag.Tem_av",
            error_keeper="lambda simu: np.nan",
        ),
        DataKeeper(
            name="Airgap flux density components",
            unit="H",
            symbol="B",
            keeper="lambda output: output.mag.B",
            error_keeper=error_keeper_mag_flux,
        ),
    ]

    multisim.datakeeper_list = datakeeper_list

    # Execute every simulation
    results = ref_simu.run()

    fig = results.plot_multi(
        x_symbol="stat_slot",
        y_symbol="Tem_av",
        title="Average torque in function of the stator slot scale factor ",
    )

    fig.savefig(join(save_path, "test_slot_scale"))
