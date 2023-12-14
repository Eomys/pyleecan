from os.path import join

from meshio import read
from numpy import append as np_append
from numpy import arange
from SciDataTool import Data1D, DataTime, Norm_ref, VectorField

from ....Classes.MeshSolution import MeshSolution
from ....Classes.MeshVTK import MeshVTK
from ....Classes.SolutionData import SolutionData
from ....Classes.SolutionVector import SolutionVector


def get_meshsolution(self, output):
    """Build the MeshSolution objects from the FEA outputs.

    Parameters
    ----------
    self : MagElmer
        a MagElmer object
    output: Output
        An Output object

    Returns
    -------
    meshsol: MeshSolution
        a MeshSolution object with Elmer outputs at every time step
    """
    project_name = self.get_path_save_fea(output)
    elmermesh_folder = project_name
    meshsol = MeshSolution(label="Elmer MagnetoDynamics")
    if not self.is_get_mesh or not self.is_save_FEA:
        self.get_logger().info("MagElmer: MeshSolution is not stored by request.")
        return False

    meshvtk = MeshVTK(path=elmermesh_folder, name="step_t0002", format="vtu")
    meshsol.mesh = meshvtk

    result_filename = join(elmermesh_folder, "step_t0002.vtu")
    meshsolvtu = read(result_filename)
    # pt_data = meshsolvtu.point_data
    cell_data = meshsolvtu.cell_data

    # indices = arange(meshsolvtu.points.shape[0])
    indices = arange(
        meshsolvtu.cells[0].data.shape[0] + meshsolvtu.cells[1].data.shape[0]
    )

    Indices = Data1D(name="indice", values=indices, is_components=True)
    # store_dict = {
    #     "magnetic vector potential": {
    #         "name": "Magnetic Vector Potential A",
    #         "unit": "Wb",
    #         "symbol": "A",
    #         "norm": 1,
    #     },
    #     "magnetic flux density": {
    #         "name": "Magnetic Flux Density B",
    #         "unit": "T",
    #         "symbol": "B",
    #         "norm": 1,
    #     },
    #     "magnetic field strength": {
    #         "name": "Magnetic Field H",
    #         "unit": "A/m",
    #         "symbol": "H",
    #         "norm": 1,
    #     },
    #     "current density": {
    #         "name": "Current Density J",
    #         "unit": "A/mm2",
    #         "symbol": "J",
    #         "norm": 1,
    #     }
    # }
    store_dict = {
        "magnetic flux density e": {
            "name": "Magnetic Flux Density B",
            "unit": "T",
            "symbol": "B",
            "norm": 1,
        },
        "magnetic vector potential e": {
            "name": "Magnetic Vector Potential A",
            "unit": "Wb",
            "symbol": "A",
            "norm": 1,
        },
        "magnetic field strength e": {
            "name": "Magnetic Field H",
            "unit": "A/m",
            "symbol": "H",
            "norm": 1,
        },
        "current density e": {
            "name": "Current Density J",
            "unit": "A/mm2",
            "symbol": "J",
            "norm": 1,
        },
    }
    comp_ext = ["x", "y", "z"]
    sol_list = []
    # for key, value in pt_data.items():
    for key, value in cell_data.items():
        if key in store_dict.keys():
            # siz = value.shape[1]
            siz = value[0].shape[1]
            if siz > 3:
                print("Some Message")
                siz = 3
            components = []
            comp_name = []
            values = np_append(value[0], value[1], axis=0)
            for i in range(siz):
                if siz == 1:
                    ext = ""
                else:
                    ext = comp_ext[i]

                data = DataTime(
                    name=store_dict[key]["name"] + ext,
                    unit=store_dict[key]["unit"],
                    symbol=store_dict[key]["symbol"] + ext,
                    axes=[Indices],
                    # values=value[:, i],
                    values=values[:, i],
                    normalizations={"ref": Norm_ref(ref=store_dict[key]["norm"])},
                )

                components.append(data)
                comp_name.append("comp_" + ext)

            if siz == 1:
                field = components[0]
                sol_list.append(
                    SolutionData(
                        field=field,
                        # type_element="point",
                        type_element="triangle",
                        label=store_dict[key]["symbol"],
                    )
                )
            else:
                comps = {}
                for i in range(siz):
                    comps[comp_name[i]] = components[i]
                field = VectorField(
                    name=store_dict[key]["name"],
                    symbol=store_dict[key]["symbol"],
                    components=comps,
                )
                sol_list.append(
                    SolutionVector(
                        field=field,
                        # type_element="point",
                        type_element="triangle",
                        label=store_dict[key]["symbol"],
                    )
                )

    meshsol.solution = sol_list
    output.mag.meshsolution = meshsol

    return True
