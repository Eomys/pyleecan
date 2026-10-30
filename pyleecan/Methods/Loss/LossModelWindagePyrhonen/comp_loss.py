from numpy import array, zeros
from numpy import sum as np_sum


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
    L = machine.rotor.L1
    OP = output.elec.OP
    felec = OP.get_felec()

    Ploss = self.comp_loss_value()

    power = 3

    coeff = Ploss / felec**power

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
