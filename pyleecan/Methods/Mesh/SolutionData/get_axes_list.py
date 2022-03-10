def get_axes_list(self, *args):
    """Get the axis of variables stored in Solution.

    Parameters
    ----------
    self : SolutionData
        an SolutionData object
    args : list
        list of SciDataTool arguments

    Returns
    -------
    field: array
        an array of field values

    """

    # Build axis list
    ax_name = list()
    ax_size = list()

    axes = self.field.get_axes()

    ax_name_orig = [axis.name for axis in axes]

    if len(args) == 0:
        for axis in axes:
            ax_name.append(axis.name)
            ax_size.append(axis.get_length())
    else:
        for arg in args:
            # TODO: fill missing SciDataTool syntax to return proper axis size
            if "[" in arg:
                # Periodicities / slicing
                arg_split = arg.split("[")
                ax_name.append(arg_split[0])
                ind_ax = ax_name_orig.index(ax_name[-1])
                if "smallest" in arg_split[1]:
                    ax_size.append(axes[ind_ax].get_length(is_smallestperiod=True))
                elif "one" in arg_split[1]:
                    ax_size.append(axes[ind_ax].get_length(is_oneperiod=True))
                elif "anti" in arg_split[1]:
                    ax_size.append(axes[ind_ax].get_length(is_antiperiod=True))
                else:
                    ax_size.append(len(eval(arg.split(ax_name[-1])[-1])))
            elif "=" in arg:
                # ignore axis
                pass
            elif "freqs" in arg and "time" in ax_name_orig:
                # FFT
                ax_name.append("freqs")
                ind_ax = ax_name_orig.index("time")
                Nt_per = axes[ind_ax].get_length(is_oneperiod=True)
                if Nt_per % 2 == 0:
                    Nfreq = int(Nt_per / 2) + 1
                else:
                    Nfreq = int((Nt_per - 1) / 2)
                ax_size.append(Nfreq)
            else:
                # No operation requested
                ax_name.append(arg)
                ind_ax = ax_name_orig.index(ax_name[-1])
                ax_size.append(axes[ind_ax].get_length())

    return ax_name, ax_size
