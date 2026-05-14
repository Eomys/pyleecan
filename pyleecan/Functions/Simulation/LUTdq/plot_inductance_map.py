from os import makedirs
from os.path import abspath, exists, join


def plot_inductance_map(
    result, save_dir, file_prefix="inductance_map", is_show_fig=False
):
    """Generate standard dq inductance-map figures and save them to disk."""

    from ....Functions.Plot.plot_3D import plot_3D

    save_dir = abspath(save_dir)
    if not exists(save_dir):
        makedirs(save_dir)

    paths = {
        "Ld_map": join(save_dir, file_prefix + "_Ld_map.png"),
        "Lq_map": join(save_dir, file_prefix + "_Lq_map.png"),
        "Phid_map": join(save_dir, file_prefix + "_Phid_map.png"),
        "Phiq_map": join(save_dir, file_prefix + "_Phiq_map.png"),
    }

    common_args = {
        "Xdata": result["Id_grid"],
        "Ydata": result["Iq_grid"],
        "xlabel": "Id [Arms]",
        "ylabel": "Iq [Arms]",
        "type_plot": "pcolormesh",
        "is_show_fig": is_show_fig,
    }

    plot_3D(
        Zdata=result["Ld"],
        zlabel="Ld [H]",
        title="d-axis Inductance Map",
        save_path=paths["Ld_map"],
        **common_args,
    )

    plot_3D(
        Zdata=result["Lq"],
        zlabel="Lq [H]",
        title="q-axis Inductance Map",
        save_path=paths["Lq_map"],
        **common_args,
    )

    plot_3D(
        Zdata=result["Phid"],
        zlabel="Phid [Wb]",
        title="d-axis Flux Map",
        save_path=paths["Phid_map"],
        **common_args,
    )

    plot_3D(
        Zdata=result["Phiq"],
        zlabel="Phiq [Wb]",
        title="q-axis Flux Map",
        save_path=paths["Phiq_map"],
        **common_args,
    )

    return paths
