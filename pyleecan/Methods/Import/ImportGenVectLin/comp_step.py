def comp_step(self):
    """Compute the Step between two points of the linspace"""

    self.check()
    data = self.get_data()
    return data[1] - data[0]
