from inspect import signature
from os.path import join


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
    list_names = self.method.split(".")

    try:
        if len(list_names) == 1:
            # Getting the name of the plot method of the output or the object given by attribute
            plot_method = getattr(output, self.method)
        else:
            # Find object which contains the plot method if attribute is not None
            obj = output

            # Get successive objects to reach the one containing the method
            for i in range(len(list_names) - 1):
                if "get_" in list_names[i]:
                    obj = getattr(obj, list_names[i])()
                else:
                    obj = getattr(obj, list_names[i])

            # Getting the name of the plot method of the output or the object given by attribute
            plot_method = getattr(obj, list_names[-1])

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

        # Execute plot method
        plot_method(
            *self.param_list,
            **self.param_dict,
        )
    except Exception as e:
        output.get_logger().error(
            "Error while running Post-processing: " + self.name + "\n" + str(e)
        )
