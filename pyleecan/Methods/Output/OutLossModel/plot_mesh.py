def plot_mesh(self, group_names=None):
    """Plot the losses on the mesh solution

    Parameters
    ----------
    self : OutLossModel
        An OutLossModel object
    group_names : list
        a list of str corresponding to group name(s)

    """

    self.get_mesh_solution().plot_contour(
        "freqs=sum",
        label=self.name + " loss density [W/m^3]",
        group_names=group_names,
    )
