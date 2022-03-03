# -*- coding: utf-8 -*-
from SciDataTool import DataFreq, Data1D
from numpy import newaxis, abs, sqrt, stack


def comp_loss_density(self, meshsolution):
    """
    Compute the losses density (per kg) according to the following model equation:
        Loss = C0*f*B^C1 + C2*(f*B)^C3 + C4*(f*B)^C4

    Parameters
    ----------
    self : LossModelBertotti
        a LossModelBertotti object
    field : DataND
        a DataND object that contains the flux density values

    Returns
    -------
    loss_density: DataND
        a DataND object of the normalized losses
    """
    # get the parameters
    Coeff = list(
        [self.k_hy, self.alpha_hy, self.k_ed, self.alpha_ed, self.k_ex, self.alpha_ex]
    )
    F_REF = self.F_REF
    B_REF = self.B_REF

    # filter needed mesh group
    sol = meshsolution.get_solution(label="B")

    # TODO Calculate principle axes and transform for exponentials other than 2
    # TODO maybe use rad. and tan. comp. as intermediate solution

    # loop over field components
    HY, ED, EX = None, None, None
    for component in sol.field.components.values():
        axes_names = ["freqs" if x.name == "time" else x.name for x in component.axes]
        axes_names2 = [name for name in axes_names if name != "z"]

        # TODO add filter function to limit max. order of harmonics
        mag_dict = component.get_magnitude_along(*axes_names2)
        symbol = component.symbol

        # TODO better data check (axis size, ...)
        freqs = mag_dict["freqs"]
        # freqs[freqs<0] = 0 # to only regard positive freqs
        k = 1  # 1 / sqrt(2)
        f_norm = abs(freqs[:, newaxis] / F_REF)
        B_norm = k * mag_dict[symbol] / B_REF
        # factor 1 / sqrt(2) to account for SciDataTool FFT of double sided spectrum
        # TODO is this factor also true for powers other than 2 ?

        HY_ = Coeff[0] * f_norm * B_norm ** Coeff[1]
        ED_ = Coeff[2] * (f_norm * B_norm) ** Coeff[3]
        EX_ = Coeff[4] * (f_norm * B_norm) ** Coeff[5]

        HY = HY_ if HY is None else HY + HY_
        ED = ED_ if ED is None else ED + ED_
        EX = EX_ if EX is None else EX + EX_

    loss = HY + ED + EX

    # setup loss density data
    Freq = Data1D(name="freqs", unit="", values=freqs)
    axes = [Freq if x.name == "time" else x for x in component.axes]
    axes2 = [x for x in axes if x.name != "z"]

    loss_density = DataFreq(
        name="Loss Density", unit="W/kg", symbol="LossDens", axes=axes, values=loss
    )

    # setup loss density components data
    Comps = Data1D(
        name="Components",
        unit="W/kg",
        values=["Hysteresis", "Eddy", "Excess"],
        is_components=True,
    )
    axes = [axis.copy() for axis in axes2]
    axes.append(Comps)

    comps_data = stack([HY, ED, EX], axis=len(axes) - 1)

    loss_density_comps = DataFreq(
        name="Loss Density Components",
        unit="W/kg",
        symbol="LossDensComps",
        axes=axes,
        values=comps_data,
    )

    return loss_density, loss_density_comps
