from os.path import join

import pytest

import numpy as np
from numpy.testing import assert_almost_equal
from numpy.testing import assert_allclose

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
from pyleecan.Classes.OutLossModel import OutLossModel
from pyleecan.Classes.Skew import Skew
from pyleecan.Functions.Electrical.comp_loss_joule import comp_loss_joule
from pyleecan.Functions.Plot import dict_2D


from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR

from SciDataTool.Functions.Plot.plot_2D import plot_2D 


is_show_fig = True

def find_best_phi0_jaguar():
    from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent
    from numpy import zeros, ones, linspace, array, sqrt, arange
    from numpy import linspace, array, pi

    Tem_av_ref = array([79, 125, 160, 192, 237, 281, 319, 343, 353, 332, 266, 164, 22]) # Yang et al, 2013
    Phi0_ref = linspace(60 * pi / 180, 180 * pi / 180, Tem_av_ref.size)
    N_speed = Tem_av_ref.size
    varload = VarLoadCurrent()
    varload.type_OP_matrix = 0 # Matrix N0, I0, Phi0

    # Creating the Operating point matrix
    OP_matrix = zeros((N_speed,4))

    # Set N0 = 2000 [rpm] for all simulation
    OP_matrix[:,0] = 2000 * ones((N_speed))

    # Set I0 = 250 / sqrt(2) [A] (RMS) for all simulation
    OP_matrix[:,1] = 250/sqrt(2) * ones((N_speed)) 

    # Set Phi0 from 60° to 180°
    OP_matrix[:,2] = Phi0_ref

    varload.OP_matrix = OP_matrix
    print(OP_matrix)

    # All the simulation use the same machine
    # No need to draw the machine for all OP
    varload.is_reuse_femm_file=True
    
    machine = load(join(DATA_DIR, "Machine", "Jaguar_I_Pace_wo_skew.json"))
    
    simu = Simu1(name="test_FEMM_Loss_Jaguar_I_Pace", machine=machine)
    Ic = 450 * np.exp(1j * 150 * np.pi / 180)
    simu.input = InputCurrent(
        Nt_tot=4 * 40 * 8,
        Na_tot=200 * 8,
        OP=OPdq(N0=1200, Id_ref=Ic.real, Iq_ref=Ic.imag), #,Ud_ref=Uc.real, Uq_ref=Uc.imag),
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
    
    simu_vop = simu.copy()
    simu_vop.var_simu = varload
    simu_vop.var_simu.is_keep_all_output = True
    
    Xout_vop = simu_vop.run()
    
    fig = Xout_vop.plot_multi("Phi0", "Tem_av")

    return Xout_vop
@pytest.mark.long_5s
@pytest.mark.FEMM
@pytest.mark.MagFEMM
@pytest.mark.periodicity
@pytest.mark.SPMSM
@pytest.mark.SingleOP
@pytest.mark.Loss
@pytest.mark.skip(reason="Work in progress")
def test_FEMM_Loss_Jaguar_wo_skew():
    """Test to calculate losses in Toyota_Prius using LossFEMM model based on motoranalysis validation"""

    machine = load(join(DATA_DIR, "Machine", "Jaguar_I_Pace_wo_skew.json"))

    simu = Simu1(name="test_FEMM_Loss_Jaguar_I_Pace", machine=machine)

    # Current for MTPA
    Ic = 450 * np.exp(1j * 120 * np.pi / 180)
    SPEED = 2000

    simu.input = InputCurrent(
        Nt_tot=4 * 40 * 8,
        Na_tot=200 * 8,
        OP=OPdq(N0=SPEED, Id_ref=Ic.real, Iq_ref=Ic.imag), #,Ud_ref=Uc.real, Uq_ref=Uc.imag),
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
                    "magnets": LossModelMagnet(group = "rotor magnets")}
    )

    out = simu.run()
    
    out.loss.loss_list.append(sum(out.loss.loss_list))
    out.loss.loss_list[-1].name = "overall"

    power_dict = {
        "Torque": out.mag.Tem_av,
        "total_power": out.mag.Pem_av,
        **dict([(o.name,o.get_loss_scalar(out.elec.OP.felec)) for o in out.loss.loss_list])
    }
    print(power_dict)

    speed_array = np.linspace(10, 8000, 100)
    p = machine.get_pole_pair_number()

    array_list = [np.array([o.get_loss_scalar(speed / 60 *p) for speed in speed_array])
                  for o in out.loss.loss_list]
    
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
        # group_names = [
        #     "stator core",
        #     "rotor core",
        #     "rotor magnets"
        # ]
        # for loss in out.loss.loss_list:
        #     if "joule" in loss.name or "proximity" in loss.name :
        #         group_names.append("stator winding")
        #         loss.get_mesh_solution().plot_contour(
        #             "freqs=sum",
        #             label=f"{loss.name} Loss",
        #             group_names = group_names
        #         )
        #         group_names.pop()
        #     else:
                
        #         loss.get_mesh_solution().plot_contour(
        #             "freqs=sum",
        #             label=f"{loss.name} Loss",
        #             group_names = group_names
        #         )

        plot_2D(
            [speed_array],
            array_list,
            xlabel="Speed [rpm]",
            ylabel="Losses [W]",
            legend_list=[o.name for o in out.loss.loss_list],
        )

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


@pytest.mark.long_5s
@pytest.mark.FEMM
@pytest.mark.MagFEMM
@pytest.mark.periodicity
@pytest.mark.SPMSM
@pytest.mark.SingleOP
@pytest.mark.Loss
@pytest.mark.skip(reason="Work in progress")
def test_FEMM_Loss_Jaguar():
    """Test to calculate losses in Toyota_Prius using LossFEMM model based on motoranalysis validation"""

    
    def comp_skew_angle(Zs, p, Nstep):
        return 2 * np.pi * (Nstep - 1) / (Nstep * np.lcm(Zs, 2 * p))

    machine = load(join(DATA_DIR, "Machine", "Jaguar_I_Pace.json"))
    Zs = machine.stator.get_Zs()  # Stator slot number
    p = machine.get_pole_pair_number()  # Pole pair number
    ssp = 2 * np.pi / Zs  # Stator slot pitch
    k=7
    rate_kseg = comp_skew_angle(Zs, p, Nstep=k) / ssp
    machine.rotor.skew = Skew(
        type_skew="vshape",
        is_step=True,
        rate=rate_kseg,
        Nstep=k,
    )

    simu = Simu1(name="test_FEMM_Loss_Jaguar_I_Pace", machine=machine)
    
    # Current for MTPA
    Ic = 450 * np.exp(1j * 120 * np.pi / 180)
    # Uc = 350 * np.exp(1j * 140 * np.pi / 180)
    SPEED = 2000

    simu.input = InputCurrent(
        Nt_tot=4 * 40 * 8,
        Na_tot=200 * 8,
        OP=OPdq(N0=SPEED, Id_ref=Ic.real, Iq_ref=Ic.imag), #,Ud_ref=Uc.real, Uq_ref=Uc.imag),
        is_periodicity_t=True,
        is_periodicity_a=True,
    )

    simu.mag = MagFEMM(
        is_periodicity_a=True,
        is_periodicity_t=True,
        nb_worker=4,
        is_get_meshsolution=False,
        is_fast_draw=True,
        is_calc_torque_energy=False,
    )
    simu.mag.Slice_enforced = None
    simu.mag.import_file = None  # Draw machine in FEMM again

    simu.loss = Loss(
        is_get_meshsolution=True,
        Tsta=100,
        model_dict={"stator core": LossModelSteinmetz(group = "stator core"),
                    "rotor core": LossModelSteinmetz(group = "rotor core"),
                    "joule": LossModelWinding(group = "stator winding"),
                    "proximity": LossModelProximity(group = "stator winding"),
                    "magnets": LossModelMagnet(group = "rotor magnets")}
    )

    out = simu.run()
    
    out.loss.loss_list.append(sum(out.loss.loss_list))
    out.loss.loss_list[-1].name = "overall"

    power_dict = {
        "Torque": out.mag.Tem_av,
        "total_power": out.mag.Pem_av,
        **dict([(o.name,o.get_loss_scalar(out.elec.OP.felec)) for o in out.loss.loss_list])
    }
    print(power_dict)

    speed_array = np.linspace(10, 8000, 100)
    p = machine.get_pole_pair_number()

    array_list = [np.array([o.get_loss_scalar(speed / 60 *p) for speed in speed_array])
                  for o in out.loss.loss_list]

    if is_show_fig:
        # group_names = [
        #     "stator core",
        #     "rotor core",
        #     "rotor magnets"
        # ]
        # for loss in out.loss.loss_list:
        #     if "joule" in loss.name or "proximity" in loss.name :
        #         group_names.append("stator winding")
        #         loss.get_mesh_solution().plot_contour(
        #             "freqs=sum",
        #             label=f"{loss.name} Loss",
        #             group_names = group_names
        #         )
        #         group_names.pop()
        #     else:
                
        #         loss.get_mesh_solution().plot_contour(
        #             "freqs=sum",
        #             label=f"{loss.name} Loss",
        #             group_names = group_names
        #         )

        plot_2D(
            [speed_array],
            array_list,
            xlabel="Speed [rpm]",
            ylabel="Losses [W]",
            legend_list=[o.name for o in out.loss.loss_list],
        )

    return out

def test_FEMM_Jaguar_with_skew():

    def comp_skew_angle(Zs, p, Nstep):
        return 2 * np.pi * (Nstep - 1) / (Nstep * np.lcm(Zs, 2 * p))

    machine = load(join(DATA_DIR, "Machine", "Jaguar_I_Pace.json"))
    Zs = machine.stator.get_Zs()  # Stator slot number
    p = machine.get_pole_pair_number()  # Pole pair number
    ssp = 2 * np.pi / Zs  # Stator slot pitch
    k=7
    rate_kseg = comp_skew_angle(Zs, p, Nstep=k) / ssp
    machine.rotor.skew = Skew(
        type_skew="vshape",
        is_step=True,
        rate=rate_kseg,
        Nstep=k,
    )

    simu = Simu1(name="test_Loss_FEMM_Jaguar", machine=machine)

    simu.input = InputCurrent(
        OP=OPdq(N0=1200, Id_ref=0, Iq_ref=0, Tem_av_ref=0),
        Na_tot=400 * 4,
        Nt_tot=40 * 4,
    )

    # Definition of the magnetic simulation (direct calculation with permeance mmf)
    simu.mag = MagFEMM(
        is_periodicity_a=True,
        is_periodicity_t=True,
        nb_worker=4,
        Kmesh_fineness=0.5,
    )
    simu.mag.Slice_enforced = None
    simu.mag.import_file = None  # Draw machine in FEMM again

    out = simu.run()

    return out

# To run it without pytest
if __name__ == "__main__":
    
    # find_best_phi0_jaguar()
    test_FEMM_Loss_Jaguar_wo_skew()
    # test_FEMM_Loss_Jaguar()
    # test_FEMM_Jaguar_with_skew()