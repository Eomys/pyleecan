def comp_periodicity_spatial(self):
    """Compute the periodicity factor of the lamination

    Parameters
    ----------
    self : LamSlotMulti
        A LamSlotMulti object

    Returns
    -------
    per_a : int
        Number of spatial periodicities of the lamination
    is_antiper_a : bool
        True if an spatial anti-periodicity is possible after the periodicities
    """

    if self.sym_dict_enforced is not None:
        self.get_logger().debug("Enforcing symmetry for LamSlotMulti")
        return (
            self.sym_dict_enforced["per_a"],
            self.sym_dict_enforced["is_antiper_a"],
        )
    else:
        # Zs = self.get_Zs()
        is_aper = False
        # TODO compute it
        self.get_logger().debug("Symmetry not available yet for LamSlotMulti")
        return 1, is_aper
