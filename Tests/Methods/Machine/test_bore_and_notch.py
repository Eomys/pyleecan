from os.path import join

import matplotlib.pyplot as plt
import pytest
from numpy import pi
from pyleecan.Classes.NotchEvenDist import NotchEvenDist
from pyleecan.Classes.BoreSinePole import BoreSinePole
from pyleecan.Classes.BoreFlower import BoreFlower
from pyleecan.Classes.SlotCirc import SlotCirc
from pyleecan.Classes.SlotW26 import SlotW26
from pyleecan.definitions import DATA_DIR
from pyleecan.Functions.load import load

mm = 1e-3

@pytest.mark.IPMSM
@pytest.mark.SCIM
def test_bore_and_notch(is_show_fig=False):
    """Validation of rotor and stator notches"""

    # Load machines
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    Audi_eTron = load(join(DATA_DIR, "Machine", "AUDI_eTron.json"))

    # Add notches to Toyota_Prius
    p = Toyota_Prius.get_pole_pair_number()

    NBs = SlotCirc(Zs=24, W0=4 * mm, H0=1 * mm)
    NBq = SlotCirc(Zs=2 * p, W0=4 * mm, H0=1 * mm)
    NBdq = SlotCirc(Zs=2 * p, W0=6 * mm, H0=1 * mm)
    NCirc1 = SlotCirc(Zs=2 * p, W0=8 * mm, H0=2 * mm)
    NSlowW26 = SlotW26(Zs=2 * p, W0=1*mm, H0=2*mm, H1=0, R1=3*mm, R2=3*mm)
    NSlowW26w = SlotW26(Zs=2 * p, W0=9*mm, H0=2*mm, H1=0, R1=5*mm, R2=5*mm) # wide slot
    a0 = 0.25

    Toyota_Prius.rotor.notch = [
        # NotchEvenDist(alpha=0, notch_shape=NBq),
        # NotchEvenDist(alpha=0.5 * pi / p + a0, notch_shape=NBdq),
        # NotchEvenDist(alpha=0.5 * pi / p - a0, notch_shape=NBdq),
        # NotchEvenDist(alpha=0.5 * pi / p, notch_shape=NCirc1),
        NotchEvenDist(alpha=0.5 * pi / p, notch_shape=NSlowW26w),
    ]
    delta_d =  Toyota_Prius.stator.Rint - Toyota_Prius.rotor.Rext
    Toyota_Prius.rotor.bore = BoreSinePole(N=8, delta_d=delta_d, delta_q=5*mm, W0=50*mm)

    # Toyota_Prius.plot(sym=8, is_show_fig=is_show_fig)
    Toyota_Prius.plot(is_show_fig=is_show_fig)

    # Add notches to Audi_eTron
    NBs = SlotCirc(Zs=16, W0=0.001, H0=0.0005)
    NBr = SlotCirc(Zs=29, W0=0.001, H0=0.0005)

    Audi_eTron.stator.notch = [NotchEvenDist(alpha=0, notch_shape=NBs)]
    Audi_eTron.rotor.notch = [NotchEvenDist(alpha=0, notch_shape=NBr)]

    # Audi_eTron.plot(sym=2, is_show_fig=is_show_fig)
    # Audi_eTron.plot(is_show_fig=is_show_fig)

    return Toyota_Prius, Audi_eTron


if __name__ == "__main__":
    Toyota_Prius, Audi_eTron = test_bore_and_notch(is_show_fig=True)
    plt.show()
    print("Done")
