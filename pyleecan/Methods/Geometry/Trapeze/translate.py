# -*-- coding: utf-8 -*


def translate(self, Zt):
    """Translate the Trapeze

    Parameters
    ----------
    self : Trapeze
        a Trapeze object

    Zt : complex
        Complex value for translation

    Returns
    -------
    None
    """
    if Zt == 0:
        return  # Nothing to do
    # check if the Trapeze is correct
    self.check()
    self.point_ref += Zt
