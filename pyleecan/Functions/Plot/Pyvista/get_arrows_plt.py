from numpy import real, max as np_max, abs as np_abs, hstack, zeros


def get_arrows_plt(mesh_pv, field, meshsol, factor, is_point_arrow, phase=1):
    """Create a pyvista arrow plot

    Parameters
    ----------
    args : tuple
        argument for extracting field
    data_list : Data or [Data]
        Data object or list to plot
    save_path : str
        path where to save the gif
    file_name : str
        name of the gif file
    index_var : str
        name of the plot parameter along which to animate
    index_max : int
        maximum value of the index
    index_step : int
        step for the index (number of frames = index_max / index_step)
    component_list : list
        list of component names to plot in separate figures
    kwargs : dict
        parameters of func
    """

    vect_field = real(field * phase)

    # Compute factor
    if factor is None:
        factor = 0.2 * np_max(np_abs(mesh_pv.bounds)) / np_max(np_abs(vect_field))

    # Add third dimension if needed
    solution = meshsol.get_solution()
    if solution.dimension == 2:
        vect_field = hstack((vect_field, zeros((vect_field.shape[0], 1))))

    # Add field to mesh
    if is_point_arrow:
        mesh_pv.vectors = vect_field * factor
        arrows_plt = mesh_pv.arrows
    else:
        mesh_pv["field"] = vect_field
        mesh_cell = mesh_pv.point_data_to_cell_data()
        surf = mesh_cell.extract_geometry()
        centers2 = surf.cell_centers()
        centers2.vectors = surf["field"] * factor
        arrows_plt = centers2.arrows

    return arrows_plt, factor
