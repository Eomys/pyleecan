import matplotlib.pyplot as plt
from numpy import min as np_min, max as np_max

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ....Functions.Plot.set_plot_gui_icon import set_plot_gui_icon
from ....Functions.Plot import dict_2D
from ....definitions import config_dict


def plot_mmf_unit(self, is_create_appli=True, save_path=None):
    """Plot the winding unit mmf as a function of space
    Parameters
    ----------

    self : LamSlotWind
        an LamSlotWind object
    is_create_appli : bool
        True to create an QApplication (required if not already created by another GUI)
    """

    name = ""
    if self.parent is not None and self.parent.name not in [None, ""]:
        name += self.parent.name + " "
    if self.is_stator:
        name += "Stator "
    else:
        name += "Rotor "

    # Compute the winding function and mmf
    wf = self.comp_wind_function(per_a=1)
    qs = self.winding.qs
    MMF_U, WF = self.comp_mmf_unit(Nt=1, Na=wf.shape[1])

    color_list = config_dict["PLOT"]["COLOR_DICT"]["COLOR_LIST"][:qs]

    plot_arg_dict = dict_2D.copy()
    plot_arg_dict["color_list"] = color_list + ["k"]
    plot_arg_dict["data_list"] = [MMF_U]

    if save_path is not None:
        WF.plot_2D_Data(
            "angle{°}",
            "phase[]",
            unit="A",
            y_min=np_min(MMF_U.values) * 1.1,
            y_max=np_max(MMF_U.values) * 1.1,
            is_show_fig=False,
            save_path=save_path,
            **plot_arg_dict,
        )

    elif is_create_appli:
        WF.plot(
            "angle{°}",
            "phase[]",
            unit="A",
            z_min=np_min(MMF_U.values) * 1.1,
            z_max=np_max(MMF_U.values) * 1.1,
            plot_arg_dict=plot_arg_dict,
            is_create_appli=is_create_appli,
            frozen_type=2,
        )
    else:
        wid = WF.plot(
            "angle{°}",
            "phase[]",
            unit="A",
            z_min=np_min(MMF_U.values) * 1.1,
            z_max=np_max(MMF_U.values) * 1.1,
            plot_arg_dict=plot_arg_dict,
            is_create_appli=is_create_appli,
            frozen_type=2,
        )

        wid.setWindowTitle(name + "Phase MMF plot")
        set_plot_gui_icon()
        # Change default file name
        wid.canvas.get_default_filename = (
            lambda: wid.windowTitle().replace(" ", "_").replace(":", "") + ".png"
        )
        return wid
