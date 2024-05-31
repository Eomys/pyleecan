# -*- coding: utf-8 -*-

from ....Classes.SolutionVector import SolutionVector
from ....Classes.MeshMat import MeshMat
from ....Classes.MeshVTK import MeshVTK
from ....Functions.Structural.conversions import DimError, cart2pol, pol2cart
from numpy import (
    einsum,
    sqrt,
    zeros,
    squeeze,
    real,
    imag,
    sum as np_sum,
    abs as np_abs,
    swapaxes,
    reshape,
)


def get_field(
    self,
    *args_list,
    label=None,
    indices=None,
    is_rthetaz=False,
    is_pol2cart=False,
    is_radial=False,
    is_normal=False,
    is_rms=False,
    is_center=False,
    is_surf=False,
    is_squeeze=True,
):
    """Return the solution corresponding to a label.

    Parameters
    ----------
    self : MeshSolution
        an MeshSolution object
    *args_list: list of strings
        List of axes requested by the user, their units and values (optional)
    label : str
        label of the solution
    indices : list
        list of indices to extract from mesh and field
    is_rthetaz : bool
        cylindrical coordinates
    is_radial : bool
        radial component only
    is_normal : bool
        normal component only (on nodes or centers)
    is_rms : bool
        rms over surface sum((F.n)**2 dS)/S
    is_center : bool
        field at element centers
    is_surf : bool
        field over outer surface
    is_squeeze : bool
        squeeze the output result

    Returns
    -------
    result : ndarray
        field

    """
    # if len(args_list) == 1 and type(args_list[0]) == tuple:
    #     args_list = args_list[0]  # if called from another script with *arg_list

    # Get field
    solution = self.get_solution(label=label)

    axes_list = solution.get_axes_list(*args_list)
    ax_names = axes_list[0]

    field = solution.get_field(
        *args_list, is_squeeze=False
    )  # Don't use is_squeeze = is_squeeze here!

    if (
        isinstance(solution, SolutionVector)
        and "comp_x" not in solution.field.components
    ):
        is_pol2cart = True

    # Enforce indice from those contained in MeshSolution if not None

    if self.group is not None and "output_nodes" in self.group and indices is None:
        indices_normals = self.group["output_nodes"]
    else:
        indices_normals = indices

    # Check dimensions
    shape = field.shape
    is_other_dim = False

    ## Check the existing axes and put indice and component in first position to ease transformation.
    if axes_list[0] is not None:
        # Swap axis indice position
        if "indice" in axes_list[0]:
            ind_indices0 = axes_list[0].index("indice")
            axes_list[0][0], axes_list[0][ind_indices0] = (
                axes_list[0][ind_indices0],
                axes_list[0][0],
            )  # names swap
            axes_list[1][0], axes_list[1][ind_indices0] = (
                axes_list[1][ind_indices0],
                axes_list[1][0],
            )  # length swap
            field = swapaxes(field, 0, ind_indices0)  # field axis swap
            ind_indices = 0

        else:
            raise Exception(
                "ERROR, MeshSolution axes list should contain 'indice' axis"
            )

        if "component" in axes_list[0]:
            # Index of component axis (degree of freedom)
            ind_component0 = axes_list[0].index("component")
            axes_list[0][1], axes_list[0][ind_component0] = (
                axes_list[0][ind_component0],
                axes_list[0][1],
            )  # names swap
            axes_list[1][1], axes_list[1][ind_component0] = (
                axes_list[1][ind_component0],
                axes_list[1][1],
            )  # length swap
            field = swapaxes(field, 1, ind_component0)  # field axis swap
            ind_component = 1
        else:
            ind_component = None

        # Init list of indices of axes that are not "component", "indice",
        ind_otherdim = [i for i in range(len(axes_list[1]))]
        ind_otherdim.pop(ind_indices)
        if ind_component is not None:
            ind_otherdim.pop(ind_component - 1)

    ## Define the type of transformation
    is_recursive = False  # If there is at least one transformation, switch to true.

    if indices is not None:
        is_recursive = True

    if is_radial:
        is_rthetaz = True
        is_recursive = True

    if is_rms:
        is_center = True
        is_normal = True
        is_recursive = True
    # if is_normal:
    #     is_surf = True
    if is_rthetaz or is_normal:
        if ind_component is None:
            raise DimError("The field should be a vector field")

    # Get mesh if necessary
    if is_center or is_normal or is_rthetaz or is_surf or is_pol2cart:
        is_recursive = True
        # Get the mesh
        mesh = self.mesh
        mesh_pv = mesh.get_mesh_pv(indices=indices_normals)
        if isinstance(mesh, MeshMat):
            mesh = MeshVTK(mesh=mesh_pv, is_pyvista_mesh=True)
    else:
        mesh, mesh_pv = None, None
    # Get nodes coordinates if necessary
    if is_rthetaz or is_pol2cart:
        is_recursive = True
        points = mesh.get_node_coordinate(indices=indices)
    else:
        points = None
    # Get normals if necessary
    if is_normal and is_center:
        is_recursive = True
        # Get normals
        normals = mesh.get_normals(indices=indices_normals)
    elif is_normal:
        is_recursive = True
        normals = mesh.get_normals(indices=indices_normals, loc="point")
    else:
        normals = None
    # Get element area if necessary
    if is_rms:
        cell_area = mesh.get_element_area(indices=indices)
    else:
        cell_area = None

    ## Perform the transformation
    shape_result = axes_list[1]

    if is_recursive:
        if is_center:
            shape_result[ind_indices] = mesh_pv.n_cells
        elif indices_normals is not None:
            shape_result[ind_indices] = len(indices_normals)

        if is_rms:
            shape_result[ind_indices] = 1

        if is_radial or is_rms or is_normal:
            shape_result[ind_component] = 1

        shape_otherdim = [shape_result[ii] for ii in ind_otherdim]

        result = apply_normal_center_surf_vectorfield(
            field,
            ind_otherdim,
            shape_otherdim,
            is_center,
            is_normal,
            is_surf,
            is_rms,
            is_rthetaz,
            is_radial,
            is_pol2cart,
            mesh_pv,
            normals,
            points,
            cell_area,
            shape_result,
            field.dtype,
            indices,
            ind_indices,
        )
    else:
        result = field  # No transformation

    # Reverse axes swaps (to match with get_axes_list)
    if ind_component is not None:
        result = swapaxes(result, 1, ind_component0)
    result = swapaxes(result, 0, ind_indices0)

    if is_squeeze:
        result = squeeze(result)
        if shape_result[ind_indices] == 1:
            # Re add node dimension which has been squeezed if there is only one node
            result = result[None, ...]

    return result


def apply_normal_center_surf_vectorfield(
    field,
    ind_otherdim,
    shape_otherdim,
    is_center,
    is_normal,
    is_surf,
    is_rms,
    is_rthetaz,
    is_radial,
    is_pol2cart,
    mesh_pv,
    normals,
    points,
    cell_area,
    shape_result,
    dtype,
    indices,
    ind_indices,
):
    """Perform the required operation on the input field by performing a recursive call on all axes.
    This function is necessary as pyvista operators require field with only indice axis (and component axis).

    Parameters
    ----------
    field : ndarray
        a vector field
    is_center : bool
        field at element centers
    indices : list
        list of indices to extract from mesh and field
    is_rthetaz : bool
        cylindrical coordinates
    is_radial : bool
        radial component only
    is_normal : bool
        normal component only (on nodes or centers)
    is_rms : bool
        rms over surface sum((F.n)**2 dS)/S

    is_surf : bool
        field over outer surface

    Returns
    -------
    result : ndarray
        field

    """

    new_ind_otherdim = list(ind_otherdim)

    if len(ind_otherdim) == 0:
        # Reduce field to requested indices
        if indices is not None:
            field = field.take(indices, axis=ind_indices)

        if is_center:
            # Add field to mesh
            if field.dtype == float:
                mesh_pv["real"] = field
            else:
                mesh_pv["real"] = real(field)
                mesh_pv["imag"] = imag(field)
            if is_center:
                # Points to centers
                mesh_cell = mesh_pv.point_data_to_cell_data()
            else:
                mesh_cell = mesh_pv
        if is_surf:
            # Extract surface
            surf = mesh_cell.extract_geometry()
            if field.dtype == float:
                field = surf["real"]
            else:
                field = surf["real"] + 1j * surf["imag"]
        elif is_center:
            if field.dtype == float:
                field = mesh_cell["real"]
            else:
                field = mesh_cell["real"] + 1j * mesh_cell["imag"]

        # Project on normals if necessary
        if is_normal:
            field = einsum("ij,ij->i", normals, field)
        # rms computation
        if is_rms:
            field = sqrt(np_sum(np_abs(field**2) * cell_area) / np_sum(cell_area))
        # Coordinates
        if is_rthetaz:
            field = cart2pol(field, points)
        if is_radial:
            field = field[:, 0]
        if is_pol2cart and not is_radial:
            field = pol2cart(field, points)

        field = reshape(field, shape_result)

        return field

    else:
        result = zeros(shape_result, dtype=dtype)

        for i in range(shape_otherdim[-1]):
            field_i = field.take((i), axis=new_ind_otherdim[-1])

            ind_other_dim_i = list(new_ind_otherdim)
            ind_other_dim_i.pop()
            shape_otherdim_i = list(shape_otherdim)
            shape_otherdim_i.pop()
            shape_result_i = list(shape_result)
            shape_result_i.pop(new_ind_otherdim[-1])

            result[..., i] = apply_normal_center_surf_vectorfield(
                field_i,
                ind_other_dim_i,
                shape_otherdim_i,
                is_center,
                is_normal,
                is_surf,
                is_rms,
                is_rthetaz,
                is_radial,
                is_pol2cart,
                mesh_pv,
                normals,
                points,
                cell_area,
                shape_result_i,
                dtype,
                indices,
                ind_indices,
            )

        return result
