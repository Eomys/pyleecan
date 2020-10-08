from numpy import pi, array, all as np_all
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

    mu_0 = 4 * pi * 1e-7

    # Load magnetic flux
    Brphiz = output.mag.B.get_rphiz_along(
        "time[smallestperiod]", "angle[smallestperiod]"
    )
    Br = Brphiz["radial"]
    Bt = Brphiz["tangential"]
    Bz = Brphiz["axial"]

    # Compute AGSF with MT formula
    Prad = (Br * Br - Bt * Bt - Bz * Bz) / (2 * mu_0)
    Ptan = Br * Bt / mu_0
    Pz = Br * Bz / mu_0

    # Store the results
    components = {}
    if not np_all((Prad == 0)):
        Prad_data = DataTime(
            name="Airgap radial surface force",
            unit="N/m2",
            symbol="P_r",
            axes=list(output.mag.B.components.values())[0].axes,
            symmetries=output.mag.B.symmetries,
            values=Prad,
        )
        components["radial"] = Prad_data
    if not np_all((Ptan == 0)):
        Ptan_data = DataTime(
            name="Airgap tangential surface force",
            unit="N/m2",
            symbol="P_t",
            symmetries=output.mag.B.symmetries,
            axes=list(output.mag.B.components.values())[0].axes,
            values=Ptan,
        )
        components["tangential"] = Ptan_data
    if not np_all((Pz == 0)):
        Pz_data = DataTime(
            name="Airgap axial surface force",
            unit="N/m2",
            symbol="P_z",
            symmetries=output.mag.B.symmetries,
            axes=list(output.mag.B.components.values())[0].axes,
            values=Pz,
        )
        components["axial"] = Pz_data
    output.force.P = VectorField(
        name="Magnetic airgap surface force", symbol="P", components=components
    )
