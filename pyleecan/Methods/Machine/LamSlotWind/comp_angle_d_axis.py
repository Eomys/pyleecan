from numpy import pi, argmax, cos, abs as np_abs, angle as np_angle


def comp_angle_d_axis(self):
    """Compute the angle between the X axis and the first d+ axis
    By convention a "Tooth" is centered on the X axis

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object

    Returns
    -------
    d_angle : float
        angle between the X axis and the first d+ axis
    """
    
    (sym_a, _) = self.comp_sym()
    
    p = self.get_pole_pair_number()

    MMF = self.comp_mmf_unit(Nt=1, Na=400 * p)

    MMF.values = MMF.values[None, :]  # TODO: correct bug in SciDataTool
        
    # Get angle values
    results1 = MMF.get_along("angle")
    angle_stator = results1["angle"]   
           
    # Get the unit mmf FFT and wavenumbers
    results = MMF.get_along("wavenumber")
    wavenumber = results["wavenumber"]
    mmf_ft = results[MMF.symbol]

    # Find the angle where the FFT is max
    indr_fund = np_abs(wavenumber - p/sym_a).argmin()
    phimax = np_angle(mmf_ft[indr_fund])
    magmax = np_abs(mmf_ft[indr_fund])
    
    # Reconstruct fundamental MMF wave
    mmf_waveform = magmax * cos(p * angle_stator + phimax)
    
    # Find index of maximum
    ind_max = argmax(mmf_waveform)
    
     # Get the first angle according to symmetry    
    d_angle = (angle_stator[ind_max]) % (2 * pi / sym_a)
       
    # import matplotlib.pyplot as plt
    # import numpy as np
    
    # fig,ax = plt.subplots()
    # ax.plot(angle_stator, np.squeeze(MMF.values), 'k')
    # ax.plot(angle_stator, mmf_waveform, 'r')
    # ax.plot([d_angle, d_angle], [-magmax,magmax], '--k')

    return d_angle 
