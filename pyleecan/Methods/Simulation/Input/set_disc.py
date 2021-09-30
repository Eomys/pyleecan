NT_MAX = 4096
NA_MAX = 2048


def set_disc(self, machine):
    """Set the value of Nt_tot and Na_tot according to a machine

    Parameters
    ----------
    self : Input
        An Input object
    machine : Machine
        A machine object to adapt the discretization
    """

    pert, is_apert, _, _ = machine.comp_periodicity_time()  # Stator
    if is_apert:
        pert = pert * 2

    self.Nt_tot = int(round(NT_MAX / pert)) * pert

    pera, is_apera = machine.comp_periodicity_spatial()

    if is_apera:
        pera = pera * 2

    if hasattr(machine.stator, "get_Zs"):
        # Na_tot/pera must be multiple of Zs for lumped force calculation in time space domain
        Zs = machine.stator.get_Zs()
    else:
        Zs = 1

    self.Na_tot = int(round(NA_MAX / Zs / pera) * Zs * pera)

    self.get_logger().debug(
        "Setting automatic discretization: Nt_tot="
        + str(self.Nt_tot)
        + ", Na_tot="
        + str(self.Na_tot)
    )
