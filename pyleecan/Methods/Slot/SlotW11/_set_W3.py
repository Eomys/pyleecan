# -*- coding: utf-8 -*-

from pyleecan.Classes._check import check_var, raise_


def _set_W3(self, value):
    """setter of W3"""
    check_var("W3", value, "float", Vmin=0)
    self._W3 = value

    # Compute W1 and W2 to match W3 tooth constraint
    try:
        self._comp_W()
    except Exception:
        pass
