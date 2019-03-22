from fractions import gcd


def comp_sym(self):
    """Compute the symmetry of the Machine
    """

    sym_s = self.stator.comp_sym()
    sym_r = self.rotor.comp_sym()

    return gcd(sym_s, sym_r)
