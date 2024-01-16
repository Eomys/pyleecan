from numpy import array, pi
from numpy import sum as np_sum
from numpy import zeros


def comp_loss(self):
    """Calculate Windage losses
    Equation from "Design of Rotating Electrical Machines", Second Edition, Pyrhönen, Jokinen, Hrabovcovà p528

    Parameters
    ----------
    self: LossModelWindagePyrhonen
        a LossModelWindagePyrhonen object

    Returns
    -------
    Pjoule_density : ndarray
        loss density function of frequency and elements [W/m3]
    freqs: ndarray
        frequency vector [Hz]
    """

    if self.parent.parent is None:
        raise ValueError("Cannot calculate losses if simu is not in an Output")
    else:
        output = self.parent.parent.parent

    if output.elec is None:
        raise ValueError("Cannot calculate losses if OutElec is None")

    if self.parent.is_get_meshsolution and output.mag is None:
        raise ValueError("Cannot calculate losses if OutMag is None")

    machine = output.simu.machine

    OP = output.elec.OP
    felec = OP.get_felec()

    Dr = machine.rotor.Rext * 2
    L = machine.rotor.L1
    p = machine.get_pole_pair_number()
    rho = 1.225  # air density
    k = 1
    omega = 2 * pi / p * felec
    delta = machine.comp_length_airgap_active()
    mu = 18.5e-6  # Dynamic viscosity of air
    # Couette Reynolds number
    Re_delta = rho * omega * Dr * delta / (2 * mu)
    # ------------------------------------------ Warning ---------------------------------------------
    # As C_M depends on Re_delta, which depends on the frequency, the coefficient that will be stored
    # in the coeff_dict below depends on frequency. So the coefficient may change with frequency and should be
    # computed again. But to build the coeff_dict, the assumption that C_M will not change must be made.
    # ------------------------------------------------------------------------------------------------
    if Re_delta < 64:
        C_M = 10 * (2 * delta / Dr) ** 0.3 / Re_delta
    elif Re_delta < 5e2:
        C_M = 2 * (2 * delta / Dr) ** 0.3 / Re_delta ** 0.6
    elif Re_delta < 1e4:
        C_M = 1.03 * (2 * delta / Dr) ** 0.3 / Re_delta ** 0.5
    else:
        C_M = 0.065 * (2 * delta / Dr) ** 0.3 / Re_delta ** 0.2

    P1 = 1 / 32 * k * C_M * pi * rho * omega ** 3 * Dr ** 4 * L

    Dri = machine.rotor.Rint

    # tip Reynolds number
    Re_r = rho * omega * Dr ** 2 / (4 * mu)

    if Re_r < 3e5:
        C_M = 3.87 / Re_r ** 0.5
    else:
        C_M = 0.146 / Re_r ** 0.2

    P2 = 1 / 64 * C_M * rho * omega ** 3 * (Dr ** 5 - Dri ** 5)

    Ploss = P1 + P2

    power = 3

    coeff = Ploss / felec ** power

    per_a = output.geo.per_a
    if output.geo.is_antiper_a:
        per_a *= 2

    # Get surface elements for windings
    ms = output.mag.meshsolution
    Se = ms.mesh.get_element_area()[ms.group["rotor core"]]

    # Constant component and twice the electrical frequency have same joule density values
    freqs = array([felec])
    P_density = zeros((freqs.size, Se.size))
    P_density[0, :] = Ploss / (per_a * L * np_sum(Se))

    self.coeff_dict = {str(power): coeff}

    return P_density, freqs
