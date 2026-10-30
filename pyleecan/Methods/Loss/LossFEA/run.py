import numpy as np
from SciDataTool import Data1D, DataFreq, DataTime

from ....Classes.LossModelBertotti import LossModelBertotti
from ....Classes.LossModelJoule import LossModelJoule
from ....Classes.LossModelMagnet import LossModelMagnet
from ....Classes.LossModelProximity import LossModelProximity
from ....Classes.LossModelSteinmetz import LossModelSteinmetz
from ....Classes.LossModelWindagePyrhonen import LossModelWindagePyrhonen
from ....Classes.OutLossModel import OutLossModel
from ....Methods.Simulation.Input import InputError


def run(self):
    """Run the LossFEA module

    Paramaters
    ----------
    self : LossFEA
        A LossFEA object
    """
    if self.parent is None:
        raise InputError("The LossFEA object must be in a Simulation object to run")
    if self.parent.parent is None:
        raise InputError("The LossFEA object must be in an Output object to run")

    self.get_logger().info("Starting Loss module")
    self.get_logger().info("Computing losses with LossFEA model")

    # get output
    output = self.parent.parent

    # Get fundamental frequency
    felec = output.elec.OP.get_felec()

    if output.mag.meshsolution_dict is None and output.mag.meshsolution is None:
        raise InputError(
            "The LossFEA object must use a magnetic meshsolution calculated by a magnetics FEA model to run"
        )

    if self.type_loss_model_core not in ["Bertotti", "Steinmetz"]:
        raise InputError(
            "The LossFEA object only accepts ['Bertotti','Steinmetz'] as self.type_loss_model_core"
        )

    axes_dict, is_mirror = self.comp_axes(output)

    # Get mesh groups names
    if output.mag.meshsolution_dict is None:
        # Get group list in meshsolution
        list_group = list(output.mag.meshsolution.group)
    else:
        # Rebuild group list from meshsolutions stored in dict
        list_group = list()
        for ms in output.mag.meshsolution_dict.values():
            list_group.extend(list(ms.group.keys()))

    # Define all relevant loss models
    self.model_dict = {}
    if "stator core" in list_group:
        if self.type_loss_model_core == "Bertotti":
            self.model_dict["stator core"] = LossModelBertotti(
                group="stator core",
                k_hy=self.k_hy_enforced,
                k_ed=self.k_ed_enforced,
                k_ex=self.k_ex_enforced,
                alpha_B=self.alpha_B_enforced,
                is_stacking_factor=self.is_stacking_factor,
            )
        elif self.type_loss_model_core == "Steinmetz":
            self.model_dict["stator core"] = LossModelSteinmetz(
                group="stator core",
                k_hy=self.k_hy_enforced,
                k_ed=self.k_ed_enforced,
                alpha_f=self.alpha_f_enforced,
                alpha_B=self.alpha_B_enforced,
                is_stacking_factor=self.is_stacking_factor,
            )

    if "stator winding" in list_group:
        self.model_dict["stator joule"] = LossModelJoule(
            group="stator winding", type_skin_effect=self.type_skin_effect
        )
        self.model_dict["stator proximity"] = LossModelProximity(
            group="stator winding", k_p=self.k_p_enforced
        )

    if "rotor core" in list_group:
        if self.type_loss_model_core == "Bertotti":
            self.model_dict["rotor core"] = LossModelBertotti(
                group="rotor core",
                k_hy=self.k_hy_enforced,
                k_ed=self.k_ed_enforced,
                k_ex=self.k_ex_enforced,
                alpha_B=self.alpha_B_enforced,
                is_stacking_factor=self.is_stacking_factor,
            )
        elif self.type_loss_model_core == "Steinmetz":
            self.model_dict["rotor core"] = LossModelSteinmetz(
                group="rotor core",
                k_hy=self.k_hy_enforced,
                k_ed=self.k_ed_enforced,
                alpha_f=self.alpha_f_enforced,
                alpha_B=self.alpha_B_enforced,
                is_stacking_factor=self.is_stacking_factor,
            )

    if "rotor magnets" in list_group:
        self.model_dict["rotor magnets"] = LossModelMagnet(group="rotor magnets")

    if self.is_calc_windage_loss and (
        "airgap" in list_group or "airgap_S" in list_group or "airgap_R" in list_group
    ):
        self.model_dict["airgap windage"] = LossModelWindagePyrhonen(group="airgap")

    loss_dict = {}
    group_all, name_all = "", ""
    for group_name, model in self.model_dict.items():
        if self.is_dynamic:
            loss_density, loss_val_dict = model.comp_loss_time(
                axes_dict, is_mirror=is_mirror
            )
        else:
            loss_density, loss_val_dict, freqs = model.comp_loss_freq()

        loss_mean = 0
        list_loss_val = []
        for key, val in loss_val_dict.items():
            if "losses" in key:
                # Ignore dict entries without losses in it since they are contributions to the loss type (e.g. hysteresis/eddy-current/excess for Bertotti iron losses)
                if self.is_dynamic:
                    # Average over time step
                    loss_mean = val.mean()
                else:
                    # Sum over frequency
                    loss_mean = val.sum()
            list_loss_val.append(val[:, None])

        Ax_losses = Data1D(
            name="type",
            unit=" ",
            values=list(loss_val_dict.keys()),
            is_components=True,
            is_overlay=True,
            filter={"type": []},
        )

        if self.is_dynamic:
            loss_data = DataTime(
                name=group_name,
                symbol="L",
                unit="W",
                values=np.hstack(list_loss_val),
                axes=[axes_dict["time"].copy(), Ax_losses],
            )

        else:
            Freqs = Data1D(
                name="freqs",
                unit="Hz",
                values=freqs,
                normalizations=axes_dict["time"].normalizations.copy(),
            )
            loss_data = DataFreq(
                name=group_name,
                symbol="L",
                unit="W",
                values=np.hstack(list_loss_val),
                axes=[Freqs, Ax_losses],
            )
        # Store results of each model in a different object
        loss_dict[group_name] = OutLossModel(
            name=group_name,
            loss_density=loss_density,
            scalar_value=loss_mean,
            group=model.group,
            loss_model=type(model).__name__,
            loss_data=loss_data,
            coeff_dict=model.coeff_dict.copy(),
        )

        if not self.is_dynamic:
            # Check consistency of scalar_value and coeff_dict
            diff = loss_mean - loss_dict[group_name].get_loss_scalar(felec)
            np.testing.assert_almost_equal(diff, 0)

        # Concatenate model group and name for the overall OutLossModel
        group_all += model.group + " + "
        name_all += group_name + " + "

    # Storing axes_dict in OutLoss (requested for OutLoss.get_meshsolution)
    output.loss.axes_dict = axes_dict

    # Storing loss_dict in OutLoss (requested for OutLoss.get_meshsolution)
    output.loss.loss_dict = loss_dict

    # Calculate meshsolution to get overall loss density
    output.loss.get_meshsolution()
    loss_density_all = output.loss.meshsolution["L"].field.values

    # Add overall OutLossModel by adding all losses sources
    coeff_dict_all = {}
    for group_name, model in loss_dict.items():
        for key, value in model.coeff_dict.items():
            if key in coeff_dict_all:
                coeff_dict_all[key] += value
            else:
                coeff_dict_all[key] = value

    output.loss.loss_dict["overall"] = OutLossModel(
        name=name_all[:-3],  # Remove last " + "
        loss_density=loss_density_all,
        coeff_dict=coeff_dict_all,
        group=group_all[:-3],  # Remove last " + "
    )

    # Store input power
    output.loss.P_in = output.mag.Pem_av + loss_dict["stator joule"].scalar_value

    # Store output power
    loss_overall = loss_dict["overall"].get_loss_scalar(felec)
    output.loss.P_out = output.loss.P_in - loss_overall

    # Store efficiency
    output.loss.efficiency = output.loss.P_out / output.loss.P_in

    # Store mechanical torque
    output.loss.Tmech_av = output.loss.P_out / (2 * np.pi * output.elec.OP.N0 / 60)

    if not self.is_get_meshsolution:
        # Remove meshsolution in OutLoss if loss meshsolution not requested
        output.loss.meshsolution = None

    if self.is_clean_magmesh and not output.simu.mag.is_get_meshsolution:
        # Remove magnetic meshsolution in OutMag if clean is requested
        output.mag.meshsolution = None
        output.mag.meshsolution_dict = None
