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
        inner = "Inner Rotor"
    else:
        inner = "Outer Rotor"
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
    # Machine mass
    try:
        Mmach = self.comp_masses()["Mmach"]
    except Exception:
        Mmach = None
    desc_dict.append(
        dict(
            {
                "name": "Mmachine",
                "path": "machine.comp_masses()['Mmach']",
                "verbose": "Machine total mass",
                "type": float,
                "unit": "kg",
                "is_input": False,
                "value": Mmach,
            }
        )
    )

    return desc_dict
