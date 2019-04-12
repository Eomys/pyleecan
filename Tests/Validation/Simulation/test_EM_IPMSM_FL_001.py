from numpy import ones, pi, array
from unittest import TestCase
from os.path import join
import matplotlib.pyplot as plt
from pyleecan.Tests import save_validation_path as save_path

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Tests.Validation.Machine.IPMSM_xxx import IPMSM_xxx

from pyleecan.Classes.InCurrent import InCurrent
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output

simu = Simu1(name="EM_IPMSM_FL_001", machine=IPMSM_xxx)

# Definition of the enforced output of the electrical module
Nr = ImportMatrixVal(value=ones(4) * 3000)
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
angle = ImportGenVectLin(start=0, stop=2 * pi, num=1024, endpoint=False)

simu.input = InCurrent(
    Is=Is,
    Ir=None,  # No winding on the rotor
    Nr=Nr,
    angle_rotor=None,  # Will be computed
    time=time,
    angle=angle,
    angle_rotor_initial=0.5216 + pi,
)

# Definition of the magnetic simulation (no symmetry)
simu.mag = MagFEMM(
    is_stator_linear_BH=2, is_rotor_linear_BH=2, is_symmetry_a=False, is_antiper_a=True
)
# Copy the simu and activate the symmetry
simu_sym = Simu1(init_dict=simu.as_dict())
simu_sym.mag.is_symmetry_a = True
simu_sym.mag.sym_a = 4
simu_sym.mag.is_antiper_a = False


class test_EM_IPMSM_FL_001(TestCase):
    """unittest FEMM machine IPMSM_xxx
    """

    def test_Magnetic_FEMM_sym(self):
        """Test compute the Flux in FEMM, with and without symmetry
		"""

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
