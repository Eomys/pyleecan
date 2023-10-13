import numpy as np


def solve(self, angle_rotor):
    """Method description

    Parameters
    ----------
    self: SdmSPMSM
        a SdmSPMSM object

    Returns
    ----------
    var: type
        var description
    """

    mat = np.zeros()

    vect = np.zeros()

    self.rotor_magnet_surface.comp_interface_airgap_magnet(mat, vect)

    self.stator_slot.comp_interface_airgap_slot(mat, vect)
