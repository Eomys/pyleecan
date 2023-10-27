def get_lamination(self, is_stator):
    self.is_stator = is_stator
    print("lamination")
    if self.is_stator == True:
        print("stator")
    else:
        print("rotor")
    return self.rules
