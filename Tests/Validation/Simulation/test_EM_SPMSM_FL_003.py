from numpy import ones, pi, array
from unittest import TestCase
from os.path import join
import matplotlib.pyplot as plt
from pyleecan.Tests import save_validation_path as save_path

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Tests.Validation.Machine.IPMSM_A import IPMSM_A

from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportDatFile import ImportDatFile
from pyleecan.Classes.ImportFemmMesh import ImportFemmMesh
from pyleecan.Generator import MAIN_DIR

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.ForceVWP import ForceVWP
from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.Output import Output
from pyleecan.Classes.InFlux import InFlux

path_project = join(MAIN_DIR, "Results", "EM_IPMSM_FL_002", "Femm") + '\\'
simu = Simu1(name="EM_IPMSM_FL_003", machine=IPMSM_A, mag=None)

# Definition of the enforced output of the magnetic module
time = ImportGenVectLin(start=0, stop=1, num=2, endpoint=True)
angle = ImportGenVectLin(start=0, stop=2 * pi, num=1024, endpoint=False)
Br = ImportDatFile(file_path=path_project+'Br.dat')
Bt = ImportDatFile(file_path=path_project+'Bt.dat')
mesh = ImportFemmMesh(project_path=path_project+'Mesh'+'\\')

simu.input = InFlux(
    time=time,
    angle=angle,
    Br=Br,
    Bt=Bt,
    mesh=mesh,
)

# Definition of the magnetic simulation (no symmetry)
# simu.mag = MagFEMM(
#     is_stator_linear_BH=2,
#     is_rotor_linear_BH=2,
#     is_symmetry_a=False,
#     is_antiper_a=True,
#     is_save_mesh=True,
#     is_save_FEA=True,
# )

simu.struct.force = ForceVWP(is_comp_nodal_force=True)

# Copy the simu and activate the symmetry
#simu_sym = Simu1(init_dict=simu.as_dict())
#simu_sym.mag.is_symmetry_a = True
#simu_sym.mag.sym_a = 4
#simu_sym.mag.is_antiper_a = True


class test_EM_IPMSM_FL_003(TestCase):
    """Validation of the TOYOTA Prius 2004 interior magnet (V shape) with distributed winding
      50 kW peak, 400 Nm peak at 1500 rpm from publication

      from publication
      Z. Yang, M. Krishnamurthy and I. P. Brown,
      "Electromagnetic and vibrational characteristic of IPM over full torque-speed range,"
      Electric Machines & Drives Conference (IEMDC), 2013 IEEE International, Chicago, IL, 2013, pp. 295-302.
      """


    def test_load_mesh_for_VWP(self):
        """Test compute and save mesh, FEA solution, and VWP results in .dat files.
        """
        # Definition of the magnetic simulation (no symmetry)
        simu.struct.force.is_save_force = True

        out = Output(simu=simu)
        out.post.legend_name = "Load mesh"
        out.post.line_color = "r--"
        simu.run()

        out.plot_nodal_force()