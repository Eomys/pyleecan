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
    self.airgap = Subdomain_Airgap(
        Rrbo=Rrbo,
        Rsbo=Rsbo,
        k=arange(per_a, antiper_a * per_a, Nhag),
    )

    # Define rotor surface magnets subdomain
    self.rotor_magnet_surface = Subdomain_MagnetSurface(
        number=polar_eq.rotor.get_Zs(),
        magnet_width=polar_eq.rotor.slot.comp_angle_active_eq(),
        Rbore=Rrbo,
        Ryoke=Rrbo - sign_rot * polar_eq.rotor.slot.Hmag,
        k=self.airgap.k,
    )

    # Define stator slots subdomains
    slotS = polar_eq.stator.slot
    if slotS.H0 > 0:
        self.stator_slot = Subdomain_SlotOpening()
    else:
        self.stator_slot = Subdomain_Slot()
    Nhss = max([floor(slotS.W2 * Nhag / pi), 2])
    theta_i0 = 0
    self.stator_slot.number = Zs
    self.stator_slot.center_angle = 2 * pi / Zs * arange(0, Zs0) + theta_i0
    self.stator_slot.slot_width = slotS.W2
    self.stator_slot.Rbore = Rsbo
    self.stator_slot.Ryoke = Rsbo + sign_rot * (slotS.H0 + slotS.H2)
    self.stator_slot.k = arange(1, Nhss)
    if slotS.H0 > 0:
        # Define stator slots opening subdomains
        Nhso = max([floor(slotS.W0 * Nhag / pi), 2])
        self.stator_slot.Ropening = Rsbo + sign_rot * slotS.H0
        self.stator_slot.opening_width = slotS.W0
        self.stator_slot.v = arange(1, Nhso)
