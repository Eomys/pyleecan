# -*- coding: utf-8 -*-

from ....Classes.MeshMat import MeshMat
from ....Classes.MeshVTK import MeshVTK
from ....Functions.Structural.conversions import DimError, cart2pol
from numpy import einsum, sqrt, zeros, squeeze, real, imag, sum as np_sum, abs as np_abs


def get_field(
    self,
    label=None,
    index=None,
    indices=None,
    is_rthetaz=False,
    is_radial=False,
    is_normal=False,
    is_rms=False,
    is_center=False,
    is_surf=False,
    args=None,
):
    """Return the solution corresponding to label or an index.

    Parameters
    ----------
    self : MeshSolution
        an MeshSolution object
    label : str
        a label
    index : int
        an index
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
        field at cell centers
    is_surf : bool
        field over outer surface

    Returns
    -------
    result : ndarray
        field

    """

    # Get field
    solution = self.get_solution(label=label, index=index)
    field = solution.get_field(args=args)
    field = squeeze(field)

    # Check dimensions
    shape = field.shape
    is_other_dim = False
    is_1d_input = False
    is_1d_output = False
    if len(shape) != 1 and shape[-1] > 3:
        is_other_dim = True
    if len(shape) == 1 or (len(shape) == 2 and is_other_dim):
        is_1d_input = True
    if is_radial:
        is_rthetaz = True
    if is_radial or is_1d_input or is_normal:
        is_1d_output = True
    if is_rms:
        is_center = True
        is_normal = True
    if is_normal:
        is_surf = True
    if is_rthetaz or is_normal:
        if is_1d_input:
            raise DimError("The field should be 3D")

    # Get mesh if necessary
    if is_center or is_normal or is_rthetaz or is_surf:
        # Get the mesh
        mesh = self.get_mesh(label=label, index=index)
        mesh_pv = mesh.get_mesh_pv(indices=indices)
        if isinstance(mesh, MeshMat):
            mesh_pv = mesh.get_mesh_pv(indices=indices)
            mesh = MeshVTK(mesh=mesh_pv, is_pyvista_mesh=True)
    # Get points coordinates if necessary
    if is_rthetaz:
        points = mesh.get_points(indices=indices)
    # Get normals if necessary
    if is_normal and is_center:
        # Get normals
        normals = mesh.get_normals(indices=indices)
    elif is_normal:
        normals = mesh.get_normals(indices=indices, loc="point")
    # Get cell area if necessary
    if is_rms:
        cell_area = mesh.get_cell_area(indices=indices)

    # 1D case: only cell-center and surf available
    if is_1d_input:
        if is_center or is_surf:
            if is_other_dim:
                # Field has other dimension -> loop over other dimension
                if is_center:
                    Nnodes = mesh.get_points(indices=indices).shape[0]
                else:
                    Nnodes = shape[0]
                result = zeros((Nnodes, shape[1]), dtype=complex)
                for i in range(shape[1]):
                    field_i = field[:, i]
                    # Extract subset of the field if necessary
                    if indices is not None:
                        if len(field_i) != len(indices):
                            field_i = field_i[indices]
                    # Add field to mesh
                    mesh_pv["real"] = real(field_i)
                    mesh_pv["imag"] = imag(field_i)
                    if is_center:
                        # Points to centers
                        mesh_cell = mesh_pv.point_data_to_cell_data()
                    else:
                        mesh_cell = mesh_pv
                    if is_surf:
                        # Extract surface
                        surf = mesh_cell.extract_geometry()
                        field_i = surf["real"] + 1j * surf["imag"]
                    else:
                        field_i = mesh_cell["real"] + 1j * mesh_cell["imag"]
                    # Store in result
                    result[:, i] = field_i
            else:
                # Extract subset of the field if necessary
                if indices is not None:
                    if len(field) != len(indices):
                        field = field[indices]
                # Add field to mesh
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
                    field = surf["real"] + 1j * surf["imag"]
                else:
                    field = mesh_cell["real"] + 1j * mesh_cell["imag"]
                # Store in result
                result = field
        else:
            result = field

    # 3D case
    else:
        if is_other_dim:
            # Field has third dimension -> loop over third dimension
            if is_center:
                Nnodes = mesh.get_normals(indices=indices).shape[0]
            else:
                Nnodes = shape[0]
            if is_1d_output:
                result = zeros((Nnodes, shape[2]), dtype=complex)
            elif is_rms:
                result = zeros(shape[2], dtype=complex)
            else:
                result = zeros((Nnodes, shape[1], shape[2]), dtype=complex)
            for i in range(shape[2]):
                field_i = field[:, :, i]
                # Extract subset of the field if necessary
                if indices is not None and field_i.shape != indices.shape:
                    field_i = field_i[indices]
                # Field to mesh if necessary
                if is_center or is_normal or is_surf:
                    # Add field to mesh
                    mesh_pv["real"] = real(field_i)
                    mesh_pv["imag"] = imag(field_i)
                    if is_center:
                        # Points to centers
                        mesh_cell = mesh_pv.point_data_to_cell_data()
                    else:
                        mesh_cell = mesh_pv
                if is_surf:
                    # Extract surface
                    surf = mesh_cell.extract_geometry()
                    field_i = surf["real"] + 1j * surf["imag"]
                elif is_center:
                    field_i = mesh_cell["real"] + 1j * mesh_cell["imag"]
                # Project on normals if necessary
                if is_normal:
                    field_i = einsum("ij,ij->i", normals, field_i)
                # rms computation
                if is_rms:
                    field_i = sqrt(
                        np_sum(np_abs(field_i ** 2) * cell_area) / np_sum(cell_area)
                    )
                # Coordinates
                if is_rthetaz:
                    field_i = cart2pol(field_i, points)
                if is_radial:
                    field_i = field_i[:, 0]
                # Store in result
                if is_1d_output:
                    result[:, i] = field_i
                elif is_rms:
                    result[i] = field_i
                else:
                    result[:, :, i] = field_i
        else:
            # Extract subset of the field if necessary
            if indices is not None and field_i.shape != indices.shape:
                field = field[indices]
            # Field to mesh if necessary
            if is_center or is_normal or is_surf:
                # Add field to mesh
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
                field = surf["real"] + 1j * surf["imag"]
            elif is_center:
                field = mesh_cell["real"] + 1j * mesh_cell["imag"]
            # Project on normals if necessary
            if is_normal:
                field = einsum("ij,ij->i", normals, field)
            # Coordinates
            if is_rthetaz:
                field = cart2pol(field, points)
            if is_radial:
                field = field[:, 0]
            # Store in result
            result = field

    return result
