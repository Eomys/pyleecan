from numpy import interp


def get_parameters(self, Tsta=None, felec=None):
    """Get the parameters dict for the ELUT at the operationnal temperature and frequency
    Parameters
    ----------
    self : ELUT
        an ELUT object

    Returns
    ----------
    param_dict : dict
        a Dict object
    """


param_dict = dict()

alphasw = self.cond_mat.elec.alpha

# stator winding phase resistance, skin effect correction
if felec is None:
    Rs_freq = self.Rs
else:
    Rs_dc = self.Rs  # DC resistance at Tsta_ref
    K_RSE_sta = self.K_RSE_sta  # skin effect factor for resistance
    Rs_freq = Rs_dc * interp(K_RSE_sta[0, :], K_RSE_sta[1, :], felec)

# stator winding phase resistance, temperature correction
if Tsta is not None:
    Rs_freq_temp = Rs_freq
else:
    Tsta_ref = self.Tsta_ref  # ref temperature
    Rs_freq_temp = Rs_freq * (1 + alphasw * (Tsta - Tsta_ref))

param_dict["Rs"] = Rs_freq_temp


# stator winding phase leakage inductance, skin effect correction
if felec is None:
    Ls_freq = self.Ls
else:
    Ls_dc = self.Ls  # DC resistance
    K_ISE_sta = self.K_ISE_sta  # skin effect factor for leakage inductance
    Ls_freq = Ls_dc * interp(K_ISE_sta[0, :], K_ISE_sta[1, :], felec)

param_dict["Ls"] = Ls_freq

return param_dict
