from numpy import array

from SciDataTool import DataPattern

from ....Classes.OutMag import OutMag
from ....Classes.Simulation import Simulation
from ....Classes.ImportMatrixXls import ImportMatrixXls
from ....Methods.Simulation.Input import InputError


def gen_input(self):
    """Generate the input for the structural module (magnetic output)

    Parameters
    ----------
    self : InFlux
        An InFlux object
    """

    output = OutMag()

    # get the simulation
    if isinstance(self.parent, Simulation):
        simu = self.parent
    elif isinstance(self.parent.parent, Simulation):
        simu = self.parent.parent
    else:
        raise InputError("InputFlux object should be inside a Simulation object")

    if simu.parent is None:
        raise InputError("The Simulation object must be in an Output object to run")

    # Set discretization
    if self.N0 is None:
        if self.OP is None:
            N0 = None  # N0 can be None if time isn't
        else:
            N0 = self.OP.N0
    else:
        N0 = self.N0

    # Import flux components
    per_a = self.per_a
    per_t = self.per_t
    is_antiper_a = self.is_antiper_a
    is_antiper_t = self.is_antiper_t
    out_dict = {}
    for key in self.B_dict:
        comp = self.B_dict[key]
        if isinstance(comp, ImportMatrixXls) and comp.axes_colrows is not None:
            B_comp, axes_values = comp.get_data()
        else:
            B_comp = comp.get_data()
            axes_values = {}
        out_dict[key] = B_comp

    axes_dict = self.comp_axes(
        axes_values,
        N0=N0,
        per_a=per_a,
        is_antiper_a=is_antiper_a,
        per_t=per_t,
        is_antiper_t=is_antiper_t,
    )

    # Compute slices and angles
    if "slice" in axes_values:
        Slice = DataPattern(
            name="z",
            unit="m",
            values=axes_values["z"],
            rebuild_indices=axes_values["slice"],
            unique_indices=axes_values["slice"],
            values_whole=axes_values["z"],
        )
    else:
        # Single slice
        Slice = DataPattern(
            name="z",
            unit="m",
            values=array([0], dtype=float),
            rebuild_indices=[0],
            unique_indices=[0],
            values_whole=array([0], dtype=float),
        )

    # Store in axes_dict
    axes_dict["z"] = Slice

    # Save the Output in the correct place
    if N0 is not None:
        simu.parent.elec.N0 = N0
    output = OutMag()
    output.store(out_dict=out_dict, axes_dict=axes_dict)
    simu.parent.mag = output

    # Define the electrical Output to set the Operating Point
    if self.OP is not None:
        self.OP.gen_input()
