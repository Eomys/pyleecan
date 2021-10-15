from os.path import join

import pytest
from Tests import save_validation_path as save_path
from pyleecan.Classes.OPdq import OPdq

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output
from pyleecan.Classes.Loss import Loss
from pyleecan.Classes.LossModel import LossModel
from pyleecan.Classes.LossModelBertotti import LossModelBertotti
from pyleecan.Classes.LossModelWinding import LossModelWinding
from pyleecan.Classes.ImportMatrixXls import ImportMatrixXls

from numpy import linspace, pi
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.long_10m
@pytest.mark.FEMM
@pytest.mark.MagFEMM
@pytest.mark.periodicity
@pytest.mark.SPMSM
@pytest.mark.SingleOP
@pytest.mark.Loss
def test_FEMM_Loss():
    """Validation of the Loss implementation using MagFEMM and compare to
    FEMM example - https://www.femm.info/wiki/SPMLoss -
    """
    # TODO stacking factor is disregarded for now but should be included

    # Reference values:
    rotor_speed = 4000  # RPM
    mechanical_power = 62.2952  # W
    rotor_core_loss = 0.0574995  # W
    stator_core_loss = 3.40587  # W
    prox_loss = 0.0585815  # W
    i_sqr_R_loss = 4.37018  # W
    magnet_loss = 1.38116  # W
    total_electromagnetic_losses = 9.27329  # W

    Id_ref = 0
    Iq_ref = 2 ** (1 / 2)

    n_step = 180
    Nrev = 1 / 2

    # readability
    machine = load(join(DATA_DIR, "Machine", "SPMSM_020.json"))
    machine.stator.winding.is_reverse_wind = True
    qs = machine.stator.winding.qs
    simu = Simu1(name="test_FEMM_Loss", machine=machine)

    # Definition of the enforced output of the electrical module
    simu.input = InputCurrent(
        OP=OPdq(N0=rotor_speed, Id_ref=Id_ref, Iq_ref=Iq_ref),
        Na_tot=2048,
    )

    # time discretization [s]
    # TODO without explicit time def. there is an error
    simu.input.time = ImportMatrixVal()
    simu.input.time.value = linspace(
        start=0, stop=60 / rotor_speed * Nrev, num=n_step, endpoint=False
    )  # n_step timesteps

    # Definition of the magnetic simulation: with periodicity
    simu.mag = MagFEMM(
        type_BH_stator=0, type_BH_rotor=0, is_periodicity_a=True, nb_worker=4
    )

    simu.mag.is_get_meshsolution = True  # To get FEA mesh for latter post-procesing

    # --- Setup the Loss Model ------------------------------------------------------- #
    simu.loss = Loss()

    myIronLoss = LossModelBertotti()
    myWindingLoss = LossModelWinding()

    simu.loss.add_model(model=myIronLoss, part_label="Stator")
    simu.loss.add_model(model=myWindingLoss, part_label="Stator")

    # FEMM ex. Ch = 143 W / m³ / T² / Hz --> k_hy = 2.089 W / kg @ F_REF, B_REF
    #          Ce = 0.53 W / m³ / T² / Hz² --> k_ed = 0.387 W / kg @ F_REF, B_REF

    # stator
    myIronLoss.name = "Stator Iron Losses"
    myIronLoss.k_hy = 2.089  # None
    myIronLoss.alpha_hy = 2
    myIronLoss.k_ed = 0.387  # None
    myIronLoss.alpha_ed = 2
    myIronLoss.k_ex = 0
    myIronLoss.alpha_ex = 1.5
    myIronLoss.group = "core"  # this is the FEMM group name
    myIronLoss.get_meshsolution = True  # to store loss density
    myIronLoss.N0 = [4000, 6000]  # list of speed to override actual speed

    # rotor
    myRotorIronLoss = myIronLoss.copy()
    myRotorIronLoss.name = "Rotor Iron Losses"
    myRotorIronLoss.group = "core"

    simu.loss.add_model(model=myRotorIronLoss, part_label="Rotor")

    # TODO load loss data with BH curve by default
    # TODO add M19 loss data to compare parameter estimates
    # LossData = ImportMatrixXls()
    # LossData.file_path = join(DATA_DIR, "Material", "M400-50A.xlsx")
    # LossData.is_transpose = False
    # LossData.sheet = "LossData"
    # LossData.skiprows = 2
    # LossData.usecols = None

    # machine.stator.mat_type.mag.LossData = LossData

    # --- Run the Loss Simulation ---------------------------------------------------- #
    out = Output(simu=simu)
    simu.run()

    loss = out.loss
    mshsol = loss.get_loss_dist(part_label="Stator", index=0)

    # mshsol.plot_contour(label="LossDens", itime=7)
    # mshsol.plot_contour(label="LossDensSum", itime=0)

    P_mech = 2 * pi * rotor_speed / 60 * out.mag.Tem_av

    loss_stator_iron = loss.get_loss(part_label="Stator", index=0)
    loss_rotor_iron = loss.get_loss(part_label="Rotor", index=0)
    loss_stator_wind = loss.get_loss(part_label="Stator", index=1)

    loss_st_iron = loss_stator_iron.get_along("Speed=4000", "time")["Loss"].mean()
    loss_ro_iron = loss_rotor_iron.get_along("Speed=4000", "time")["Loss"].mean()
    loss_st_wdg = loss_stator_wind.get_along("time", "phase=sum")["Loss"].mean()

    print(f"mechanical power = {P_mech} W")
    print(f"stator iron loss = {loss_st_iron} W")
    print(f"rotor iron loss = {loss_ro_iron} W")
    print(f"stator winding loss = {loss_st_wdg} W")

    delta = 5 / 100  # arbitary allowed relative difference

    assert mshsol is not None
    assert (abs(loss_st_iron - stator_core_loss) / stator_core_loss) <= delta
    # rotor loss is disregarded since absolute value seems to be too small
    # assert abs(loss_rotor_iron - rotor_core_loss)/rotor_core_loss <= delta
    assert loss_stator_wind is not None
    assert (abs(mechanical_power - P_mech) / mechanical_power) <= delta

    return out


# To run it without pytest
if __name__ == "__main__":
    out = test_FEMM_Loss()
