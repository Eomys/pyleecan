from ....Functions.Winding.gen_phase_list import gen_name


def get_name_phase(self):
    """Return the name of the winding phases

    Parameters
    ----------
    self : Lamination
        A Lamination object

    Returns
    -------
    name_phase: list
        Empty list

    """
    if (
        not hasattr(self, "winding")
        or self.winding is None
        # or self.winding.conductor is None
    ):
        return list()
    return gen_name(self.winding.qs)
