import pytest
from os.path import join
from pyleecan.Classes.OPdq import OPdq

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
from pyleecan.Classes.PostFunction import PostFunction
from pyleecan.Classes.PostMethod import PostMethod
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent


class ExamplePostMethod(PostMethod):
    def run(self, output):
        output.simu.machine.stator.slot.W0 += 2


@pytest.mark.IPMSM
@pytest.mark.SingleOP
def test_post_simu():
    """Test the simulation.post_list"""

    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    # simu1, simu without postprocessing
    simu1 = Simu1(name="test_post_simu", machine=Toyota_Prius)
    # Definition of the input
    simu1.input = InputCurrent(
        OP=OPdq(N0=2000, Id_ref=-100, Iq_ref=200), Nt_tot=10, Na_tot=2048, rot_dir=1
    )

    # simu2, postprocessing 1 PostFunction, 1 PostMethod
    simu2 = simu1.copy()
    simu2.name = "test_post_simu2"

    def example_post(output):
        output.simu.machine.stator.slot.H0 += 1

    # Create the postprocessings and add it
    post1 = PostFunction(run=example_post)
    post2 = ExamplePostMethod()

    simu2.postproc_list.extend([post1, post2])

    # First simulation without postprocessings
    out1 = simu1.run()

    # Second simulation with postprocessing
    out2 = simu2.run()

    assert out1.simu.machine.stator.slot.W0 + 2 == out2.simu.machine.stator.slot.W0
    assert out1.simu.machine.stator.slot.H0 + 1 == out2.simu.machine.stator.slot.H0


# To run it without pytest
if __name__ == "__main__":
    out = test_post_simu()
