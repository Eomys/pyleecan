from numpy import ones, pi, array, linspace, zeros
from os.path import join
import pytest
from multiprocessing import cpu_count

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
import time


@pytest.mark.MagFEMM
@pytest.mark.IPMSM
@pytest.mark.periodicity
def test_copy_out():
    """Test the compare method"""
    # Create reference object
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    simu = Simu1(name="test_copy_out", machine=Toyota_Prius)

    # Initialization of the simulation starting point
    simu.input = InputCurrent()
    # Set time and space discretization
    simu.input.Nt_tot = 128
    simu.input.Na_tot = 2048
    simu.input.OP = OPdq(N0=3000, Id_ref=0, Iq_ref=0)

    varload = VarLoadCurrent()
    varload.type_OP_matrix = 0  # Matrix N0, I0, Phi0, Tem_ref

    # creating the Operating point matrix
    OP_matrix = array([[10, 0, 0], [100, 0, 0], [1000, 0, 0]])
    varload.OP_matrix = OP_matrix
    simu.var_simu = varload

    # Use first OP as reference (to skip one computation)
    simu.input.set_OP_from_array(
        OP_matrix=OP_matrix, type_OP_matrix=varload.type_OP_matrix, index=1
    )

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(
        is_periodicity_a=True, is_periodicity_t=True, nb_worker=cpu_count(),
    )
    simu.force = None
    simu.struct = None

    out = simu.run()
    Nb_copy = 1

    # New copy method
    T_new = 0
    for ii in range(Nb_copy):
        T1 = time.time()
        out_3 = out.copy()
        T2 = time.time()
        T_new += T2 - T1

    # Old copy method
    T_old = 0
    for ii in range(Nb_copy):
        T1 = time.time()
        out_2 = type(out)(init_dict=out.as_dict())
        T2 = time.time()
        T_old += T2 - T1

    print("Old method: " + str(T_old / Nb_copy))
    print("New method: " + str(T_new / Nb_copy))

    assert len(out_3.compare(out_2, is_add_value=True)) == 0


if __name__ == "__main__":
    test_copy_out()
