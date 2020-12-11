from ....Functions.Load.import_class import import_class


def convert_to_UD(self):
    """Convert the hole to HoleUD"""
    HoleUD = import_class("pyleecan.Classes", "HoleUD")
    surf_list = self.build_geometry()
    magnet_dict = self.get_magnet_dict()

    return HoleUD(
        surf_list=surf_list, magnet_dict=magnet_dict, Zh=self.Zh, mat_void=self.mat_void
    )
