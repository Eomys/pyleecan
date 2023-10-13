from numpy import pi, arange, floor

from ....Classes.Subdomain_Airgap import Subdomain_Airgap
from ....Classes.Subdomain_MagnetSurface import Subdomain_MagnetSurface
from ....Classes.Subdomain_Slot import Subdomain_Slot
from ....Classes.Subdomain_SlotOpening import Subdomain_SlotOpening


def set_subdomains(self, Nharm_coeff=1):
    """Method to calcul

    Parameters
    ----------
    self: SubdomainModel_SPMSM
        a SubdomainModel_SPMSM object


    """

    per_a = self.per_a
    antiper_a = 2 if self.is_antiper_a else 1
    polar_eq = self.machine_polar_eq
    Rrbo = polar_eq.rotor.comp_radius_mec()
    Rsbo = polar_eq.stator.comp_radius_mec()
    Zs = polar_eq.stator.get_Zs()
    Zs0 = int(Zs / per_a / antiper_a)
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
        radius_min=min(radii),
        radius_max=max(radii),
        k=arange(per_a, antiper_a * per_a, Nhag),
    )

    # Define rotor surface magnets subdomain
    radii = [Rrbo, Rsbo - sign_rot * polar_eq.rotor.slot.Hmag]
    self.rotor_magnet_surface = Subdomain_MagnetSurface(
        number=polar_eq.rotor.get_Zs(),
        magnet_width=polar_eq.rotor.slot.comp_angle_active_eq(),
        radius_min=min(radii),
        radius_max=max(radii),
        k=self.airgap.k,
    )

    # Define stator slots subdomains
    if polar_eq.stator.slot.H0 > 0:
        self.stator_slot = Subdomain_SlotOpening()
    else:
        self.stator_slot = Subdomain_Slot()
    Nhss = max([floor(polar_eq.stator.slot.W2 * Nhag / pi), 2])
    radii = [
        Rsbo + sign_rot * polar_eq.stator.slot.H0,
        Rsbo + sign_rot * (polar_eq.stator.slot.H0 + polar_eq.stator.slot.H2),
    ]
    theta_i0 = 0
    self.stator_slot.number = Zs
    self.stator_slot.center_angle = 2 * pi / Zs * arange(0, Zs0) + theta_i0
    self.stator_slot.slot_width = polar_eq.stator.slot.W2
    self.stator_slot.radius_min = min(radii)
    self.stator_slot.radius_max = max(radii)
    self.stator_slot.k = arange(1, Nhss)
    if polar_eq.stator.slot.H0 > 0:
        # Define stator slots opening subdomains
        Nhso = max([floor(polar_eq.stator.slot.W0 * Nhag / pi), 2])
        self.stator_slot.opening_width = polar_eq.stator.slot.W0
        self.stator_slot.v = arange(1, Nhso)
