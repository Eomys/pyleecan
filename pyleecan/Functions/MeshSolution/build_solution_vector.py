from numpy import all as np_all
from SciDataTool import DataFreq, DataND, DataTime, VectorField

from ...Classes.SolutionVector import SolutionVector


def build_solution_vector(
    field, axis_list, name="", symbol="", unit="", is_real=True, type_element="triangle"
) -> SolutionVector:
    """Build a SolutionVector object

    Parameters
    ----------
    field : ndarray
        a vector vield
    axis_list : list
        a list of SciDataTool axis

    Returns
    -------
    solution: SolutionVector
        a SolutionVector object
    """

    if axis_list[0].name == "time":
        DataClass = DataTime
    elif axis_list[0].name == "freqs":
        DataClass = DataFreq
    else:
        DataClass = DataND

    components = {}

    x_data = DataClass(
        name=name,
        unit=unit,
        symbol=symbol + "x",
        axes=axis_list,
        values=field[..., 0],
        is_real=is_real,
    )
    components["comp_x"] = x_data

    y_data = DataClass(
        name=name,
        unit=unit,
        symbol=symbol + "y",
        axes=axis_list,
        values=field[..., 1],
        is_real=is_real,
    )
    components["comp_y"] = y_data

    if field.shape[-1] == 3 and not np_all(field[..., 2] == 0):
        z_data = DataClass(
            name=name,
            unit=unit,
            symbol=symbol + "z",
            axes=axis_list,
            values=field[..., 2],
            is_real=is_real,
        )
        components["comp_z"] = z_data

    vectorfield = VectorField(name=name, symbol=symbol, components=components)

    solution = SolutionVector(
        field=vectorfield, label=symbol, type_element=type_element
    )

    return solution
