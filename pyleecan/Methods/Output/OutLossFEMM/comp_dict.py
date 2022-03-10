def comp_dict(self):
    """Compute dict containing fft of magnetic quantities requested for loss calculation
    in LossFEMM model

    Parameter
    ---------
    self : OutLossFEMM
        an OutLossFEMM object

    """

    groups_core = ["stator core", "rotor core", "stator winding"]

    fft_dict = dict()
    surf_dict = dict()

    for group in groups_core:
        key = "B " + group
        if key not in fft_dict:
            # Get magnetic flux density complex amplitude over frequency and for each element center in current group
            fft_dict[key], surf_dict[group] = self.parent.mag.get_fft_from_meshsol(
                group, label="B"
            )

    group = "rotor magnets"
    key = "A_z " + group
    if key not in fft_dict:
        # Get magnetic vector potential complex amplitude over frequency and for each element center in rotor magnets
        fft_dict[key], surf_dict[group] = self.parent.mag.get_fft_from_meshsol(
            group, label="A_z"
        )

    self.fft_dict = fft_dict
    self.surf_dict = surf_dict
