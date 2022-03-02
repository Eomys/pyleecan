from ....Functions.load import import_class


def comp_periodicity_spatial(self):
    """Compute the periodicity factor of the lamination
    Parameters
    ----------
    self : LamSquirrelCage
        A LamSquirrelCage object
    Returns
    -------
    per_a : int
        Number of spatial periodicities of the lamination
    is_antiper_a : bool
        True if an spatial anti-periodicity is possible after the periodicities
    """

    # Reuse method from Lamination instead of LamSlotWind since winding periodicity is given by lamination periodicity
    Lamination = import_class("pyleecan.Classes", "Lamination")

    per_a, is_antiper_a = Lamination.comp_periodicity_spatial(self)

    return per_a, is_antiper_a