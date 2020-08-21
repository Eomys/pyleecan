from ....Classes.SurfLine import SurfLine


def get_surfaces(self):
    """Convert surf_dict to a list of surfaces without lines
    """

    surf_list = list()

    for key, value in self.surf_dict.items():
        surf_list.append(SurfLine(line_list=[], point_ref=key, label=value))

    return surf_list
