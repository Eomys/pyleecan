import pytest
from pyleecan.Classes.CondType11 import CondType11
from pyleecan.Classes.CondType12 import CondType12

from Tests import save_plot_path as save_path
from os.path import join, isdir, isfile
from os import makedirs, remove

SCHEMATICS_PATH = join(save_path, "Schematics")

if not isdir(SCHEMATICS_PATH):
    makedirs(SCHEMATICS_PATH)

cond_test = list()
cond_test.append(
    {
        "test_obj": CondType11(),
    }
)
cond_test.append(
    {
        "test_obj": CondType12(),
    }
)


class Test_cond_schematics(object):
    @pytest.mark.parametrize("test_dict", cond_test)
    def test_cond(self, test_dict):
        """Conductor Schematics"""
        file_name = type(test_dict["test_obj"]).__name__ + ".png"
        file_path = join(SCHEMATICS_PATH, file_name)
        # Delete previous plot
        if isfile(file_path):
            remove(file_path)
        # Plot / Save schematics
        test_obj = test_dict["test_obj"]
        test_obj.plot_schematics(
            is_default=True,
            is_add_schematics=True,
            is_add_main_line=True,
            save_path=file_path,
            is_show_fig=False,
        )
        file_name_single = type(test_dict["test_obj"]).__name__ + "_single.png"
        file_path_single = join(SCHEMATICS_PATH, file_name_single)
        # Delete previous plot
        if isfile(file_path_single):
            remove(file_path_single)
        test_obj.plot_schematics(
            is_default=True,
            is_add_schematics=True,
            is_add_main_line=True,
            save_path=file_path_single,
            is_show_fig=False,
            is_single=True,
        )
