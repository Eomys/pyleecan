from numpy import diff, zeros, newaxis


def comp_emf(self):
    """Compute the Electromotive force [V]
    
    Parameters
    ----------
    self : OutMag
        an OutMag object

    """
    
    Phi_wind = self.Phi_wind_stator
    phi_wind = Phi_wind.get_along("time[smallestperiod]", "phase")[Phi_wind.symbol]    
    
    time = self.Time.get_values(is_oneperiod=False)
    
    #Calculate EMF and store it in OutMag
    if time.size > 1:
        emf = zeros(phi_wind.size)
        emf[:-1, :] = diff(phi_wind, 1, 0) / diff(time, 1, 0)[:, newaxis]
        # We approximate the phi_wind to be periodic to compute the last value
        # And we assume time to be a linspace
        emf[-1] = (phi_wind[0] - phi_wind[-1]) / (time[1] - time[0])
        
        EMF = Phi_wind.copy()
        EMF.values = emf
    
        self.emf = EMF
