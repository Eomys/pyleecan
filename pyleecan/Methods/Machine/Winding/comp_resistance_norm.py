# from ....Methods.Machine.Winding import WindingError


def comp_resistance_norm(self, T=20):
    """Compute the winding resistance per meter,
    i.e. winding resistance divided by coil side length (including end winding).
    The actual winding resistance is comp_resistance_norm * (length_active + length_end_winding)

    Parameters
    ----------
    self : Winding
        A Winding object

    T : float
        Winding Temperature [°C]

    Returns
    -------
    winding_resistance_norm: float
        normalized winding resistance

    """
    cond_surf = self.conductor.comp_surface_active()
    cond_rho = self.conductor.cond_mat.elec.rho  # Specific Resistivity
    alpha = self.conductor.cond_mat.elec.alpha  # Temperature Coefficient
    Npcpp = self.Npcpp  # Number of Parallel Circuits per Phase
    Ntspc = self.comp_Ntspc()  # Number of Turns in Series per Phase

    kT = 1 + alpha * (T - 20)
    winding_resistance_norm = 2 * Ntspc * cond_rho * kT / (cond_surf * Npcpp)

    return winding_resistance_norm
