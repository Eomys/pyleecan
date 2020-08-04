from numpy import ones, pi, array

from pyleecan.Classes.Simu1 import Simu1
from Tests.Validation.Simulation.CEFC_Lam import CEFC_Lam

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output
import pytest


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
def test_CEFC_001():
    """Test compute the Flux in FEMM without slots and without sliding band.
    """
    simu = Simu1(name="SM_CEFC_001", machine=CEFC_Lam, struct=None)

    # Definition of the enforced output of the electrical module
    N0 = 3000
    Is = ImportMatrixVal(value=array([[2.25353053e02, 2.25353053e02, 2.25353053e02]]))
    time = ImportGenVectLin(start=0, stop=1, num=1, endpoint=True)
    angle = ImportGenVectLin(start=0, stop=2 * pi, num=1024, endpoint=False)

    simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        N0=N0,
        angle_rotor=None,  # Will be computed
        time=time,
        angle=angle,
    )

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(type_BH_stator=2, type_BH_rotor=0, is_sliding_band=False)
    simu.force = None
    simu.struct = None

    out = Output(simu=simu)
    out.post.legend_name = "Slotless lamination"
    simu.run()
