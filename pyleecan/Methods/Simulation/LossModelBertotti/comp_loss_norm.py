# -*- coding: utf-8 -*-
from SciDataTool import DataFreq, Data1D
from numpy import newaxis, abs, sqrt


def comp_loss_norm(self, meshsolution):
    """
    Compute the normalized (per kg) losses according to the following model equation:
        Loss = C0*f*B^C1 + C2*(f*B)^C3 + C4*(f*B)^C4

    Parameters
    ----------
    self : LossModelBertotti
        a LossModelBertotti object
    field : DataND
        a DataND object that contains the flux density values

    Returns
    -------
    loss_data: DataND
        a DataND object of the normalized losses
    """
    # get the parameters
    Coeff = list(
        [self.k_hy, self.alpha_hy, self.k_ed, self.alpha_ed, self.k_ex, self.alpha_ex]
    )
    F_REF = self.F_REF
    B_REF = self.B_REF

    # filter needed mesh group
    sol = meshsolution.get_group(self.group).get_solution(label="B")

    # TODO Calculate principle axes and transform for exponentials other than 2
    # TODO maybe use rad. and tan. comp. as intermediate solution

    # loop over field components
    loss = None
    for component in sol.field.components.values():
        axes_names = ["freqs" if x.name == "time" else x.name for x in component.axes]

        # TODO add filter function to limit max. order of harmonics
        mag_dict = component.get_magnitude_along(*axes_names)
        symbol = component.symbol

        # TODO better data check (axis size, ...)
        freqs = mag_dict["freqs"]
        # freqs[freqs<0] = 0 # to only regard positive freqs
        k = 1 # 1 / sqrt(2)
        f_norm = abs(freqs[:, newaxis] / F_REF)
        B_norm = k * mag_dict[symbol] / B_REF
        # factor 1 / sqrt(2) to account for SciDataTool FFT of double sided spectrum
        # TODO is this factor also true for powers other than 2 ?

        HY = Coeff[0] * f_norm * B_norm ** Coeff[1]
        ED = Coeff[2] * (f_norm * B_norm) ** Coeff[3]
        EX = Coeff[4] * (f_norm * B_norm) ** Coeff[5]

        loss_ = HY + ED + EX
        loss = loss_ if loss is None else loss + loss_

    Freq = Data1D(name="freqs", unit="", values=freqs)
    axes = [Freq if x.name == "time" else x for x in component.axes]

    loss_data = DataFreq(
        name="Loss Density", unit="T", symbol="LossDens", axes=axes, values=loss
    )
    print(freqs)
    return loss_data
