import numpy as np
from SciDataTool import DataLinspace, DataTime


def comp_force(self, output):
    """Compute the air-gap surface force based on Maxwell Tensor (MT).

    Parameters
    ----------
    self : ForceMT
        A ForceMT object

    output : Output
        an Output object (to update)
    """

    mu_0 = 4 * np.pi * 1e-7
    angle = output.force.angle
    Na_tot = output.force.Na_tot
    time = output.force.time
    Nt_tot = output.force.Nt_tot

    # Load magnetic flux
    Br = output.mag.Br.values
    Bt = output.mag.Bt.values

    # Compute AGSF with MT formula
    Prad = (Br * Br - Bt * Bt) / (2 * mu_0)
    Ptan = Br * Bt / mu_0

    # Store the results
    Time = DataLinspace(
        name="time",
        unit="s",
        symmetries={},
        initial=time[0],
        final=time[-1],
        number=Nt_tot,
    )

    Angle = DataLinspace(
        name="angle",
        unit="rad",
        symmetries={},
        initial=angle[0],
        final=angle[-1],
        number=Na_tot,
    )
    output.force.Prad = DataTime(
        name="Airgap radial surface force",
        unit="T",
        symbol="P_r",
        axes=[Time, Angle],
        values=Prad,
    )
    output.force.Ptan = DataTime(
        name="Airgap radial surface force",
        unit="T",
        symbol="P_t",
        axes=[Time, Angle],
        values=Ptan,
    )
