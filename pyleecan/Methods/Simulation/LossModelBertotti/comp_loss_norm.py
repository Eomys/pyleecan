# -*- coding: utf-8 -*-
from SciDataTool import DataFreq, Data1D, VectorField, DataTime

from numpy import newaxis, abs


def _get_data_(axes, components, field):
    # only valid for field.shape.size == 3, i.e. 2 axes and >1 components
    comps = {}
    for idx, component in enumerate(components):
        comp_data = DataTime(
            name=component + "Field",
            unit="",
            symbol="F" + component,
            axes=axes,
            values=field[:, :, idx],
        )
        comps[component] = comp_data

    field = VectorField(name="VectorField", symbol="F", components=comps)

    return field


def _get_axes_(meshsolution, indices, label):
    components = meshsolution.get_solution(label=label).field.components

    axes = []
    for axis in components["x"].axes:
        if axis.name != "indice":
            axes.append(axis)  # TODO copy axis (dereferencing)

    inds = Data1D(
        name="indices",
        unit="",
        symbol="",
        values=indices,
        symmetries={},
        is_components=False,
    )
    axes.append(inds)

    dirs = [comp for comp in components.keys()]

    return axes, dirs


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
    Coeff = list(
        [self.k_hy, self.alpha_hy, self.k_ed, self.alpha_ed, self.k_ex, self.alpha_ex,]
    )
    print(Coeff)

    F_REF = self.F_REF
    B_REF = self.B_REF

    # filter needed mesh group
    grp_sol = meshsolution.get_group(self.group)

    sol = grp_sol.get_solution(label="B")
    fld = sol.get_field()  # have to use get_field TODO check shape

    # get data
    # TODO temp. hotfix for axes (working with SolutionVector only)
    axes, comps = _get_axes_(meshsolution, sol.indice, label="B")
    field = _get_data_(axes, comps, fld)

    # get components
    components = []
    for comp in field.components.values():
        components.append(comp)

    loss = None
    for component in components:
        axes_names = ["freqs" if x.name == "time" else x.name for x in component.axes]

        mag_dict = component.get_magnitude_along(*axes_names)
        symbol = component.symbol
        # TODO assumption is that direction is 3rd axis
        # TODO better data check (axis size, ...) and data handling
        # TODO Calculate principle axes and transform for exponentials other than 2

        f_norm = abs(mag_dict["freqs"][:, newaxis] / F_REF)
        B_norm = (
            1 / 2 * mag_dict[symbol] / B_REF
        )  # factor 1/2 to account for SciDataTool FFT of double sided spectrum

        HY = Coeff[0] * f_norm * B_norm ** Coeff[1]
        ED = Coeff[2] * (f_norm * B_norm) ** Coeff[3]
        EX = Coeff[4] * (f_norm * B_norm) ** Coeff[5]

        loss_ = HY + ED + EX
        loss = loss_ if loss is None else loss + loss_

    Freq = Data1D(name="freqs", unit="", values=mag_dict["freqs"])
    axes = [Freq if x.name == "time" else x for x in component.axes]

    loss_data = DataFreq(
        name="Loss Density", unit="T", symbol="LossDens", axes=axes, values=loss,
    )

    return loss_data
