from os.path import join

import pytest

from numpy import pi
from numpy.testing import assert_almost_equal

from pyleecan.Classes.EndWindingRect import EndWindingRect
from pyleecan.Classes.EndWindingCirc import EndWindingCirc

from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR


@pytest.mark.IPMSM
def test_resistance_inductance():
    """Validation of resistance and inductance calculation in comparison with
    "Electromagnetic Analysis and Design Methodology
    for Permanent Magnet Motors Using MotorAnalysis-PM Software" """

    # T_ref = 20s
    # T_op = 100

    # Load machines
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius_loss.json"))

    Ks = Toyota_Prius.stator.comp_fill_factor()
    assert_almost_equal(Ks, 0.46, decimal=2)

    Rs = Toyota_Prius.stator.comp_resistance_wind()
    assert_almost_equal(Rs, 0.0508, decimal=3)

    Toyota_Prius.stator.winding.end_winding = EndWindingCirc()
    Lw_circ = Toyota_Prius.stator.winding.end_winding.comp_inductance()

    # Get permeance coefficients for end-winding inductance calculation
    # from "Design of Rotating Electrical Machines", J. Pyrhonen, second edition, Table 4.2, second line
    lambda_length = 0.321
    lambda_width = 0.215
    Toyota_Prius.stator.winding.end_winding = EndWindingRect(
        lambda_length=lambda_length, lambda_width=lambda_width
    )
    Lw_rect = Toyota_Prius.stator.winding.end_winding.comp_inductance()


if __name__ == "__main__":
    test_resistance_inductance()
