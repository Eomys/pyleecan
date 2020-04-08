from numpy import ones, pi, array, linspace
from os.path import join
import matplotlib.pyplot as plt
from ....Tests import save_validation_path as save_path

from ....Classes.Simu1 import Simu1
from ....Tests.Validation.Machine.IPMSM_xxx import IPMSM_xxx

from ....Classes.InputCurrent import InputCurrent
from ....Classes.ImportGenVectLin import ImportGenVectLin
from ....Classes.ImportMatrixVal import ImportMatrixVal

from ....Classes.MagFEMM import MagFEMM
from ....Classes.Output import Output


def test_EM_IPMSM_FL_001():
    """Test compute the Flux in FEMM of machine IPMSM_xxx, with and without symmetry
    """
    simu = Simu1(name="EM_IPMSM_FL_001", machine=IPMSM_xxx)

    # Initialization of the simulation starting point
    simu.input = InputCurrent()
    # Set time and space discretization
    simu.input.time.value = linspace(start=0, stop=0.015, num=4, endpoint=True)
    simu.input.angle.value = linspace(start=0, stop=2 * pi, num=1024, endpoint=False)
    # Definition of the enforced output of the electrical module
    simu.input.Is.value = array(  # Stator currents as a function of time
        [
            [6.97244193e-06, 2.25353053e02, -2.25353060e02],
            [-2.60215295e02, 1.30107654e02, 1.30107642e02],
            [-6.97244208e-06, -2.25353053e02, 2.25353060e02],
            [2.60215295e02, -1.30107654e02, -1.30107642e02],
        ]
    )
    simu.input.Ir = None  # SPMSM machine => no rotor currents to define
    simu.input.set_Nr(3000)  # Rotor speed [rpm]
    simu.input.angle_rotor_initial = 0.5216 + pi  # Rotor position at t=0 [rad]

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(
        is_stator_linear_BH=2,
        is_rotor_linear_BH=2,
        is_symmetry_a=False,
        is_antiper_a=True,
    )
    simu.struct = None
    # Copy the simu and activate the symmetry
    simu_sym = Simu1(init_dict=simu.as_dict())
    simu_sym.mag.is_symmetry_a = True
    simu_sym.mag.sym_a = 4
    simu_sym.mag.is_antiper_a = False

    out = Output(simu=simu)
    out.post.legend_name = "No symmetry"
    simu.run()

    out2 = Output(simu=simu_sym)
    out2.post.legend_name = "1/2 symmetry"
    out2.post.line_color = "r--"
    simu_sym.run()

    # Plot the result by comparing the two simulation
    plt.close("all")
    out.plot_B_space(out_list=[out2])

    fig = plt.gcf()
    fig.savefig(join(save_path, "test_EM_IPMSM_FL_001_sym.png"))
