from ....Classes.DataKeeper import DataKeeper
from ....Classes.InputCurrent import InputCurrent


def gen_datakeeper_list(self):
    """Generate default DataKeepers for VarLoadSpeed workflow"""
    datakeeper_list = []

    simu = self.parent
    # Save speed
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
        datakeeper_list.extend(self.get_elec_datakeeper())
    if simu and simu.mag:
        datakeeper_list.extend(self.get_mag_datakeeper())
    if simu and simu.force:
        datakeeper_list.extend(self.get_force_datakeeper())

    self.datakeeper_list.extend(datakeeper_list)
