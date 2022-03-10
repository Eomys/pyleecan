def get_surf_dict(self):
    """Get dict containing surface elemetns of magnetic quantities requested for loss calculation
    in LossFEMM model

    Parameter
    ---------
    self : OutLossFEMM
        an OutLossFEMM object

    Return
    ------
    surf_dict : {ndarray}
        Dict of surface elements for each group

    """

    if self.surf_dict is None:
        self.comp_dict()

    return self.surf_dict
