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
from pyleecan.Classes.SlotM19 import SlotM19

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
from pyleecan.Classes.HoleM52R import HoleM52R
from pyleecan.Classes.HoleM53 import HoleM53
from pyleecan.Classes.HoleM54 import HoleM54
from pyleecan.Classes.HoleM57 import HoleM57
from pyleecan.Classes.HoleM58 import HoleM58
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.VentilationTrap import VentilationTrap
from pyleecan.Classes.HoleMLSRPM import HoleMLSRPM
from pyleecan.Classes.BoreFlower import BoreFlower
from pyleecan.Classes.BoreSinePole import BoreSinePole
from pyleecan.Classes.HoleM60 import HoleM60
from pyleecan.Classes.HoleM61 import HoleM61
from Tests import SCHEMATICS_PATH
from os.path import join, isdir, isfile
from os import makedirs, remove

if not isdir(SCHEMATICS_PATH):
    makedirs(SCHEMATICS_PATH)

slot_test = list()

SlotM_list = [
    SlotM12(),
    SlotM13(),
    SlotM14(),
    SlotM15(),
    SlotM16(),
    SlotM17(),
    SlotM18(),
]

SlotW_list = [
    SlotW10(),
    SlotW11(),
    SlotW12(),
    SlotW13(),
    SlotW14(),
    SlotW15(),
    SlotW16(),
    SlotW21(),
    SlotW22(),
    SlotW23(),
    SlotW24(),
    SlotW25(),
    SlotW26(),
    SlotW27(),
    SlotW28(),
    SlotW29(),
    SlotW60(),
    SlotW61(),
    SlotWLSRPM(),
]

Hole_list = [
    HoleM50(),
    HoleM51(),
    HoleM52(),
    HoleM52R(),
    HoleM53(),
    HoleM54(),
    HoleM57(),
    HoleM58(),
    HoleM54(),
    HoleMLSRPM(),
    VentilationCirc(),
    VentilationPolar(),
    HoleM60(),
    HoleM61(),
]


for slot in SlotM_list:
    slot_test.append(
        {
            "test_obj": slot,
            "type_add_active": 2,
        }
    )


slot_test.append(
    {
        "test_obj": SlotCirc(),
        "type_add_active": 0,
        "is_default": 2,
    }
)

slot_test.append(
    {
        "test_obj": SlotM10(),
        "type_add_active": 2,
        "is_default": 2,
    }
)
slot_test.append(
    {
        "test_obj": SlotM11(),
        "type_add_active": 2,
        "is_default": 2,
    }
)

slot_test.append(
    {
        "test_obj": SlotM19(),
        "type_add_active": 2,
        "is_default": 2,
    }
)

for slot in SlotW_list:
    slot_test.append(
        {
            "test_obj": slot,
            "type_add_active": 1,
        }
    )

slot_test.append(
    {
        "test_obj": SlotW10(),
        "type_add_active": 1,
    }
)

slot_test.append(
    {
        "test_obj": SlotW11(),
        "type_add_active": 1,
        "method_name": "plot_schematics_constant_tooth",
    }
)
slot_test.append(
    {
        "test_obj": SlotW14(),
        "type_add_active": 4,
    }
)

slot_test.append(
    {
        "test_obj": SlotW23(),
        "type_add_active": 1,
        "method_name": "plot_schematics_constant_tooth",
    }
)

slot_test.append(
    {
        "test_obj": SlotW29(),
        "type_add_active": 4,
    }
)


hole_test = list()
for hole in Hole_list:
    hole_test.append(
        {
            "test_obj": hole,
            "type_add_active": 1,
        }
    )


slot_test.extend(hole_test)


# python -m pytest ./Tests/Plot/Schematics/test_plot_schematics.py
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
            is_show_fig=False,
        )
        pass

    def test_BoreSinePole(self):
        """Bore Flower schematics"""
        file_name = "BoreSinePole.png"
        file_path = join(SCHEMATICS_PATH, file_name)
        # Delete previous plot
        if isfile(file_path):
            remove(file_path)
        # Plot / Save schematics
        test_obj = BoreSinePole()
        test_obj.plot_schematics(
            is_default=True,
            is_add_schematics=True,
            is_add_main_line=True,
            save_path=file_path,
            is_show_fig=False,
        )
        pass

    @pytest.mark.parametrize("test_dict", slot_test)
    def name(self, test_dict):
        test_obj = test_dict["test_obj"]
        type_active = test_dict["type_add_active"]

        # Get plot_method
        if "method_name" in test_dict:
            plot_meth = getattr(test_obj, test_dict["method_name"])
        else:
            plot_meth = getattr(test_obj, "plot_schematics")

        if "is_default" in test_dict and test_dict["is_default"] != 1:
            value = plot_meth(
                is_return_default=True,
                is_default=2,
            )
            type_active = 0

        else:
            value = plot_meth(
                is_return_default=True,
                is_default=True,
            )

        schematics_name = type(test_dict["test_obj"]).__name__

        if type_active == 0:
            file_name = schematics_name + "_empty"

        elif type_active == 1:
            file_name = schematics_name + "_wind"

        elif type_active == 2:
            file_name = schematics_name + "_mag"

        elif type_active == 3:
            file_name = schematics_name + "_wedge_full"

        elif type_active == 4:
            file_name = schematics_name + "_wedge_type_1"

        if value.is_internal == True:
            file_name = file_name + "_int"

        else:
            file_name = file_name + "_ext"

        if value.is_stator == True:
            file_name = file_name + "_stator"

        else:
            file_name = file_name + "_rotor"

        if (
            "method_name" in test_dict
            and test_dict["method_name"] == "plot_schematics_constant_tooth"
        ):
            file_name = file_name + "_constant_tooth"

        if (
            "method_name" in test_dict
            and test_dict["method_name"] == "plot_schematics_radial"
        ):
            file_name = file_name + "_radial"

        file_name = file_name + ".png"
        return file_name

    @pytest.mark.parametrize("test_dict", slot_test)
    def test_slot(self, test_dict):
        """Slot Schematics"""
        test_obj = test_dict["test_obj"]
        file_name = self.name(test_dict)
        file_path = join(SCHEMATICS_PATH, file_name)
        # Delete previous plot
        if isfile(file_path):
            remove(file_path)
        # Plot / Save schematics
        print("Generating " + file_name)

        # Get plot_method
        if "method_name" in test_dict:
            plot_meth = getattr(test_obj, test_dict["method_name"])
        else:
            plot_meth = getattr(test_obj, "plot_schematics")

        if "is_default" in test_dict and test_dict["is_default"] != 1:
            plot_meth(
                is_default=2,
                is_add_point_label=False,
                is_add_schematics=True,
                is_add_main_line=True,
                type_add_active=0,
                save_path=file_path,
                is_show_fig=False,
            )
            test_dict["is_default"] = True
            self.test_slot(test_dict)

        else:
            if test_dict["type_add_active"] == 1:
                ## Wind only
                plot_meth(
                    is_default=True,
                    is_add_point_label=False,
                    is_add_schematics=True,
                    is_add_main_line=True,
                    type_add_active=1,
                    save_path=file_path,
                    is_show_fig=False,
                )
                test_dict["type_add_active"] = 3
                file_name = self.name(test_dict)
                file_path = join(SCHEMATICS_PATH, file_name)

            if test_dict["type_add_active"] == 2:
                ## Magnet only
                plot_meth(
                    is_default=True,
                    is_add_point_label=False,
                    is_add_schematics=True,
                    is_add_main_line=True,
                    type_add_active=2,
                    save_path=file_path,
                    is_show_fig=False,
                )

            if test_dict["type_add_active"] == 3:
                ## Wind and Wedge
                plot_meth(
                    is_default=True,
                    is_add_point_label=False,
                    is_add_schematics=True,
                    is_add_main_line=True,
                    type_add_active=3,
                    save_path=file_path,
                    is_show_fig=False,
                )

            if test_dict["type_add_active"] == 4:
                ## wedge_type
                plot_meth(
                    is_default=True,
                    is_add_point_label=False,
                    is_add_schematics=True,
                    is_add_main_line=True,
                    type_add_active=4,
                    save_path=file_path,
                    is_show_fig=False,
                )

            # Empty
            test_dict["type_add_active"] = 0
            file_name = self.name(test_dict)
            file_path = join(SCHEMATICS_PATH, file_name)
            # Delete previous plot
            if isfile(file_path):
                remove(file_path)
            # Plot / Save schematics
            print("Generating " + file_name)
            plot_meth(
                is_default=True,
                is_add_point_label=False,
                is_add_schematics=True,
                is_add_main_line=True,
                type_add_active=0,
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

    def test_slotCirc_old(self):
        """Slot Schematics for SlotCirc, old H0 definition"""
        ## Empty
        test_obj = SlotCirc()
        file_name = "SlotCirc_empty_int_rot_old.png"
        file_path = join(SCHEMATICS_PATH, file_name)
        # Delete previous plot
        if isfile(file_path):
            remove(file_path)
        # Plot / Save schematics
        print("Generating " + file_name)
        test_obj.plot_schematics(
            is_default=True,
            is_add_point_label=False,
            is_add_schematics=True,
            is_add_main_line=True,
            is_enforce_default_H0_bore=False,
            type_add_active=0,
            save_path=file_path,
            is_show_fig=False,
        )
        # Ext stator
        file_name = "SlotCirc_empty_ext_sta_old.png"
        file_path = join(SCHEMATICS_PATH, file_name)
        # Delete previous plot
        if isfile(file_path):
            remove(file_path)
        # Plot / Save schematics
        print("Generating " + file_name)
        test_obj.plot_schematics(
            is_default=2,
            is_add_point_label=False,
            is_add_schematics=True,
            is_add_main_line=True,
            is_enforce_default_H0_bore=False,
            type_add_active=0,
            save_path=file_path,
            is_show_fig=False,
        )


if __name__ == "__main__":
    a = Test_plot_schematics()
    # a.test_BoreFlower()
    # a.test_BoreSinePole()
    # a.test_slot(slot_test[47])
    # a.test_slot_point(slot_test[47])
    # a.test_slot(slot_test[13])
    #

    for slot in slot_test:
        a.test_slot(slot)
        a.test_slot_point(slot)
    #
    #
    # print("Done")
