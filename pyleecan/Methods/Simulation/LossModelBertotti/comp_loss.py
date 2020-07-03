# -*- coding: utf-8 -*-

import numpy as np
from SciDataTool import DataTime, DataFreq

from ....Methods.Simulation.Input import InputError


def _ft_data(data):
    # ---------------------------------------------------------------
    # workaround
    # fourier transform with data with multiple components
    # axes/components order won't be restored
    # ---------------------------------------------------------------

    # get axes and components
    axes = []
    components = []
    n_comp = 1
    for axis in data.axes:
        if axis.is_components:
            components.append(axis)
            n_comp = len(axis.values)
        else:
            axes.append(axis)

    axes_str = [x.name for x in axes]

    # transform each field component at a time
    if n_comp > 1:
        values = []
        for id in range(n_comp):
            component_str = components[0].name + f"[{id}]"
            component_data = data.get_along(component_str, *axes_str)
            _data = DataTime(
                name=data.name,
                unit=data.unit,
                symbol=data.symbol,
                axes=axes,
                values=component_data[data.symbol],
            )

            _dataFt = _data.time_to_freq()
            values.append(_dataFt.values)

        values = np.array([*values])

        # recombine transformed field components
        dataFt = DataFreq(
            name=_dataFt.name,
            unit=_dataFt.unit,
            symbol=_dataFt.symbol,
            axes=[components[0], *_dataFt.axes],
            values=values,
        )
    else:
        dataFt = data.time_to_freq()

    return dataFt


def comp_loss(self, output, lam, typ):
    """Compute the Losses
    """
    if self.parent is None:
        raise InputError(
            "ERROR: The LossModelBertotti object must be in a Loss object to run"
        )
    if self.parent.parent is None:
        raise InputError(
            "ERROR: The LossModel object must be in a Simulation object to run"
        )

    if self.parent.parent.parent is None:
        raise InputError(
            "ERROR: The LossModelBertotti object must be in an Output object to run"
        )

    # compute needed model parameter from material data
    self.comp_coeff_Bertotti(lam.mat_type)

    # comp. fft of elemental FEA results
    B_fft = _ft_data(output.mag.meshsolution.solution[0].field)
    print("FFT of B calculated")

    # apply model

    # store results
    if typ == "Lamination":
        if lam.is_stator:
            output.loss.Plam_stator = np.array([np.nan])

    return B_fft
