# -*- coding: utf-8 -*-

from pyleecan.Classes.OutGeoLam import OutGeoLam


def comp_output_geo(self):
    """Compute the main geometry output

    Parameters
    ----------
    self : Lamination
        A Lamination object

    Returns
    -------
    output: OutGeoLam
        Main geometry output of the lamintion

    """

    output = OutGeoLam()
    output.name_phase = self.get_name_phase()
    output.BH_curve = self.mat_type.mag.get_BH()

    return output
