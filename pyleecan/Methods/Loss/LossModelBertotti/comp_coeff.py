import numpy as np
from scipy.optimize import curve_fit


@staticmethod
def comp_loss_val(xdata, k_hy, k_ed, k_ex, alpha_B):
    """A function that compute the loss with respect to the maximum value and the frequency of the magnetic flux density

    Parameters
    ----------
    xdata : ndarray
        input matrix with f in the first line and B in the second line
    k_hy : float
        hysteresis loss coefficient
    k_ed : float
        Eddy current loss coefficient
    k_ex : float
        excess loss coefficient
    alpha_B : float
        hysteresis flux density amplitude exponent

    Returns
    -------
    loss : ndarray
        loss for each value of f and B in the input array
    """

    f = xdata[0]
    B = xdata[1]

    return k_hy * f * B**alpha_B + k_ed * (f * B) ** 2 + k_ex * (f * B) ** 1.5


def comp_coeff(self, material):
    """Enables to compute the coefficients of the loss model with a curve fitting
    on loss data stored in the material (stored in self.k_hy, self.k_ed, self.k_ex)

    Parameters
    ----------
    self : LossModelBertotti
        A loss model to compute Bertotti losses
    material : Material
        A material object, corresponding to the material used in the electrical machine.
        This material object must contain loss data as an ImportMatrixVal object.
        This matrix must contain 3 rows, correspoding to the excitation frequency (Hz),
        the peak magnetic flux density (T), and the loss density (W/kg) in this order.
    """

    parameter_names = ["k_hy", "k_ed", "k_ex", "alpha_B"]
    parameters = [getattr(self, name) for name in parameter_names]
    free_indices = [index for index, value in enumerate(parameters) if value is None]

    def comp_loss(xdata, *free_parameters):
        """A function that compute the loss with respect to the maximum value and the frequency of the magnetic flux density

        Parameters
        ----------
        xdata : ndarray
            input matrix with f in the first line and B in the second line
        *free_parameters : float
            Values of the coefficients that are not fixed on the loss model

        Returns
        -------
        loss : ndarray
            loss for each value of f and B in the input array
        """

        fitted_parameters = parameters.copy()
        for index, value in zip(free_indices, free_parameters):
            fitted_parameters[index] = value

        return comp_loss_val(xdata, *fitted_parameters)

    loss_data = material.mag.LossData.get_data()

    f = loss_data[0]
    B = loss_data[1]
    loss = loss_data[2]

    xdata = np.array([f, B])
    ydata = np.array(loss)

    if free_indices:
        popt, _ = curve_fit(
            comp_loss,
            xdata,
            ydata,
            p0=np.ones(len(free_indices)),
            bounds=(
                np.zeros(len(free_indices)),
                np.full(len(free_indices), np.inf),
            ),
        )

        for index, value in zip(free_indices, popt):
            setattr(self, parameter_names[index], value)
