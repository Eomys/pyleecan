from pyleecan.Functions.Winding.comp_wind_sym import comp_wind_sym


def comp_sym(self):
    """Compute the symmetry of the Lamination (according to its winding)
    """

    wind_mat = self.winding.comp_connection_mat(self.slot.Zs)
    return comp_wind_sym(wind_mat)[0]
