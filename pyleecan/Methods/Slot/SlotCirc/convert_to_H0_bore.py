def convert_to_H0_bore(self):
    """Convert the slot to the other definition of H0

    Parameters:
    -----------
    self : SlotCirc
        A SlotCirc objec with is_H0_bore==False
    """

    if self.is_H0_bore:
        raise Exception("Error, slot is already H0 bore type!")

    self.H0 = self.comp_height()
    self.is_H0_bore = True
