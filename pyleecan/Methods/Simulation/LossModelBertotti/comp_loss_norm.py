# -*- coding: utf-8 -*-
from SciDataTool import DataFreq, Data1D, VectorField, DataTime

from numpy import newaxis, abs


def _get_field_comps(axes, components, field):
    """Return a list of DataTime objects created by a field array with respective axes

    Parameters
    ----------
    axes : list
        list of Data1D axis objects
    components : list
        list of field components names
    field : ndarray
        ndarray of the field data with last dimension equals the number of components

    Return
    ------
    comps : list
        list of DataTime objects
    """
    # only valid for field.shape.size == 3, i.e. 2 axes and >1 components
    comps = []
    for idx, component in enumerate(components):
        data = DataTime(
            name=component + "Field",
            unit="",
            symbol="F" + component,
            axes=axes,
            values=field[:, :, idx],
        )
        comps.append(data)

    return comps


def _get_axes_(meshsolution, indices, label):
    """Get the axes of the first solution of a SolutionVector and the respective
    components names. The SolutionVector is the solution with given label.
    Further the indices axis is replaced by input indices.

    Parameters
    ----------
    meshsolution : MeshSolution
        MeshSolution
    label : string
        label of the solution that contains the requested axis
    indices : ndarray
        ndarray of indices to create the indices axes

    Returns
    -------
    axes : list
        list of Data1D axes
    comp_names : list
        list of components names of the SolutionVector components
    """
    components = meshsolution.get_solution(label=label).field.components

    comp_names = [comp for comp in components.keys()]

    axes = []
    for axis in components[comp_names[0]].axes:
        if axis.name != "indice":
            axes.append(axis.copy())

    inds = Data1D(
        name="indices",
        unit="",
        symbol="",
        values=indices,
        symmetries={},
        is_components=True,
    )
    axes.append(inds)

    return axes, comp_names


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
        [
            self.k_hy,
            self.alpha_hy,
            self.k_ed,
            self.alpha_ed,
            self.k_ex,
            self.alpha_ex,
        ]
    )

    F_REF = self.F_REF
    B_REF = self.B_REF

    # TODO temp. fix: MeshSolution.get_group() return data of type SolutionMat
    #                 so appropriate component data have to be reconstructed

    # filter needed mesh group
    sol = meshsolution.get_group(self.group).get_solution(label="B")
    fld = sol.get_field()

    # get data
    axes, comps = _get_axes_(meshsolution, sol.indice, label="B")
    components = _get_field_comps(axes, comps, fld)
    # TODO Calculate principle axes and transform for exponentials other than 2
    # TODO maybe use rad. and tan. comp. as intermediate solution

    # loop over field components
    loss = None
    for component in components:
        axes_names = ["freqs" if x.name == "time" else x.name for x in component.axes]

        # TODO add filter function to limit max. order of harmonics
        mag_dict = component.get_magnitude_along(*axes_names)
        symbol = component.symbol

        # TODO better data check (axis size, ...)

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
        name="Loss Density",
        unit="T",
        symbol="LossDens",
        axes=axes,
        values=loss,
    )

    return loss_data
