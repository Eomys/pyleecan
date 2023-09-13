from os.path import join, isfile

import pytest

import numpy as np
from numpy.testing import assert_almost_equal

from SciDataTool.Functions.Plot.plot_2D import plot_2D

from pyleecan.Classes.Electrical import Electrical
from pyleecan.Classes.EEC_SCIM import EEC_SCIM
from pyleecan.Classes.LUTslip import LUTslip
from pyleecan.Classes.InputVoltage import InputVoltage
from pyleecan.Classes.ImportMatlab import ImportMatlab
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.OPslip import OPslip

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D

from pyleecan.definitions import DATA_DIR, TEST_DIR

is_show_fig = True


param_list_Audi_eTron = [
    {
        "U0_ref": 144,
        "N0": 4832,
        "slip_ref": 0.047,
        "Tem_av": 247,
        "I1_abs": 333,
        "Pjoule_s": 6304,
        "Pjoule_r": 6160,
    },
    {
        "U0_ref": 200,
        "N0": 9664,
        "slip_ref": 0.018,
        "Tem_av": 107,
        "I1_abs": 181,
        "Pjoule_s": 1869,
        "Pjoule_r": 1979,
    },
]


@pytest.mark.SCIM
@pytest.mark.Electrical
def test_EEC_ELUT_Railway_Traction(is_run=True, is_linear=False):
    """Validation of the Railway Traction SCIM electrical equivalent circuits"""

    # Load reference results
    matlab_path = TEST_DIR + "/Data/ELUT_Railway_Traction.mat"

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
    Railway_Traction = load(join(DATA_DIR, "Machine", "Railway_Traction.json"))

    # Check material data
    assert Railway_Traction.stator.winding.conductor.cond_mat.elec.alpha == 0.00393
    assert Railway_Traction.stator.winding.conductor.cond_mat.elec.rho == 1.73e-8

    assert Railway_Traction.rotor.winding.conductor.cond_mat.elec.alpha == 0.003
    assert Railway_Traction.rotor.winding.conductor.cond_mat.elec.rho == 2.2e-8
    assert Railway_Traction.rotor.ring_mat.elec.alpha == 0.003
    assert Railway_Traction.rotor.ring_mat.elec.rho == 2.2e-8

    simu = Simu1(name="test_EEC_ELUT_Railway_Traction", machine=Railway_Traction)

    simu.input = InputVoltage(
        OP=OPslip(
            U0_ref=param_dict["U0"], N0=param_dict["N0"], slip_ref=param_dict["slip"]
        ),
        Na_tot=2016,
        Nt_tot=2016,
    )

    if is_linear:
        Lm_table = np.array([param_dict["Lm"][0], param_dict["Lm"][0]])
        Im_table = np.array([param_dict["Im"][0], param_dict["Im"][-1]])
    else:
        Lm_table = param_dict["Lm"]
        Im_table = param_dict["Im"]

    ELUT_Railway_Traction = LUTslip()
    ELUT_Railway_Traction.simu = Simu1(machine=Railway_Traction)
    ELUT_Railway_Traction.simu.elec = Electrical(
        eec=EEC_SCIM(
            R1=param_dict["R1_20"],
            L1=param_dict["L10"],
            Tsta=20,
            R2=param_dict["R2_20"],
            L2=param_dict["L20"],
            Trot=20,
            Lm_table=Lm_table,
            Im_table=Im_table,
            type_skin_effect=0,
        )
    )

    # Configure simulation
    simu.elec = Electrical(
        Tsta=param_dict["Tswind"],
        Trot=param_dict["Trwind"],
        LUT_enforced=ELUT_Railway_Traction,
    )

    if is_run:
        # Run simulation
        out = simu.run()

        assert_almost_equal(out.elec.Tem_av, param_dict["Cem"], decimal=1)
        assert_almost_equal(out.elec.eec.R1, param_dict["R10"], decimal=4)
        assert_almost_equal(out.elec.eec.R2, param_dict["R20"], decimal=4)
        assert_almost_equal(out.elec.eec.L1, param_dict["L10"], decimal=4)
        assert_almost_equal(out.elec.eec.L2, param_dict["L20"], decimal=4)
        assert_almost_equal(
            out.elec.Pj_losses / 100,
            (param_dict["Pjs0"] + param_dict["Pjr0"]) / 100,
            decimal=0,
        )

    return Railway_Traction, param_dict, ELUT_Railway_Traction


@pytest.mark.SCIM
@pytest.mark.Electrical
@pytest.mark.parametrize("param_dict", param_list_Audi_eTron)
def test_EEC_ELUT_SCIM_Audi_eTron(param_dict, is_run=True, is_linear=False):
    """Validation of the Audi eTron SCIM electrical equivalent circuits"""

    Audi_eTron = load(join(DATA_DIR, "Machine", "Audi_eTron.json"))
    Audi_eTron.stator.winding.Lewout = 0.05
    Audi_eTron.rotor.slot.wedge_mat = Audi_eTron.rotor.mat_type

    simu = Simu1(name="test_EEC_ELUT_SCIM_Audi_eTron", machine=Audi_eTron)

    param_dict["Lm"] = np.array(
        [
            0.00364256,
            0.00364256,
            0.00295137,
            0.00213818,
            0.00160483,
            0.00128478,
            0.00107101,
            0.00091922,
            0.00080651,
            0.00071975,
            0.00065101,
        ]
    )

    param_dict["Im"] = np.array(
        [
            0,
            1.00000000e-01,
            3.34222222e01,
            6.67444444e01,
            1.00066667e02,
            1.33388889e02,
            1.66711111e02,
            2.00033333e02,
            2.33355556e02,
            2.66677778e02,
            3.00000000e02,
        ]
    )

    if is_linear:
        Lm_table = np.array([param_dict["Lm"][0], param_dict["Lm"][0]])
        Im_table = np.array([param_dict["Im"][0], param_dict["Im"][-1]])
    else:
        Lm_table = param_dict["Lm"]
        Im_table = param_dict["Im"]

    simu.input = InputVoltage(
        OP=OPslip(
            U0_ref=param_dict["U0_ref"],
            N0=param_dict["N0"],
            slip_ref=param_dict["slip_ref"],
        ),
        Na_tot=1000 * 2,
        Nt_tot=400 * 2,
        is_periodicity_a=True,
        is_periodicity_t=False,
        # Nrev=1,
        angle_rotor_initial=0 * 0.02,
    )

    ELUT_Audi_eTron = LUTslip()
    ELUT_Audi_eTron.simu = Simu1(machine=Audi_eTron)
    R1_135 = 1 / (3 * 333 ** 2 / 6304)  # from Joule losses
    ELUT_Audi_eTron.simu.elec = Electrical(
        eec=EEC_SCIM(
            R1=R1_135,
            L1=0.975 * 1.0899e-04,
            Tsta=135,
            R2=0.0108,
            L2=8.4080e-07,
            Trot=20,
            Lm_table=Lm_table,
            Im_table=Im_table,
            type_skin_effect=0,
        )
    )

    # Configure simulation
    simu.elec = Electrical(
        Tsta=135,
        Trot=175,
        LUT_enforced=ELUT_Audi_eTron,
    )

    if is_run:
        # Run simulation
        # %%
        out = simu.run()

        eec = out.elec.eec
        I1_abs = abs(eec.I1)
        qs = Audi_eTron.stator.winding.qs
        Pjoule_s = qs * eec.R1 * abs(eec.I1) ** 2
        Pjoule_r = qs * eec.R2 * abs(eec.I2) ** 2

        # Ir = out.elec.Ir.get_data_along(
        #     "time=axis_data",
        #     "phase[smallestperiod]",
        #     axis_data={"time": out.elec.axes_dict["time"].get_values()},
        # )

        assert_almost_equal(out.elec.Tem_av / 10, param_dict["Tem_av"] / 10, decimal=0)
        assert_almost_equal(I1_abs / 10, param_dict["I1_abs"] / 10, decimal=0)
        assert_almost_equal(Pjoule_s / 1000, param_dict["Pjoule_s"] / 1000, decimal=0)
        assert_almost_equal(Pjoule_r / 100, param_dict["Pjoule_r"] / 100, decimal=0)

    return Audi_eTron, param_dict, ELUT_Audi_eTron


if __name__ == "__main__":
    test_EEC_ELUT_Railway_Traction()
    test_EEC_ELUT_SCIM_Audi_eTron(param_dict=param_list_Audi_eTron[0])
    test_EEC_ELUT_SCIM_Audi_eTron(param_dict=param_list_Audi_eTron[1])

    print("Done")
