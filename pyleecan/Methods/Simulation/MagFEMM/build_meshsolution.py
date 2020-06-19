
from ....Classes.SolutionData import SolutionData
from ....Classes.MeshSolution import MeshSolution
from SciDataTool import DataTime, Data1D

def build_meshsolution(self, Nt_tot, meshFEMM, Time, B, H, mu):
    """ Build the MeshSolution objets from FEMM outputs.

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
    cond = self.is_sliding_band or Nt_tot == 1
    if cond:
        indices_cell = meshFEMM[0].cell["Triangle3"].indice
        Direction = Data1D(name="Direction", values=["x", "y"], is_components=True)
        Indices_Cell = Data1D(name="Indices", values=indices_cell, is_components=True)

        solB = DataTime(
            name="Magnetic Flux Density",
            unit="T",
            symbol="B",
            axes=[Time, Indices_Cell, Direction],
            values=B,
        )

        solH = DataTime(
            name="Magnetic Field",
            unit="A/m",
            symbol="H",
            axes=[Time, Indices_Cell, Direction],
            values=H,
        )

        solmu = DataTime(
            name="Magnetic Permeability",
            unit="H/m",
            symbol="\mu",
            axes=[Time, Indices_Cell],
            values=mu,
        )

        sollist.append(SolutionData(field=solB, type_cell="Triangle")) # Face solution
        sollist.append(SolutionData(field=solH, type_cell="Triangle"))
        sollist.append(SolutionData(field=solmu, type_cell="Triangle"))

    meshsol = MeshSolution(
        label="FEMM_magnetotatic",
        mesh=meshFEMM,
        solution=sollist,
        is_same_mesh=cond,
    )

    return meshsol
