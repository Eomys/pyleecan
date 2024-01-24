from numpy import zeros
from numpy.linalg import solve as np_solve


def solve(self, angle, angle_rotor):
    """Method description

    Parameters
    ----------
    self: SubdomainModel_SPMSM
        a SubdomainModel_SPMSM object

    Returns
    ----------
    var: type
        var description
    """

    # Init topological matrix and source vector
    Nmat = sum(self.csts_number)
    self.mat = zeros((Nmat, Nmat))
    self.vect = zeros((Nmat, angle_rotor.size))

    # Build interface conditions between rotor and airgap
    self.rotor_magnet_surface.comp_interface_airgap(angle_rotor)

    # Build interface conditions between stator and airgap
    self.stator_slot.comp_interface_airgap()

    # Solve linear system
    Csts = np_solve(self.mat, self.vect)

    # Store integration constants in subdomain
    self.store_constants(Csts)

    # Get airgap flux density at mean radius
    Rag = (self.airgap.Rrbo + self.airgap.Rsbo) / 2
    Br, Btheta = self.airgap.comp_flux_density(Rag, angle)

    Tem = self.airgap.comp_torque()

    Phi_wind_stator = self.stator_slot.comp_Phi_wind()

    return Br, Btheta, Tem, Phi_wind_stator
