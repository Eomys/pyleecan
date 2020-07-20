import numpy as np
from SciDataTool import Data1D, DataFreq, VectorField


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

    # Load magnetic flux
    Brphiz = output.mag.B.get_rphiz_along("freqs", "wavenumber")
    Br = Brphiz["radial"]
    Bt = Brphiz["tangential"]
    Bz = Brphiz["axial"]
    freqs = Brphiz["freqs"]
    wavenumber = Brphiz["wavenumber"]

    # Compute AGSF with MT formula
    Prad = -(Br * Br - Bt * Bt - Bz * Bz) / (2 * mu_0)
    Ptan = -Br * Bt / mu_0
    Pz = -Br * Bz / mu_0

    # Store the results
    Freqs = Data1D(name="freqs", unit="Hz", values=freqs,)
    Wavenumber = Data1D(name="wavenumber", unit="dimless", values=wavenumber,)
    Prad_data = DataFreq(
        name="Airgap radial surface force",
        unit="N/m2",
        symbol="P_r",
        axes=[Freqs, Wavenumber],
        values=Prad,
    )
    Ptan_data = DataFreq(
        name="Airgap tangential surface force",
        unit="N/m2",
        symbol="P_t",
        axes=[Freqs, Wavenumber],
        values=Ptan,
    )
    Pz_data = DataFreq(
        name="Airgap axial surface force",
        unit="N/m2",
        symbol="P_z",
        axes=[Freqs, Wavenumber],
        values=Pz,
    )
    output.force.P = VectorField(
        name="Magnetic airgap surface force",
        symbol="P",
        components={"radial": Prad_data, "tangential": Ptan_data, "axial": Pz_data},
    )
