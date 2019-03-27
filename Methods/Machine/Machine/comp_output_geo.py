# -*- coding: utf-8 -*-

from pyleecan.Classes.OutGeo import OutGeo


def comp_output_geo(self):
    """Compute the main geometry output

    Parameters
    ----------
    self : Machine
        A Machine object

    Returns
    -------
    output: OutGeo
        Main geometry output of the machine

    """

    output = OutGeo()
    output.Wgap_mec = self.comp_width_airgap_mec()
    output.Wgap_mag = self.comp_width_airgap_mag()
    output.Rgap_mec = self.comp_Rgap_mec()
    output.Lgap = self.comp_length_airgap_active()

    output.stator = self.stator.comp_output_geo()
    output.rotor = self.rotor.comp_output_geo()

    return output
