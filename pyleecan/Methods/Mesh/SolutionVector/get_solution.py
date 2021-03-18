# -*- coding: utf-8 -*-
from numpy import take
from SciDataTool import Data1D


def get_solution(self, indice=None):
    """Return a copy of the solution with the option to only include specified indices.

    Parameters
    ----------
    self : SolutionVector
        a SolutionVector object
    indices : list
        list of indices, if list is empty or None all indices are included

    Returns
    -------
    solution: SolutionMat
        solution

    """
    logger = self.get_logger()

    # create copy to directly manipulate data
    solution = self.copy()

    if indice:
        for field in solution.field.components.values():
            # get axes data
            axes = field.axes
            axes_names = [axis.name for axis in field.axes]
            ax_idx = axes_names.index("indice")

            org_indice = axes[ax_idx].get_values()

            if set(indice) - set(org_indice):
                logger.warning(
                    "At least one input indice is not part of the solution. "
                    + "Respective indice will be skipped."
                )

            # skip indice that are not part of the solution
            new_indice = [ii for ii in indice if ii in org_indice]

            # create requested axes list to get field values (see SciDataTool ref.)
            args = [
                name + "[smallestperiod]" if name != "indice" else name
                for name in axes_names
            ]
            args[ax_idx] += "=axis_data"

            # get the field values
            field_dict = field.get_along(*args, axis_data={"indice": new_indice})

            # set new indice axis
            axes[ax_idx] = Data1D(
                values=new_indice,
                is_components=axes[ax_idx].is_components,
                symmetries=axes[ax_idx].symmetries,
                symbol=axes[ax_idx].symbol,
                name=axes[ax_idx].name,
                unit=axes[ax_idx].unit,
                normalizations=axes[ax_idx].normalizations,
            )

            # set new field data
            field.values = field_dict[field.symbol]

    return solution
