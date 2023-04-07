import matplotlib.pyplot as plt
from numpy import min as np_min, max as np_max

from SciDataTool.GUI.DDataPlotter.DDataPlotter import DDataPlotter
from SciDataTool.Functions import parser

from ....Functions.Plot import dict_2D, TEXT_BOX
from ....definitions import config_dict, RES_PATH
from ....Functions.Plot.set_plot_gui_icon import set_plot_gui_icon

PHASE_COLORS = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"]


def plot_mmf_unit(self, is_create_appli=True, save_path=None, is_show_fig=False):
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
    qs = self.winding.qs
    p = self.get_pole_pair_number()
    MMF_U, WF = self.comp_mmf_unit(Nt=100, Na=400 * p)

    color_list = PHASE_COLORS[:qs]

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
            is_show_fig=is_show_fig,
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
        axes_request_list = parser.read_input_strings(
            ["angle{°}", "phase[]"], axis_data={}
        )
        plt.rcParams.update(
            {
                "font.family": config_dict["PLOT"]["FONT_NAME"],
                "font.size": config_dict["PLOT"]["FONT_SIZE_LEGEND"],
            }
        )
        wid = DDataPlotter(
            data=WF,
            axes_request_list=axes_request_list,
            unit="A",
            z_min=np_min(MMF_U.values) * 1.1,
            z_max=np_max(MMF_U.values) * 1.1,
            plot_arg_dict=plot_arg_dict,
            path_to_image=RES_PATH,
            text_box=TEXT_BOX,
            frozen_type=2,
        )
        wid.setWindowTitle(name + "Phase MMF plot")
        set_plot_gui_icon()
        # Change default file name
        wid.canvas.get_default_filename = (
            lambda: wid.windowTitle().replace(" ", "_").replace(":", "") + ".png"
        )
        wid.show()
        return wid
