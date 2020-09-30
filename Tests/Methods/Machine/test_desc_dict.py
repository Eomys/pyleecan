import pytest
from os.path import join

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


def test_desc_SCIM():
    """Check that the description of a SCIM is correct"""
    SCIM_001 = load(join(DATA_DIR, "Machine", "SCIM_001.json"))
    desc_dict = SCIM_001.comp_desc_dict()
    assert len(desc_dict) == 9
    assert desc_dict[0]["name"] == "Type"
    assert desc_dict[0]["value"] == "SCIM"

    assert desc_dict[1]["name"] == "Zs"
    assert desc_dict[1]["value"] == 36

    assert desc_dict[2]["name"] == "Zr"
    assert desc_dict[2]["value"] == 28

    assert desc_dict[3]["name"] == "p"
    assert desc_dict[3]["value"] == 3

    assert desc_dict[4]["name"] == "Topology"
    assert desc_dict[4]["value"] == "Inner Rotor"

    assert desc_dict[5]["name"] == "qs"
    assert desc_dict[5]["value"] == 3

    assert desc_dict[6]["name"] == "Winding"
    assert desc_dict[6]["value"] == "double layer distributed"

    assert desc_dict[7]["name"] == "Rwinds"
    assert desc_dict[7]["value"] == pytest.approx(0.02392, rel=0.1)

    assert desc_dict[8]["name"] == "Mmachine"
    assert desc_dict[8]["value"] == pytest.approx(328.1, rel=0.1)


def test_desc_IPMSM():
    """Check that the description of an IPMSM is correct"""
    IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))
    desc_dict = IPMSM_A.comp_desc_dict()
    assert len(desc_dict) == 8
    assert desc_dict[0]["name"] == "Type"
    assert desc_dict[0]["value"] == "IPMSM"

    assert desc_dict[1]["name"] == "Zs"
    assert desc_dict[1]["value"] == 48

    assert desc_dict[2]["name"] == "p"
    assert desc_dict[2]["value"] == 4

    assert desc_dict[3]["name"] == "Topology"
    assert desc_dict[3]["value"] == "Inner Rotor"

    assert desc_dict[4]["name"] == "qs"
    assert desc_dict[4]["value"] == 3

    assert desc_dict[5]["name"] == "Winding"
    assert desc_dict[5]["value"] == "single layer distributed"

    assert desc_dict[6]["name"] == "Rwinds"
    assert desc_dict[6]["value"] == pytest.approx(0.0359, rel=0.1)

    assert desc_dict[7]["name"] == "Mmachine"
    assert desc_dict[7]["value"] == pytest.approx(33.37, rel=0.1)
