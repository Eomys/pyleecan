# -*- coding: utf-8 -*-

from SciDataTool import VectorField


def get_data(self):
    """Generate VectorField object

    Parameters
    ----------
    self : ImportVectorField
        An ImportVectorField object

    Returns
    -------
    VectField: VectorField
        The generated VectorField object

    """

    comp_dict = {}
    for key, component in self.components.items():
        comp_dict[key] = component.get_data()

    VectField = VectorField(name=self.name, symbol=self.symbol, components=comp_dict,)

    return VectField
