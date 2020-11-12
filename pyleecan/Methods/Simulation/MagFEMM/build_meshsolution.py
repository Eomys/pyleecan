from ....Classes.SolutionData import SolutionData
from ....Classes.SolutionVector import SolutionVector
from ....Classes.MeshSolution import MeshSolution
from SciDataTool import DataTime, Data1D, VectorField
import numpy as np


def build_meshsolution(self, Nt, meshFEMM, Time, B, H, mu, groups):
    """Build the MeshSolution objets from FEMM outputs.

    Parameters
    ----------
    self : MagFEMM
        a MagFEMM object
    is_get_mesh : bool
        1 to load the mesh and solution into the simulation
    is_save_FEA : bool
        1 to save the mesh and solution into a .json file
    j_t0 : int
        Targeted time step

    Returns
    -------
    meshsol: MeshSolution
        a MeshSolution object with FEMM outputs at every time step
    """

    sollist = list()
    cond = self.is_sliding_band or Nt == 1
    if cond:
        indices_cell = meshFEMM[0].cell["triangle"].indice
        # Direction = Data1D(name="direction", values=["x", "y", "z"], is_components=True)
        Indices_Cell = Data1D(name="indice", values=indices_cell, is_components=True)
        # Nodirection = Data1D(name="direction", values=["scalar"], is_components=False)

        # Store the results for B
        components = {}

        Bx_data = DataTime(
            name="Magnetic Flux Density Bx",
            unit="T",
            symbol="Bx",
            axes=[Time, Indices_Cell],
            values=B[:, :, 0],
        )
        components["x"] = Bx_data

        By_data = DataTime(
            name="Magnetic Flux Density By",
            unit="T",
            symbol="By",
            axes=[Time, Indices_Cell],
            values=B[:, :, 1],
        )
        components["y"] = By_data

        if not np.all((B[:, :, 2] == 0)):
            Bz_data = DataTime(
                name="Magnetic Flux Density Bz",
                unit="T",
                symbol="Bz",
                axes=[Time, Indices_Cell],
                values=B[:, :, 2],
            )
            components["z"] = Bz_data

        solB = VectorField(
            name="Magnetic Flux Density", symbol="B", components=components
        )

        # Store the results for H
        componentsH = {}

        Hx_data = DataTime(
            name="Magnetic Field Hx",
            unit="A/m",
            symbol="Hx",
            axes=[Time, Indices_Cell],
            values=H[:, :, 0],
        )
        componentsH["x"] = Hx_data

        Hy_data = DataTime(
            name="Magnetic Field Hy",
            unit="A/m",
            symbol="Hy",
            axes=[Time, Indices_Cell],
            values=H[:, :, 1],
        )
        componentsH["y"] = Hy_data

        if not np.all((H[:, :, 2] == 0)):
            Hz_data = DataTime(
                name="Magnetic Field Hz",
                unit="A/m",
                symbol="Hz",
                axes=[Time, Indices_Cell],
                values=H[:, :, 2],
            )
            componentsH["z"] = Hz_data

        solH = VectorField(name="Magnetic Field", symbol="H", components=componentsH)

        solmu = DataTime(
            name="Magnetic Permeability",
            unit="H/m",
            symbol="\mu",
            axes=[Time, Indices_Cell],
            values=mu,
        )

        sollist.append(
            SolutionVector(field=solB, type_cell="triangle", label="B")
        )  # Face solution
        sollist.append(SolutionVector(field=solH, type_cell="triangle", label="H"))
        sollist.append(SolutionData(field=solmu, type_cell="triangle", label="\mu"))

    meshsol = MeshSolution(
        label="FEMM_magnetotatic",
        mesh=meshFEMM,
        solution=sollist,
        is_same_mesh=cond,
        dimension=2,
    )

    meshsol.group = groups[0]

    return meshsol
