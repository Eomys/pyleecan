# -*- coding: utf-8 -*-
from os import cpu_count
import pytest
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.SolutionMat import SolutionMat
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
import numpy as np
from os.path import join

from Tests import save_plot_path as save_path

@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.SPMSM
def test_plot_contour_B_FEMM():
    """Validation of the implementaiton of periodic angle axis in Magnetic (MagFEMM) and Force (ForceMT) modules"""

    SPMSM_015 = load(join(DATA_DIR, "Machine", "SPMSM_015.json"))

    simu = Simu1(name="test_FEMM_periodicity_time_no_periodicity_a", machine=SPMSM_015)

    # Definition of the enforced output of the electrical module
    I0_rms = 250 / np.sqrt(2)
    Phi0 = 140 * np.pi / 180  # Maximum Torque Per Amp

    Id_ref = (I0_rms * np.exp(1j * Phi0)).real
    Iq_ref = (I0_rms * np.exp(1j * Phi0)).imag

    simu.input = InputCurrent(
        Id_ref=Id_ref,
        Iq_ref=Iq_ref,
        Na_tot=252 * 9,
        Nt_tot=4 * 9,
        N0=1000,
    )

    # Definition of the magnetic simulation: with periodicity
    simu.mag = MagFEMM(
        type_BH_stator=1,
        type_BH_rotor=1,
        is_periodicity_a=False,
        is_periodicity_t=True,
        nb_worker=cpu_count(),
        is_get_meshsolution=True,
        Kmesh_fineness=0.5,
    )

    out = simu.run()

    out.mag.meshsolution.plot_contour(is_show_fig=False, save_path=join(save_path, "plot_mesh.png"))
    out.mag.meshsolution.plot_contour(
        group_names="stator core",
        is_show_fig=False,
        save_path=join(save_path, "plot_mesh_stator.png"),
    )
    out.mag.meshsolution.plot_contour(
        is_animated=True,
        group_names="stator core",
        is_show_fig=False,
        save_path=join(save_path, "plot_mesh_stator.gif"),
    )

    pass

if __name__ == "__main__":
    test_plot_contour_B_FEMM()
