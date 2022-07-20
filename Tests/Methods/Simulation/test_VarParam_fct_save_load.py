from os.path import join, isdir
from os import makedirs, remove

import numpy as np

from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.VarParam import VarParam
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.DataKeeper import DataKeeper
from pyleecan.Classes.ParamExplorerSet import ParamExplorerSet


from pyleecan.Functions.load import load

from Tests import save_validation_path as save_path
from pyleecan.definitions import DATA_DIR


def test_VarParam_fct_save_load():
    """Test to check keeper, setter and getter functions defined as path containing
    global variable <PARAM_DIR>"""

    machine = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    # First simulation creating femm file
    simu = Simu1(name="test_VarParam_fct_save_load", machine=machine)

    result_folder = join(save_path, simu.name)
    result_folder = result_folder.replace("\\", "/")
    if not isdir(result_folder):
        makedirs(result_folder)

    # Create function files
    keeper_path = join(result_folder, "keeper_fct.py")
    with open(keeper_path, "w+") as keeper_file:
        keeper_file.write("def keeper_fct(out):\n    return 1")

    setter_path = join(result_folder, "setter_fct.py")
    with open(setter_path, "w+") as setter_file:
        setter_file.write("def setter_fct(out, val):\n    return None")

    getter_path = join(result_folder, "getter_fct.py")
    with open(getter_path, "w+") as getter_file:
        getter_file.write("def getter_fct(out):\n    return 2")

    # Initialization of the simulation starting point
    simu.input = InputCurrent(
        OP=OPdq(N0=1000, Id_ref=0, Iq_ref=0),
        Nt_tot=8 * 10,
        Na_tot=8 * 200,
        is_periodicity_a=True,
        is_periodicity_t=True,
    )

    # Generate parameter sweep
    simu.var_simu = VarParam(
        stop_if_error=True,
        is_keep_all_output=True,
        datakeeper_list=[
            DataKeeper(
                name="Dummy result",
                symbol="res",
                unit="-",
                keeper=result_folder + "/keeper_fct.py",
                error_keeper="lambda simu: np.nan",
            )
        ],
        paramexplorer_list=[
            ParamExplorerSet(
                name="Dummy variable",
                symbol="X",
                unit="-",
                setter=result_folder + "/setter_fct.py",
                getter=result_folder + "/getter_fct.py",
                value=[ii for ii in range(2)],
            )
        ],
        is_reuse_femm_file=False,
        is_reuse_LUT=False,
    )

    out = simu.run()

    out_h5_path = join(result_folder, simu.name + ".h5")

    out.save(out_h5_path)

    out_load = load(out_h5_path)

    diff_list = out.compare(out_load)

    assert len(diff_list) == 0

    # Delete files
    # remove(keeper_path)
    # remove(setter_path)
    # remove(getter_path)
    # remove(out_h5_path)


if __name__ == "__main__":

    test_VarParam_fct_save_load()
    print("Done")
