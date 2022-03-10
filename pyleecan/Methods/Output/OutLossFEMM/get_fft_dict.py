def get_fft_dict(self):
    """Get dict containing fft of magnetic quantities requested for loss calculation
    in LossFEMM model

    Parameter
    ---------
    self : OutLossFEMM
        an OutLossFEMM object

    Return
    ------
    fft_dict : {ndarray}
        Dict of FFT quantities for each group

    """

    if self.fft_dict is None:
        self.comp_dict()

    return self.fft_dict
