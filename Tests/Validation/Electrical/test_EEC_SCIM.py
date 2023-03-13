from os.path import join

import numpy as np
from numpy.testing import assert_almost_equal

from multiprocessing import cpu_count

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.EEC_SCIM import EEC_SCIM


from SciDataTool.Functions.Plot.plot_2D import plot_2D

from numpy import angle, cos
import pytest

is_show_fig = False


@pytest.mark.skip
def test_EEC_SCIM():
    """Calculate magnetizing flux"""

    # Prepare simulation
    machine = load(join(DATA_DIR, "Machine", "Audi_eTron.json"))

    Rs = machine.stator.comp_resistance_wind()
    Rr = machine.rotor.comp_resistance_wind()

    mag_model = MagFEMM(
        is_periodicity_t=True,
        is_periodicity_a=True,
        is_sliding_band=True,  # self.is_sliding_band,
        Kgeo_fineness=1,  # self.Kgeo_fineness
        Kmesh_fineness=0.5,  # self.Kmesh_fineness
        nb_worker=int(0.5 * cpu_count()),
    )

    Im_array = np.linspace(0.1, 300, 10)
    Phi_m_list = list()
    Phi_wind_list = list()
    for Im in Im_array:
        OP_I = OPdq(N0=1000, Id_ref=Im, Iq_ref=0)
        eec = EEC_SCIM(fluxlink=mag_model)
        Phi_m, Phi_wind = eec.comp_fluxlinkage(machine=machine, OP=OP_I)
        Phi_m_list.append(Phi_m)
        Phi_wind_list.append(Phi_wind)

    BH = machine.stator.mat_type.mag.BH_curve.get_data()
    mu_r = BH[:, 1] / (4 * np.pi * 1e-7 * BH[:, 0])

    Lm_table = np.array(
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

    Im_table = np.array(
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
    assert_almost_equal(Rs, 0.0055, 0)
    assert_almost_equal(Rr, 9.1e-5, 0)
    assert_almost_equal(np.array(Phi_m_list)[:, 0] / Im_array, Lm_table[1:], 0)

    if is_show_fig:
        plot_2D(
            [BH[:, 1]],
            [mu_r],
            xlabel="Magnetic flux density [T]",
            ylabel="Magnetic relative permeability []",
        )

        plot_2D(
            [Im_array],
            [np.array(Phi_m_list)[:, 0] / Im_array],
            xlabel="Magnetizing current [A]",
            ylabel="Magnetizing inductance [H]",
            legend_list=["LUT", "FEA"],
        )

    return Phi_m_list, Phi_wind_list


if __name__ == "__main__":
    Phi_m_list, Phi_wind_list = test_EEC_SCIM()
