def comp_desc_dict(self):
    """Compute a dictionary with the main parameters/output of the machine

    Parameters
    ----------
    self : Machine
        A Machine object

    Returns
    -------
    desc_dict: list
        list of dictionary containing the main parameters of the machine
    """

    desc_dict = list()

    # Machine Type
    desc_str = self.get_machine_type()
    desc_dict.append(
        dict(
            {
                "name": "Type",
                "path": "type(machine)",
                "verbose": "Machine Type",
                "type": str,
                "unit": "",
                "is_input": False,
                "value": desc_str.split(" ")[0],
            }
        )
    )
    # Zs
    desc_dict.append(
        dict(
            {
                "name": "Zs",
                "path": "machine.stator.slot.Zs",
                "verbose": "Stator slot number",
                "type": int,
                "unit": "",
                "is_input": True,
                "value": self.stator.slot.Zs,
            }
        )
    )
    # p
    desc_dict.append(
        dict(
            {
                "name": "p",
                "path": "machine.stator.winding.p",
                "verbose": "Pole pair number",
                "type": int,
                "unit": "",
                "is_input": True,
                "value": self.stator.get_pole_pair_number(),
            }
        )
    )
    # is_inner_rotor
    if self.rotor.is_internal:
        inner = "Internal Rotor"
    else:
        inner = "External Rotor"
    desc_dict.append(
        dict(
            {
                "name": "Topology",
                "path": "machine.rotor.is_internal",
                "verbose": "Topology",
                "type": str,
                "unit": "",
                "is_input": False,
                "value": inner,
            }
        )
    )
    # qs
    desc_dict.append(
        dict(
            {
                "name": "qs",
                "path": "machine.stator.winding.qs",
                "verbose": "Stator phase number",
                "type": int,
                "unit": "",
                "is_input": True,
                "value": self.stator.winding.qs,
            }
        )
    )
    # Stator winding resistance
    try:
        Rwind = self.stator.comp_resistance_wind()
    except Exception:
        Rwind = None
    desc_dict.append(
        dict(
            {
                "name": "Rwinds",
                "path": "machine.stator.comp_resistance_wind()",
                "verbose": "Stator winding resistance",
                "type": float,
                "unit": "Ohm",
                "is_input": False,
                "value": Rwind,
            }
        )
    )

    # Machine masses
    try:
        M_dict = self.comp_masses()
        Mmach = M_dict["All"]
    except Exception:
        M_dict = None
        Mmach = None
    desc_dict.append(
        dict(
            {
                "name": "Mmachine",
                "path": "machine.comp_masses()['All']",
                "verbose": "Machine total mass",
                "type": float,
                "unit": "kg",
                "is_input": False,
                "value": Mmach,
            }
        )
    )

    # Stator lamination mass
    if M_dict is not None and "Stator-0" in M_dict and "Mlam" in M_dict["Stator-0"]:
        Mslam = M_dict["Stator-0"]["Mlam"]
    else:
        Mslam = None
    desc_dict.append(
        dict(
            {
                "name": "Mslam",
                "path": "machine.comp_masses()['Stator-0']['Mlam']",
                "verbose": "Stator lamination mass",
                "type": float,
                "unit": "kg",
                "is_input": False,
                "value": Mslam,
            }
        )
    )

    # Stator winding mass
    if M_dict is not None and "Stator-0" in M_dict and "Mwind" in M_dict["Stator-0"]:
        Mswind = M_dict["Stator-0"]["Mwind"]
    else:
        Mswind = None
    desc_dict.append(
        dict(
            {
                "name": "Mswind",
                "path": "machine.comp_masses()['Stator-0']['Mwind']",
                "verbose": "Stator winding mass",
                "type": float,
                "unit": "kg",
                "is_input": False,
                "value": Mswind,
            }
        )
    )

    # Rotor lamination mass
    if M_dict is not None and "Rotor-0" in M_dict and "Mlam" in M_dict["Rotor-0"]:
        Mrlam = M_dict["Rotor-0"]["Mlam"]
    else:
        Mrlam = None
    desc_dict.append(
        dict(
            {
                "name": "Mrlam",
                "path": "machine.comp_masses()['Rotor-0']['Mlam']",
                "verbose": "Rotor lamination mass",
                "type": float,
                "unit": "kg",
                "is_input": False,
                "value": Mrlam,
            }
        )
    )

    # Rotor winding mass only if necessary
    if M_dict is not None and "Rotor-0" in M_dict and "Mwind" in M_dict["Rotor-0"]:
        Mrwind = M_dict["Rotor-0"]["Mwind"]
        desc_dict.append(
            dict(
                {
                    "name": "Mrwind",
                    "path": "machine.comp_masses()['Rotor-0']['Mwind']",
                    "verbose": "Rotor winding mass",
                    "type": float,
                    "unit": "kg",
                    "is_input": False,
                    "value": Mrwind,
                }
            )
        )

    # Magnet mass only if necessary
    if M_dict is not None and "Rotor-0" in M_dict and "Mmag" in M_dict["Rotor-0"]:
        Mmag = M_dict["Rotor-0"]["Mmag"]
        desc_dict.append(
            dict(
                {
                    "name": "Mmag",
                    "path": "machine.comp_masses()['Rotor-0']['Mmag']",
                    "verbose": "Rotor magnet mass",
                    "type": float,
                    "unit": "kg",
                    "is_input": False,
                    "value": Mmag,
                }
            )
        )

    return desc_dict
