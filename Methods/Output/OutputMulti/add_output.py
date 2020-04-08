from ....Classes.Output import Output
import numpy as np


def add_output(self, output, is_valid, design_var):
    """Add an output to the OutputMulti"""

    # Check the type of the data
    if type(output) != Output:
        raise TypeError(
            "Expected type Output for output but got " + str(type(output)) + "."
        )

    if type(is_valid) not in [bool, np.bool_]:
        raise TypeError(
            "Expected type bool for is_valid but got " + str(type(is_valid)) + "."
        )

    self.outputs.append(output)
    self.design_var.append(design_var)
    self.is_valid.append(is_valid)
