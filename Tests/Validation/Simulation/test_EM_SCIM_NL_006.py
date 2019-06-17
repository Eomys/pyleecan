from numpy import ones, pi, array, zeros
from unittest import TestCase
from os.path import join
import matplotlib.pyplot as plt
from pyleecan.Tests import save_validation_path as save_path

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Tests.Validation.Machine.SCIM_006 import SCIM_006

from pyleecan.Classes.InCurrent import InCurrent
from pyleecan.Classes.InFlux import InFlux
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.ImportMatlab import ImportMatlab

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output
from pyleecan.Tests import DATA_DIR

simu = Simu1(name="EM_SCIM_NL_006", machine=SCIM_006)

# Definition of the enforced output of the electrical module
Nr = ImportMatrixVal(value=ones(1) * 1500)
Is = ImportMatrixVal(value=array([[20, -10, -10]]))
Ir = ImportMatrixVal(value=zeros((1, 28)))
time = ImportGenVectLin(start=0, stop=0, num=1, endpoint=False)
angle = ImportGenVectLin(start=0, stop=2 * pi, num=4096, endpoint=False)

simu.input = InCurrent(
    Is=Is,
    Ir=Ir,  # zero current for the rotor
    Nr=Nr,
    angle_rotor=None,  # Will be computed
    time=time,
    angle=angle,
    angle_rotor_initial=0.2244,
)

# Definition of the magnetic simulation (no symmetry)
simu.mag = MagFEMM(
    is_stator_linear_BH=2, is_rotor_linear_BH=2, is_symmetry_a=False, is_antiper_a=True
)
simu.struct = None
# Copy the simu and activate the symmetry
simu_sym = Simu1(init_dict=simu.as_dict())
simu_sym.mag.is_symmetry_a = True
simu_sym.mag.sym_a = 2

# Just load the Output and ends (we could also have directly filled the Output object)
simu_load = Simu1(init_dict=simu.as_dict())
simu_load.mag = None
mat_file = join(DATA_DIR, "EM_SCIM_NL_006_MANATEE_MMF.mat")
Br = ImportMatlab(file_path=mat_file, var_name="XBr")
angle2 = ImportGenVectLin(start=0, stop=pi, num=4096 / 2, endpoint=False)
simu_load.input = InFlux(time=time, angle=angle2, Br=Br, Bt=None)


class test_EM_SCIM_NL_006(TestCase):
    """Validation of the FEMM model of a polar SCIM machine
    Only one time step
    
    From publication:
    K. Boughrara
    Analytical Analysis of Cage Rotor Induction Motors in Healthy, Defective and Broken Bars Conditions
    IEEE Trans on Mag, 2014
    """

    def test_Magnetic_FEMM_sym(self):
        """Test compute the Flux in FEMM, with and without symmetry
        and with MANATEE MMF analytical model
		"""

        out = Output(simu=simu)
        out.post.legend_name = "No symmetry"
        simu.run()

        out2 = Output(simu=simu_sym)
        out2.post.legend_name = "1/2 symmetry"
        out2.post.line_color = "r--"
        simu_sym.run()

        out3 = Output(simu=simu_load)
        out3.post.legend_name = "MANATEE MMF"
        out3.post.line_color = "g--"
        simu_load.run()

        # Plot the result by comparing the two simulation (sym / no sym)
        plt.close("all")
        out.plot_B_space(out_list=[out2])

        fig = plt.gcf()
        fig.savefig(join(save_path, "test_EM_SCIM_NL_006_sym.png"))

        # Plot the result by comparing the two simulation (no sym / MANATEE)
        plt.close("all")
        out.plot_B_space(j_t0=0, is_deg=False, out_list=[out3])

        fig = plt.gcf()
        fig.savefig(join(save_path, "test_EM_SCIM_NL_006_MMF.png"))
