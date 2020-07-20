# -*- coding: utf-8 -*-

from SciDataTool import Data1D, DataTime, DataFreq


def get_data(self):
    """Generate Data objects

    Parameters
    ----------
    self : ImportData
        An ImportData object

    Returns
    -------
    Data: DataND
        The generated Data object

    """

    axes_list = []
    for axis in self.axes:
        axes_list.append(Data1D(values=axis.field.get_data(), name=axis.name,))

    if self.is_freq:
        Data = DataFreq(
            axes=axes_list,
            values=self.field.get_data(),
            name=self.name,
            symbol=self.symbol,
        )
    else:
        Data = DataTime(
            axes=axes_list,
            values=self.field.get_data(),
            name=self.name,
            symbol=self.symbol,
        )

    return Data
