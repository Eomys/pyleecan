import pytest
from pyleecan.Functions.load import load

from Tests import save_plot_path as save_path
from pyleecan.definitions import DATA_DIR
from os.path import join, isdir, isfile
from os import makedirs, remove
import matplotlib.pyplot as plt
from pyleecan.Functions.init_fig import init_fig


SCHEMATICS_PATH = join(save_path, "Schematics")

if not isdir(SCHEMATICS_PATH):
    makedirs(SCHEMATICS_PATH)

MACH_PATH = join(DATA_DIR, "Machine")
mach_test = list()
mach_test.append(
    {"json_path": join(MACH_PATH, "SCIM_001.json"), "machine_name": "SCIM"}
)
mach_test.append(
    {"json_path": join(MACH_PATH, "IPMSM_A.json"), "machine_name": "IPMSM"}
)
mach_test.append(
    {"json_path": join(MACH_PATH, "SynRM_001.json"), "machine_name": "SynRM"}
)
mach_test.append(
    {"json_path": join(MACH_PATH, "Benchmark.json"), "machine_name": "SPMSM"}
)


class Test_machine_img(object):
    @pytest.mark.parametrize("test_dict", mach_test)
    def test_machine(self, test_dict):
        """Machine Illustration images (first page of the GUI)"""
        file_name = "machine_" + test_dict["machine_name"] + ".png"
        save_path = join(SCHEMATICS_PATH, file_name)
        # Delete previous plot
        if isfile(save_path):
            remove(save_path)
        # Save schematics
        test_obj = load(test_dict["json_path"])
        fig, ax, _, _ = init_fig(shape="square")
        test_obj.plot(
            fig=fig,
            ax=ax,
            save_path=None,
            is_show_fig=False,
        )
        # Clean axes
        ax.set_title("")
        W = test_obj.stator.Rext * 1.05
        ax.set_xlim(-W, W)
        ax.set_ylim(-W, W)
        ax.get_legend().remove()
        ax.set_axis_off()
        # Save
        fig.savefig(save_path)
