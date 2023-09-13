from numpy import pi, zeros, linspace, cos
from os.path import join

import pytest

import json

from multiprocessing import cpu_count

from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D, dict_3D

from pyleecan.definitions import DATA_DIR

from Tests import save_validation_path as save_path


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.ForceMT
@pytest.mark.SynRM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_AGSF_SynRM(nb_worker=int(cpu_count() / 2)):
    """Validation of a SynRM machine from Syr-e r29 open source software
    https://sourceforge.net/projects/syr-e/
    Test compute air-gap surface force with Maxwell Tensor and load the results
    """
    # The aim of this validation test is to compute the torque as a function of Phi0
    # As (for now) there is no electrical model, we will compute the current for each Phi0 here
    SynRM_001 = load(join(DATA_DIR, "Machine", "SynRM_001.json"))
    freq0 = 50  # supply frequency [Hz]
    qs = 3  # Number of phases
    p = 2  # Number of pole pairs
    Nt_tot = 2**6  # Number of time step for each current angle Phi0
    Imax = 28.6878  # Nominal stator current magnitude [A]
    # to have one torque ripple period since torque ripple appears at multiple of 6*freq0
    Nrev = 1
    time = linspace(0, Nrev * p / freq0 * (1 - 1 / Nt_tot), Nt_tot)

    Is = zeros((Nt_tot, qs))
    for q in range(qs):
        Is[:, q] = Imax * cos(2 * pi * freq0 * time - q * 2 * pi / qs)

    # Definition of the main simulation
    simu = Simu1(name="test_AGSF_SynRM", machine=SynRM_001)

    Na_tot = 2016

    simu.input = InputCurrent(
        Is=ImportMatrixVal(value=Is),
        Ir=None,  # No winding on the rotor
        OP=OPdq(N0=None, felec=freq0),
        time=ImportMatrixVal(value=time),
        Na_tot=Na_tot,
        Nt_tot=Nt_tot,
    )

    # Definition of the magnetic simulation (1/2 symmetry)
    simu.mag = MagFEMM(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_a=True,
        nb_worker=nb_worker,
    )

    # Definition of the magnetic simulation (no symmetry)
    simu.force = ForceMT(is_periodicity_a=True)

    # Run simulation
    out = simu.run()

    # Test save with MeshSolution object in out
    out.save(save_path=save_path + "\Output.json")

    # Plot the AGSF as a function of space with the spatial fft
    r_max = 78
    out.force.AGSF.plot_2D_Data(
        "angle{°}",
        "time[0]",
        save_path=join(save_path, "test_FM_SynRM_FL_001_plot_force_space.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.force.AGSF.plot_2D_Data(
        "wavenumber=[0," + str(r_max) + "]",
        "time[0]",
        save_path=join(save_path, "test_FM_SynRM_FL_001_plot_force_space_fft.png"),
        is_show_fig=False,
        **dict_2D
    )

    # Plot the AGSF as a function of time with the time fft
    freq_max = 1000
    out.force.AGSF.plot_2D_Data(
        "time",
        "angle[0]",
        save_path=join(save_path, "test_FM_SynRM_FL_001_plot_force_time.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.force.AGSF.plot_2D_Data(
        "freqs=[0," + str(freq_max) + "]",
        "angle[0]",
        save_path=join(save_path, "test_FM_SynRM_FL_001_plot_force_time_fft.png"),
        is_show_fig=False,
        **dict_2D
    )

    # ------------------------------------------------------

    load_path = join(save_path, "Output.json")

    # Test to load the Meshsolution object (inside the output):
    with open(load_path) as json_file:
        json_tmp = json.load(json_file)
        out = Output(init_dict=json_tmp)

    # Plot the AGSF as a function of space with the spatial fft
    r_max = 78
    out.force.AGSF.plot_2D_Data(
        "angle{°}",
        "time[0]",
        save_path=join(save_path, "test_FM_SynRM_FL_001_plot_force_space2.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.force.AGSF.plot_2D_Data(
        "wavenumber=[0," + str(r_max) + "]",
        "time[0]",
        save_path=join(save_path, "test_FM_SynRM_FL_001_plot_force_space_fft2.png"),
        is_show_fig=False,
        **dict_2D
    )

    # Plot the AGSF as a function of time with the time fft
    freq_max = 1000
    out.force.AGSF.plot_2D_Data(
        "time",
        "angle[0]",
        save_path=join(save_path, "test_FM_SynRM_FL_001_plot_force_space2.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.force.AGSF.plot_2D_Data(
        "freqs=[0," + str(freq_max) + "]",
        "angle[0]",
        save_path=join(save_path, "test_FM_SynRM_FL_001_plot_force_space_fft2.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.force.AGSF.plot_3D_Data(
        "freqs=[0," + str(freq_max) + "]",
        "wavenumber=[-" + str(r_max) + "," + str(r_max) + "]",
        component_list=["radial"],
        save_path=join(save_path, "test_FM_SynRM_FL_001_plot_force_fft2.png"),
        is_show_fig=False,
        is_2D_view=True,
        **dict_3D
    )

    out.force.AGSF.plot_3D_Data(
        "freqs=[0," + str(freq_max) + "]",
        "wavenumber=[-" + str(r_max) + "," + str(r_max) + "]",
        component_list=["radial"],
        save_path=join(save_path, "test_FM_SynRM_FL_001_plot_force_cfft2.png"),
        is_show_fig=False,
        **dict_3D
    )

    out.force.AGSF.plot_3D_Data(
        "time",
        "angle{°}",
        component_list=["radial"],
        save_path=join(save_path, "test_FM_SynRM_FL_001_plot_force_time_space"),
        is_show_fig=False,
        is_2D_view=True,
        **dict_3D
    )
    out.mag.B.plot_3D_Data(
        "time",
        "angle{°}",
        component_list=["radial"],
        save_path=join(save_path, "test_FM_SynRM_FL_001_plot_flux_time_space"),
        is_show_fig=False,
        is_2D_view=True,
        **dict_3D
    )

    return out

    # ------------------------------------------------------


# To run it without pytest
if __name__ == "__main__":
    out = test_AGSF_SynRM()
