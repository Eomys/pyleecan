import numpy as np
from SciDataTool import Data1D, DataTime, VectorField


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
    Brphiz = output.mag.B.get_rphiz_along("time", "angle")
    Br = Brphiz["radial"]
    Bt = Brphiz["tangential"]
    Bz = Brphiz["axial"]
    time = Brphiz["time"]
    angle = Brphiz["angle"]

    # Compute AGSF with MT formula
    Prad = -(Br * Br - Bt * Bt - Bz * Bz) / (2 * mu_0)
    Ptan = -Br * Bt / mu_0
    Pz = -Br * Bz / mu_0

    # Store the results
    Time = Data1D(name="time", unit="s", values=time)
    Angle = Data1D(name="angle", unit="rad", values=angle)
    Prad_data = DataTime(
        name="Airgap radial surface force",
        unit="N/m2",
        symbol="P_r",
        axes=[Time, Angle],
        values=Prad,
    )
    Prad_freq = Prad_data.time_to_freq()
    Ptan_data = DataTime(
        name="Airgap tangential surface force",
        unit="N/m2",
        symbol="P_t",
        axes=[Time, Angle],
        values=Ptan,
    )
    Ptan_freq = Ptan_data.time_to_freq()
    Pz_data = DataTime(
        name="Airgap axial surface force",
        unit="N/m2",
        symbol="P_z",
        axes=[Time, Angle],
        values=Pz,
    )
    Pz_freq = Pz_data.time_to_freq()
    output.force.P = VectorField(
        name="Magnetic airgap surface force",
        symbol="P",
        components={"radial": Prad_freq, "tangential": Ptan_freq, "axial": Pz_freq},
    )
