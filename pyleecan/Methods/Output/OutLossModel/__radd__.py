from ....Functions.Load.import_class import import_class


def __radd__(self, other):
    if other == 0:
        return self
    try:
        other_loss_density = other.loss_density
        other_coeff_dict = other.coeff_dict
        other_group = other.group
        other_name = other.name
    except AttributeError:
        other_loss_density = other["loss_density"]
        other_coeff_dict = other["coeff_dict"]
        other_name = other["name"]
        other_group = other["group"]

    OutLossModel = import_class("pyleecan.Classes", "OutLossModel")
    new_loss_density = self.loss_density + other_loss_density
    new_coeff_dict = self.coeff_dict.copy()
    for key, value in other_coeff_dict.items():
        if key in new_coeff_dict:
            new_coeff_dict[key] += value
        else:
            new_coeff_dict[key] = value
    new_group = self.group + " + " + other_group
    new_name = self.name + " + " + other_name
    return OutLossModel(
        name=new_name,
        loss_density=new_loss_density,
        coeff_dict=new_coeff_dict,
        group=new_group,
    )