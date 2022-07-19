from numpy import gcd


def comp_periodicity_geo(self):
    """Compute the geometric periodicity factor of the lamination

    Parameters
    ----------
    self : lamination
        A lamination object

    Returns
    -------
    per_a : int
        Number of spatial periodicities of the lamination
    is_antiper_a : bool
        True if an spatial anti-periodicity is possible after the periodicities
    """

    if hasattr(self, "get_Zs"):
        Zs = self.get_Zs()

        nb_list = [Zs]
        # account for notches and bore
        if self.notch is not None:
            for notch in self.notch:
                nb_list.append(notch.comp_periodicity_spatial()[0])

        if self.bore:
            nb_list.append(self.bore.comp_periodicity_spatial()[0])
        if self.yoke:
            nb_list.append(self.yoke.comp_periodicity_spatial()[0])

        # compute the gcd of the list
        if len(nb_list) == 1:
            per_a = nb_list[0]
        else:
            per_a = gcd(nb_list[0], nb_list[1])
            for ii in range(2, len(nb_list)):
                per_a = gcd(per_a, nb_list[ii])

        nb_list.pop(0)
        is_antiper_a = False

        # Account for duct periodicity
        per_a, is_antiper_a = self.comp_periodicity_duct_spatial(per_a, is_antiper_a)
        per_a = int(per_a)

    else:
        per_a = None
        is_antiper_a = False

    return per_a, is_antiper_a
