from os.path import join

import pytest

import numpy as np
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.LossFEMM import LossFEMM
from pyleecan.Classes.Loss import Loss
from pyleecan.Classes.LossModelSteinmetz import LossModelSteinmetz
from pyleecan.Classes.LossModelJordan import LossModelJordan
from pyleecan.Classes.LossModelBertotti import LossModelBertotti
from pyleecan.Classes.LossModelWinding import LossModelWinding
from pyleecan.Classes.LossModelProximity import LossModelProximity
from pyleecan.Classes.LossModelMagnet import LossModelMagnet
from pyleecan.Classes.LossModelWindage import LossModelWindage
from pyleecan.Classes.OutLossModel import OutLossModel
from pyleecan.Functions.Electrical.comp_loss_joule import comp_loss_joule


from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR

from SciDataTool.Functions.Plot.plot_2D import plot_2D 


is_show_fig = True


@pytest.mark.long_5s
@pytest.mark.FEMM
@pytest.mark.MagFEMM
@pytest.mark.periodicity
@pytest.mark.SPMSM
@pytest.mark.SingleOP
@pytest.mark.Loss
@pytest.mark.skip(reason="Work in progress")
def test_FEMM_Loss_Prius():
    """Test to calculate losses in Toyota_Prius using LossFEMM model based on motoranalysis validation"""

    machine = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    simu = Simu1(name="Id=0,Iq=0", machine=machine)

    # Current for MTPA
    SPEED = 1200

    simu.input = InputCurrent(
        Nt_tot=4 * 10 * 8,
        Na_tot=200 * 8,
        OP=OPdq(N0=SPEED, Id_ref=0, Iq_ref=0),
        
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

    simu.loss = Loss(
        is_get_meshsolution=True,
        Tsta=100,
        model_dict={"stator core": LossModelSteinmetz(group = "stator core"),
                    "rotor core": LossModelSteinmetz(group = "rotor core"),
                    "joule": LossModelWinding(group = "stator winding"),
                    "proximity": LossModelProximity(group = "stator winding"),
                    "magnets": LossModelMagnet(group = "rotor magnets"),
                    "mechanical": LossModelWindage(group = "rotor core")}
    )

    simu_list=[simu]
    simu_dict = {"Id=-200,Iq=0":(-200,0),
                 "Id=0,Iq=200":(0,200),
                 "Id=-125,Iq=125":(-125,125)}
    
    for key,value in simu_dict.items():
        temp_simu=simu.copy()
        temp_simu.name=key
        temp_simu.input.OP=OPdq(N0=SPEED, Id_ref=value[0], Iq_ref=value[1])
        simu_list.append(temp_simu)
    
    out_list=[]
    for sim in simu_list:
        output = sim.run()
        out_list.append(output)
        # out.plot_B_mesh()
        power_dict = {
            "total_power": output.mag.Pem_av,
            "torque": output.mag.Tem_av,
            "current_density": output.elec.get_Jrms()/1e6,
            **dict([(o.name,o.get_loss_scalar(output.elec.OP.felec)) for o in output.loss.loss_list]),
            "efficiency": (output.mag.Pem_av-output.loss.loss_list[-1].get_loss_scalar(output.elec.OP.felec))/output.mag.Pem_av
        }
        print(power_dict)

    group_names="stator core"
    for i, out in enumerate(out_list[:]):
        for j, other in enumerate(out_list[:]):
            if i != j:
                out.loss.loss_list[0].get_mesh_solution().plot_contour(
                "freqs=sum",
                label=f"{out.loss.loss_list[0].name} Loss",
                group_names = group_names)
                other.loss.loss_list[0].get_mesh_solution().plot_contour(
                "freqs=sum",
                label=f"{other.loss.loss_list[0].name} Loss",
                group_names = group_names)
                out.loss.loss_list.append(out.loss.loss_list[0]-other.loss.loss_list[0])
                out.loss.loss_list[-1].name = simu_list[i].name +" - "+simu_list[j].name
                out.loss.loss_list[-1].get_mesh_solution().plot_contour(
                "freqs=sum",
                label=f"{out.loss.loss_list[-1].name} Loss",
                group_names = group_names)
                
            
    # for out in out_list:
    #     for loss in out.loss.loss_list[-3:]:
    #         loss.get_mesh_solution().plot_contour()
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
            "rotor magnets"
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

    return out


# To run it without pytest
if __name__ == "__main__":

    test_FEMM_Loss_Prius()