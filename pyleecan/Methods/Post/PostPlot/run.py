def run(self, output):
    """Execute the plot contained in the PostPlot object and save it to save_path

    Parameters
    ----------
    self : PostPlot
        A PostPlot object
    output : Output
        an Output object

    """

    # Find object which contains the plot method if attribute is not None
    obj = output
    if self.attribute is not None:
        names = self.attribute.split(".")
        for i in range(len(names)):
            obj = getattr(obj, names[i])

    # Getting the name of the plot method of the output or the object given by attribute
    plot_method = getattr(obj, self.module_plot)

    # Get path of results folder in the Output
    result_path = output.get_path_result()

    # Check in case format begins with a "."
    if self.save_format[0] == ".":
        str_format = self.save_format
    else:
        str_format = "." + self.save_format

    # Build save_path of the picture
    save_path = result_path + "/" + self.name + str_format

    # Execute plot method
    plot_method(**self.parameters, is_show_plot=self.is_show_plot, save_path=save_path)
