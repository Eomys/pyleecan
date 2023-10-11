from numpy import pi, arange, floor

from ....Classes.Subdomain_Airgap import Subdomain_Airgap
from ....Classes.Subdomain_MagnetSurface import Subdomain_MagnetSurface
from ....Classes.Subdomain_SlotWinding import Subdomain_SlotWinding
from ....Classes.Subdomain_SlotOpening import Subdomain_SlotOpening


def set_subdomains(self, Nharm_coeff=1):
    """Method to calcul

    Parameters
    ----------
    self: SubdomainModel_SPMSM
        a SubdomainModel_SPMSM object


    """
    polar_eq = self.machine_polar_eq
    Rrbo = polar_eq.rotor.comp_radius_mec()
    Rsbo = polar_eq.stator.comp_radius_mec()
    Zs = polar_eq.stator.get_Zs()
    Zs0 = int(Zs / self.per_a)
    p = polar_eq.get_pole_pair_number()

    # Checking internal or external rotor
    if polar_eq.rotor.is_internal:
        sign_rot = 1
    else:
        sign_rot = -1

    # Define airgap subdomain
    Nhag = floor(Nharm_coeff * 10 * Zs + p)
    radii = [Rrbo, Rsbo]
    self.airgap = Subdomain_Airgap(
        periodicity=1,
        angular_width=2 * pi,
        radius_min=min(radii),
        radius_max=max(radii),
        k=arange(self.per_a, self.antiper_a * self.per_a, Nhag),
    )

    # Define stator slots subdomains
    Nhss = max([floor(polar_eq.stator.slot.W2 * Nhag / pi), 2])
    radii = [
        Rsbo + sign_rot * polar_eq.stator.slot.H0,
        Rsbo + sign_rot * (polar_eq.stator.slot.H0 + polar_eq.stator.slot.H2),
    ]
    self.stator_slot = Subdomain_SlotWinding(
        periodicity=Zs,
        center_angle=arange(0, Zs0) + 1,
        angular_width=polar_eq.stator.slot.W2,
        radius_min=min(radii),
        radius_max=max(radii),
        k=arange(1, Nhss),
    )

    # Define rotor surface magnets subdomain
    radii = [Rrbo, Rsbo - sign_rot * polar_eq.rotor.slot.Hmag]
    self.rotor_magnet_surface = (
        Subdomain_MagnetSurface(
            periodicity=int(2 * p / self.periodicity),
            angular_width=polar_eq.rotor.slot.Wmag,
            radius_min=min(radii),
            radius_max=max(radii),
            k=self.airgap.k,
        ),
    )

    if polar_eq.stator.slot.H0 > 0:
        # Define stator slots opening subdomains
        Nhso = max([floor(d * Nhag / pi), 2])
        radii = [Rsbo, Rsbo + sign_rot * polar_eq.stator.slot.H0]
        self.stator_slot_opening = Subdomain_SlotOpening(
            periodicity=Zs,
            center_angle=self.stator_slot.center_angle,
            angular_width=polar_eq.stator.slot.W0,
            radius_min=min(radii),
            radius_max=max(radii),
            k=arange(1, Nhso),
        )
