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
def test_bore_and_notch_merge_type_0(is_show_fig=False):
    """Validation of bore shape and notches"""

    # Load machines
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    # Add notches to Toyota_Prius
    p = Toyota_Prius.get_pole_pair_number()

    Nq = SlotCirc(Zs=2 * p, W0=5 * mm, H0=2 * mm)
    NCirc1 = SlotCirc(Zs=2 * p, W0=8 * mm, H0=2 * mm)

    a0 = 0.2

    Toyota_Prius.rotor.notch = [
        NotchEvenDist(alpha=0, notch_shape=Nq),  # q-axis notch -> test sym. cut
        NotchEvenDist(alpha=0.5 * pi / p + a0, notch_shape=NCirc1),  # wide notch
        NotchEvenDist(alpha=0.5 * pi / p - a0, notch_shape=NCirc1),  # wide notch
    ]
    delta_d = Toyota_Prius.stator.Rint - Toyota_Prius.rotor.Rext
    Toyota_Prius.rotor.bore = BoreSinePole(
        N=8, delta_d=delta_d, delta_q=3 * mm, W0=50 * mm
    )
    Toyota_Prius.rotor.bore.type_merge_slot = 0

    Toyota_Prius.plot(sym=8, is_show_fig=is_show_fig)
    Toyota_Prius.plot(is_show_fig=is_show_fig)

    return Toyota_Prius


@pytest.mark.IPMSM
@pytest.mark.SCIM
def test_bore_and_notch_merge_type_1(is_show_fig=False):
    """Validation of rotor and stator notches"""

    # Load machines
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    Audi_eTron = load(join(DATA_DIR, "Machine", "AUDI_eTron.json"))

    # Add notches to Toyota_Prius
    p = Toyota_Prius.get_pole_pair_number()

    Nq = SlotW26(Zs=2 * p, W0=1 * mm, H0=4 * mm, H1=0, R1=3 * mm, R2=3 * mm)
    NCirc1 = SlotCirc(Zs=2 * p, W0=8 * mm, H0=2 * mm)
    NCirc2 = SlotCirc(Zs=2 * p, W0=3 * mm, H0=1 * mm)
    NSlotW26 = SlotW26(Zs=2 * p, W0=1 * mm, H0=2 * mm, H1=0, R1=3 * mm, R2=3 * mm)

    a0 = 0.2
    a1 = 0.33

    Toyota_Prius.rotor.notch = [
        NotchEvenDist(alpha=0, notch_shape=Nq),  # q-axis notch -> test sym. cut
        NotchEvenDist(alpha=0.5 * pi / p + a0, notch_shape=NCirc1),  # wide notch
        NotchEvenDist(alpha=0.5 * pi / p - a0, notch_shape=NCirc1),  # wide notch
        NotchEvenDist(
            alpha=0.5 * pi / p + a1, notch_shape=NCirc2
        ),  # cut out completely
        NotchEvenDist(alpha=0.5 * pi / p, notch_shape=NSlotW26),  # small notch
    ]
    delta_d = Toyota_Prius.stator.Rint - Toyota_Prius.rotor.Rext
    Toyota_Prius.rotor.bore = BoreSinePole(
        N=8, delta_d=delta_d, delta_q=5 * mm, W0=50 * mm
    )

    Toyota_Prius.plot(sym=8, is_show_fig=is_show_fig)
    Toyota_Prius.plot(is_show_fig=is_show_fig)

    # Add notches to Audi_eTron
    NBs = SlotCirc(Zs=16, W0=0.001, H0=0.0005)
    NBr = SlotCirc(Zs=29, W0=0.001, H0=0.0005)

    Audi_eTron.stator.notch = [NotchEvenDist(alpha=0, notch_shape=NBs)]
    Audi_eTron.rotor.notch = [NotchEvenDist(alpha=0, notch_shape=NBr)]
    Audi_eTron.stator.slot.H0 = 4 * mm
    Audi_eTron.stator.bore = BoreFlower(N=4, Rarc=Audi_eTron.stator.Rint + 10 * mm)

    Audi_eTron.plot(sym=2, is_show_fig=is_show_fig)
    Audi_eTron.plot(is_show_fig=is_show_fig)

    return Toyota_Prius, Audi_eTron


@pytest.mark.IPMSM
@pytest.mark.SCIM
def test_bore_and_notch_merge_type_2(is_show_fig=False):
    """Validation of rotor and stator notches"""

    # Load machines
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    # Add notches to Toyota_Prius
    p = Toyota_Prius.get_pole_pair_number()

    Nq = SlotW26(Zs=2 * p, W0=1 * mm, H0=4 * mm, H1=0, R1=3 * mm, R2=3 * mm)
    NCirc1 = SlotCirc(Zs=2 * p, W0=8 * mm, H0=2 * mm)
    NCirc2 = SlotCirc(Zs=2 * p, W0=3 * mm, H0=1 * mm)
    NSlotW26 = SlotW26(Zs=2 * p, W0=1 * mm, H0=2 * mm, H1=0, R1=3 * mm, R2=3 * mm)

    a0 = 0.2
    a1 = 0.33

    Toyota_Prius.rotor.notch = [
        NotchEvenDist(alpha=0, notch_shape=Nq),  # q-axis notch -> test sym. cut
        NotchEvenDist(alpha=0.5 * pi / p + a0, notch_shape=NCirc1),  # wide notch
        NotchEvenDist(alpha=0.5 * pi / p - a0, notch_shape=NCirc1),  # wide notch
        NotchEvenDist(alpha=0.5 * pi / p + a1, notch_shape=NCirc2),  # cut out at all
        NotchEvenDist(alpha=0.5 * pi / p, notch_shape=NSlotW26),  # small notch
    ]
    delta_d = Toyota_Prius.stator.Rint - Toyota_Prius.rotor.Rext
    Toyota_Prius.rotor.bore = BoreSinePole(
        N=8, delta_d=delta_d, delta_q=5 * mm, W0=50 * mm
    )

    Toyota_Prius.rotor.bore.type_merge_slot = 2

    Toyota_Prius.plot(sym=8, is_show_fig=is_show_fig)
    Toyota_Prius.plot(is_show_fig=is_show_fig)

    return Toyota_Prius


if __name__ == "__main__":
    # Toyota_Prius = test_bore_and_notch_merge_type_0(is_show_fig=True)
    # Toyota_Prius, Audi_eTron = test_bore_and_notch_merge_type_1(is_show_fig=True)
    Toyota_Prius = test_bore_and_notch_merge_type_2(is_show_fig=True)
    print("Done")
