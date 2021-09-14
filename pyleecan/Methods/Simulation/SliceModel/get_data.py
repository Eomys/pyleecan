from numpy import array, unique

from SciDataTool import DataPattern


def get_data(self):
    """Return the slice data object

    Parameters
    ----------
    self : SliceModel
        a SliceModel object

    Returns
    -------
    Slice: DataPattern
        Slice axis

    """

    # Get all z values
    values_whole = array(self.z_list)

    if self.is_skew:
        # Keep only unique values of relative skew between stator and rotor
        (_, unique_indices, rebuild_indices) = unique(
            (self.angle_stator - self.angle_rotor).round(decimals=4),
            return_index=True,
            return_inverse=True,
        )
        values = values_whole[unique_indices]
        unique_indices = unique_indices.tolist()
        rebuild_indices = rebuild_indices.tolist()

    else:
        # Keep all slices
        values = values_whole
        rebuild_indices = [ii for ii in range(values_whole.size)]
        unique_indices = rebuild_indices

    # Setup other parameters
    normalizations = {"x L": self.L}
    is_step = self.is_step

    # Create DataPattern
    Slice = DataPattern(
        name="z",
        unit="m",
        values=values,
        rebuild_indices=rebuild_indices,
        unique_indices=unique_indices,
        values_whole=values_whole,
        is_step=is_step,
        normalizations=normalizations,
    )

    return Slice
