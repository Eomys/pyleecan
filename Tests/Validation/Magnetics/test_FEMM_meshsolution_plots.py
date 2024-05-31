from multiprocessing import cpu_count
from os.path import join

import pytest
from numpy import array, pi, zeros

from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Output import Output
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.definitions import DATA_DIR
from pyleecan.Functions.load import load
from Tests import save_load_path, save_plot_path


@pytest.mark.long_5s
@pytest.mark.SPMSM
@pytest.mark.MagFEMM
@pytest.mark.MeshSol
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_meshsolution_plots_SPMSM():
    """Validation of a polar SIPMSM with surface magnet
    Linear lamination material

    From publication
    Lubin, S. Mezani, and A. Rezzoug,
    “2-D Exact Analytical Model for Surface-Mounted Permanent-Magnet Motors with Semi-Closed Slots,”
    IEEE Trans. Magn., vol. 47, no. 2, pp. 479–492, 2011.
    Test compute the Flux in FEMM, with and without symmetry
    and with MANATEE semi-analytical subdomain model
    """
    SPMSM_003 = load(join(DATA_DIR, "Machine", "SPMSM_003.json"))
    simu = Simu1(name="test_meshsolution_plots_SPMSM", machine=SPMSM_003)

    # Definition of the enforced output of the electrical module
    N0 = 3000
    Is = ImportMatrixVal(
        value=array(
            [
                [6.97244193e-06, 2.25353053e02, -2.25353060e02],
                [-2.60215295e02, 1.30107654e02, 1.30107642e02],
                [-6.97244208e-06, -2.25353053e02, 2.25353060e02],
                [2.60215295e02, -1.30107654e02, -1.30107642e02],
            ]
        )
    )
    time = ImportGenVectLin(start=0, stop=0.015, num=4, endpoint=True)
    Na_tot = 1024

    simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        OP=OPdq(N0=N0),
        time=time,
        Na_tot=Na_tot,
        angle_rotor_initial=0.5216 + pi,
    )

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=2,
        is_periodicity_a=False,
        is_get_meshsolution=True,
        nb_worker=cpu_count(),
    )
    simu.force = None
    simu.struct = None
    # Copy the simu and activate the symmetry
    assert SPMSM_003.comp_periodicity_spatial() == (1, True)
    simu_sym = Simu1(init_dict=simu.as_dict())
    simu_sym.mag.is_periodicity_a = True

    out = Output(simu=simu_sym)
    simu_sym.run()

    out.mag.meshsolution.plot_mesh(
        save_path=join(save_plot_path, simu.name + "_mesh.png"), is_show_fig=False
    )

    out.mag.meshsolution.get_group("stator core").plot_mesh(
        save_path=join(save_plot_path, simu.name + "_mesh_stator.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.get_group(
        ["stator core", "/", "airgap", "stator winding"]
    ).plot_mesh(
        save_path=join(save_plot_path, simu.name + "_mesh_stator_interface.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.plot_contour(
        label="\mu",
        save_path=join(save_plot_path, simu.name + "_mu.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.plot_contour(
        label="B",
        save_path=join(save_plot_path, simu.name + "_B.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.get_group("stator core").plot_contour(
        label="H",
        save_path=join(save_plot_path, simu.name + "_H_stator.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.plot_contour(
        "time[2]",
        label="H",
        save_path=join(save_plot_path, simu.name + "_H_time2.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.plot_contour(
        "time[3]",
        label="H",
        save_path=join(save_plot_path, simu.name + "_H_time3.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.plot_contour(
        "freqs[1]",
        label="H",
        save_path=join(save_plot_path, simu.name + "_H_freqs1.png"),
        is_show_fig=False,
    )

    return out


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.MeshSol
@pytest.mark.periodicity
@pytest.mark.IPMSM
@pytest.mark.SingleOP
def test_FEMM_meshsolution_plots_slotless():
    """Validation of extracting FEMM data with MeshSolution.

    Electrical machine is an academic slotless machine inspired
    from [R. Pile et al., Application Limits of the Airgap Maxwell
    Tensor, CEFC, 2018] but with interior magnet such as Toyota
    Prius machine.

    """
    Slotless_CEFC = load(join(DATA_DIR, "Machine", "Slotless_CEFC.json"))
    simu = Simu1(name="test_meshsolution_plots_slotless", machine=Slotless_CEFC)

    simu.input = InputCurrent(
        OP=OPdq(N0=1200, Id_ref=0, Iq_ref=0),
        Ir=None,
        Na_tot=2**6,
        Nt_tot=1,
    )

    simu.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=0,
        is_get_meshsolution=True,
        is_periodicity_a=True,
        is_periodicity_t=False,
    )

    out = simu.run()

    out.mag.meshsolution.plot_mesh(
        save_path=join(save_plot_path, simu.name + "_mesh_save.png"), is_show_fig=False
    )

    out.mag.meshsolution.get_group(["stator core", "airgap"]).plot_mesh(
        save_path=join(save_plot_path, simu.name + "_mesh_stator_airgap_save.png"),
        is_show_fig=False,
    )

    test_meshsol = out.mag.meshsolution.get_group(["stator core", "airgap"])
    test_meshsol.get_group("stator core").plot_mesh(
        save_path=join(save_plot_path, simu.name + "_mesh_stator_bis_save.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.get_group(["stator core", "/", "airgap"]).plot_mesh(
        save_path=join(save_plot_path, simu.name + "_mesh_interface_save.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.plot_contour(
        label="\mu",
        save_path=join(save_plot_path, simu.name + "_mu_save.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.plot_contour(
        label="B",
        save_path=join(save_plot_path, simu.name + "_B_save.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.plot_contour(
        label="H",
        save_path=join(save_plot_path, simu.name + "_H_save.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.get_group("stator core").plot_contour(
        label="H",
        save_path=join(save_plot_path, simu.name + "_stator_save.png"),
        is_show_fig=False,
    )

    test_meshsol.get_group("stator core").plot_contour(
        label="H",
        save_path=join(save_plot_path, simu.name + "_H_stator_bis_save.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.get_group(["stator core", "airgap"]).plot_contour(
        label="\mu",
        save_path=join(save_plot_path, simu.name + "_mu_stator_airgap_save.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.get_group(["rotor core", "rotor magnets"]).plot_contour(
        label="\mu",
        save_path=join(save_plot_path, simu.name + "_mu_rotor_save.png"),
        is_show_fig=False,
    )

    # Test save with MeshSolution object in out
    load_path = join(save_load_path, simu.name + ".h5")

    out.save(save_path=load_path)

    # Test to load the Meshsolution object (inside the output):
    FEMM = load(load_path)

    # TODO : out.compare(FEMM)

    # [Important] To test that fields are still working after saving and loading
    FEMM.mag.meshsolution.plot_mesh(
        save_path=join(save_plot_path, simu.name + "_mesh_load.png"), is_show_fig=False
    )

    FEMM.mag.meshsolution.plot_contour(
        label="B",
        save_path=join(save_plot_path, simu.name + "_B_load.png"),
        is_show_fig=False,
    )

    FEMM.mag.meshsolution.get_group(["rotor core", "rotor magnets"]).plot_contour(
        label="\mu",
        save_path=join(save_plot_path, simu.name + "_mu_rotor_load.png"),
        is_show_fig=False,
    )


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.MeshSol
@pytest.mark.IPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_meshsolution_plots_Prius():
    """Validation of extracting FEMM data with MeshSolution with Toyota Prius electrical machine."""
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    simu = Simu1(name="test_meshsolution_plots_Toyota_Prius", machine=Toyota_Prius)

    # Definition of the enforced output of the electrical module
    N0 = 2504
    Is_mat = zeros((1, 3))
    Is_mat[0, :] = array([0, 12.2474, -12.2474])
    Is = ImportMatrixVal(value=Is_mat)
    Nt_tot = 1
    Na_tot = 2048

    simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        OP=OPdq(N0=N0),
        Nt_tot=Nt_tot,
        Na_tot=Na_tot,
        angle_rotor_initial=0.86,
    )

    simu.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=0,
        is_get_meshsolution=True,
        is_periodicity_a=True,
        is_periodicity_t=False,
    )

    out = simu.run()

    out.mag.meshsolution.plot_mesh(
        save_path=join(save_plot_path, simu.name + "_mesh_save.png"), is_show_fig=False
    )

    out.mag.meshsolution.get_group(["stator core", "airgap"]).plot_mesh(
        save_path=join(save_plot_path, simu.name + "_mesh_stator_airgap_save.png"),
        is_show_fig=False,
    )

    test_meshsol = out.mag.meshsolution.get_group(["stator core", "airgap"])
    test_meshsol.get_group(["stator core"]).plot_mesh(
        save_path=join(save_plot_path, simu.name + "_mesh_stator_bis_save.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.get_group(["stator core", "/", "airgap"]).plot_mesh(
        save_path=join(save_plot_path, simu.name + "_mesh_interface_save.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.plot_contour(
        label="\mu",
        save_path=join(save_plot_path, simu.name + "_mu_save.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.plot_contour(
        label="B",
        save_path=join(save_plot_path, simu.name + "_B_save.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.plot_contour(
        label="H",
        save_path=join(save_plot_path, simu.name + "_H_save.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.get_group("stator core").plot_contour(
        label="H",
        save_path=join(save_plot_path, simu.name + "_stator_save.png"),
        is_show_fig=False,
    )

    test_meshsol.get_group("stator core").plot_contour(
        label="H",
        save_path=join(save_plot_path, simu.name + "_H_stator_bis_save.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.get_group(["stator core", "airgap"]).plot_contour(
        label="\mu",
        save_path=join(save_plot_path, simu.name + "_mu_stator_airgap_save.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.get_group(["rotor core", "rotor magnets"]).plot_contour(
        label="\mu",
        save_path=join(save_plot_path, simu.name + "_mu_rotor_save.png"),
        is_show_fig=False,
    )

    # Test save with MeshSolution object in out
    load_path = join(save_load_path, simu.name + ".h5")

    out.save(save_path=load_path)

    # Test to load the Meshsolution object (inside the output):
    FEMM = load(load_path)

    # TODO : out.compare(FEMM)

    # [Important] To test that fields are still working after saving and loading
    FEMM.mag.meshsolution.plot_mesh(
        save_path=join(save_plot_path, simu.name + "_mesh_load.png"), is_show_fig=False
    )

    FEMM.mag.meshsolution.plot_contour(
        label="B",
        save_path=join(save_plot_path, simu.name + "_B_load.png"),
        is_show_fig=False,
    )

    FEMM.mag.meshsolution.get_group(["rotor core", "rotor magnets"]).plot_contour(
        label="\mu",
        save_path=join(save_plot_path, simu.name + "_mu_rotor_load.png"),
        is_show_fig=False,
    )


# To run it without pytest
if __name__ == "__main__":
    out = test_FEMM_meshsolution_plots_SPMSM()
    # out = test_FEMM_meshsolution_plots_slotless()
    # out = test_FEMM_meshsolution_plots_Prius()
    # out = test_FEMM_meshsolution_plots_Prius()
