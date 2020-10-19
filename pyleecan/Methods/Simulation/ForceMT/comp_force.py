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

    # Get time and angular axes without anti-periodicity in axes
    Angle_comp, Time_comp = self.get_axes(
        output, is_remove_apera=True, is_remove_apert=True
    )
    # Check if the angular axis is anti-periodic
    _, is_antiper_a = Angle_comp.get_periodicity()

    # Import angular vector from Data object
    angle = Angle_comp.get_values(
        is_oneperiod=self.is_periodicity_a,
        is_antiperiod=is_antiper_a and self.is_periodicity_a,
    )

    # Check if the angular axis is anti-periodic
    _, is_antiper_t = Time_comp.get_periodicity()

    time = Time_comp.get_values(
        is_oneperiod=self.is_periodicity_t,
        is_antiperiod=is_antiper_t and self.is_periodicity_t,
    )

    # Initialize list of axes and symmetry dict for VectorField P
    axes_list = list(output.mag.B.get_axes())
    sym_dict = dict()

    # Update axes and symmetry lists by removing anti-periodicity
    for ii, axe in enumerate(axes_list):
        if axe.name == Angle_comp.name:
            axes_list[ii] = Angle_comp
        if axe.name == Time_comp.name:
            axes_list[ii] = Time_comp

        if axes_list[ii].symmetries:
            sym_dict.update(axes_list[ii].symmetries)

    # Load magnetic flux
    Brphiz = output.mag.B.get_rphiz_along(
        "time=axis_data", "angle=axis_data", axis_data={"time":time, "angle":angle},
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

    # Store the results
    components = {}
    if not np_all((Prad == 0)):
        Prad_data = DataTime(
            name="Airgap radial surface force",
            unit="N/m2",
            symbol="P_r",
            axes=axes_list,
            symmetries=sym_dict,
            values=Prad,
        )
        components["radial"] = Prad_data
    if not np_all((Ptan == 0)):
        Ptan_data = DataTime(
            name="Airgap tangential surface force",
            unit="N/m2",
            symbol="P_t",
            axes=axes_list,
            symmetries=sym_dict,
            values=Ptan,
        )
        components["tangential"] = Ptan_data
    if not np_all((Pz == 0)):
        Pz_data = DataTime(
            name="Airgap axial surface force",
            unit="N/m2",
            symbol="P_z",
            axes=axes_list,
            symmetries=sym_dict,
            values=Pz,
        )
        components["axial"] = Pz_data
    output.force.P = VectorField(
        name="Magnetic airgap surface force", symbol="P", components=components
    )
