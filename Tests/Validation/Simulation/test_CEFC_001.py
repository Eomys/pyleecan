from numpy import ones, pi, array
from unittest import TestCase

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Tests.Validation.Machine.CEFC_Lam import CEFC_Lam

from pyleecan.Classes.InCurrent import InCurrent
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output

simu = Simu1(name="SM_CEFC_001", machine=CEFC_Lam, struct=None)

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
simu.mag = MagFEMM(is_stator_linear_BH=2, is_rotor_linear_BH=0, is_sliding_band=False)


class test_CEFC_001(TestCase):
    """ A slotless stator.

    """

    def test_Magnetic_FEMM(self):
        """Test compute the Flux in FEMM without sliding band.
        """

        out = Output(simu=simu)
        out.post.legend_name = "Slotless lamination"
        simu.run()
