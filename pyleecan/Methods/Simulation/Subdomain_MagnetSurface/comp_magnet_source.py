from numpy import pi, zeros, sinc, isinf, cos


def comp_magnet_source(self, rotor, sign_rot):
    """Method description

    Parameters
    ----------
    self: Subdomain_MagnetSurface
        a Subdomain_MagnetSurface object


    """

    self.permeability_relative = rotor.magnet.mat_type.mag.get_mur()
    Brm = rotor.magnet.mat_type.mag.get_Brm()
    p = rotor.get_pole_pair_number()
    taum = self.magnet_width / (pi / p)
    type_magnetization = rotor.magnet.type_magnetization
    n = self.k

    if type_magnetization == 0:
        # radial magnetization Fourier series
        self.Mrn = 2 * taum * Brm * sinc(n * taum / (2 * p))
        self.Mtn = zeros(n.size)

    elif type_magnetization == 1:
        # parallel magnetization Fourier series
        spos = sinc((n + 1) * taum / (2 * p))
        sneg = sinc((n - 1) * taum / (2 * p))
        self.Mrn = Brm * taum * (spos + sneg)
        self.Mtn = Brm * taum * (spos - sneg)

    elif type_magnetization == 2:
        # Hallbach magnetization
        Mrn = (
            4
            * taum
            / pi
            * Brm
            * cos(n * pi * taum / (2 * p))
            / (1 - (n * taum / p) ** 2)
        )
        Mrn[isinf(Mrn)] = p / taum * Brm / n(isinf(Mrn))
        Mtn = sign_rot * taum / p * n * Mrn
        Mtn[isinf(Mrn)] = sign_rot * Mrn[isinf(Mrn)]

    # removing harmonics not multiple of n*p+1
    In = (n / p % 2) != 1
    self.Mrn[In] = 0
    self.Mtn[In] = 0
