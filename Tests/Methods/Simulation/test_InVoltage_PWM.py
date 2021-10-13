from os.path import join

from pyleecan.Classes.ImportGenPWM import ImportGenPWM
from pyleecan.Classes.InputVoltage import InputVoltage
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.definitions import DATA_DIR
from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D
from Tests import save_plot_path as save_path

is_show_fig = True


def test_InVoltage_PWM():

    fmax = 20000
    fswi = 7000
    Vdc1 = 2  # Bus voltage
    U0 = 0.5  # Phase voltage

    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    simu = Simu1(name="test_InVoltage_PWM", machine=Toyota_Prius)

    simu.input = InputVoltage(
        N0=2000,
        Na_tot=1024,
        Nt_tot=1024,
        PWM=ImportGenPWM(fmax=fmax, fswi=fswi, Vdc1=Vdc1, U0=U0),
    )

    out = simu.run()

    if is_show_fig:
        out.elec.Us_harm.plot_2D_Data(
            "freqs",
            is_auto_ticks=False,
            save_path=join(save_path, "test_InVoltage_PWM.png"),
            **dict_2D
        )

    return out


# To run it without pytest
if __name__ == "__main__":
    out = test_InVoltage_PWM()
