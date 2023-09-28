from numpy import arange, array

from SciDataTool import DataPattern

from ....Classes.OutMag import OutMag
from ....Classes.ImportMatrixXls import ImportMatrixXls
from ....Classes.ImportMatrixVal import ImportMatrixVal
from ....Classes.Input import Input
from ....Classes.InputCurrent import InputCurrent


VERBOSE_KEY = {"B_{rad}": "Radial", "B_{circ}": "Tangential", "B_{ax}": "Axial"}


def gen_input(self):
    """Generate the input for the force/stress module (magnetic output)

    Parameters
    ----------
    self : InputFlux
        An InputFlux object
    """

    # Call InputCurrent.gen_input()
    InputCurrent.gen_input(self)

    # Get simulation and outputs
    simu = self.parent
    output = simu.parent

    if simu.machine is not None:
        machine = simu.machine
    else:
        raise Exception("Cannot import flux if simu.machine is None")

    logger = simu.get_logger()

    # Import flux components
    out_mag = OutMag()
    if self.B_enforced is None:
        per_a = self.per_a
        per_t = self.per_t
        is_antiper_a = self.is_antiper_a
        is_antiper_t = self.is_antiper_t
        out_dict = {}
        for key in self.B_dict:
            comp = self.B_dict[key]
            if isinstance(comp, list):
                for i, B_import in enumerate(comp):
                    if i == 0:
                        values, axes_values = B_import.get_data()
                        B_comp = values[..., None]
                    else:
                        values, _ = B_import.get_data()
                        B_comp.append(B_comp, values[..., None], axis=-1)
                if self.slice is not None:
                    axes_values["slice"] = self.slice
                else:
                    axes_values["slice"] = arange(len(comp))
            elif isinstance(comp, ImportMatrixXls):
                # Only this one is used to import flux from excel files
                logger.info(
                    "Importing "
                    + VERBOSE_KEY[key].lower()
                    + " flux from "
                    + comp.file_path
                )
                B_comp, axes_values = comp.get_data(logger=logger)

            else:
                B_comp = comp.get_data()
                axes_values = {}
            if len(B_comp.shape) < 3:
                B_comp = B_comp[..., None]

            out_dict[key] = B_comp

        # Create import object for time values
        if self.time is None and "time" in axes_values:
            self.time = ImportMatrixVal(value=axes_values["time"])

        # Create import object for angle values
        if self.angle is None and "angle" in axes_values:
            self.angle = ImportMatrixVal(value=axes_values["angle"])

        # Calculate time and angle axes
        axes_dict = Input.comp_axes(
            self,
            axes_list=["time", "angle"],
            per_a=per_a,
            is_antiper_a=is_antiper_a,
            per_t=per_t,
            is_antiper_t=is_antiper_t,
        )

        # Compute slices and angles
        if "slice" in axes_values and len(axes_values["slice"]) > 1:
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
            L1 = simu.machine.rotor.L1
            Slice = DataPattern(
                name="z",
                unit="m",
                values=array([-L1 / 2], dtype=float),
                rebuild_indices=[0, 0],
                unique_indices=[0],
                values_whole=array([-L1 / 2, L1 / 2], dtype=float),
            )

        # Store in axes_dict
        axes_dict["z"] = Slice

        # Save the Output in the correct place
        out_mag.store(out_dict=out_dict, axes_dict=axes_dict)

    else:
        # Enforce input VectorField
        out_mag.B = self.B_enforced
        out_mag.axes_dict = dict()
        axes_list = self.B_enforced.get_axes()
        for ax in axes_list:
            out_mag.axes_dict[ax.name] = ax.copy()

    output.mag = out_mag
