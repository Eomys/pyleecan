# -*- coding: utf-8 -*-
from SciDataTool import DataTime, VectorField


def store(self, out_dict, axes_dict):
    """Store the standard outputs of Force that are temporarily in out_dict as arrays into OutForce as Data object

    Parameters
    ----------
    self: OutForce
        the OutForce object to update
    out_dict : dict
        Dict containing all force quantities
    axes_dict: {Data}
        Dict of axes used for magnetic calculation

    """

    # Store air-gap surface force as VectorField object

    # Axes for each component
    axis_list = [axes_dict["Time"], axes_dict["Angle"]]

    # Create VectorField with empty components
    self.AGSF = VectorField(
        name="Air gap Surface Force",
        symbol="AGSF",
    )
    # Radial air-gap surface force component
    if "AGSF_r" in out_dict:
        self.AGSF.components["radial"] = DataTime(
            name="Radial air gap surface force",
            unit="N/m^2",
            symbol="AGSF_r",
            axes=axis_list,
            values=out_dict.pop("AGSF_r"),
        )
    # Tangential air-gap surface force component
    if "AGSF_t" in out_dict:
        self.AGSF.components["tangential"] = DataTime(
            name="Tangential air gap surface force",
            unit="N/m^2",
            symbol="AGSF_t",
            axes=axis_list,
            values=out_dict.pop("AGSF_t"),
        )
    # Axial air-gap surface force component
    if "AGSF_z" in out_dict:
        self.AGSF.components["axial"] = DataTime(
            name="Axial air gap surface force",
            unit="N/m^2",
            symbol="AGSF_z",
            axes=axis_list,
            values=out_dict.pop("AGSF_z"),
        )

    if "Rag" in out_dict:
        self.Rag = out_dict.pop("Rag")

    if "meshsolution" in out_dict:
        self.meshsolution = out_dict.pop("meshsolution")
