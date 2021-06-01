from os.path import join
import pytest

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


@pytest.mark.IPMSM
def test_material_dict():
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    mat_dict = Toyota_Prius.get_material_dict()

    # Check only names
    for key, value in mat_dict.items():
        mat_dict[key] = value.name

    exp_dict = {
        "self.stator.mat_type": "M400-50A",
        "self.stator.winding.conductor.ins_mat": "Insulator1",
        "self.stator.winding.conductor.cond_mat": "Copper1",
        "self.rotor.mat_type": "M400-50A",
        "self.rotor.hole.mat_void": "Air",
        "self.rotor.hole.magnet_0.mat_type": "MagnetPrius",
        "self.rotor.hole.magnet_1.mat_type": "MagnetPrius",
        "self.shaft.mat_type": "M400-50A",
    }

    assert mat_dict == exp_dict


@pytest.mark.IPMSM
def test_material_dict_unique():
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    mat_dict = Toyota_Prius.get_material_dict(is_unique=True)

    # Check only names
    for key, value in mat_dict.items():
        mat_dict[key] = value.name

    exp_dict = {
        "self.shaft.mat_type": "M400-50A",
        "self.stator.winding.conductor.ins_mat": "Insulator1",
        "self.stator.winding.conductor.cond_mat": "Copper1",
        "self.rotor.hole.mat_void": "Air",
        "self.rotor.hole.magnet_0.mat_type": "MagnetPrius",
    }

    assert mat_dict == exp_dict


if __name__ == "__main__":
    test_material_dict()
    test_material_dict_unique()
