from ....Classes.Machine import Machine


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

    desc_dict = Machine.comp_desc_dict(self)

    Zr_dict = dict(
        {
            "name": "Zr",
            "path": "machine.rotor.slot.Zs",
            "verbose": "Rotor slot number",
            "type": int,
            "unit": "",
            "is_input": True,
            "value": self.rotor.slot.Zs,
        }
    )
    desc_dict.insert(2, Zr_dict)
    return desc_dict
