def plot_mesh(self, group_names=None):
    """Plot the losses on the mesh solution

    Parameters
    ----------
    self : OutLossModel
        An OutLossModel object
    group_names : list
        a list of str corresponding to group name(s)

    """

    return (
        self.get_mesh_solution()
        .get_group(group_names)
        .plot_contour(
            "freqs=sum",
            label=f"{self.name} loss density",
        )
    )
