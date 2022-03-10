from numpy import sqrt

from SciDataTool import DataTime


def get_fft_from_meshsol(self, group, label):
    """Get fft of the magnetic quantity given by label and associated mesh element surfaces
    for requested group mesh

    Parameters
    ----------
    self: OutMag
        an OutMag object
    group: str
        Name of the group that must be a key of self.meshsolution.group dictionnary
    label: str
        "B" to calculate fft of magnetic flux density
        "A_z" to calculate fft of magnetic vector potential

    Returns
    -------
    val_fft: ndarray
        FFT values for requested quantity (Nfreq, Nelem)
    Se: ndarray
        Element surface (Nelem,) [m^2]
    """

    if self.meshsolution is None:
        raise Exception("Cannot calculate fft from meshsolutionis meshsolution is None")
    else:
        meshsol = self.meshsolution

    group_list = list(meshsol.group.keys())

    if group not in group_list:
        raise Exception("Cannot calculate fft from meshsolution for group=" + group)

    if label not in ["A_z", "B"]:
        raise Exception(
            "Cannot calculate fft from meshsolution if label is not 'B' ot 'A_z'"
        )

    ms_group = meshsol.get_group(group)

    Se = ms_group.mesh[0].get_cell_area()

    if label == "B":

        Bvect = ms_group.get_solution(label=label)

        Bval = sqrt(
            Bvect.field.components["comp_x"].values ** 2
            + Bvect.field.components["comp_y"].values ** 2
        )

        axes_list = Bvect.field.get_axes()

        if "antiperiod" in axes_list[0].symmetries:
            axes_list[0].symmetries = {"period": axes_list[0].symmetries["antiperiod"]}

        Bamp_dt = DataTime(
            name=group + " flux density magnitude",
            symbol=label,
            unit="T",
            axes=axes_list,
            values=Bval,
        )

        val_fft = Bamp_dt.get_along("freqs", "indice", "z[0]")[label]

    elif label == "A_z":

        label_list = [sol.label for sol in meshsol.solution]

        ind = label_list.index(label)

        Time = ms_group.solution[ind].field.axes[0]
        if "antiperiod" in Time.symmetries:
            Time.symmetries = {"period": Time.symmetries["antiperiod"]}

        val_fft = ms_group.get_field("freqs", "indice", index=ind, is_center=True)

    return val_fft, Se
