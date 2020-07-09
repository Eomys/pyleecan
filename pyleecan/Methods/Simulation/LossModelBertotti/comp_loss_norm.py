# -*- coding: utf-8 -*-
from SciDataTool import DataFreq, Data1D
from numpy import newaxis, abs

def comp_loss_norm(self, data):
    """ 
    Compute the normalized (per kg) losses according to the following model equation:
        Loss = C0*f*B^C1 + C2*(f*B)^C3 + C4*(f*B)^C4

    Parameters
    ----------
    self : LossModelBertotti
        a LossModelBertotti object
    data : DataND
        a DataND object that contains the flux density values

    Returns
    -------
    loss_data: DataND
        a DataND object of the normalized losses
    """
    Coeff = list(
        [self.k_hy, self.alpha_hy, self.k_ed, self.alpha_ed, self.k_ex, self.alpha_ex,]
    )

    axes_names = ["freqs" if x.name == "time" else x.name for x in data.axes]

    mag_dict = data.get_magnitude_along(*axes_names)
    # TODO assumption is that direction is 3rd axis
    # TODO better data check (axis size, ...) and data handling

    # TODO filter indices

    f_norm = abs(mag_dict["freqs"][:, newaxis, newaxis] / self.F_REF)
    B_norm = 1 / 2* mag_dict["B"] / self.B_REF # factor 1/2 to account for SciDataTool FFT

    HY = Coeff[0] * f_norm * B_norm ** Coeff[1]
    ED = Coeff[2] * (f_norm * B_norm) ** Coeff[3]
    EX = Coeff[4] * (f_norm * B_norm) ** Coeff[5]

    loss = HY + ED + EX

    Freq = Data1D(name="freqs", unit="", values=mag_dict["freqs"])
    axes = [Freq if x.name == "time" else x for x in data.axes]

    loss_data = DataFreq(name="Losses", unit="T", symbol="P", axes=axes, values=loss,)

    return loss_data
