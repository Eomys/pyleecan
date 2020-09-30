import pytest
from os.path import join

# -*- coding: utf-8 -*-
import sys
from os.path import dirname, abspath, normpath, join, realpath
from os import listdir, remove, system
import json


# Add the directory to the python path
sys.path.append(normpath(abspath(join(dirname(__file__), "../.."))))

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
from pyleecan.Classes.PostFunction import PostFunction
from pyleecan.Classes.PostMethod import PostMethod
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputElec import InputElec
from pyleecan.Classes.VarParam import VarParam
from pyleecan.Classes.ParamExplorerSet import ParamExplorerSet
from pyleecan.Classes.DataKeeper import DataKeeper
from copy import copy


class ExamplePostMethod(PostMethod):
    def __init__(self):
        PostMethod.__init__(self)

    def run(self, output):
        output.simu.machine.stator.slot.W0 += 2

    def copy(self):
        return copy(self)

    def as_dict(self):
        return copy(self)


# @pytest.mark.skip  # Skip it until class generator is not fixed (definition of attribute as empty dict get the same reference)
def test_post_var_simu():
    """Test the simulation.var_simu.post_list"""

    IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))

    # simu1, simu without postprocessing
    simu1 = Simu1(name="test_post_simu", machine=IPMSM_A)
    # Definition of the input
    simu1.input = InputElec(
        N0=2000, Id_ref=-100, Iq_ref=200, Nt_tot=10, Na_tot=2048, rot_dir=1
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
        keeper="lambda output: output.simu.machine.stator.slot.W0",
    )

    simu1.var_simu = VarParam(
        ref_simu_index=0,
        paramexplorer_list=[pe1],
        datakeeper_list=[dk1],
        stop_if_error=True,
    )

    # simu2, postprocessing 1 PostFunction, 1 PostMethod
    simu2 = simu1.copy()

    # Create the postprocessings and add it
    post1 = PostFunction(run=join(dirname(__file__), "example_post.py"))
    post2 = PostFunction(run=join(dirname(__file__), "example_post2.py"))
    print(
        id(simu1.var_simu.datakeeper_list[0].result),
        id(simu2.var_simu.datakeeper_list[0].result),
    )
    simu2.postproc_list = [post1]
    simu2.var_simu.postproc_list = [post2]

    print(simu1.var_simu.datakeeper_list[0])
    print(simu2.var_simu.datakeeper_list[0])
    # First simulation without postprocessings
    out1 = simu1.run()

    # Second simulation with postprocessing
    out2 = simu2.run()
    assert (
        list(map(lambda val: val + 2, out1["D_S_s_w"].result)) == out2["D_S_s_w"].result
    )
    assert out1.simu.machine.stator.slot.H0 + 1 == out2.simu.machine.stator.slot.H0


if __name__ == "__main__":

    test_post_var_simu()
