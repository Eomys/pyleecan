from ....Classes.DataKeeper import DataKeeper


def get_elec_datakeeper_dict():
    """Generate DataKeepers to store by default results from input/electric module
    Returns
    -------
    dk_dict: dict
        dict of DataKeeper for input/electric module
    """

    dk_dict = dict()

    dk_dict["Id"] = DataKeeper(
        name="Stator current along d-axis",
        physic="elec",
        symbol="Id",
        unit="Arms",
        keeper="lambda output: output.elec.OP.get_Id_Iq()['Id']",
    )

    dk_dict["Iq"] = DataKeeper(
        name="Stator current along q-axis",
        physic="elec",
        symbol="Iq",
        unit="Arms",
        keeper="lambda output: output.elec.OP.get_Id_Iq()['Iq']",
    )

    dk_dict["Ud"] = DataKeeper(
        name="Stator voltage along d-axis",
        symbol="Ud",
        unit="Vrms",
        keeper="lambda output: output.elec.OP.get_Ud_Uq()['Ud']",
    )

    dk_dict["Uq"] = DataKeeper(
        name="Stator voltage along q-axis",
        symbol="Uq",
        unit="Vrms",
        keeper="lambda output: output.elec.OP.get_Ud_Uq()['Uq']",
    )

    dk_dict["I0"] = DataKeeper(
        name="Stator current rms amplitude",
        symbol="I0",
        unit="Arms",
        keeper="lambda output: output.elec.OP.get_I0_Phi0()['I0']",
    )

    dk_dict["Phi0"] = DataKeeper(
        name="Stator current phase",
        symbol="Phi0",
        unit="rad",
        keeper="lambda output: output.elec.OP.get_I0_Phi0()['Phi0']",
    )

    dk_dict["U0"] = DataKeeper(
        name="Stator voltage rms amplitude",
        symbol="U0",
        unit="Vrms",
        keeper="lambda output: output.elec.OP.get_U0_UPhi0()['U0']",
    )

    dk_dict["UPhi0"] = DataKeeper(
        name="Stator voltage phase",
        symbol="UPhi0",
        unit="rad",
        keeper="lambda output: output.elec.OP.get_U0_UPhi0()['UPhi0']",
    )

    dk_dict["slip"] = DataKeeper(
        name="Rotor mechanical slip",
        symbol="slip",
        unit="-",
        keeper="lambda output: output.elec.OP.get_slip()",
    )

    dk_dict["Tem_av_ref"] = DataKeeper(
        name="Reference Average Torque",
        symbol="Tem_av_ref",
        unit="N.m",
        keeper="lambda output: output.elec.OP.Tem_av_ref",
    )

    dk_dict["Tem_av_elec"] = DataKeeper(
        name="Average Torque from EEC",
        symbol="Tem_av_elec",
        unit="N.m",
        keeper="lambda output: output.elec.Tem_av_ref",
    )

    return dk_dict