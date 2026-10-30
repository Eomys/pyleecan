from SciDataTool import DataFreq, DataND, DataTime

from ...Classes.SolutionData import SolutionData


def build_solution_data(
    field, axis_list, name="", symbol="", unit="", is_real=True, type_element="triangle"
) -> SolutionData:
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

    if axis_list[0].name == "time":
        DataClass = DataTime
    elif axis_list[0].name == "freqs":
        DataClass = DataFreq
    else:
        DataClass = DataND

    data = DataClass(
        name=name,
        unit=unit,
        symbol=symbol,
        axes=axis_list,
        values=field,
        is_real=is_real,
    )

    return SolutionData(field=data, label=symbol, type_element=type_element)
