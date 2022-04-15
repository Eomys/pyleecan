from os.path import join

import pytest

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
    Toyota_Prius.stator.winding.Lewout = 0.003

    Ks = Toyota_Prius.stator.comp_fill_factor()
    assert_almost_equal(Ks, 0.46, decimal=2)

    Toyota_Prius.stator.winding.end_winding = EndWindingCirc()
    Lw_circ = Toyota_Prius.stator.winding.end_winding.comp_inductance()
    Rs = Toyota_Prius.stator.comp_resistance_wind()
    assert_almost_equal(Rs, 0.06, decimal=2)

    # Get permeance coefficients for end-winding inductance calculation
    # from "Design of Rotating Electrical Machines", J. Pyrhonen, second edition, Table 4.2, second line
    lambda_length = 0.321
    lambda_width = 0.215
    Toyota_Prius.stator.winding.end_winding = EndWindingRect(
        lambda_length=lambda_length, lambda_width=lambda_width
    )
    Lw_rect = Toyota_Prius.stator.winding.end_winding.comp_inductance()
    Rs = Toyota_Prius.stator.comp_resistance_wind()
    assert_almost_equal(Rs, 0.05, decimal=2)


if __name__ == "__main__":
    test_resistance_inductance()
