from ....Classes.DataKeeper import DataKeeper
from ....Classes.InputCurrent import InputCurrent


def gen_datakeeper_list(self):
    """Generate default DataKeepers for VarLoadSpeed workflow"""
    datakeeper_list = []

    simu = self.parent
    symbol_list = [dk.symbol for dk in self.datakeeper_list]
    # Save speed
    if "N0" not in symbol_list:
        datakeeper_list.append(
            DataKeeper(
                name="Speed",
                symbol="N0",
                unit="rpm",
                keeper="lambda output: output.elec.N0",
            )
        )

    # Get default datakeeper
    if simu and (simu.elec or isinstance(simu.input, InputCurrent)):
        datakeeper_list.extend(self.get_elec_datakeeper(symbol_list))
    if simu and simu.mag:
        datakeeper_list.extend(self.get_mag_datakeeper(symbol_list))
    if simu and simu.force:
        datakeeper_list.extend(self.get_force_datakeeper(symbol_list))

    self.datakeeper_list.extend(datakeeper_list)
