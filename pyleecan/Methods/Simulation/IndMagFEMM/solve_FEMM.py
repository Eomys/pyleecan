from ....Functions.Electrical.solve_FEMM import solve_FEMM as solve_FEMM_


def solve_FEMM(self, femm, output, sym, FEMM_dict):
    return solve_FEMM_(self, femm, output, sym, FEMM_dict)
