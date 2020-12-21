from os.path import join

import pytest
from Tests import save_validation_path as save_path

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

from numpy import linspace
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
# @pytest.mark.DEV
def test_FEMM_Loss():
    """Validation of the Loss implementaiton using FEMM.
    Only test for simulation running without errors for now."""

    machine = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))
    pp = machine.rotor.get_pole_pair_number()
    simu = Simu1(name="FEMM_IronLoss", machine=machine)

    rotor_speed = 2000

    # Definition of the enforced output of the electrical module
    simu.input = InputCurrent(Id_ref=0, Iq_ref=0, Na_tot=2048, N0=rotor_speed)

    # time discretization [s]
    n_step = 16

    simu.input.time = ImportMatrixVal()
    simu.input.time.value = linspace(
        start=0, stop=60 / rotor_speed / pp, num=n_step, endpoint=False
    )  # n_step timesteps

    # Definition of the magnetic simulation: with periodicity
    simu.mag = MagFEMM(
        type_BH_stator=0, type_BH_rotor=0, is_periodicity_a=True, nb_worker=4
    )

    simu.mag.is_get_mesh = True  # To get FEA mesh for latter post-procesing

    # --- Setup the Loss Model ----------------------------------------------------------- #
    simu.loss = Loss()

    myIronLoss = LossModelBertotti()
    myWindingLoss = LossModelWinding()

    simu.loss.iron["Stator"] = [myIronLoss]
    simu.loss.winding["Stator"] = [myWindingLoss]

    myIronLoss.name = "Stator Iron Losses"
    myIronLoss.k_hy = None
    myIronLoss.alpha_hy = 2
    myIronLoss.k_ed = None
    myIronLoss.alpha_ed = 2
    myIronLoss.k_ex = 0
    myIronLoss.alpha_ex = 1.5
    myIronLoss.group = "stator core"  # this is the FEMM group name

    # TODO load loss data with BH curve by default
    LossData = ImportMatrixXls()
    # LossData.file_path = "pyleecan\\pyleecan\\Data\\Material\\M400-50A.xlsx"
    LossData.file_path = join(DATA_DIR, "Material", "M400-50A.xlsx")
    LossData.is_transpose = False
    LossData.sheet = "LossData"
    LossData.skiprows = 2
    LossData.usecols = None

    machine.stator.mat_type.mag.LossData = LossData

    # --- Run the Loss Simulation -------------------------------------------------------- #
    out = Output(simu=simu)
    simu.run()

    loss = out.loss
    mshsol = loss.get_loss_dist(loss_type="Iron", label="Stator", index=0)
    assert mshsol is not None

    # mshsol.plot_contour(label="LossDens", itime=7)
    # mshsol.plot_contour(label="LossDensSum", itime=0)

    loss_stator_iron = loss.get_loss(loss_type="Iron", label="Stator", index=0)
    loss_stator_wind = loss.get_loss(loss_type="Winding", label="Stator", index=0)

    print(f"stator iron loss = {loss_stator_iron.get_field([]).mean()} W")
    print(f"stator winding loss = {loss_stator_wind.get_field([]).mean()} W")

    assert mshsol is not None
    assert loss_stator_iron is not None
    assert loss_stator_wind is not None

    return out


# To run it without pytest
if __name__ == "__main__":

    out = test_FEMM_Loss()
