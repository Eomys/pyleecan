from ...Classes.SolutionData import SolutionData
from SciDataTool import DataTime
import numpy as np


def build_solution_data(
    field, axis_list, name="", symbol="", unit="", is_real=True, type_cell="triangle"
):
    """Build the MeshSolution objets from FEMM outputs.

    Parameters
    ----------
    field : ndarray
        a data field
    axis_list : list
        a list of SciDataTool axis

    Returns
    -------
    solution: SolutionData
        a SolutionData object
    """

    data = DataTime(
        name=name,
        unit=unit,
        symbol=symbol,
        axes=axis_list,
        values=field,
        is_real=is_real,
    )

    return SolutionData(field=data, label=symbol, type_cell=type_cell)
