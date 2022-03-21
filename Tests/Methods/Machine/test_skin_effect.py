from os.path import join

from numpy.testing import assert_almost_equal

import pytest

# from pyleecan.Classes.Simu1 import Simu1
# from pyleecan.Classes.InputCurrent import InputCurrent
# from pyleecan.Classes.Electrical import Electrical
# from pyleecan.Classes.EEC_PMSM import EEC_PMSM
# from pyleecan.Classes.Output import Output

from pyleecan.Classes.CondType11 import CondType11
from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR


def test_skin_effect_preformed_rectangular():
    """Validation case from "Design of Rotating Electrical Machines", J. Pyrhonen, second edition
    Example 5.1 (a) p273
    """

    # Data from example
    hc0 = 2e-3
    bc0 = 10e-3
    b = 14e-3  # slot width
    zp = 6
    za = 1
    zt = 2  # number of turns in series per coil
    freq = 50
    T_op = 20
    sigma = 57e6

    cond_mat = load(join(DATA_DIR, "Material", "Copper1.json"))
    cond_mat.elec.rho = 1 / sigma

    cond = CondType11(
        Hwire=hc0, Wwire=bc0, Nwppc_rad=zp, Nwppc_tan=za, cond_mat=cond_mat
    )

    kr_skin = cond.comp_skin_effect_resistance(T_op=T_op, freq=freq, b=b, zt=zt)

    assert_almost_equal(kr_skin, 1.54, decimal=1)
    # assert_almost_equal(out2.mag.Tem_av, 81.70, decimal=1)


if __name__ == "__main__":
    test_skin_effect_preformed_rectangular()
