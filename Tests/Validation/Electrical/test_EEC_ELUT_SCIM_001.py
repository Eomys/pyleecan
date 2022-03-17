from os.path import join, isfile

import pytest

from numpy import abs as np_abs
from numpy.testing import assert_almost_equal

from pyleecan.Classes.Electrical import Electrical
from pyleecan.Classes.EEC_SCIM import EEC_SCIM
from pyleecan.Classes.LUTslip import LUTslip
from pyleecan.Classes.InputVoltage import InputVoltage
from pyleecan.Classes.ImportMatlab import ImportMatlab
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.OPslip import OPslip

from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR, TEST_DIR

is_show_fig = False


@pytest.mark.SCIM
@pytest.mark.Electrical
def test_EEC_ELUT_SCIM_001():
    """Validation of the SCIM electrical equivalent circuits"""

    # Load reference results
    matlab_path = TEST_DIR + "/Data/ELUT_SCIM_001.mat"

    assert isfile(matlab_path)

    param_dict = dict()
    param_list = [
        "slip",
        "N0",
        "Im",
        "Lm",
        "R10",
        "R20",
        "R1_20",
        "R2_20",
        "L10",
        "L20",
        "I10",
        "U0",
        "I20",
        "Tswind",
        "Trwind",
        "Cem",
        "Pjr0",
        "Pjs0",
    ]

    for param in param_list:
        value = ImportMatlab(file_path=matlab_path, var_name=param).get_data()
        if value.size == 1:
            if value.dtype == complex:
                param_dict[param] = complex(value)
            else:
                param_dict[param] = float(value)
        else:
            param_dict[param] = value

    # Prepare simulation
    SCIM_001 = load(join(DATA_DIR, "Machine", "SCIM_001.json"))

    # Update material data
    # (#TODO check also difference of rotor bar section)
    SCIM_001.stator.winding.conductor.cond_mat.elec.alpha = 0.0039
    SCIM_001.stator.winding.conductor.cond_mat.elec.rho = 1.73e-8

    SCIM_001.stator.winding.conductor.cond_mat.elec.alpha = 0.0039
    SCIM_001.stator.winding.conductor.cond_mat.elec.rho = 1.73e-8

    SCIM_001.rotor.winding.conductor.cond_mat.elec.alpha = 0.003
    SCIM_001.rotor.winding.conductor.cond_mat.elec.rho = 2.2e-8
    SCIM_001.rotor.ring_mat.elec.alpha = 0.003
    SCIM_001.rotor.ring_mat.elec.rho = 2.2e-8

    simu = Simu1(name="test_EEC_ELUT_SCIM_001", machine=SCIM_001)

    simu.input = InputVoltage(
        OP=OPslip(
            U0_ref=param_dict["U0"], N0=param_dict["N0"], slip_ref=param_dict["slip"]
        ),
        Na_tot=2016,
        Nt_tot=2016,
    )

    ELUT_SCIM_001 = LUTslip()
    ELUT_SCIM_001.simu = Simu1(machine=SCIM_001)
    ELUT_SCIM_001.simu.elec = Electrical(
        eec=EEC_SCIM(
            R1=param_dict["R1_20"],
            L1=param_dict["L10"],
            Tsta=20,
            R2=param_dict["R2_20"],
            L2=param_dict["L20"],
            Trot=20,
            Lm_table=np_abs(param_dict["Lm"]),
            Im_table=np_abs(param_dict["Im"]),
        )
    )

    # Configure simulation
    simu.elec = Electrical(
        Tsta=param_dict["Tswind"],
        Trot=param_dict["Trwind"],
        LUT_enforced=ELUT_SCIM_001,
    )

    # Run simulation
    out = simu.run()

    assert_almost_equal(out.elec.Tem_av_ref, param_dict["Cem"], decimal=1)
    assert_almost_equal(out.elec.eec.R1, param_dict["R10"], decimal=4)
    assert_almost_equal(out.elec.eec.R2, param_dict["R20"], decimal=4)
    assert_almost_equal(out.elec.eec.L1, param_dict["L10"], decimal=4)
    assert_almost_equal(out.elec.eec.L2, param_dict["L20"], decimal=4)
    assert_almost_equal(
        out.elec.Pj_losses / 100,
        (param_dict["Pjs0"] + param_dict["Pjr0"]) / 100,
        decimal=0,
    )

    return out


if __name__ == "__main__":

    out = test_EEC_ELUT_SCIM_001()
    print("Done")
