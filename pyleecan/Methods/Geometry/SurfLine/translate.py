def translate(self, Zt):
    """Translate the surface

    Parameters
    ----------
    self : SurfLine
        A SurfLine object

    Zt : complex
        Complex value for translation

    Returns
    -------
    None
    """
    if Zt == 0:
        return  # Nothing to do
    # Check if the Surface is correct
    self.check()

    # Translation  of every line in the Surface
    for line in self.line_list:
        line.translate(Zt)

    if self.point_ref is not None:
        self.point_ref += Zt
