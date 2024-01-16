import numpy as np
from SciDataTool import Data1D, DataTime, VectorField

from ....Classes.MeshSolution import MeshSolution
from ....Classes.SolutionVector import SolutionVector


def comp_force_nodal(self, output, axes_dict):
    """Run the nodal forces calculation based on a tensor.

    from publications:


    Parameters
    ----------
    self : ForceTensor
        A ForceTensor object

    output : Output
        an Output object (to update)

    """

    dim = 2
    Time = axes_dict["time"]
    Nt_tot = Time.get_length()  # Number of time step

    meshsolution_mag = output.mag.meshsolution  # Comes from FEMM simulation

    # Select the target group (stator, rotor ...) or all the domain
    if self.group is None:
        meshsolution_group = meshsolution_mag
    else:
        meshsolution_group = meshsolution_mag.get_group(self.group)

    mesh = meshsolution_group.mesh

    # New meshsolution object for output, that could be different from the one inputed
    meshsolution = MeshSolution(mesh=mesh.copy(), dimension=dim)

    # Load magnetic flux B and H and mu objects
    B_sol = meshsolution_group.get_solution(label="B")
    H_sol = meshsolution_group.get_solution(label="H")
    mu_sol = meshsolution_group.get_solution(label="\mu")

    # Import time vector from Time Data object
    if self.is_periodicity_t is not None:
        is_periodicity_t = self.is_periodicity_t

    is_periodicity_t, is_antiper_t = Time.get_periodicity()
    time = Time.get_values(
        is_oneperiod=is_periodicity_t,
        is_antiperiod=is_antiper_t and is_periodicity_t,
    )

    # Load magnetic flux B and H of size (Nt_tot, nb_elem, dim) and mu (Nt_tot, nb_elem)
    resultB = B_sol.field.get_xyz_along(
        "indice",
        "time=axis_data",
        axis_data={"time": time},
        is_squeeze=False,
    )
    indice = resultB["indice"]  # Store elements indices

    Bx = resultB["comp_x"]
    By = resultB["comp_y"]
    B = np.stack((Bx, By), axis=2)

    resultH = H_sol.field.get_xyz_along(
        "indice",
        "time=axis_data",
        axis_data={"time": time},
        is_squeeze=False,
    )
    Hx = resultH["comp_x"]
    Hy = resultH["comp_y"]
    H = np.stack((Hx, Hy), axis=2)

    resultmu = mu_sol.field.get_along(
        "indice",
        "time=axis_data",
        axis_data={"time": time},
        is_squeeze=False,
    )
    mu = resultmu["\\mu"]

    # Move time axis at the end for clarity purpose
    B = np.moveaxis(B, 0, -1)
    H = np.moveaxis(H, 0, -1)
    mu = np.moveaxis(mu, 0, -1)

    # Loop on elements and nodes for nodal forces
    f, connect = self.element_loop(mesh, B, H, mu, indice, dim, Nt_tot)

    indices_nodes = mesh.node.indice.copy()
    Indices_Point = Data1D(name="indice", values=indices_nodes, is_components=True)

    # Time axis goes back to first axis
    f = np.moveaxis(f, -1, 0)

    components = {}

    fx_data = DataTime(
        name="Nodal force (x)",
        unit="N",
        symbol="Fx",
        axes=[Time, Indices_Point],
        values=f[..., 0],
    )
    components["comp_x"] = fx_data

    fy_data = DataTime(
        name="Nodal force (y)",
        unit="N",
        symbol="Fy",
        axes=[Time, Indices_Point],
        values=f[..., 1],
    )
    components["comp_y"] = fy_data

    vec_force = VectorField(name="Nodal forces", symbol="F", components=components)
    solforce = SolutionVector(field=vec_force, type_element="node", label="F")
    meshsolution.solution.append(solforce)

    out_dict = dict()
    out_dict["meshsolution"] = meshsolution

    return out_dict
