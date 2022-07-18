from os.path import isfile
from shutil import copyfile

from numpy import zeros, concatenate, append

from SciDataTool import Data1D

from ....Classes._FEMMHandler import _FEMMHandler
from ....Classes.OutMagFEMM import OutMagFEMM

from ....Functions.labels import STATOR_LAB
from ....Functions.FEMM.draw_FEMM import draw_FEMM
from ....Functions.MeshSolution.build_solution_data import build_solution_data
from ....Functions.MeshSolution.build_meshsolution import build_meshsolution
from ....Functions.MeshSolution.build_solution_vector import build_solution_vector


def build_MS_sliced(self, MS_sliced, MS, axes_dict, Nslices, ii):
    """Build and solve FEMM model to calculate and store magnetic quantities

    Parameters
    ----------
    self : MagFEMM
        a MagFEMM object
    output : Output
        an Output object
    axes_dict: {Data}
        Dict of axes used for magnetic calculation
    delta_xy: ndarray
        Rotor center position function of time

    Returns
    -------
    out_dict: dict
        Dict containing the following quantities:
            Br : ndarray
                Airgap radial flux density (Nt,Na) [T]
            Bt : ndarray
                Airgap tangential flux density (Nt,Na) [T]
            Tem : ndarray
                Electromagnetic torque over time (Nt,) [Nm]
            Phi_wind_stator : ndarray
                Stator winding flux (qs,Nt) [Wb]
            Phi_wind : dict
                Dict of winding fluxlinkage with respect to Machine.get_lam_list_label (qs,Nt) [Wb]
            meshsolution: MeshSolution
                MeshSolution object containing magnetic quantities B, H, mu for each time step
    """

    logger = self.get_logger()
    list_solution = list()

    for solution in MS_sliced.solution:
        # Define axis
        name, _ = solution.get_axes_list()

        if hasattr(solution.field, "components"):
            comp_x = solution.field.components["comp_x"]
            field_x = comp_x.values
            comp_y = solution.field.components["comp_y"]
            field_y = comp_y.values
            field = concatenate((field_x[..., None], field_y[..., None]), axis=-1)

            axes_list = comp_x.axes

            new_solution = MS.get_solution(label=solution.label)
            new_comp_x = new_solution.field.components["comp_x"]
            new_field_x = new_comp_x.values
            new_comp_y = new_solution.field.components["comp_y"]
            new_field_y = new_comp_y.values
            new_field = concatenate(
                (new_field_x[..., None], new_field_y[..., None]), axis=-1
            )
        else:
            data = solution.field
            axes_list = data.axes
            field = data.values

            new_solution = MS.get_solution(label=solution.label)
            new_field = new_solution.field.values

        if "z" in name:
            axis_slice = axes_list[2].copy()
            axis_slice.values = append(axis_slice.values, ii)
            new_field = concatenate((field, new_field[:, :, None]), axis=2)
        else:
            axis_slice = Data1D(name="z", values=[ii - 1, ii])
            new_field = concatenate((field[:, :, None], new_field[:, :, None]), axis=2)

        if ii == Nslices:
            axis_slice = axes_dict["z"]

        new_axis_list = [axes_list[0], axes_list[1], axis_slice]

        if hasattr(solution.field, "components"):
            new_sol = build_solution_vector(
                field=new_field,
                axis_list=new_axis_list,
                name=comp_x.name,
                symbol=solution.field.symbol,
                unit=comp_x.unit,
                type_cell=solution.type_cell,
            )
        else:
            new_sol = build_solution_data(
                field=new_field,
                axis_list=new_axis_list,
                name=data.name,
                symbol=data.symbol,
                unit=data.unit,
                type_cell=solution.type_cell,
            )

        list_solution.append(new_sol)

    MS_sliced_new = build_meshsolution(
        list_solution=list_solution,
        label=MS_sliced.label,
        list_mesh=MS_sliced.mesh,
        group=MS_sliced.group,
    )

    return MS_sliced_new
