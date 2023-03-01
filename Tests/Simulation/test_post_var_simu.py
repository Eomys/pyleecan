import pytest
from os.path import join

from copy import copy

from numpy import sqrt
import numpy as np
from pyleecan.Classes.HoleM51 import HoleM51
from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.Classes.HoleM53 import HoleM53
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.PostFunction import PostFunction
from pyleecan.Classes.PostMethod import PostMethod
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.VarParamSweep import VarParamSweep
from pyleecan.Classes.ParamExplorerSet import ParamExplorerSet
from pyleecan.Classes.DataKeeper import DataKeeper

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

from Tests import TEST_DATA_DIR


class ExamplePostMethod(PostMethod):
    def __init__(self):
        PostMethod.__init__(self)

    def run(self, output):
        output.simu.machine.stator.slot.W0 += 10

    def copy(self, **kwargs):
        return copy(self)

    def as_dict(self, **kwargs):
        return copy(self)


@pytest.mark.IPMSM
@pytest.mark.VarParam
def test_post_var_simu():
    """Test the simulation.var_simu.post_list"""

    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    # simu1, simu without postprocessing
    simu1 = Simu1(name="test_post_simu", machine=Toyota_Prius)
    # Definition of the input
    simu1.input = InputCurrent(
        OP=OPdq(N0=2000, Id_ref=-100, Iq_ref=200), Nt_tot=10, Na_tot=2048, rot_dir=1
    )

    # Vary Stator slot H0
    pe1 = ParamExplorerSet(
        value=[1, 2, 3],
        setter="simu.machine.stator.slot.W0",
        name="Stator slot width",
        unit="m",
        symbol="S_s_w",
    )

    # Save in a datakeeper Stator slot H0
    dk1 = DataKeeper(
        name="Stator slot width",
        unit="m",
        symbol="D_S_s_w",
        keeper="lambda output: np.sqrt(output.simu.machine.stator.slot.W0)",
    )

    simu1.var_simu = VarParamSweep(
        paramexplorer_list=[pe1],
        datakeeper_list=[dk1],
        stop_if_error=True,
    )

    # simu2, postprocessing 1 PostFunction, 1 PostMethod
    simu2 = simu1.copy()
    simu2.name = "test_post_simu2"

    # Create the postprocessings and add it
    # xoutput.simu.machine.stator.slot.H0 += 1
    post1 = PostFunction(run=join(TEST_DATA_DIR, "example_post.py"))

    # xoutput.simu.machine.stator.slot.W0 += 2
    post2 = PostFunction(run=join(TEST_DATA_DIR, "example_post2.py"))

    post3 = PostFunction(run=join(TEST_DATA_DIR, "example_post3.py"))
    post4 = ExamplePostMethod()

    simu2.postproc_list = [post2, post3, post4]
    simu2.var_simu.postproc_list = [post1]
    simu2.var_simu.is_keep_all_output = True

    # First simulation without postprocessings
    out1 = simu1.run()

    # Second simulation with postprocessing
    out2 = simu2.run()
    # Check ref simu
    assert out1["D_S_s_w"].result == [1, sqrt(2), sqrt(3)]
    # Check post 2 + 4
    assert [output.simu.machine.stator.slot.W0 for output in out2] == [13, 14, 15]
    # Check post 1
    assert out1.simu.machine.stator.slot.H0 + 1 == pytest.approx(
        out2.simu.machine.stator.slot.H0, 0.001
    )
    # Check post 3 with import + using result of post2
    assert type(out2[0].simu.machine.rotor.hole[0]) is HoleM51
    assert type(out2[1].simu.machine.rotor.hole[0]) is HoleM52
    assert type(out2[2].simu.machine.rotor.hole[0]) is HoleM53


if __name__ == "__main__":

    test_post_var_simu()
