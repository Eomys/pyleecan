from numpy import pi, all as np_all
from SciDataTool import DataTime, VectorField


def comp_force(self, output, axes_dict):
    """Compute the air-gap surface force based on Maxwell Tensor (MT).

    Parameters
    ----------
    self : ForceMT
        A ForceMT object
    output : Output
        an Output object (to update)
    axes_dict: {Data}
        Dict of axes used for force calculation
    """

    # Get time and angular axes
    Angle = axes_dict["Angle"]
    Time = axes_dict["Time"]

    # Import angular vector from Angle Data object
    _, is_antiper_a = Angle.get_periodicity()
    angle = Angle.get_values(
        is_oneperiod=self.is_periodicity_a,
        is_antiperiod=is_antiper_a and self.is_periodicity_a,
    )

    # Import time vector from Time Data object
    _, is_antiper_t = Time.get_periodicity()
    time = Time.get_values(
        is_oneperiod=self.is_periodicity_t,
        is_antiperiod=is_antiper_t and self.is_periodicity_t,
    )

    # Load magnetic flux
    Brphiz = output.mag.B.get_rphiz_along(
        "time=axis_data",
        "angle=axis_data",
        axis_data={"time": time, "angle": angle},
    )
    Br = Brphiz["radial"]
    Bt = Brphiz["tangential"]
    Bz = Brphiz["axial"]

    # Magnetic void permeability
    mu_0 = 4 * pi * 1e-7

    # Compute AGSF with MT formula
    Prad = (Br * Br - Bt * Bt - Bz * Bz) / (2 * mu_0)
    Ptan = Br * Bt / mu_0
    Pz = Br * Bz / mu_0

    # Store Maxwell Stress tensor P in VectorField
    # Build axes list
    axes_list = list()
    for axe in output.mag.B.get_axes():
        if axe.name == Angle.name:
            axes_list.append(Angle)
        elif axe.name == Time.name:
            axes_list.append(Time)
        else:
            axes_list.append(axe)

    # Build components list
    components = {}
    if not np_all((Prad == 0)):
        Prad_data = DataTime(
            name="Airgap radial surface force",
            unit="N/m2",
            symbol="P_r",
            axes=axes_list,
            values=Prad,
        )
        components["radial"] = Prad_data
    if not np_all((Ptan == 0)):
        Ptan_data = DataTime(
            name="Airgap tangential surface force",
            unit="N/m2",
            symbol="P_t",
            axes=axes_list,
            values=Ptan,
        )
        components["tangential"] = Ptan_data
    if not np_all((Pz == 0)):
        Pz_data = DataTime(
            name="Airgap axial surface force",
            unit="N/m2",
            symbol="P_z",
            axes=axes_list,
            values=Pz,
        )
        components["axial"] = Pz_data

    # Store components in VectorField
    output.force.P = VectorField(
        name="Magnetic airgap surface force", symbol="P", components=components
    )
