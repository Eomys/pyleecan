from numpy import ones, pi, array, zeros, linspace
from unittest import TestCase
from os.path import join
import matplotlib.pyplot as plt
from pyleecan.Tests import save_plot_path as save_path
from pyleecan.Tests.Plot.LamWind import wind_mat
from pyleecan.Classes.import_all import *
from pyleecan.Tests.Validation.Machine.SPMSM_015 import SPMSM_015


simu = Simu1(name="EM_SPMSM_NL_001", machine=SPMSM_015)
# Modify stator Rext to get move convinsing translation
SPMSM_015.stator.Rext = SPMSM_015.stator.Rext * 0.9
gap = SPMSM_015.comp_width_airgap_mec()

# Definition of the enforced output of the electrical module
Nr = ImportMatrixVal(value=ones(1) * 3000)
Is = ImportMatrixVal(value=array([[0, 0, 0]]))
time = ImportGenVectLin(start=0, stop=0, num=1, endpoint=True)
angle = ImportGenVectLin(start=0, stop=2 * 2 * pi / 9, num=2043, endpoint=False)

simu.input = InCurrent(
    Is=Is,
    Ir=None,  # No winding on the rotor
    Nr=Nr,
    angle_rotor=None,
    time=time,
    angle=angle,
    angle_rotor_initial=0,
)

# Definition of the magnetic simulation (is_mmfr=False => no flux from the magnets)
simu.mag = MagFEMM(
    is_stator_linear_BH=0,
    is_rotor_linear_BH=0,
    is_sliding_band=False,
    is_symmetry_a=False,
    is_mmfs=False,
    is_get_mesh=True,
    is_save_FEA=True,
    sym_a=1,
)
simu.struct = None


class test_plot_transform_FEMM(TestCase):
    """Check that you can apply transformation on FEMM
    """

    def test_ecc(self):
        """Test compute the Flux in FEMM and import the mesh.
        """
        transform_list = [
            {"type": "rotate", "value": 0.08, "label": "MagnetRotorRadial_S_R0_T0_S3"}
        ]
        transform_list.append(
            {"type": "translate", "value": gap * 0.75, "label": "Rotor"}
        )
        simu.mag.transform_list = transform_list

        out = Output(simu=simu)
        simu.run()

        out.plot_mesh_field(
            mesh=out.mag.meshsolution.mesh[0],
            title="Permeability",
            field=out.mag.meshsolution.solution[0].face["mu"],
        )
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_ecc_FEMM.png"))
