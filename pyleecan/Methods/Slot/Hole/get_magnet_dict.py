def get_magnet_dict(self):
    """Return a dictionnary with all the magnets of the Hole

    Parameters
    ----------
    self : Hole
        A Hole object

    Returns
    -------
    magnet_dict : {Magnet}
        Dictionnary of magnet (key = magnet_X, value= Magnet or None)
    """

    if hasattr(self, "magnet_dict"):
        return self.magnet_dict
    else:
        ii = 0
        magnet_dict = dict()
        while hasattr(self, "magnet_" + str(ii)):
            magnet_dict["magnet_" + str(ii)] = getattr(self, "magnet_" + str(ii))
            ii += 1
        return magnet_dict
