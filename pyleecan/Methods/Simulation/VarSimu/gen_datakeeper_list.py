from ....Classes.DataKeeper import DataKeeper
from ....Functions.Load.import_class import import_class


def gen_datakeeper_list(self, ref_simu):
    """Generate default DataKeepers according the reference simulation type"""
    datakeeper_list = []

    # To avoid adding twice a DataKeeper
    symbol_list = [dk.symbol for dk in self.datakeeper_list]
    # For multi-simulation of multi-simulation (different DataKeepe<r)
    is_multi = ref_simu.var_simu is not None
    # Dynamic import to avoid loop
    InputCurrent = import_class("pyleecan.Classes", "InputCurrent", "")

    # Save speed
    if not is_multi and "N0" not in symbol_list:
        datakeeper_list.append(
            DataKeeper(
                name="Speed",
                symbol="N0",
                unit="rpm",
                keeper="lambda output: output.elec.N0",
            )
        )

    # Get default datakeeper
    if ref_simu.elec or isinstance(ref_simu.input, InputCurrent):
        datakeeper_list.extend(self.get_elec_datakeeper(symbol_list, is_multi=is_multi))
    if ref_simu.mag:
        datakeeper_list.extend(self.get_mag_datakeeper(symbol_list, is_multi=is_multi))
    if ref_simu.force:
        datakeeper_list.extend(
            self.get_force_datakeeper(symbol_list, is_multi=is_multi)
        )

    self.datakeeper_list.extend(datakeeper_list)
