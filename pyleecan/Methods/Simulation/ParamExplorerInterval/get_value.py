from numpy import linspace


def get_value(self):
    """Return parameters values"""
    assert self.min_value < self.max_value

    if self.type_value_gen == 0:  # linspace
        if self.type_value == 0:
            dtype = float
        elif self.type_value == 1:
            dtype = int
        value = linspace(
            start=self.min_value,
            stop=self.max_value,
            num=self.N,
            endpoint=True,
            dtype=dtype,
        )
        value.tolist()
    return value
