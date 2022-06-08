from os.path import join

import matplotlib.pyplot as plt
import pytest
from numpy import pi
from pyleecan.Classes.NotchEvenDist import NotchEvenDist
from pyleecan.Classes.SlotCirc import SlotCirc
from pyleecan.definitions import DATA_DIR
from pyleecan.Functions.load import load


@pytest.mark.IPMSM
@pytest.mark.SCIM
def test_notch(is_show_fig=False):
    """Validation of rotor and stator notches"""

    # Load machines
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    Audi_eTron = load(join(DATA_DIR, "Machine", "Audi_eTron.json"))

    # Add notches to Toyota_Prius
    p = Toyota_Prius.get_pole_pair_number()

    NBs = SlotCirc(Zs=24, W0=0.004, H0=0.001)
    NBq = SlotCirc(Zs=2 * p, W0=0.004, H0=0.001)
    NBdq = SlotCirc(Zs=2 * p, W0=0.006, H0=0.001)
    NBd = SlotCirc(Zs=2 * p, W0=0.008, H0=0.001)
    a0 = 0.25
    Toyota_Prius.stator.notch = [NotchEvenDist(alpha=0, notch_shape=NBs)]
    Toyota_Prius.rotor.notch = [
        NotchEvenDist(alpha=0, notch_shape=NBq),
        NotchEvenDist(alpha=0.5 * pi / p + a0, notch_shape=NBdq),
        NotchEvenDist(alpha=0.5 * pi / p - a0, notch_shape=NBdq),
        NotchEvenDist(alpha=0.5 * pi / p, notch_shape=NBd),
    ]

    Toyota_Prius.plot(sym=8, is_show_fig=is_show_fig)
    Toyota_Prius.plot(is_show_fig=is_show_fig)

    # Add notches to Audi_eTron
    NBs = SlotCirc(Zs=16, W0=0.001, H0=0.0005)
    NBr = SlotCirc(Zs=29, W0=0.001, H0=0.0005)

    Audi_eTron.stator.notch = [NotchEvenDist(alpha=0, notch_shape=NBs)]
    Audi_eTron.rotor.notch = [NotchEvenDist(alpha=0, notch_shape=NBr)]

    Audi_eTron.plot(sym=2, is_show_fig=is_show_fig)
    Audi_eTron.plot(is_show_fig=is_show_fig)

    return Toyota_Prius, Audi_eTron


if __name__ == "__main__":
    Toyota_Prius, Audi_eTron = test_notch(is_show_fig=True)
    plt.show()
    print("Done")
