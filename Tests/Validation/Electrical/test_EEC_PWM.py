from os.path import join

import pytest

import numpy as np
from numpy.testing import assert_array_less, assert_almost_equal

from SciDataTool.Functions.Plot.plot_2D import plot_2D

from pyleecan.Classes.ImportGenPWM import ImportGenPWM
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputVoltage import InputVoltage
from pyleecan.Classes.Electrical import Electrical
from pyleecan.Classes.EEC_PMSM import EEC_PMSM
from pyleecan.Classes.OPdq import OPdq

from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR


is_show_fig = False

param_list = [
    {"strategy": "Sine", "type_PWM": 8, "val1": 0.34, "val2": 0.371},
    {"strategy": "Space_Vector", "type_PWM": 7, "val1": 0.23, "val2": 0.393},
]


@pytest.mark.long_5s
@pytest.mark.parametrize("param_dict", param_list)
def test_EEC_PWM(param_dict):
    """Validate that voltage amplitudes are consistent with modulation index"""

    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    simu = Simu1(name="test_EEC_PWM_" + param_dict["strategy"], machine=Toyota_Prius)

    Vdc1 = 500
    fswi = 5000
    freq_max = 20000

    M_I_val = np.linspace(0.05, 1.1, 13)

    # Definition of the input
    simu.input = InputVoltage(
        OP=OPdq(N0=1000, Ud_ref=0, Uq_ref=0),
        Na_tot=256 * 8,
        Nt_tot=256 * 8,
        PWM=ImportGenPWM(
            fmax=2 * freq_max, fswi=5000, Vdc1=Vdc1, typePWM=param_dict["type_PWM"]
        ),
    )

    simu.elec = Electrical(
        eec=EEC_PMSM(Ld=0.0005, Lq=0.001, Phid_mag=0.1, Phiq_mag=0),
        freq_max=freq_max,
    )

    output_list = list()
    PWM_orders = np.array([[1, 0], [-2, 1], [2, 1], [-1, 2], [1, 2], [-2, 3], [2, 3]])
    Us_PWM = np.zeros((M_I_val.size, PWM_orders.shape[0]))
    Is_PWM = np.zeros((M_I_val.size, PWM_orders.shape[0]))
    for ii, M_I in enumerate(M_I_val):
        simu_M_I = simu.copy()

        U0 = M_I * Vdc1 / (2 * np.sqrt(2))
        simu_M_I.input.OP.Ud_ref = U0
        simu_M_I.input.PWM.U0 = U0
        assert_almost_equal(M_I - simu_M_I.input.PWM.get_modulation_index(), 0)

        out_M_I = simu_M_I.run()

        assert_almost_equal(M_I - out_M_I.elec.PWM.get_modulation_index(), 0)

        freq0 = np.array([out_M_I.elec.OP.felec, fswi])

        freqs_PWM = np.matmul(PWM_orders, freq0).tolist()

        Us_PWM[ii, :] = out_M_I.elec.Us.get_magnitude_along(
            "freqs=" + str(freqs_PWM), "phase[0]"
        )[out_M_I.elec.Us.symbol]

        Is_PWM[ii, :] = out_M_I.elec.Is.get_magnitude_along(
            "freqs=" + str(freqs_PWM), "phase[0]"
        )[out_M_I.elec.Is.symbol]

        output_list.append(out_M_I)

    legend_list = list()
    for orders in PWM_orders.tolist():
        if orders[1] == 0:
            orders_lab = str(orders[0]) + "fe"
        elif orders[0] > 0:
            orders_lab = str(orders[1]) + "fs + " + str(orders[0]) + "fe"
        else:
            orders_lab = str(orders[1]) + "fs - " + str(abs(orders[0])) + "fe"

        legend_list.append(orders_lab)

    # Check harmonic level: fsi +/- 2*fe
    assert_array_less(2 * Us_PWM[:, 1:3] / Vdc1, param_dict["val1"])

    # Check harmonic level: 2*fsi +/- fe
    assert_array_less(2 * Us_PWM[:, 3:5] / Vdc1, param_dict["val2"])

    if is_show_fig:
        plot_2D(
            [M_I_val],
            [2 * Us_PWM[:, ii] / Vdc1 for ii in range(Us_PWM.shape[1])],
            title="Voltage PWM harmonics function of modulation index ("
            + param_dict["strategy"]
            + ")",
            xlabel="Modulation index []",
            ylabel="Amplitude [p.u]",
            legend_list=legend_list,
        )

        plot_2D(
            [M_I_val],
            [Is_PWM[:, ii] for ii in range(Is_PWM.shape[1])],
            title="Current PWM harmonics function of modulation index ("
            + param_dict["strategy"]
            + ")",
            xlabel="Modulation index []",
            ylabel="Amplitude [A]",
            legend_list=legend_list,
        )

    pass


if __name__ == "__main__":
    for param_dict in param_list:
        test_EEC_PWM(param_dict)

    # test_EEC_PWM(param_list[1])
