from os.path import join

import pytest

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.LamSlotWind import LamSlotWind


@pytest.mark.SCIM
def test_desc_SCIM():
    """Check that the description of a SCIM is correct"""
    Railway_Traction = load(join(DATA_DIR, "Machine", "Railway_Traction.json"))
    desc_dict = Railway_Traction.comp_desc_dict()
    assert len(desc_dict) == 12
    assert desc_dict[0]["name"] == "Type"
    assert desc_dict[0]["value"] == "SCIM"

    assert desc_dict[1]["name"] == "Zs"
    assert desc_dict[1]["value"] == 36

    assert desc_dict[2]["name"] == "Zr"
    assert desc_dict[2]["value"] == 28

    assert desc_dict[3]["name"] == "p"
    assert desc_dict[3]["value"] == 3

    assert desc_dict[4]["name"] == "Topology"
    assert desc_dict[4]["value"] == "Internal Rotor"

    assert desc_dict[5]["name"] == "qs"
    assert desc_dict[5]["value"] == 3

    assert desc_dict[6]["name"] == "Rwinds"
    assert desc_dict[6]["value"] == pytest.approx(0.02392, rel=0.1)

    assert desc_dict[7]["name"] == "Mmachine"
    assert desc_dict[7]["value"] == pytest.approx(342.819, rel=0.1)

    assert desc_dict[8]["name"] == "Mslam"
    assert desc_dict[8]["value"] == pytest.approx(143.598, rel=0.1)

    assert desc_dict[9]["name"] == "Mswind"
    assert desc_dict[9]["value"] == pytest.approx(59.055, rel=0.1)

    assert desc_dict[10]["name"] == "Mrlam"
    assert desc_dict[10]["value"] == pytest.approx(97.5362, rel=0.1)

    assert desc_dict[11]["name"] == "Mrwind"
    assert desc_dict[11]["value"] == pytest.approx(21.118, rel=0.1)


@pytest.mark.IPMSM
def test_desc_IPMSM():
    """Check that the description of an IPMSM is correct"""
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    desc_dict = Toyota_Prius.comp_desc_dict()
    assert len(desc_dict) == 11
    assert desc_dict[0]["name"] == "Type"
    assert desc_dict[0]["value"] == "IPMSM"

    assert desc_dict[1]["name"] == "Zs"
    assert desc_dict[1]["value"] == 48

    assert desc_dict[2]["name"] == "p"
    assert desc_dict[2]["value"] == 4

    assert desc_dict[3]["name"] == "Topology"
    assert desc_dict[3]["value"] == "Internal Rotor"

    assert desc_dict[4]["name"] == "qs"
    assert desc_dict[4]["value"] == 3

    assert desc_dict[5]["name"] == "Rwinds"
    assert desc_dict[5]["value"] == pytest.approx(0.0359, rel=0.1)

    assert desc_dict[6]["name"] == "Mmachine"
    assert desc_dict[6]["value"] == pytest.approx(33.37, rel=0.1)

    assert desc_dict[7]["name"] == "Mslam"
    assert desc_dict[7]["value"] == pytest.approx(15.78146, rel=0.1)

    assert desc_dict[8]["name"] == "Mswind"
    assert desc_dict[8]["value"] == pytest.approx(4.0014, rel=0.1)

    assert desc_dict[9]["name"] == "Mrlam"
    assert desc_dict[9]["value"] == pytest.approx(5.0063, rel=0.1)

    assert desc_dict[10]["name"] == "Mmag"
    assert desc_dict[10]["value"] == pytest.approx(1.235, rel=0.1)


@pytest.mark.outer_rotor
def test_desc_Outer_Rotor():
    """Check that the description with External Rotor is correct"""

    test_obj = MachineIPMSM()
    test_obj.stator = LamSlotWind(is_stator=True, is_internal=True)
    test_obj.rotor = LamHole(
        is_internal=False,
        Rint=0.021,
        Rext=0.075,
        is_stator=False,
        L1=0.7,
        Nrvd=0,
        Kf1=0.95,
    )

    desc_dict = test_obj.comp_desc_dict()
    assert desc_dict[3]["name"] == "Topology"
    assert desc_dict[3]["value"] == "External Rotor"


if __name__ == "__main__":
    test_desc_IPMSM()
    test_desc_SCIM()
    test_desc_Outer_Rotor()
    print("Done")
