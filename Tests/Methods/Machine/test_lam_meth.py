from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.NotchEvenDist import NotchEvenDist
from pyleecan.Classes.SlotM10 import SlotM10
import pytest
import matplotlib.pyplot as plt

lam_list = list()

# Circular lamination
lam_list.append(Lamination(Rint=0, Rext=1, is_internal=True))

# Lamination with notches
lam1 = Lamination(Rint=0.5, Rext=1, is_internal=True)
lam1.notch = [NotchEvenDist(notch_shape=SlotM10(Zs=8, W0=0.05, H0=0.1))]
lam_list.append(lam1)

# Lamintion with yoke notches
lam2 = Lamination(Rint=0.5, Rext=1, is_internal=True)
lam2.notch = [NotchEvenDist(notch_shape=SlotM10(Zs=8, W0=0.05, H0=0.1, is_bore=False))]
lam_list.append(lam2)

# Lamination with both notches
lam3 = Lamination(Rint=0.5, Rext=1, is_internal=True)
lam3.notch = [NotchEvenDist(notch_shape=SlotM10(Zs=8, W0=0.05, H0=0.1, is_bore=True))]
lam3.notch.append(
    NotchEvenDist(notch_shape=SlotM10(Zs=8, W0=0.2, H0=0.1, is_bore=False))
)
lam_list.append(lam3)


@pytest.mark.parametrize("test_obj", lam_list)
def test_lam_comp_surface(test_obj):
    """Check that the Lamination surface is correctly computed"""

    # test_obj.notch[0].notch_shape.plot()
    # test_obj.plot()
    # plt.show()
    S1 = test_obj.comp_surfaces()["Slam"]

    # Numerical computation
    surf = test_obj.build_geometry()
    S2 = surf[0].comp_surface()

    assert S1 == pytest.approx(S2, rel=1e-4)

    # Check symetry
    # test_obj.plot(sym=4)
    # plt.show()
    surf = test_obj.build_geometry(sym=4)
    S3 = surf[0].comp_surface()

    assert S1 / 4 == pytest.approx(S3, rel=1e-4)


if __name__ == "__main__":
    test_lam_comp_surface(lam_list[0])
    test_lam_comp_surface(lam_list[1])
    test_lam_comp_surface(lam_list[2])
    test_lam_comp_surface(lam_list[3])
    print("Done")
