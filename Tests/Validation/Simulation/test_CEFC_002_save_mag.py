from numpy import zeros, ones, pi, array
from unittest import TestCase

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Tests.Validation.Machine.CEFC_Lam import CEFC_Lam

from pyleecan.Classes.InCurrent import InCurrent
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output
from pyleecan.Tests import save_validation_path as save_path
from pyleecan.Functions.FEMM import GROUP_SC

simu = Simu1(name="SM_CEFC_002_save_mag", machine=CEFC_Lam, struct=None)

# Definition of the enforced output of the electrical module
Nr = ImportMatrixVal(value=ones(1) * 3000)
Is = ImportMatrixVal(value=array([[2.25353053e02, 2.25353053e02, 2.25353053e02]]))
time = ImportGenVectLin(start=0, stop=1, num=1, endpoint=True)
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
    is_get_mesh=True,
    is_save_FEA=True,
    is_sliding_band=False,
)


class test_CEFC_001(TestCase):
    """Validation of the TOYOTA Prius 2004 interior magnet (V shape) with distributed winding
    50 kW peak, 400 Nm peak at 1500 rpm from publication

    from publication
    Z. Yang, M. Krishnamurthy and I. P. Brown,
    "Electromagnetic and vibrational characteristic of IPM over full torque-speed range,"
    Electric Machines & Drives Conference (IEMDC), 2013 IEEE International, Chicago, IL, 2013, pp. 295-302.
    """

    def test_Magnetic_FEMM(self):
        """Test compute the Flux in FEMM and import the mesh.
        """

        out = Output(simu=simu)
        out.post.legend_name = "Slotless lamination"
        simu.run()

        out.plot_mesh_field(
            mesh=out.mag.meshsolution[0].mesh,
            field=out.mag.meshsolution[0].solution.get_field("mu"),
            title="Permeability",
        )

        out.plot_mesh_field(
            mesh=out.mag.meshsolution[0].mesh,
            field=out.mag.meshsolution[0].solution.get_field("B"),
            title="Magnetic flux",
            group=GROUP_SC,
        )

        # out.save(save_path=save_path)


#    def test_magnetic_force(self):
