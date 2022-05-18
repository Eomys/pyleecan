from os.path import join

import pytest

import numpy as np
from numpy.testing import assert_almost_equal

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.OPslip import OPslip
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.LossFEMM import LossFEMM
from pyleecan.Classes.LossModelSteinmetz import LossModelSteinmetz
from pyleecan.Classes.LossModelBertotti import LossModelBertotti
from pyleecan.Classes.LossModelWinding import LossModelWinding
from pyleecan.Classes.LossModelProximity import LossModelProximity
from pyleecan.Classes.LossModelMagnet import LossModelMagnet
from pyleecan.Classes.OutLoss import OutLoss
from pyleecan.Functions.Electrical.comp_loss_joule import comp_loss_joule


from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR

from SciDataTool.Functions.Plot.plot_2D import plot_2D 
from pyleecan.Functions.Plot import dict_2D


is_show_fig = True

@pytest.mark.long_5s
@pytest.mark.FEMM
@pytest.mark.MagFEMM
@pytest.mark.periodicity
@pytest.mark.SPMSM
@pytest.mark.SingleOP
@pytest.mark.Loss
@pytest.mark.skip(reason="Work in progress")
def test_loss_SCIM():
    """Test to calculate losses in Toyota_Prius using LossFEMM model based on motoranalysis validation"""

    machine = load(join(DATA_DIR, "Machine", "SCIM_L2EP_48s_2p.json"))

    simu = Simu1(name="test_FEMM_Loss_Prius", machine=machine)


    simu.input = InputCurrent(
        Nt_tot=4 * 40 ,
        Na_tot=200 * 8,
        OP=OPslip(felec = 50, slip_ref = 0.03, I0_ref=230, IPhi0_ref=140*np.pi/180),
        is_periodicity_t=True,
        is_periodicity_a=True,
    )

    simu.mag = MagFEMM(
        is_periodicity_a=True,
        is_periodicity_t=True,
        nb_worker=4,
        is_get_meshsolution=True,
        is_fast_draw=True,
        is_calc_torque_energy=False,
    )

    simu.loss = LossFEMM(
        is_get_meshsolution=True,
        Tsta=100,
        model_dict={"stator core Steinmetz": LossModelSteinmetz(group = "stator core"),
                    "rotor core Steinmetz": LossModelSteinmetz(group = "rotor core"),
                    "joule": LossModelWinding(group = "stator winding",
                                              type_skin_effect = 0),
                    "proximity": LossModelProximity(group = "stator winding")}
    )

    out = simu.run()

    power_dict = {
        "total_power": out.mag.Pem_av,
        **dict([(o.name,o.get_loss_scalar(out.elec.OP.felec)) for o in out.loss.loss_list])
    }
    print(power_dict)

    speed_array = np.linspace(10, 8000, 100)
    p = machine.get_pole_pair_number()

    array_list = [np.array([o.get_loss_scalar(speed / 60 *p) for speed in speed_array])
                  for o in out.loss.loss_list if o.name != 'overall']
    array_list.append(sum(array_list))
    
    # def calc_loss(coeff, B):
    #     f=80
    #     if len(coeff)==4:
    #         return coeff[0] * 80 ** coeff[2] *B**coeff[3]+coeff[1]*(f*B)**2
    #     else:
    #         return coeff[0]*80*B**coeff[1]+coeff[2]*(80*B)**coeff[3]+coeff[4]*(80*B)**coeff[5]
    
    # B_list=np.linspace(0,3.5,100)
    # loss=simu.loss.model_dict["stator core Steinmetz"]
    # coeffs = loss.k_hy, loss.k_ed, loss.alpha_f, loss.alpha_B
    # plot_loss_S=np.array([calc_loss(coeffs, B) for B in B_list])
    # loss=simu.loss.model_dict["stator core Bertotti"]
    # coeffs = loss.k_hy, loss.alpha_hy, loss.k_ed, loss.alpha_ed, loss.k_ex, loss.alpha_ex
    # plot_loss_B=np.array([calc_loss(coeffs, B) for B in B_list])
    # import matplotlib.pyplot as plt 
    
    # plt.plot(B_list, plot_loss_S, color='red')
    # plt.plot(B_list, plot_loss_B, color='blue')
    # plt.show()

    if is_show_fig:
        group_names = [
            "stator core",
            "rotor core",
        ]
        for loss in out.loss.loss_list:
            if "joule" in loss.name or "proximity" in loss.name :
                group_names.append("stator winding")
                loss.get_mesh_solution().plot_contour(
                    "freqs=sum",
                    label=f"{loss.name} Loss",
                    group_names = group_names
                )
                group_names.pop()
            else:
                
                loss.get_mesh_solution().plot_contour(
                    "freqs=sum",
                    label=f"{loss.name} Loss",
                    group_names = group_names
                )

        plot_2D(
            [speed_array],
            array_list,
            xlabel="Speed [rpm]",
            ylabel="Losses [W]",
            legend_list=[o.name for o in out.loss.loss_list] + ["overall loss"],
        )
        
         # Plot the flux
        out.mag.B.plot_2D_Data("angle", **dict_2D)
        # Plot the torque
        out.mag.Tem.plot_2D_Data("time", **dict_2D)
        # Plot the current
        out.elec.get_Is().plot_2D_Data("time", "phase[]", **dict_2D)

    # out.loss.meshsol_list[0].plot_contour(
    #     "freqs=sum",
    #     label="Loss",
    #     group_names=["stator core", "stator winding"],
    #     # clim=[2e4, 2e7],
    # )

    # out.loss.meshsol_list[0].plot_contour(
    #     "freqs=sum",
    #     label="Loss",
    #     group_names=["rotor core", "rotor magnets"],
    #     # clim=[2e4, 2e7],
    # )
    # txt = f"total_power: {out.mag.Pem_av}\n"
    # txt += F"speed = {SPEED} rpm\n"
    # txt += "\n".join([f"{o.name}: {o.get_loss_scalar(out.elec.OP.felec)}" for o in out.loss.loss_list])
    # txt += F"speed = {SPEED/3} rpm\n"
    # txt += "\n".join([f"{o.name}: {o.get_loss_scalar(SPEED /3/60 * p)}" for o in out.loss.loss_list])

    # with open(F"{SPEED} rpm.txt", "w") as f:
    #     f.write(txt)


    return out


# To run it without pytest
if __name__ == "__main__":

    out = test_loss_SCIM() 
