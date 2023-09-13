# -*- coding: utf-8 -*-

import pytest
from os.path import join

from mock import MagicMock
from numpy import array, pi, zeros

from pyleecan.Classes.MachineUD import MachineUD
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

# For AlmostEqual
DELTA = 1e-4

M_test = list()
test_obj = MachineIPMSM()
test_obj.rotor = LamHole(
    is_internal=True, Rint=0.021, Rext=0.075, is_stator=False, L1=0.7, Nrvd=0, Kf1=0.95
)
test_obj.rotor.hole = list()
test_obj.rotor.hole.append(
    HoleM50(
        Zh=8,
        W0=50e-3,
        W1=2e-3,
        W2=1e-3,
        W3=1e-3,
        W4=20.6e-3,
        H0=17.3e-3,
        H1=1.25e-3,
        H2=0.5e-3,
        H3=6.8e-3,
        H4=0,
    )
)
test_obj.rotor.hole[0].magnet_0.Lmag = 0.3
test_obj.rotor.hole[0].magnet_1.Lmag = 0.5
test_obj.rotor.hole[0].magnet_0.mat_type.struct.rho = 1000
test_obj.rotor.hole[0].magnet_1.mat_type.struct.rho = 1000
test_obj.rotor.axial_vent = list()
test_obj.rotor.axial_vent.append(VentilationCirc(Zh=8, Alpha0=0, D0=5e-3, H0=40e-3))
test_obj.rotor.axial_vent.append(
    VentilationCirc(Zh=8, Alpha0=pi / 8, D0=7e-3, H0=40e-3)
)
test_obj.rotor.mat_type.struct.rho = 7600
test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=1.2)
test_obj.shaft.mat_type.struct.rho = 5000
test_obj.stator = LamSlotWind(
    Rint=0.078, Rext=0.104, is_internal=False, is_stator=True, L1=0.8, Nrvd=0, Kf1=0.95
)
test_obj.stator.slot = None
test_obj.stator.winding = None
test_obj.stator.axial_vent.append(
    VentilationPolar(Zh=8, H0=0.08, D0=0.01, W1=pi / 8, Alpha0=pi / 8)
)
test_obj.stator.axial_vent.append(
    VentilationPolar(Zh=8, H0=0.092, D0=0.01, W1=pi / 8, Alpha0=0)
)
test_obj.stator.mat_type.struct.rho = 8000
test_obj.frame = Frame(Rint=0.104, Rext=0.114, Lfra=1)
test_obj.frame.mat_type.struct.rho = 4000

M_test.append(
    {
        "test_obj": test_obj,
        "Mfra": 4000 * pi * (0.114**2 - 0.104**2),
        "Msha": 5000 * 1.2 * pi * 0.021**2,
    }
)
M_test[-1]["rotor"] = {
    "Slam": 1.2797e-2,
    "Svent": 8 * pi * (2.5e-3**2 + 3.5e-3**2),
    "Smag": 6.8e-3 * 20.6e-3 * 2 * 8,
}
M_test[-1]["rotor"]["Vlam"] = M_test[-1]["rotor"]["Slam"] * 0.7
M_test[-1]["rotor"]["Vvent"] = M_test[-1]["rotor"]["Svent"] * 0.7
M_test[-1]["rotor"]["Vmag"] = M_test[-1]["rotor"]["Smag"] * 0.4
M_test[-1]["Mrot"] = (
    M_test[-1]["rotor"]["Vmag"] * 1000 + M_test[-1]["rotor"]["Vlam"] * 7600 * 0.95
)

M_test[-1]["stator"] = {"Slam": 9.1483e-3, "Svent": 5.7177e-3}
M_test[-1]["stator"]["Vlam"] = M_test[-1]["stator"]["Slam"] * 0.8
M_test[-1]["stator"]["Vvent"] = M_test[-1]["stator"]["Svent"] * 0.8
M_test[-1]["stator"]["Mwind"] = 0
M_test[-1]["stator"]["Mtot"] = (
    M_test[-1]["stator"]["Vlam"] * 8000 * 0.95 + M_test[-1]["stator"]["Mwind"]
)
M_test[-1]["Mmach"] = (
    M_test[-1]["Mrot"]
    + M_test[-1]["stator"]["Mtot"]
    + M_test[-1]["Mfra"]
    + M_test[-1]["Msha"]
)
# Toyota_Prius
M_test.append(
    {
        "test_obj": Toyota_Prius,
        "Mfra": 0,
        "Msha": 7650 * 0.1 * pi * (0.11064 / 2) ** 2,
    }  # No frame
)
M_test[-1]["rotor"] = {"Slam": 0.0082186, "Svent": 0, "Smag": 0.0189 * 0.0065 * 2 * 8}
M_test[-1]["rotor"]["Vlam"] = M_test[-1]["rotor"]["Slam"] * 0.08382
M_test[-1]["rotor"]["Vvent"] = M_test[-1]["rotor"]["Svent"] * 0.08382
M_test[-1]["rotor"]["Vmag"] = M_test[-1]["rotor"]["Smag"] * 0.08382
M_test[-1]["Mrot"] = (
    M_test[-1]["rotor"]["Vmag"] * 7500 + M_test[-1]["rotor"]["Vlam"] * 7650 * 0.95
)

M_test[-1]["stator"] = {"Slam": 0.0259068, "Svent": 0}
M_test[-1]["stator"]["Vlam"] = M_test[-1]["stator"]["Slam"] * 0.08382
M_test[-1]["stator"]["Vvent"] = M_test[-1]["stator"]["Svent"] * 0.08382
M_test[-1]["stator"]["Mwind"] = 4.0015
M_test[-1]["stator"]["Mtot"] = (
    M_test[-1]["stator"]["Vlam"] * 7650 * 0.95 + M_test[-1]["stator"]["Mwind"]
)
M_test[-1]["Mmach"] = 33.38
# Toyota Prius as MachineUD
UD_dict = M_test[-1].copy()
UD_dict["test_obj"] = MachineUD(
    frame=Toyota_Prius.frame,
    shaft=Toyota_Prius.shaft,
    lam_list=[Toyota_Prius.rotor, Toyota_Prius.stator],
)


@pytest.mark.parametrize("test_dict", M_test)
def test_comp_surface_rotor(test_dict):
    """Check that the computation of the surface is correct"""
    result = test_dict["test_obj"].rotor.comp_surfaces()

    a = result["Slam"]
    b = test_dict["rotor"]["Slam"]
    msg = "For Slam, Return " + str(a) + " expected " + str(b)
    assert a == pytest.approx(b, rel=DELTA), msg

    a = result["Svent"]
    b = test_dict["rotor"]["Svent"]
    msg = "For Svent, Return " + str(a) + " expected " + str(b)
    assert a == pytest.approx(b, rel=DELTA), msg

    if "Smag" in result.keys():
        a = result["Smag"]
        b = test_dict["rotor"]["Smag"]
        msg = "For Smag, Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

    a = result["Syoke"]


@pytest.mark.parametrize("test_dict", M_test)
def test_comp_surface_stator(test_dict):
    """Check that the computation of the surface is correct"""
    result = test_dict["test_obj"].stator.comp_surfaces()

    a = result["Slam"]
    b = test_dict["stator"]["Slam"]
    msg = "Return " + str(a) + " expected " + str(b)
    assert a == pytest.approx(b, rel=DELTA), msg

    a = result["Svent"]
    b = test_dict["stator"]["Svent"]
    msg = "Return " + str(a) + " expected " + str(b)
    assert a == pytest.approx(b, rel=DELTA), msg

    if "Smag" in result.keys():
        a = result["Smag"]
        b = test_dict["stator"]["Smag"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg


@pytest.mark.parametrize("test_dict", M_test)
def test_comp_volume_rotor(test_dict):
    """Check that the computation of the volume is correct"""
    result = test_dict["test_obj"].rotor.comp_volumes()

    a = result["Vlam"]
    b = test_dict["rotor"]["Vlam"]
    msg = "Return " + str(a) + " expected " + str(b)
    assert a == pytest.approx(b, rel=DELTA), msg

    a = result["Vvent"]
    b = test_dict["rotor"]["Vvent"]
    msg = "Return " + str(a) + " expected " + str(b)
    assert a == pytest.approx(b, rel=DELTA), msg

    if "Vmag" in result.keys():
        a = result["Vmag"]
        b = test_dict["rotor"]["Vmag"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg


@pytest.mark.parametrize("test_dict", M_test)
def test_comp_volume_stator(test_dict):
    """Check that the computation of the volume is correct"""
    result = test_dict["test_obj"].stator.comp_volumes()

    a = result["Vlam"]
    b = test_dict["stator"]["Vlam"]
    msg = "Return " + str(a) + " expected " + str(b)
    assert a == pytest.approx(b, rel=DELTA), msg

    a = result["Vvent"]
    b = test_dict["stator"]["Vvent"]
    msg = "Return " + str(a) + " expected " + str(b)
    assert a == pytest.approx(b, rel=DELTA), msg

    if "Vmag" in result.keys():
        a = result["Vmag"]
        b = test_dict["stator"]["Vmag"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg


@pytest.mark.parametrize("test_dict", M_test + [UD_dict])
def test_comp_mass(test_dict):
    """Check that the computation of the mass is correct"""
    result = test_dict["test_obj"].comp_masses()

    a = result["Frame"]
    b = test_dict["Mfra"]
    msg = "Mfra, Return " + str(a) + " expected " + str(b)
    assert a == pytest.approx(b, rel=DELTA), msg

    a = result["Shaft"]
    b = test_dict["Msha"]
    msg = "Msha, Return " + str(a) + " expected " + str(b)
    assert a == pytest.approx(b, rel=DELTA), msg

    a = result["Rotor-0"]["Mtot"]
    b = test_dict["Mrot"]
    msg = "Mrot, Return " + str(a) + " expected " + str(b)
    assert a == pytest.approx(b, rel=DELTA), msg

    assert result["Rotor-0"]["Myoke"] + result["Rotor-0"]["Mteeth"] == pytest.approx(
        result["Rotor-0"]["Mlam"], rel=DELTA
    )
    assert result["Stator-0"]["Myoke"] + result["Stator-0"]["Mteeth"] == pytest.approx(
        result["Stator-0"]["Mlam"], rel=DELTA
    )

    a = result["Stator-0"]["Mwind"]
    b = test_dict["stator"]["Mwind"]
    msg = "Msta[Mwind], Return " + str(a) + " expected " + str(b)
    assert a == pytest.approx(b, rel=DELTA), msg

    a = result["Stator-0"]["Mtot"]
    b = test_dict["stator"]["Mtot"]
    msg = "Msta[Mtot], Return " + str(a) + " expected " + str(b)
    assert a == pytest.approx(b, rel=DELTA), msg

    a = result["All"]
    b = test_dict["Mmach"]
    msg = "Mmach, Return " + str(a) + " expected " + str(b)
    assert a == pytest.approx(b, rel=DELTA), msg


def test_comp_mass_shaft_none():
    """Check that the compytation of the mass is correct even if there is no shaft"""
    test_obj.shaft = None
    result = test_obj.comp_masses()

    assert result["Shaft"] == 0


if __name__ == "__main__":
    for test_dict in M_test:
        test_comp_surface_rotor(test_dict)
        test_comp_surface_stator(test_dict)
        test_comp_volume_rotor(test_dict)
        test_comp_volume_stator(test_dict)
        test_comp_mass(test_dict)

    test_comp_mass_shaft_none()
    print("Done")
