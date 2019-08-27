from numpy import ones, pi, array
from unittest import TestCase
from os.path import join
import matplotlib.pyplot as plt
from pyleecan.Tests import save_validation_path as save_path

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Tests.Validation.Machine.IPMSM_A import IPMSM_A

from pyleecan.Classes.InCurrent import InCurrent
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.ForceVWP import ForceVWP
from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.Output import Output

simu = Simu1(name="EM_IPMSM_FL_002", machine=IPMSM_A)

# Definition of the enforced output of the electrical module
Nr = ImportMatrixVal(value=ones(2) * 3000)
Is = ImportMatrixVal(
    value=array(
        [
            [2.25353053e02, 2.25353053e02, 2.25353053e02],
            [2.25353053e02, 2.25353053e02, 2.25353053e02]
        ]
    )
)
time = ImportGenVectLin(start=0, stop=1, num=2, endpoint=True)
angle = ImportGenVectLin(start=0, stop=2 * pi, num=1024, endpoint=False)

simu.input = InCurrent(
    Is=Is,
    Ir=None,  # No winding on the rotor
    Nr=Nr,
    angle_rotor=None,  # Will be computed
    time=time,
    angle=angle,
)

# Definition of the magnetic simulation (no symmetry)
simu.mag = MagFEMM(
    is_stator_linear_BH=2,
    is_rotor_linear_BH=2,
    is_symmetry_a=False,
    is_antiper_a=True,
    is_save_mesh=True,
    is_save_FEA=True,
    is_load_FEA=False
)

simu.struct.force = ForceVWP(is_comp_nodal_force=True)

# Copy the simu and activate the symmetry
simu_sym = Simu1(init_dict=simu.as_dict())
simu_sym.mag.is_symmetry_a = True
simu_sym.mag.sym_a = 4
simu_sym.mag.is_antiper_a = True


class test_EM_IPMSM_FL_004(TestCase):
    """Validation of the TOYOTA Prius 2004 interior magnet (V shape) with distributed winding
      50 kW peak, 400 Nm peak at 1500 rpm from publication

      from publication
      Z. Yang, M. Krishnamurthy and I. P. Brown,
      "Electromagnetic and vibrational characteristic of IPM over full torque-speed range,"
      Electric Machines & Drives Conference (IEMDC), 2013 IEEE International, Chicago, IL, 2013, pp. 295-302.
      """

    def test_comp_force_VWP(self):
        """Test compute nodal forces based on the VWP
		"""


        out = Output(simu=simu_sym)
        out.post.legend_name = "1/2 symmetry"
        out.post.line_color = "r--"
        simu_sym.run()

        # Plot the result by comparing the two simulation
        out.plot_nodal_force()

        # plt.close("all")

        fig = plt.gcf()
        fig.savefig(join(save_path, "test_EM_SPMSM_FL_004_quiverVWP.png"))


    def test_load_mesh_for_VWP(self):
        """Test compute and save mesh, FEA solution, and VWP results in .dat files.
        """
        # Definition of the magnetic simulation (no symmetry)
        simu_sym.mag.is_load_FEA = True
        simu_sym.struct.force.is_save_force = True

        out = Output(simu=simu_sym)
        out.post.legend_name = "Load mesh"
        out.post.line_color = "r--"
        simu_sym.run()

        out.plot_nodal_force()