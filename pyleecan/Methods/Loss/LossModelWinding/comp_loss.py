from numpy import array
from numpy import sum as np_sum
from numpy import zeros

from ....Functions.Electrical.comp_loss_joule import comp_loss_joule


def comp_loss(self):
    """Calculate joule losses in stator windings

    Parameters
    ----------
    self: LossModelWinding
        a LossModelWinding object

    Returns
    -------
    Pjoule_density : ndarray
        Joule loss density function of frequency and elements [W/m3]
    freqs: ndarray
        frequency vector [Hz]
    """

    if self.parent.parent is None:
        raise ValueError("Cannot calculate joule losses if simu is not in an Output")
    else:
        output = self.parent.parent.parent

    if output.elec is None:
        raise ValueError("Cannot calculate joule losses if OutElec is None")

    if self.parent.is_get_meshsolution and output.mag is None:
        raise ValueError("Cannot calculate joule losses if OutMag is None")

    machine = output.simu.machine

    OP = output.elec.OP
    felec = OP.get_felec()

    lam = machine.stator
    T_op = self.parent.Tsta

    Rs = lam.comp_resistance_wind(T=T_op)
    qs = lam.winding.qs

    if self.type_skin_effect > 0:
        # Account for skin effect
        k = self.comp_coeff(
            T_op=T_op,
        )
    else:
        k = 0

    # Calculate overall joule losses
    Id_Iq = OP.get_Id_Iq()
    coeff = qs * Rs * (Id_Iq["Id"] ** 2 + Id_Iq["Iq"] ** 2)
    Pjoule = coeff * (1 + k * felec**2)

    per_a = output.geo.per_a
    if output.geo.is_antiper_a:
        per_a *= 2

    Lst = lam.L1

    # Get surface elements for windings
    ms = output.mag.meshsolution
    Se = ms.mesh.get_element_area()[ms.group[self.group]]

    # Constant component and twice the electrical frequency have same joule density values
    freqs = array([felec])
    Pjoule_density = zeros((freqs.size, Se.size))
    Pjoule_density[0, :] = Pjoule / (per_a * Lst * np_sum(Se))

    A = coeff * k
    B = coeff
    self.coeff_dict = {"2": A, "0": B}

    return Pjoule_density, freqs
