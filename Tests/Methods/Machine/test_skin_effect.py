from os.path import join

from numpy.testing import assert_almost_equal

from pyleecan.Classes.CondType11 import CondType11
from pyleecan.Classes.CondType21 import CondType21
from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR


def test_skin_effect():
    """Test skin effect on resistance and inductance of conductor
    Validation case from "Design of Rotating Electrical Machines", J. Pyrhonen, second edition
    """

    ###### Example 5.1 (a) p273
    # Single layer winding, two turns per coil, 6 parallel wires per conductor, no transposition
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
    kl_skin = cond.comp_skin_effect_inductance(
        T_op=T_op, freq=freq, b4=b, h4=zt * zp * hc0, zt=zt
    )

    assert_almost_equal(kr_skin, 1.54, decimal=1)  # from book
    assert_almost_equal(kl_skin, 0.641, decimal=1)  # not validated in book

    ###### Example 5.1 (b) p273
    # Single layer winding, two turns per coil, 6 parallel wires per conductor, transposition
    # Data from example
    hc0 = 2e-3
    bc0 = 10e-3
    b = 14e-3  # slot width
    zp = 1
    za = 1
    zt = 12  # number of wires in coil = 2*6 due to transposition
    freq = 50
    T_op = 20
    sigma = 57e6

    cond_mat = load(join(DATA_DIR, "Material", "Copper1.json"))
    cond_mat.elec.rho = 1 / sigma

    cond = CondType11(
        Hwire=hc0, Wwire=bc0, Nwppc_rad=zp, Nwppc_tan=za, cond_mat=cond_mat
    )

    kr_skin = cond.comp_skin_effect_resistance(T_op=T_op, freq=freq, b=b, zt=zt)
    kl_skin = cond.comp_skin_effect_inductance(
        T_op=T_op, freq=freq, b4=b, h4=zt * zp * hc0, zt=zt
    )

    assert_almost_equal(kr_skin, 1.01, decimal=1)  # from book
    assert_almost_equal(kl_skin, 0.620, decimal=1)  # not validated in book

    ###### Example 5.4 (b) 275
    # Rotor bar in squirrel cage
    # Data from example
    hc0 = 50e-3
    bc0 = 14e-3  # bar width
    b = 14e-3  # slot width
    zt = 1
    freq = 50
    T_op = 50
    sigma = 57e6

    cond_mat = load(join(DATA_DIR, "Material", "Copper1.json"))
    cond_mat.elec.rho = 1 / sigma

    cond = CondType21(Hbar=hc0, Wbar=bc0, cond_mat=cond_mat)

    kr_skin = cond.comp_skin_effect_resistance(T_op=T_op, freq=freq, b=b, zt=zt)
    kl_skin = cond.comp_skin_effect_inductance(
        T_op=T_op, freq=freq, b4=b, h4=hc0, zt=zt
    )

    assert_almost_equal(kr_skin, 5.0, decimal=1)  # from book
    assert_almost_equal(kl_skin, 0.299, decimal=1)  # not validated in book


if __name__ == "__main__":
    test_skin_effect()
