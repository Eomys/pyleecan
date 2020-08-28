# -*- coding: utf-8 -*-

import numpy as np
from SciDataTool import DataTime, DataFreq, Data1D
from pyleecan.Classes.SolutionData import SolutionData

from ....Methods.Simulation.Input import InputError


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
    print(type(output.mag.meshsolution).__name__)
    print(type(output.mag.meshsolution.solution[0]).__name__)

    #B_fft = output.mag.meshsolution.solution[0].field.time_to_freq()
    #print("FFT of B calculated")

    # calculate principle axes and transform for exponentials other than 2
    # TODO

    # apply model
    # #TODO model equation should be a func that takes SciDataTool Data as input
    field = output.mag.meshsolution.get_solution(label="B").field

    field_fft = []
    for comp in field.components.values():
        field_fft.append(comp.time_to_freq())
    
    # if "radial" in field.components.keys():
    #     field_1 = field.components['radial'].time_to_freq()
    #     field_2 = field.components['tangential'].time_to_freq()
        
    # elif "x" in field.components.keys() and "y" in field.components.keys():
    #     field_1 = field.components['x'].time_to_freq()
    #     field_2 = field.components['y'].time_to_freq()

    # TODO filter machine parts
    Loss = self.comp_loss_norm(field_fft)

    # store losses field
    sol = SolutionData()
    sol.field = Loss
    sol.label = 'P'
    output.mag.meshsolution.solution.append(sol)

    # compute sum over freqs axes
    axes_list = [axis.name for axis in sol.field.axes]
    freqs_idx = [idx for idx, axis_name in enumerate(axes_list) if axis_name == 'freqs']
    if len(freqs_idx) > 1:
        # TODO error
        raise('more than one freqs axis found')
    if len(freqs_idx) == 0:
        # TODO error
        raise('no freqs axis found')
    
    loss_sum = sol.field.get_along(*axes_list)['P'].sum(axis=freqs_idx[0])

    # compute FFT of induction magnitude
    field_list = [f for f in field.components.values()]
    Bmag_sq = None
    for component in field_list:
        axes_names = ["freqs" if x.name == "time" else x.name for x in component.axes]

        mag_dict = component.get_magnitude_along(*axes_names)
        symbol = component.symbol

        Bmag_sq = mag_dict[symbol]**2 if Bmag_sq is None else Bmag_sq + mag_dict[symbol]**2

    Freq = Data1D(name="freqs", unit="", values=mag_dict["freqs"])
    axes = [Freq if x.name == "time" else x for x in component.axes]

    Bmag = DataFreq(name="Bfft", unit="T", symbol="Bfft", axes=axes, values=Bmag_sq ** 0.5,)
    sol = SolutionData()
    sol.field = Bmag
    sol.label = 'Bfft'
    output.mag.meshsolution.solution.append(sol)

    # store results
    if typ == "Lamination":
        if lam.is_stator:
            output.loss.Plam_stator = np.array([np.nan])


    return Loss
