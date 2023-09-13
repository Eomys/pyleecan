from ....Classes.Lamination import Lamination


def comp_periodicity(self):
    """Computes the winding matrix (anti-)periodicity

    Parameters
    ----------
    self : WindingSC
        A WindingSC object

    Returns
    -------
    per_a: int
        Number of spatial periods of the winding
    is_aper_a: bool
        True if the winding is anti-periodic over space

    """

    lamination = self.parent

    if lamination is not None:
        # Call comp_periodicity of Lamination class since squirrel cage periodicity
        # depends on lamination properties: number of pole pairs and number of slots
        per_a, is_aper_a = Lamination.comp_periodicity_spatial(lamination)

        if is_aper_a:
            # Multiply periodicity by 2 to be compliant with Winding.comp_periodicity()
            per_a = int(2 * per_a)

        return per_a, is_aper_a

    else:
        return None, False
