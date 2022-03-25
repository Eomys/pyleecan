from os.path import join

import numpy as np
from numpy.testing import assert_almost_equal


from pyleecan.Classes.Electrical import Electrical
from pyleecan.Classes.EEC_SCIM import EEC_SCIM
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.LUTslip import LUTslip
from pyleecan.Classes.InputVoltage import InputVoltage
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.OPslip import OPslip

from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR

from SciDataTool.Functions.Plot.plot_2D import plot_2D


is_show_fig = False


def test_EEC_ELUT_Audi_eTron():
    """Test to calculate """

    machine = load(join(DATA_DIR, "Machine", "Audi_eTron_loss.json"))
    machine.stator.winding.Lewout = 0.05

    Rs = machine.stator.comp_resistance_wind()
    Rr = machine.rotor.comp_resistance_wind()

    simu = Simu1(name="test_EEC_ELUT_Audi_eTron", machine=machine)

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

    simu.input = InputVoltage(
        OP=OPslip(U0_ref=144, N0=4832, slip_ref=0.047),
        Na_tot=1000,
        Nt_tot=1000,
    )

    ELUT_Audi_eTron = LUTslip()
    ELUT_Audi_eTron.simu = Simu1(machine=machine)
    R1_135 = 1 / (3 * 333 ** 2 / 6304)
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

    # Run simulation
    out = simu.run()

    eec = out.elec.eec
    I1_abs = abs(eec.I1)
    qs = machine.stator.winding.qs
    P_joule_s = qs * eec.R1 * abs(eec.I1) ** 2
    P_joule_r = qs * eec.R2 * abs(eec.I2) ** 2

    assert_almost_equal(out.elec.Tem_av, 247, decimal=1)
    assert_almost_equal(I1_abs, 333, decimal=1)
    assert_almost_equal(P_joule_s, 6304, decimal=0)
    assert_almost_equal(P_joule_r, 6160, decimal=0)


def test_EEC_ELUT_Audi_eTron2():
    """Test to calculate """

    machine = load(join(DATA_DIR, "Machine", "Audi_eTron_loss.json"))
    machine.stator.winding.Lewout = 0.05

    Rs = machine.stator.comp_resistance_wind()
    Rr = machine.rotor.comp_resistance_wind()

    simu = Simu1(name="test_EEC_ELUT_Audi_eTron", machine=machine)

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

    simu.input = InputVoltage(
        OP=OPslip(U0_ref=200, N0=9664, slip_ref=0.018),
        Na_tot=1000 * 2,
        Nt_tot=4 * 10,
        is_periodicity_a=True,
        is_periodicity_t=False,
    )

    ELUT_Audi_eTron = LUTslip()
    ELUT_Audi_eTron.simu = Simu1(machine=machine)
    R1_135 = 1 / (3 * 333 ** 2 / 6304)
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

    simu.mag = MagFEMM(is_periodicity_a=True, is_periodicity_t=False, nb_worker=1)

    # Run simulation
    out = simu.run()

    eec = out.elec.eec
    I1_abs = abs(eec.I1)
    qs = machine.stator.winding.qs
    P_joule_s = qs * eec.R1 * abs(eec.I1) ** 2
    P_joule_r = qs * eec.R2 * abs(eec.I2) ** 2

    assert_almost_equal(out.elec.Tem_av, 107, decimal=1)
    assert_almost_equal(I1_abs, 333, decimal=1)
    assert_almost_equal(P_joule_s, 6304, decimal=0)
    assert_almost_equal(P_joule_r, 6160, decimal=0)


# To run it without pytest
if __name__ == "__main__":

    # out = test_EEC_ELUT_Audi_eTron()

    out = test_EEC_ELUT_Audi_eTron2()
