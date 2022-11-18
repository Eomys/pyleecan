from ....Classes.SurfLine import SurfLine


def get_surface(self):
    """Returns the bore shape as a Surface object

    Parameters
    ----------
    self : Bore
        A Bore object

    Returns
    -------
    Sbore : Surface
        Surface object to draw the bore
    """

    line_list = self.get_bore_line()

    return SurfLine(line_list=line_list, point_ref=0, label="Bore")
