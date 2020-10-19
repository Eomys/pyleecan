from os.path import join

import pytest
from Tests import save_validation_path as save_path

from numpy import exp, sqrt, pi

from pyleecan.Classes.Simu1 import Simu1

from pyleecan.Classes.InputCurrent import InputCurrent

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.Output import Output

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
def test_FEMM_periodicity():
    """Validation of the implementaiton of periodic angle axis in Magnetic (MagFEMM) and Force (ForceMT) modules"""
    
    IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))
    
    simu = Simu1(name="test_FEMM_periodicity", machine=IPMSM_A)
    
    # Definition of the enforced output of the electrical module
    I0_rms = 250/sqrt(2)
    Phi0 = 140*pi/180  # Maximum Torque Per Amp
    
    Id_ref = (I0_rms*exp(1j*Phi0)).real
    Iq_ref = (I0_rms*exp(1j*Phi0)).imag
    
    simu.input = InputCurrent(
        Id_ref=Id_ref,
        Iq_ref=Iq_ref,
        Na_tot=252 * 8,
        Nt_tot=10*8,
        N0=1000,
    )

    # Definition of the magnetic simulation: with periodicity
    simu.mag = MagFEMM(is_periodicity_a=True, is_periodicity_t=True)
    simu.force = ForceMT(is_periodicity_a=True, is_periodicity_t=True)
    
   # Definition of the magnetic simulation: no periodicity
    simu2 = simu.copy()
    simu2.mag = MagFEMM(is_periodicity_a=False, is_periodicity_t=False)
    simu2.force = ForceMT(is_periodicity_a=False, is_periodicity_t=False)

    # Run simulations
    out = Output(simu=simu)
    simu.run()
    
    out2 = None
    # out2 = Output(simu=simu2)
    # simu2.run()
        
    # # # Plot the result  
    # out.plot_A_time(
    #     "mag.B",
    #     is_fft=False,
    #     data_list=[out2.mag.B],
    #     legend_list=["Periodic", "Full"],
    #     save_path=join(save_path, "test_FEMM_periodicity_B_time.png"),
    #     linestyle_list=["-", "dotted"],
    # )
    
    # out.plot_A_space(
    #     "mag.B",
    #     t_index=0,
    #     is_fft=True,
    #     data_list=[out2.mag.B],
    #     legend_list=["Periodic", "Full"],
    #     save_path=join(save_path, "test_FEMM_periodicity_B_space.png"),
    #     linestyle_list=["-", "dotted"],
    # )
    
    # out.plot_A_space(
    #     "force.P",
    #     t_index=0,
    #     is_fft=True,
    #     data_list=[out2.force.P],
    #     legend_list=["Periodic", "Full"],
    #     save_path=join(save_path, "test_FEMM_periodicity_P_space.png"),
    #     linestyle_list=["-", "dotted"],
    # )
    
    # out.plot_A_time(
    #     "force.P",
    #     is_fft=False,
    #     data_list=[out2.force.P],
    #     legend_list=["Periodic", "Full"],
    #     save_path=join(save_path, "test_FEMM_periodicity_P_time.png"),
    #     linestyle_list=["-", "dotted"],
    # )    
    
    # out.plot_A_time(
    #     "mag.Tem",
    #     is_fft=False,
    #     data_list=[out2.mag.Tem],
    #     legend_list=["Periodic", "Full"],
    #     save_path=join(save_path, "test_FEMM_periodicity_Tem_time.png"),
    #     linestyle_list=["-", "dotted"],
    #     )  

    # out.plot_A_time(
    #     "mag.Phi_wind_stator",
    #     is_fft=False,
    #     index_list=[0],
    #     data_list=[out2.mag.Phi_wind_stator],
    #     legend_list=["Periodic", "Full"],
    #     save_path=join(save_path, "test_FEMM_periodicity_Phi_wind_stator_time.png"),
    #     linestyle_list=["-", "dotted"],
    #     )
    
    return out, out2

# To run it without pytest
if __name__ == "__main__":
    out, out2 = test_FEMM_periodicity()
    
    out.plot_A_time(
        "mag.Tem",
        is_fft=True,
        # data_list=[out2.mag.Tem],
        # legend_list=["Periodic", "Full"],
        # save_path=join(save_path, "test_FEMM_periodicity_Tem_time.png"),
        # linestyle_list=["-", "dotted"],
        )  