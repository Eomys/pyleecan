import pytest
from pyleecan.Classes.SlotCirc import SlotCirc
from pyleecan.Classes.SlotM10 import SlotM10
from pyleecan.Classes.SlotM11 import SlotM11
from pyleecan.Classes.SlotM12 import SlotM12
from pyleecan.Classes.SlotM13 import SlotM13
from pyleecan.Classes.SlotM14 import SlotM14
from pyleecan.Classes.SlotM15 import SlotM15
from pyleecan.Classes.SlotM16 import SlotM16
from pyleecan.Classes.SlotM17 import SlotM17
from pyleecan.Classes.SlotM18 import SlotM18

from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Classes.SlotW12 import SlotW12
from pyleecan.Classes.SlotW13 import SlotW13
from pyleecan.Classes.SlotW14 import SlotW14
from pyleecan.Classes.SlotW15 import SlotW15
from pyleecan.Classes.SlotW16 import SlotW16
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.Classes.SlotW23 import SlotW23
from pyleecan.Classes.SlotW24 import SlotW24
from pyleecan.Classes.SlotW25 import SlotW25
from pyleecan.Classes.SlotW26 import SlotW26
from pyleecan.Classes.SlotW27 import SlotW27
from pyleecan.Classes.SlotW28 import SlotW28
from pyleecan.Classes.SlotW29 import SlotW29
from pyleecan.Classes.SlotW60 import SlotW60
from pyleecan.Classes.SlotW61 import SlotW61
from pyleecan.Classes.SlotWLSRPM import SlotWLSRPM

from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.HoleM51 import HoleM51
from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.Classes.HoleM53 import HoleM53
from pyleecan.Classes.HoleM54 import HoleM54
from pyleecan.Classes.HoleM57 import HoleM57
from pyleecan.Classes.HoleM58 import HoleM58
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.VentilationTrap import VentilationTrap
from pyleecan.Classes.HoleMLSRPM import HoleMLSRPM
from pyleecan.Classes.BoreFlower import BoreFlower
from Tests import SCHEMATICS_PATH
from os.path import join, isdir, isfile
from os import makedirs, remove

if not isdir(SCHEMATICS_PATH):
    makedirs(SCHEMATICS_PATH)

slot_test = list()

slot_test.append(
    {"test_obj": SlotCirc(), "type_add_active": 0, "is_default": 2,}
)

slot_test.append(
    {"test_obj": SlotM10(), "type_add_active": 2, "is_default": 2,}
)
slot_test.append(
    {"test_obj": SlotM11(), "type_add_active": 2, "is_default": 2,}
)
slot_test.append(
    {"test_obj": SlotM12(), "type_add_active": 2,}
)
slot_test.append(
    {"test_obj": SlotM13(), "type_add_active": 2,}
)
slot_test.append(
    {"test_obj": SlotM14(), "type_add_active": 2,}
)
slot_test.append(
    {"test_obj": SlotM15(), "type_add_active": 2,}
)
slot_test.append(
    {"test_obj": SlotM16(), "type_add_active": 2,}
)
slot_test.append(
    {"test_obj": SlotM17(), "type_add_active": 2,}
)
slot_test.append(
    {"test_obj": SlotM18(), "type_add_active": 2,}
)

slot_test.append(
    {"test_obj": SlotW10(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW11(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW12(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW13(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW14(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW15(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW16(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW21(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW22(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW23(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW24(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW25(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW26(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW27(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW28(), "type_add_active": 1,}
)
slot_test.append(
    {"test_obj": SlotW29(), "type_add_active": 1,}
)
slot_test.append(
    {
        "test_obj": SlotW60(),
        "type_add_active": 1,
    }
)

slot_test.append(
    {
        "test_obj": SlotW61(),
        "type_add_active": 1,
    }
)

slot_test.append(
    {
        "test_obj": SlotWLSRPM(),
        "type_add_active": 1,
    }
)

hole_test = list()
hole_test.append(
    {"test_obj": HoleM50(), "type_add_active": 2,}
)
hole_test.append(
    {"test_obj": HoleM51(), "type_add_active": 2,}
)
hole_test.append(
    {"test_obj": HoleM52(), "type_add_active": 2,}
)
hole_test.append(
    {"test_obj": HoleM53(), "type_add_active": 2,}
)
hole_test.append(
    {"test_obj": HoleM54(), "type_add_active": 2,}
)
hole_test.append(
    {"test_obj": HoleM57(), "type_add_active": 2,}
)
hole_test.append(
    {"test_obj": HoleM58(), "type_add_active": 2,}
)
hole_test.append(
    {"test_obj": HoleMLSRPM(), "type_add_active": 2,}
)
hole_test.append(
    {"test_obj": VentilationCirc(), "type_add_active": 2,}
)
hole_test.append(
    {"test_obj": VentilationPolar(), "type_add_active": 2,}
)
hole_test.append(
    {"test_obj": VentilationTrap(), "type_add_active": 2,}
)
slot_test.extend(hole_test)


class Test_plot_schematics(object):

    def test_BoreFlower(self):
        """Bore Flower schematics"""
        file_name = "BoreFlower.png"
        file_path = join(SCHEMATICS_PATH, file_name)
        # Delete previous plot
        if isfile(file_path):
            remove(file_path)
        # Plot / Save schematics
        test_obj = BoreFlower()
        test_obj.plot_schematics(
            is_default=True,
            is_add_schematics=True,
            is_add_main_line=True,
            save_path=file_path,
            is_show_fig=True,
        )
        pass

    @pytest.mark.parametrize("test_dict", hole_test)
    def test_hole_no_mag(self, test_dict):
        """Slot Schematics"""
        file_name = type(test_dict["test_obj"]).__name__ + "_no_mag.png"
        file_path = join(SCHEMATICS_PATH, file_name)
        # Delete previous plot
        if isfile(file_path):
            remove(file_path)
        # Plot / Save schematics
        test_obj = test_dict["test_obj"]
        test_obj.plot_schematics(
            is_default=True,
            is_add_point_label=False,
            is_add_schematics=True,
            is_add_main_line=True,
            type_add_active=0,
            save_path=file_path,
            is_show_fig=False,
        )

    @pytest.mark.parametrize("test_dict", slot_test)
    def test_slot(self, test_dict):
        """Slot Schematics"""
        ## Empty
        if "is_default" in test_dict:
            file_name = type(test_dict["test_obj"]).__name__ + "_empty_int_rot.png"
        else:
            file_name = type(test_dict["test_obj"]).__name__ + "_empty.png"
        file_path = join(SCHEMATICS_PATH, file_name)
        # Delete previous plot
        if isfile(file_path):
            remove(file_path)
        # Plot / Save schematics
        print("Generating " + file_name)
        test_obj = test_dict["test_obj"]
        test_obj.plot_schematics(
            is_default=True,
            is_add_point_label=False,
            is_add_schematics=True,
            is_add_main_line=True,
            type_add_active=0,
            save_path=file_path,
            is_show_fig=False,
        )
        if "is_default" in test_dict:
            if test_dict["is_default"] == 2:  # External schematics
                file_name = type(test_dict["test_obj"]).__name__ + "_empty_ext_sta.png"
            else:
                file_name = (
                    type(test_dict["test_obj"]).__name__
                    + "_empty_"
                    + str(test_dict["is_default"])
                    + ".png"
                )
            file_path = join(SCHEMATICS_PATH, file_name)
            # Delete previous plot
            if isfile(file_path):
                remove(file_path)
            print("Generating " + file_name)
            test_obj = test_dict["test_obj"]
            test_obj.plot_schematics(
                is_default=test_dict["is_default"],
                is_add_point_label=False,
                is_add_schematics=True,
                is_add_main_line=True,
                type_add_active=0,
                save_path=file_path,
                is_show_fig=False,
            )
        if test_dict["type_add_active"] == 1:
            ## Wind only
            file_name = type(test_dict["test_obj"]).__name__ + "_wind.png"
            file_path = join(SCHEMATICS_PATH, file_name)
            # Delete previous plot
            if isfile(file_path):
                remove(file_path)
            # Plot / Save schematics
            print("Generating " + file_name)
            test_obj = test_dict["test_obj"]
            test_obj.plot_schematics(
                is_default=True,
                is_add_point_label=False,
                is_add_schematics=True,
                is_add_main_line=True,
                type_add_active=1,
                save_path=file_path,
                is_show_fig=False,
            )
            ## Wind and Wedge
            file_name = type(test_dict["test_obj"]).__name__ + "_wedge_full.png"
            file_path = join(SCHEMATICS_PATH, file_name)
            # Delete previous plot
            if isfile(file_path):
                remove(file_path)
            # Plot / Save schematics
            print("Generating " + file_name)
            test_obj = test_dict["test_obj"]
            test_obj.plot_schematics(
                is_default=True,
                is_add_point_label=False,
                is_add_schematics=True,
                is_add_main_line=True,
                type_add_active=3,
                save_path=file_path,
                is_show_fig=False,
            )
        elif test_dict["type_add_active"] == 2:
            ## Magnet only
            file_name = type(test_dict["test_obj"]).__name__ + "_mag.png"
            file_path = join(SCHEMATICS_PATH, file_name)
            # Delete previous plot
            if isfile(file_path):
                remove(file_path)
            # Plot / Save
            print("Generating " + file_name)
            test_obj = test_dict["test_obj"]
            test_obj.plot_schematics(
                is_default=True,
                is_add_point_label=False,
                is_add_schematics=True,
                is_add_main_line=True,
                type_add_active=2,
                save_path=file_path,
                is_show_fig=False,
            )

    @pytest.mark.parametrize("test_dict", slot_test)
    def test_slot_point(self, test_dict):
        """Slot Schematics"""
        file_name = type(test_dict["test_obj"]).__name__ + "_point.png"
        file_path = join(SCHEMATICS_PATH, file_name)
        # Delete previous plot
        if isfile(file_path):
            remove(file_path)
        # Plot / Save schematics
        test_obj = test_dict["test_obj"]
        test_obj.plot_schematics(
            is_default=True,
            is_add_point_label=True,
            is_add_schematics=False,
            is_add_main_line=True,
            type_add_active=test_dict["type_add_active"],
            save_path=file_path,
            is_show_fig=False,
        )


if __name__ == "__main__":
    a = Test_plot_schematics()
    a.test_BoreFlower()
    # a.test_slot(slot_test[26])
    # a.test_slot_point(slot_test[-1])
    # for slot in slot_test:
    #     a.test_slot(slot)
    #     a.test_slot_point(slot)
    print("Done")
