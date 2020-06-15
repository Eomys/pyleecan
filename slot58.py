from sympy import symbols, simplify
from sympy.functions import cos, sin, tan
from sympy.solvers import solve

X3, Xc, X5, Y3, Yc, Y5, R0 = symbols(
    "X3, Xc, X5, Y3, Yc, Y5, R0", real=True, positive=True
)

Eq_list = list()
Eq_list.append((X3 - X5) * (X3 - Xc) + (Y3 - Y5) * (Y3 - Yc))
Eq_list.append((X3 - Xc) ** 2 + (Y3 - Yc) ** 2 - R0 ** 2)

result = solve(Eq_list, [X3, Y3])

print("S1: ")
print(simplify(result[0][0]))
print(simplify(result[0][1]))
print("S1: ")
print(simplify(result[1][0]))
print(simplify(result[1][1]))
