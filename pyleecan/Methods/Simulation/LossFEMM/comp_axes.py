from SciDataTool import Data1D


def comp_axes(self, output):
    """Compute the axes required in LossFEMM module

    Parameters
    ----------
    self : LossFEMM
        a LossFEMM object
    output : Output
        an Output object (to update)

    Returns
    -------
    axes_dict: {Data}
        Dict containing Time and Angle axes including (anti-)periodicties used in any Force module
    """

    axes_list = output.mag.meshsolution.solution[0].field.get_axes()
    Time = axes_list[0]
    if "antiperiod" in Time.symmetries:
        Time.symmetries = {"period": Time.symmetries["antiperiod"]}

    freqs = Time.get_values(is_oneperiod=True, operation="time_to_freqs")

    Freqs = Data1D(
        name="freqs", unit="Hz", values=freqs, normalizations=Time.normalizations.copy()
    )

    axes_dict = {"freqs": Freqs, "indice": axes_list[1]}

    return axes_dict
