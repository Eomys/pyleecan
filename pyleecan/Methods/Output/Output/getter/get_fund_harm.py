# -*- coding: utf-8 -*-
from SciDataTool import VectorField
from .....Functions.Plot import fft_dict


def get_fund_harm(self, data):
    """Return the fundamental harmonic of the physical quantity in the data object

    Parameters
    ----------
    self : Output
        an Output object
    data : Data
        a Data object

    Returns
    -------
    fund_harm: dict
        Dict containing axis name as key and frequency/order/wavenumber of fundamental harmonic as value

    """

    if data.symbol in ["B", "P", "Is", "Phi_{wind}"]:

        # Init output dict
        fund_harm = dict()

        # Extract first component in case of VectorField
        if isinstance(data, VectorField):
            comp_keys = list(data.components.keys())
            axes_list = data.components[comp_keys[0]].axes
        else:
            axes_list = data.axes

        # Get machine pole pair number
        p = self.simu.machine.get_pole_pair_number()

        # Get electrical fundamental frequency
        f_elec = self.simu.input.comp_felec()

        # Loop on axes to express the fundamental harmonic of the Data object
        # including normalizations
        for axe in axes_list:
            # Init fundamental value to None for current axis
            coeff = None

            # Search if the current axis in SciDataTool axis dictionnary
            if axe.name in fft_dict.keys():
                # If yes, find the axis name of the fft
                axe_fft = fft_dict[axe.name]

                # Assign fundamental value depending on axis name
                if axe.name == "time":
                    coeff = f_elec
                elif axe.name == "angle":
                    coeff = p

                # Add in fund_harm dict the values with different normalizations
                if coeff is not None:
                    # Assign fundamental value depending on physical quantity
                    if data.symbol == "P":
                        coeff = 2 * coeff
                    # Store value in dict
                    fund_harm[axe_fft] = coeff

                    # Add also normalizations in dict
                    for key, val in axe.normalizations.items():
                        fund_harm[key] = fund_harm[axe_fft] / val

    # Cannot calculate dict of fundamental harmonic values
    else:
        fund_harm = None

    return fund_harm
