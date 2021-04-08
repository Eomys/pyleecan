import pytest

from pyleecan.Classes.Loss import Loss
from pyleecan.Classes.LossModel import LossModel


# @pytest.mark.dev
def test_Loss_methods():
    """Test Loss methods add_model and remove_model"""
    # create objects
    loss = Loss()
    mdl = LossModel()
    mdl.name = "Test Loss Model"

    # add models
    loss.add_model(model=mdl, part_label="Stator")
    loss.add_model(model=mdl, part_label="Stator", index=1)
    loss.add_model(model=mdl, part_label="Stator", index=0)  # override
    loss.add_model(model=mdl, part_label="Rotor")
    loss.add_model(model=mdl, part_label="Frame")

    assert len(loss.model_list) == 4

    # remove models
    loss.remove_model(part_label="Stator", index=1)

    assert len(loss.model_list) == 4  # length stay the same
    assert loss.model_list[1] is None

    # try to remove non existing models -> only warning should occur
    loss.remove_model(part_label="Shaft", index=1)
    loss.remove_model(part_label="Stator", index=1)  # removed previously


# To run it without pytest
if __name__ == "__main__":
    test_Loss_methods()
