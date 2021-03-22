from inspect import signature
from os.path import join

from ....Functions.Plot import dict_2D, dict_3D


def run(self, output):
    """Execute the plot contained in the PostPlot object and save it to save_path

    Parameters
    ----------
    self : PostPlot
        A PostPlot object
    output : Output
        an Output object

    """

    output.get_logger().info("Running Post-processing: " + self.name)
    try:
        if self.quantity is not None:
            obj = output.get_data_from_str(self.quantity)
        else:
            obj = output

        # Get plot method
        plot_method = getattr(obj, self.method)

        # Path to save the figure if save_path is not already in param_dict and is an argument of the plot method
        if "save_path" not in self.param_dict and "save_path" in str(
            signature(plot_method)
        ):
            # Get path of results folder in the Output
            result_path = output.get_path_result()

            # Check in case format begins with a "."
            if self.save_format[0] == ".":
                str_format = self.save_format
            else:
                str_format = "." + self.save_format

            # Build save_path of the picture
            self.param_dict["save_path"] = join(result_path, self.name + str_format)
        # Disabling the display of the figure when plotting
        if "is_show_fig" not in self.param_dict:
            self.param_dict["is_show_fig"] = False
        # Add window title
        self.param_dict["win_title"] = self.name
        # Adding colors and fonts
        if self.method == "plot_2D_Data":
            self.param_dict = dict(self.param_dict, **dict_2D)
            self.param_dict["fund_harm_dict"] = output.get_fund_harm(obj)
        elif self.method == "plot_3D_Data":
            self.param_dict = dict(self.param_dict, **dict_3D)

        # Execute plot method
        plot_method(
            *self.param_list,
            **self.param_dict,
        )

    except Exception as e:
        output.get_logger().error(
            "Error while running Post-processing: " + self.name + "\n" + str(e)
        )
