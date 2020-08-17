from ....Classes.DataKeeper import DataKeeper


def gen_datakeeper_list(self):
    """Generate default DataKeepers for VarLoadSpeed workflow"""
    datakeeper_list = []

    # Save speed
    datakeeper_list.append(
        DataKeeper(
            name="Speed", symbol="N0", unit="rpm", keeper=lambda output: output.elec.N0
        )
    )

    # Get default datakeeper
    datakeeper_list.extend(self.get_elec_datakeeper())
    datakeeper_list.extend(self.get_mag_datakeeper())
    datakeeper_list.extend(self.get_force_datakeeper())

    self.datakeeper_list.extend(datakeeper_list)
