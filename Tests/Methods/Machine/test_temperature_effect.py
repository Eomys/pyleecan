from os.path import join

import pytest

from numpy import pi
from numpy.testing import assert_almost_equal

from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR


@pytest.mark.IPMSM
def test_temperature_effect_magnet():
    """Validation of temperature effects on magnet properties"""

    T_ref = 20
    T_op = 100
    # Load machines
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    magnet = Toyota_Prius.rotor.hole[0].magnet_0.mat_type

    assert magnet.mag.alpha_Br == -0.001
    assert magnet.mag.Brm20 == 1.24
    assert magnet.mag.mur_lin == 1.05

    Hc20 = magnet.mag.get_Hc()
    Hc100 = magnet.mag.get_Hc(T_op=T_op)
    assert_almost_equal(Hc20, magnet.mag.Brm20 / (4 * pi * 1e-7 * magnet.mag.mur_lin))
    assert_almost_equal(Hc100 / Hc20, 1 + magnet.mag.alpha_Br * (T_op - T_ref))

    Brm20 = magnet.mag.get_Brm()
    Brm100 = magnet.mag.get_Brm(T_op=T_op)
    assert_almost_equal(Brm100 / Brm20, 1 + magnet.mag.alpha_Br * (T_op - T_ref))


if __name__ == "__main__":
    test_temperature_effect_magnet()
