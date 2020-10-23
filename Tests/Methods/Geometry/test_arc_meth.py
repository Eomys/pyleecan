# -*- coding: utf-8 -*-

import pytest

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Arc2 import Arc2
from pyleecan.Classes.Arc3 import Arc3
from numpy import pi, array, exp, sqrt


# For AlmostEqual
DELTA = 1e-6

split_test = list()
# 1) Arc1, 1 Intersection
split_test.append(
    {
        "arc": Arc1(begin=1, end=1j, radius=1, is_trigo_direction=True),  # Arc to split
        "Z1": 0,  # First point of cutting line
        "Z2": 1j + 1,  # Second point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [1 * exp(1j * pi / 4)],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=1 * exp(1j * pi / 4), end=1j, radius=1, is_trigo_direction=True)
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=1, end=1 * exp(1j * pi / 4), radius=1, is_trigo_direction=True)
        ],  # Expected result for slip not is_top
    }
)
# 2) Case 1 with is_trigo = False
split_test.append(
    {
        "arc": Arc1(
            begin=1, end=1j, radius=1, is_trigo_direction=False
        ),  # Arc to split
        "Z1": 0,  # First point of cutting line
        "Z2": 1j + 1,  # Second point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [1 * exp(1j * 5 * pi / 4)],  # Expected intersection points
        "Zs_top": [
            Arc1(
                begin=1 * exp(1j * 5 * pi / 4),
                end=1j,
                radius=-1,
                is_trigo_direction=False,
            )
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(
                begin=1,
                end=1 * exp(1j * 5 * pi / 4),
                radius=-1,
                is_trigo_direction=False,
            )
        ],  # Expected result for slip not is_top
    }
)
# 3) Case 1 with reverse Z1 and Z2
split_test.append(
    {
        "arc": Arc1(begin=1, end=1j, radius=1, is_trigo_direction=True),  # Arc to split
        "Z1": 1j + 1,  # First point of cutting line
        "Z2": 0,  # Second point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [1 * exp(1j * pi / 4)],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=1, end=1 * exp(1j * pi / 4), radius=1, is_trigo_direction=True)
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=1 * exp(1j * pi / 4), end=1j, radius=1, is_trigo_direction=True)
        ],  # Expected result for slip not is_top
    }
)
# 4) Arc1, No Intersection
split_test.append(
    {
        "arc": Arc1(
            begin=1 - 1j, end=-1 - 1j, radius=1, is_trigo_direction=True
        ),  # Arc to split
        "Z1": 1 - 1.1j,  # First point of cutting line
        "Z2": -1 - 1.1j,  # Second point of cutting line
        "center": -1j,  # Center of the arc (should not be changed by the split)
        "Zi": [],  # Expected intersection points
        "Zs_top": [],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=1 - 1j, end=-1 - 1j, radius=1, is_trigo_direction=True)
        ],  # Expected result for slip not is_top
    }
)
# 5) Arc1, 1 Intersection = begin (no tangent)
split_test.append(
    {
        "arc": Arc1(
            begin=1 - 1j, end=-1 - 1j, radius=1, is_trigo_direction=True
        ),  # Arc to split
        "Z1": -2j,  # First point of cutting line
        "Z2": 2,  # Second point of cutting line
        "center": -1j,  # Center of the arc (should not be changed by the split)
        "Zi": [1 - 1j],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=1 - 1j, end=-1 - 1j, radius=1, is_trigo_direction=True)
        ],  # Expected result for slip is_top
        "Zs_bot": [],  # Expected result for slip not is_top
    }
)
# 6) Arc1, 1 Intersection = end (no tangent)
split_test.append(
    {
        "arc": Arc1(
            begin=-2 - 2j, end=-2 + 2j, radius=-sqrt(5), is_trigo_direction=False
        ),  # Arc to split
        "Z1": 1 + 2j,  # First point of cutting line
        "Z2": 2 + 2j,  # Second point of cutting line
        "center": -1,  # Center of the arc (should not be changed by the split)
        "Zi": [-2 + 2j],  # Expected intersection points
        "Zs_top": [],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=-2 - 2j, end=-2 + 2j, radius=-sqrt(5), is_trigo_direction=False)
        ],  # Expected result for slip not is_top
    }
)
# 7) Arc1, 1 Intersection (tangent)
split_test.append(
    {
        "arc": Arc1(
            begin=-2 - 2j, end=-2 + 2j, radius=2, is_trigo_direction=False
        ),  # Arc to split
        "Z1": -4 + 2j,  # First point of cutting line
        "Z2": -4 - 2j,  # Second point of cutting line
        "center": -2,  # Center of the arc (should not be changed by the split)
        "Zi": [-4],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=-2 - 2j, end=-2 + 2j, radius=2, is_trigo_direction=False)
        ],  # Expected result for slip is_top
        "Zs_bot": [],  # Expected result for slip not is_top
    }
)
# 8) Arc1, 2 intersection
X = 0.43588989
split_test.append(
    {
        "arc": Arc1(
            begin=1 + 1j,
            end=1j + exp(1j * 3 * pi / 4),
            radius=1,
            is_trigo_direction=True,
        ),  # Arc to split
        "Z1": 1 + 1.9j,  # First point of cutting line
        "Z2": 2 + 1.9j,  # Second point of cutting line
        "center": 1j,  # Center of the arc (should not be changed by the split)
        "Zi": [X + 1.9j, -X + 1.9j],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=X + 1.9j, end=-X + 1.9j, radius=1, is_trigo_direction=True)
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=1 + 1j, end=X + 1.9j, radius=1, is_trigo_direction=True),
            Arc1(
                begin=-X + 1.9j,
                end=1j + exp(1j * 3 * pi / 4),
                radius=1,
                is_trigo_direction=True,
            ),
        ],  # Expected result for slip not is_top
    }
)
# 9) Same as 8 with reversed cutting line
split_test.append(
    {
        "arc": Arc1(
            begin=1 + 1j,
            end=1j + exp(1j * 3 * pi / 4),
            radius=1,
            is_trigo_direction=True,
        ),  # Arc to split
        "Z1": 2 + 1.9j,  # First point of cutting line
        "Z2": 1 + 1.9j,  # Second point of cutting line
        "center": 1j,  # Center of the arc (should not be changed by the split)
        "Zi": [X + 1.9j, -X + 1.9j],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=1 + 1j, end=X + 1.9j, radius=1, is_trigo_direction=True),
            Arc1(
                begin=-X + 1.9j,
                end=1j + exp(1j * 3 * pi / 4),
                radius=1,
                is_trigo_direction=True,
            ),
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=X + 1.9j, end=-X + 1.9j, radius=1, is_trigo_direction=True)
        ],  # Expected result for slip not is_top
    }
)
# 10) Arc1, 2 intersection, is_trigo=False
split_test.append(
    {
        "arc": Arc1(
            begin=1, end=1j, radius=1, is_trigo_direction=False
        ),  # Arc to split
        "Z1": -0.5 + 1j,  # First point of cutting line
        "Z2": -0.5 + 2j,  # Second point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [
            -0.5 - sqrt(0.75) * 1j,
            -0.5 + sqrt(0.75) * 1j,
        ],  # Expected intersection points
        "Zs_top": [
            Arc1(
                begin=-0.5 - sqrt(0.75) * 1j,
                end=-0.5 + sqrt(0.75) * 1j,
                radius=-1,
                is_trigo_direction=False,
            )
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(
                begin=1, end=-0.5 - sqrt(0.75) * 1j, radius=-1, is_trigo_direction=False
            ),
            Arc1(
                begin=-0.5 + sqrt(0.75) * 1j,
                end=1j,
                radius=-1,
                is_trigo_direction=False,
            ),
        ],  # Expected result for slip not is_top
    }
)
# 11) Arc1, 2 intersections, begin = int1
split_test.append(
    {
        "arc": Arc1(
            begin=-1 - 1j, end=-3 - 3j, radius=2, is_trigo_direction=True
        ),  # Arc to split
        "Z1": 1,  # First point of cutting line
        "Z2": -3 - 2j,  # Second point of cutting line
        "center": -1 - 3j,  # Center of the arc (should not be changed by the split)
        "Zi": [-1 - 1j, -2.6 - 1.8j],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=-2.6 - 1.8j, end=-3 - 3j, radius=2, is_trigo_direction=True)
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=-1 - 1j, end=-2.6 - 1.8j, radius=2, is_trigo_direction=True)
        ],  # Expected result for slip not is_top
    }
)
# 12) Arc1, 2 intersections, end = int2
split_test.append(
    {
        "arc": Arc1(
            begin=1j, end=-1, radius=1, is_trigo_direction=True
        ),  # Arc to split
        "Z1": 2j,  # First point of cutting line
        "Z2": -1,  # Second point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [-0.6 + 0.8j, -1],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=1j, end=-0.6 + 0.8j, radius=1, is_trigo_direction=True)
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=-0.6 + 0.8j, end=-1, radius=1, is_trigo_direction=True)
        ],  # Expected result for slip not is_top
    }
)
# 13 Arc1, 2 intersections, begin = int1 and end = int2
split_test.append(
    {
        "arc": Arc1(
            begin=-1j + 3 * exp(1j * pi / 4),
            end=-1j + 3 * exp(1j * 3 * pi / 4),
            radius=3,
            is_trigo_direction=True,
        ),  # Arc to split
        "Z1": -1j + sqrt(4.5) * (2 + 1j),  # First point of cutting line
        "Z2": -1j + sqrt(4.5) * (3 + 1j),  # Second point of cutting line
        "center": -1j,  # Center of the arc (should not be changed by the split)
        "Zi": [
            -1j + sqrt(4.5) * (1 + 1j),
            -1j + sqrt(4.5) * (-1 + 1j),
        ],  # Expected intersection points
        "Zs_top": [
            Arc1(
                begin=-1j + 3 * exp(1j * pi / 4),
                end=-1j + 3 * exp(1j * 3 * pi / 4),
                radius=3,
                is_trigo_direction=True,
            )
        ],  # Expected result for slip is_top
        "Zs_bot": [],  # Expected result for slip not is_top
    }
)
# 14) Arc2, 1 Intersection
split_test.append(
    {
        "arc": Arc2(begin=1j, center=0, angle=pi),  # Arc to split
        "Z1": -3,  # First point of cutting line
        "Z2": 1,  # Second point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [-1],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=1j, end=-1, radius=1, is_trigo_direction=True)
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=-1, end=-1j, radius=1, is_trigo_direction=True)
        ],  # Expected result for slip not is_top
    }
)
# 15) Case 14 with angle = -angle
split_test.append(
    {
        "arc": Arc2(begin=1j, center=0, angle=-pi),  # Arc to split
        "Z1": -3,  # First point of cutting line
        "Z2": 1,  # Second point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [1],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=1j, end=1, radius=-1, is_trigo_direction=False)
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=1, end=-1j, radius=-1, is_trigo_direction=False)
        ],  # Expected result for slip not is_top
    }
)
# 16) Case 14 with reverse Z1 and Z2
split_test.append(
    {
        "arc": Arc2(begin=1j, center=0, angle=pi),  # Arc to split
        "Z1": 1,  # First point of cutting line
        "Z2": -3,  # Second point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [-1],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=-1, end=-1j, radius=1, is_trigo_direction=True)
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=1j, end=-1, radius=1, is_trigo_direction=True)
        ],  # Expected result for slip not is_top
    }
)
# 17) Arc2, No Intersection
split_test.append(
    {
        "arc": Arc2(begin=0, center=-1 - 1j, angle=-pi / 4),  # Arc to split
        "Z1": 1 - 1.5j,  # First point of cutting line
        "Z2": 2 - 1.5j,  # Second point of cutting line
        "center": -1 - 1j,  # Center of the arc (should not be changed by the split)
        "Zi": [],  # Expected intersection points
        "Zs_top": [
            Arc2(begin=0, center=-1 - 1j, angle=-pi / 4)
        ],  # Expected result for slip is_top
        "Zs_bot": [],  # Expected result for slip not is_top
    }
)
# 18) Arc2, 1 Intersection = begin (no tangent)
split_test.append(
    {
        "arc": Arc2(begin=1j + 1, center=1j, angle=-3 * pi / 4),  # Arc to split
        "Z1": 2j,  # First point of cutting line
        "Z2": 2,  # Second point of cutting line
        "center": 1j,  # Center of the arc (should not be changed by the split)
        "Zi": [1 + 1j],  # Expected intersection points
        "Zs_top": [],  # Expected result for slip is_top
        "Zs_bot": [
            Arc2(begin=1j + 1, center=1j, angle=-3 * pi / 4)
        ],  # Expected result for slip not is_top
    }
)
# 19) Arc2, 1 Intersection = end (tangent)
split_test.append(
    {
        "arc": Arc2(begin=-1j, center=2 - 1j, angle=-pi),  # Arc to split
        "Z1": 4 + 1j,  # First point of cutting line
        "Z2": 4 + 2j,  # Second point of cutting line
        "center": 2 - 1j,  # Center of the arc (should not be changed by the split)
        "Zi": [4 - 1j],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=-1j, end=4 - 1j, radius=2, is_trigo_direction=False)
        ],  # Expected result for slip is_top
        "Zs_bot": [],  # Expected result for slip not is_top
    }
)
# 20) Arc2, 1 Intersection (tangent) => Arc on top
split_test.append(
    {
        "arc": Arc2(begin=1, center=0, angle=pi),  # Arc to split
        "Z1": 3 + 1j,  # First point of cutting line
        "Z2": -1 + 1j,  # Second point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [1j],  # Expected intersection points
        "Zs_top": [
            Arc2(begin=1, center=0, angle=pi)
        ],  # Expected result for slip is_top
        "Zs_bot": [],  # Expected result for slip not is_top
    }
)
# 21) Arc2, 1 Intersection (tangent) => Arc on bottom
split_test.append(
    {
        "arc": Arc2(begin=1, center=0, angle=pi),  # Arc to split
        "Z1": -1 + 1j,  # First point of cutting line
        "Z2": 3 + 1j,  # Second point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [1j],  # Expected intersection points
        "Zs_top": [],  # Expected result for slip is_top
        "Zs_bot": [
            Arc2(begin=1, center=0, angle=pi)
        ],  # Expected result for slip not is_top
    }
)
# 22) Arc2, 2 intersection
X = 0.322875655
split_test.append(
    {
        "arc": Arc2(begin=-1j, center=1, angle=-5 * pi / 4),  # Arc to split
        "Z1": -1 + 0.5j,  # First point of cutting line
        "Z2": 2 + 0.5j,  # Second point of cutting line
        "center": 1,  # Center of the arc (should not be changed by the split)
        "Zi": [-X + 0.5j, 2 + X + 0.5j],  # Expected intersection points
        "Zs_top": [
            Arc1(
                begin=-X + 0.5j,
                end=2 + X + 0.5j,
                radius=-sqrt(2),
                is_trigo_direction=False,
            )
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=-1j, end=-X + 0.5j, radius=-sqrt(2), is_trigo_direction=False),
            Arc1(
                begin=2 + X + 0.5j,
                end=1 + sqrt(2),
                radius=-sqrt(2),
                is_trigo_direction=False,
            ),
        ],  # Expected result for slip not is_top
    }
)
# 23) Same as 22 with reversed cutting line
split_test.append(
    {
        "arc": Arc2(begin=-1j, center=1, angle=-5 * pi / 4),  # Arc to split
        "Z1": 2 + 0.5j,  # First point of cutting line
        "Z2": -1 + 0.5j,  # Second point of cutting line
        "center": 1,  # Center of the arc (should not be changed by the split)
        "Zi": [-X + 0.5j, 2 + X + 0.5j],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=-1j, end=-X + 0.5j, radius=-sqrt(2), is_trigo_direction=False),
            Arc1(
                begin=2 + X + 0.5j,
                end=1 + sqrt(2),
                radius=-sqrt(2),
                is_trigo_direction=False,
            ),
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(
                begin=-X + 0.5j,
                end=2 + X + 0.5j,
                radius=-sqrt(2),
                is_trigo_direction=False,
            )
        ],  # Expected result for slip not is_top
    }
)
# 24) Arc2, 2 intersection, angle < 0
split_test.append(
    {
        "arc": Arc2(begin=-1, center=0, angle=-pi / 2),  # Arc to split
        "Z1": -1.1,  # First point of cutting line
        "Z2": 1.1j,  # Second point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [
            -0.99441 + 0.10559j,
            -0.10559 + 0.99441j,
        ],  # Expected intersection points
        "Zs_top": [
            Arc1(
                begin=-0.99441 + 0.10559j,
                end=-0.10559 + 0.99441j,
                radius=-1,
                is_trigo_direction=False,
            )
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(
                begin=-1, end=-0.99441 + 0.10559j, radius=-1, is_trigo_direction=False
            ),
            Arc1(
                begin=-0.10559 + 0.99441j, end=1j, radius=-1, is_trigo_direction=False
            ),
        ],  # Expected result for slip not is_top
    }
)
# 25) Arc2, 2 intersections, begin = int1
split_test.append(
    {
        "arc": Arc2(begin=1j + 2, center=1j, angle=3 * pi / 4),  # Arc to split
        "Z1": 4j - 1,  # First point of cutting line
        "Z2": 3,  # Second point of cutting line
        "center": 1j,  # Center of the arc (should not be changed by the split)
        "Zi": [1j + 2, 3j],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=1j + 2, end=3j, radius=2, is_trigo_direction=True)
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(
                begin=3j,
                end=1j + 2 * exp(1j * 3 * pi / 4),
                radius=2,
                is_trigo_direction=True,
            )
        ],  # Expected result for slip not is_top
    }
)
# 26) Arc2, 2 intersections, end = int2
split_test.append(
    {
        "arc": Arc2(begin=1, center=0, angle=-pi),  # Arc to split
        "Z1": -1,  # First point of cutting line
        "Z2": -1j,  # Second point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [-1j, -1],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=1, end=-1j, radius=-1, is_trigo_direction=False)
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=-1j, end=-1, radius=-1, is_trigo_direction=False)
        ],  # Expected result for slip not is_top
    }
)
# 27 Arc2, 2 intersections, begin = int1 and end = int2
split_test.append(
    {
        "arc": Arc2(begin=1 + 1j, center=0, angle=pi / 2),  # Arc to split
        "Z1": -2 + 1j,  # First point of cutting line
        "Z2": 1 + 1j,  # Second point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [1 + 1j, -1 + 1j],  # Expected intersection points
        "Zs_top": [
            Arc2(begin=1 + 1j, center=0, angle=pi / 2)
        ],  # Expected result for slip is_top
        "Zs_bot": [],  # Expected result for slip not is_top
    }
)
# 28) Arc3, 1 Intersection
split_test.append(
    {
        "arc": Arc3(begin=10, end=-10, is_trigo_direction=True),  # Arc to split
        "Z1": -3j,  # First point of cutting line
        "Z2": 1j,  # Second point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [10j],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=10j, end=-10, radius=10, is_trigo_direction=True)
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=10, end=10j, radius=10, is_trigo_direction=True)
        ],  # Expected result for slip not is_top
    }
)
# 29) Case 28 with is_trigo=False
split_test.append(
    {
        "arc": Arc3(begin=10, end=-10, is_trigo_direction=False),  # Arc to split
        "Z1": -3j,  # First point of cutting line
        "Z2": 1j,  # Second point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [-10j],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=-10j, end=-10, radius=-10, is_trigo_direction=False)
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=10, end=-10j, radius=-10, is_trigo_direction=False)
        ],  # Expected result for slip not is_top
    }
)
# 30) Case 28 with reverse Z1 and Z2
split_test.append(
    {
        "arc": Arc3(begin=10, end=-10, is_trigo_direction=True),  # Arc to split
        "Z1": -3j,  # First point of cutting line
        "Z2": 1j,  # Second point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [10j],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=10j, end=-10, radius=10, is_trigo_direction=True)
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=10, end=10j, radius=10, is_trigo_direction=True)
        ],  # Expected result for slip not is_top
    }
)
# 31) Arc3 No Intersection
split_test.append(
    {
        "arc": Arc3(begin=1, end=-1, is_trigo_direction=False),  # Arc to split
        "Z1": 2 + 2j,  # First point of cutting line
        "Z2": 3 + 2j,  # Second point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [],  # Expected intersection points
        "Zs_top": [],  # Expected result for slip is_top
        "Zs_bot": [
            Arc3(begin=1, end=-1, is_trigo_direction=False)
        ],  # Expected result for slip not is_top
    }
)
# 32) Arc3, 1 Intersection = begin (tangent)
split_test.append(
    {
        "arc": Arc3(
            begin=-1 + 1j, end=1 + 1j, is_trigo_direction=False
        ),  # Arc to split
        "Z1": -1 + 1j,  # First point of cutting line
        "Z2": -1 - 1j,  # Second point of cutting line
        "center": 1j,  # Center of the arc (should not be changed by the split)
        "Zi": [-1 + 1j],  # Expected intersection points
        "Zs_top": [
            Arc3(begin=-1 + 1j, end=1 + 1j, is_trigo_direction=False)
        ],  # Expected result for slip is_top
        "Zs_bot": [],  # Expected result for slip not is_top
    }
)
# 33) Arc3, 1 Intersection = end (no tangent)
split_test.append(
    {
        "arc": Arc3(begin=-5j, end=5, is_trigo_direction=True),  # Arc to split
        "Z1": 4,  # First point of cutting line
        "Z2": 8,  # Second point of cutting line
        "center": 2.5 - 2.5j,  # Center of the arc (should not be changed by the split)
        "Zi": [5],  # Expected intersection points
        "Zs_top": [],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=-5j, end=5, radius=sqrt(50) / 2, is_trigo_direction=True)
        ],  # Expected result for slip not is_top
    }
)
# 34) Arc3, 1 Intersection (tangent) => Arc on bottom
split_test.append(
    {
        "arc": Arc3(begin=1j, end=-1j, is_trigo_direction=False),  # Arc to split
        "Z1": 1 + 1j,  # First point of cutting line
        "Z2": 1 - 1j,  # Second point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [1],  # Expected intersection points
        "Zs_top": [],  # Expected result for slip is_top
        "Zs_bot": [
            Arc3(begin=1j, end=-1j, is_trigo_direction=False)
        ],  # Expected result for slip not is_top
    }
)
# 35) Arc3, 1 Intersection (tangent) => Arc on top
split_test.append(
    {
        "arc": Arc3(begin=2 - 1j, end=-2 - 1j, is_trigo_direction=True),  # Arc to split
        "Z1": -2 + 1j,  # First point of cutting line
        "Z2": -4 + 1j,  # Second point of cutting line
        "center": -1j,  # Center of the arc (should not be changed by the split)
        "Zi": [1j],  # Expected intersection points
        "Zs_top": [
            Arc3(begin=2 - 1j, end=-2 - 1j, is_trigo_direction=True)
        ],  # Expected result for slip is_top
        "Zs_bot": [],  # Expected result for slip not is_top
    }
)
# 36) Arc3, 2 intersection
X = 4.44948974
split_test.append(
    {
        "arc": Arc3(begin=5, end=5j, is_trigo_direction=False),  # Arc to split
        "Z1": 4,  # First point of cutting line
        "Z2": 4j,  # Second point of cutting line
        "center": 2.5 + 2.5j,  # Center of the arc (should not be changed by the split)
        "Zi": [X - (X - 4) * 1j, -(X - 4) + X * 1j],  # Expected intersection points
        "Zs_top": [
            Arc1(
                begin=X - (X - 4) * 1j,
                end=-(X - 4) + X * 1j,
                radius=-sqrt(50) / 2,
                is_trigo_direction=False,
            )
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(
                begin=5,
                end=X - (X - 4) * 1j,
                radius=-sqrt(50) / 2,
                is_trigo_direction=False,
            ),
            Arc1(
                begin=-(X - 4) + X * 1j,
                end=5j,
                radius=-sqrt(50) / 2,
                is_trigo_direction=False,
            ),
        ],  # Expected result for slip not is_top
    }
)
# 37) Same as 36 with reversed cutting line
split_test.append(
    {
        "arc": Arc3(begin=5, end=5j, is_trigo_direction=False),  # Arc to split
        "Z1": 4j,  # First point of cutting line
        "Z2": 4,  # Second point of cutting line
        "center": 2.5 + 2.5j,  # Center of the arc (should not be changed by the split)
        "Zi": [X - (X - 4) * 1j, -(X - 4) + X * 1j],  # Expected intersection points
        "Zs_top": [
            Arc1(
                begin=5,
                end=X - (X - 4) * 1j,
                radius=-sqrt(50) / 2,
                is_trigo_direction=False,
            ),
            Arc1(
                begin=-(X - 4) + X * 1j,
                end=5j,
                radius=-sqrt(50) / 2,
                is_trigo_direction=False,
            ),
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(
                begin=X - (X - 4) * 1j,
                end=-(X - 4) + X * 1j,
                radius=-sqrt(50) / 2,
                is_trigo_direction=False,
            )
        ],  # Expected result for slip not is_top
    }
)
# 38) Arc2, 2 intersection, is_trigo=True
split_test.append(
    {
        "arc": Arc3(begin=1, end=-1, is_trigo_direction=True),  # Arc to split
        "Z1": 0.5j,  # First point of cutting line
        "Z2": 1 + 0.5j,  # Second point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [sqrt(0.75) + 0.5j, -sqrt(0.75) + 0.5j],  # Expected intersection points
        "Zs_top": [
            Arc1(
                begin=sqrt(0.75) + 0.5j,
                end=-sqrt(0.75) + 0.5j,
                radius=1,
                is_trigo_direction=True,
            )
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=1, end=sqrt(0.75) + 0.5j, radius=1, is_trigo_direction=True),
            Arc1(begin=-sqrt(0.75) + 0.5j, end=-1, radius=1, is_trigo_direction=True),
        ],  # Expected result for slip not is_top
    }
)
# 39) Arc3, 2 intersections, begin = int1
split_test.append(
    {
        "arc": Arc3(begin=0, end=4j, is_trigo_direction=False),  # Arc to split
        "Z1": 0,  # First point of cutting line
        "Z2": -4 + 4j,  # Second point of cutting line
        "center": 2j,  # Center of the arc (should not be changed by the split)
        "Zi": [0, -2 + 2j],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=0, end=-2 + 2j, radius=-2, is_trigo_direction=False)
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=-2 + 2j, end=4j, radius=-2, is_trigo_direction=False)
        ],  # Expected result for slip not is_top
    }
)
# 40) Arc3, 2 intersections, end = int2
split_test.append(
    {
        "arc": Arc3(begin=-4 + 1j, end=1j, is_trigo_direction=True),  # Arc to split
        "Z1": -1,  # First point of cutting line
        "Z2": 1 + 2j,  # Second point of cutting line
        "center": -2 + 1j,  # Center of the arc (should not be changed by the split)
        "Zi": [-2 - 1j, 1j],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=-4 + 1j, end=-2 - 1j, radius=2, is_trigo_direction=True)
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=-2 - 1j, end=1j, radius=2, is_trigo_direction=True)
        ],  # Expected result for slip not is_top
    }
)
# 41) Arc2, 2 intersections, begin = int1 and end = int2
split_test.append(
    {
        "arc": Arc3(begin=-4 - 4j, end=6 + 6j, is_trigo_direction=True),  # Arc to split
        "Z1": 0,  # First point of cutting line
        "Z2": 1 + 1j,  # Second point of cutting line
        "center": 1 + 1j,  # Center of the arc (should not be changed by the split)
        "Zi": [-4 - 4j, 6 + 6j],  # Expected intersection points
        "Zs_top": [],  # Expected result for slip is_top
        "Zs_bot": [
            Arc3(begin=-4 - 4j, end=6 + 6j, is_trigo_direction=True)
        ],  # Expected result for slip not is_top
    }
)


"""unittest for Arc split methods"""


@pytest.mark.parametrize("test_dict", split_test)
def test_split_line(test_dict):
    """Check that the intersection and the split_line is computed correctly"""
    arc_obj = test_dict["arc"]

    # Check center
    Zc = arc_obj.get_center()
    msg = (
        "Wrong center: returned " + str(Zc) + ", expected: " + str(test_dict["center"])
    )
    assert abs(Zc - test_dict["center"]) == pytest.approx(0, abs=DELTA), msg

    # Check intersection
    result = arc_obj.intersect_line(test_dict["Z1"], test_dict["Z2"])
    assert len(result) == len(test_dict["Zi"])
    msg = (
        "Wrong intersection: returned "
        + str(result)
        + ", expected: "
        + str(test_dict["Zi"])
    )
    for ii in range(len(result)):
        assert result[ii] == pytest.approx(test_dict["Zi"][ii], abs=DELTA), msg

    # Check split_line is_top=True
    split_list = arc_obj.split_line(test_dict["Z1"], test_dict["Z2"], is_top=True)
    assert len(split_list) == len(test_dict["Zs_top"])
    msg = "Wrong split top: returned [\n"
    for split in split_list:
        msg += (
            "beg:"
            + str(split.get_begin())
            + ", end:"
            + str(split.get_end())
            + ", R:"
            + str(split.comp_radius())
            + ", alpha:"
            + str(split.get_angle())
            + "\n"
        )
    msg += "], expected: [\n"
    for split in test_dict["Zs_top"]:
        msg += (
            "beg:"
            + str(split.get_begin())
            + ", end:"
            + str(split.get_end())
            + ", R:"
            + str(split.comp_radius())
            + ", alpha:"
            + str(split.get_angle())
            + "\n"
        )
    msg += "]"
    for ii in range(len(split_list)):
        assert type(split_list[ii]) == type(test_dict["Zs_top"][ii]), (
            "Type error for index " + str(ii) + " returned " + str(type(split_list[ii]))
        )
        assert abs(split_list[ii].get_center() - test_dict["center"]) == pytest.approx(
            0, abs=DELTA
        ), ("Center error: " + msg)
        assert abs(
            split_list[ii].get_begin() - test_dict["Zs_top"][ii].get_begin()
        ) == pytest.approx(0, abs=DELTA), ("Begin error: " + msg)
        assert abs(
            split_list[ii].get_end() - test_dict["Zs_top"][ii].get_end()
        ) == pytest.approx(0, abs=DELTA), ("End error: " + msg)
        assert split_list[ii].comp_radius() == test_dict["Zs_top"][ii].comp_radius(), (
            "Radius error: " + msg
        )
        assert split_list[ii].get_angle() == pytest.approx(
            test_dict["Zs_top"][ii].get_angle(), abs=DELTA
        ), ("Angle error: " + msg)

    # Check split_line is_top=False
    split_list = arc_obj.split_line(test_dict["Z1"], test_dict["Z2"], is_top=False)
    assert len(split_list) == len(test_dict["Zs_bot"])
    msg = "Wrong split bot: returned [\n"
    for split in split_list:
        msg += (
            "beg:"
            + str(split.get_begin())
            + ", end:"
            + str(split.get_end())
            + ", R:"
            + str(split.comp_radius())
            + ", alpha:"
            + str(split.get_angle())
            + "\n"
        )
    msg += "\n], expected: [\n"
    for split in test_dict["Zs_bot"]:
        msg += (
            "beg:"
            + str(split.get_begin())
            + ", end:"
            + str(split.get_end())
            + ", R:"
            + str(split.comp_radius())
            + ", alpha:"
            + str(split.get_angle())
            + "\n"
        )
    msg += "]"
    for ii in range(len(split_list)):
        assert type(split_list[ii]) == type(test_dict["Zs_bot"][ii]), (
            "Type error for index " + str(ii) + " returned " + str(type(split_list[ii]))
        )
        assert abs(split_list[ii].get_center() - test_dict["center"]) == pytest.approx(
            0, abs=DELTA
        ), ("Center error: " + msg)
        assert abs(
            split_list[ii].get_begin() - test_dict["Zs_bot"][ii].get_begin()
        ) == pytest.approx(0, abs=DELTA), ("Begin error: " + msg)
        assert abs(
            split_list[ii].get_end() - test_dict["Zs_bot"][ii].get_end()
        ) == pytest.approx(0, abs=DELTA), ("End error: " + msg)
        assert split_list[ii].comp_radius() == test_dict["Zs_bot"][ii].comp_radius(), (
            "Radius error: " + msg
        )
        assert split_list[ii].get_angle() == pytest.approx(
            test_dict["Zs_bot"][ii].get_angle(), abs=DELTA
        ), ("Angle error: " + msg)


# Compute the distance
D_test = list()
# 0
D_test.append(
    {
        "arc": Arc1(begin=1, end=1j, radius=1, is_trigo_direction=True),
        "Z": 2,  # First point of cutting line
        "D": 1,
    }
)
# 1
D_test.append(
    {
        "arc": Arc1(begin=1, end=1j, radius=1, is_trigo_direction=True),
        "Z": 0,  # First point of cutting line
        "D": 1,
    }
)
# 2
D_test.append(
    {
        "arc": Arc1(begin=1, end=1j, radius=1, is_trigo_direction=True),
        "Z": -1j,  # First point of cutting line
        "D": sqrt(2),
    }
)
# 3
D_test.append(
    {
        "arc": Arc1(begin=1, end=1j, radius=1, is_trigo_direction=True),
        "Z": -2j,  # First point of cutting line
        "D": sqrt(5),
    }
)
# 4
D_test.append(
    {
        "arc": Arc1(begin=1, end=1j, radius=1, is_trigo_direction=True),
        "Z": exp(1j * pi / 4),  # First point of cutting line
        "D": 0,
    }
)
# 5
D_test.append(
    {
        "arc": Arc1(begin=1, end=1j, radius=1, is_trigo_direction=True),
        "Z": 1 + 1j,  # First point of cutting line
        "D": abs(1 + 1j - exp(1j * pi / 4)),
    }
)
# 6
D_test.append(
    {
        "arc": Arc1(begin=-2j, end=-1 - 1j, radius=1, is_trigo_direction=False),
        "Z": -2j + 1,  # First point of cutting line
        "D": 1,
    }
)
# 7
D_test.append(
    {
        "arc": Arc1(begin=-2j, end=-1 - 1j, radius=-1, is_trigo_direction=False),
        "Z": -1j,  # First point of cutting line
        "D": 1,
    }
)
# 8
D_test.append(
    {
        "arc": Arc1(begin=-2j, end=-1 - 1j, radius=-1, is_trigo_direction=False),
        "Z": 0,  # First point of cutting line
        "D": sqrt(2),
    }
)
# 9
D_test.append(
    {
        "arc": Arc1(begin=-2j, end=-1 - 1j, radius=-1, is_trigo_direction=False),
        "Z": 1,  # First point of cutting line
        "D": sqrt(5),
    }
)
# 10
D_test.append(
    {
        "arc": Arc1(begin=-2j, end=-1 - 1j, radius=-1, is_trigo_direction=False),
        "Z": -1j + exp(1j * 5 * pi / 4),  # First point of cutting line
        "D": 0,
    }
)
# 11
D_test.append(
    {
        "arc": Arc1(begin=-2j, end=-1 - 1j, radius=-1, is_trigo_direction=False),
        "Z": -1 - 2j,  # First point of cutting line
        "D": abs(-1 - 2j - (-1j + exp(1j * 5 * pi / 4))),
    }
)


@pytest.mark.parametrize("test_dict", D_test)
def test_distance(test_dict):
    """Check the comp_distance method"""
    arc_obj = test_dict["arc"]

    # Check center
    result = arc_obj.comp_distance(test_dict["Z"])
    msg = (
        "Wrong distance: returned " + str(result) + ", expected: " + str(test_dict["D"])
    )
    assert result == pytest.approx(test_dict["D"], abs=DELTA), msg


"""Tests of the function is_on_line from Arc meth"""

is_on_line_list = list()

# 1  Check not on the circle
is_on_line_list.append(
    {
        "arc": Arc1(begin=-2j, end=-1 - 1j, radius=-1, is_trigo_direction=False),
        "Z": -1 - 2j,  # First point of cutting line
        "result": False,
    }
)

# 2  Check on the circle
is_on_line_list.append(
    {
        "arc": Arc1(begin=-2j, end=-1 - 1j, radius=-1, is_trigo_direction=False),
        "Z": -1j + exp(1j * 5 * pi / 4),  # First point of cutting line
        "result": True,
    }
)

# 3 Check on the beg of the arc
is_on_line_list.append(
    {
        "arc": Arc1(begin=-2j, end=-1 - 1j, radius=-1, is_trigo_direction=False),
        "Z": -2j,  # First point of cutting line
        "result": True,
    }
)

# 4 Check on the end of the arc
is_on_line_list.append(
    {
        "arc": Arc1(begin=-2j, end=-1 - 1j, radius=-1, is_trigo_direction=False),
        "Z": -1 -1j,  # First point of cutting line
        "result": True,
    }
)

# 5 Check above the arc
is_on_line_list.append(
    {
        "arc": Arc1(begin=-2j, end=-1 - 1j, radius=-1, is_trigo_direction=False),
        "Z": -1j,  # First point of cutting line
        "result": False,
    }
)

# 6 Check beneath the arc
is_on_line_list.append(
    {
        "arc": Arc1(begin=-2j, end=-1 - 1j, radius=-1, is_trigo_direction=False),
        "Z": -1-2j,  # First point of cutting line
        "result": False,
    }
)


@pytest.mark.parametrize("test_dict", is_on_line_list)
def test_is_on_line(test_dict):
    """Check is_on_line method"""
    arc_obj = test_dict["arc"]

    # Check on the circle
    result = arc_obj.is_on_line(test_dict["Z"])

    assert result == test_dict["result"]
