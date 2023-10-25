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

    Nmat = (
        self.stator_slot.get_constants_number()
        + self.airgap.get_constants_number()
        + self.magnet_surface.get_constants_number()
    )

    mat = np.zeros((Nmat, Nmat))

    vect = np.zeros((Nmat, angle_rotor.size))

    self.rotor_magnet_surface.comp_interface_airgap(self.airgap, mat, vect, angle_rotor)

    per_a = self.per_a
    is_antiper_a = self.is_antiper_a

    self.stator_slot.comp_interface_airgap(self.airgap, mat, vect, per_a, is_antiper_a)
