from pyleecan.Functions.Geometry.merge_notch_list import merge_notch_list


def get_notch_list(self, sym=1):
    """Returns an ordered description of the notches
    """

    if len(self.notch) == 0:
        return list()
    else:
        notch_list = self.notch[0].get_notch_list(sym=sym)
        for ii in range(len(self.notch) - 1):
            notch_list = merge_notch_list(
                notch_list, self.notch[ii + 1].get_notch_list(sym=sym)
            )
        return notch_list
