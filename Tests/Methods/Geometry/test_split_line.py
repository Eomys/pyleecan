from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine
import pytest

line_list = list()
line_list.append(Segment(begin=-1j, end=1j))
line_list.append(Segment(begin=1j, end=1j + 1))
line_list.append(Segment(begin=1j + 1, end=-1j + 1))
line_list.append(Segment(begin=-1j + 1, end=-1j))

surf = SurfLine(line_list=line_list, label="test", point_ref=0.5)

split_test = list()
# Cut Square top
line_list = list()
line_list.append(Segment(begin=0, end=1j))
line_list.append(Segment(begin=1j, end=1j + 1))
line_list.append(Segment(begin=1j + 1, end=1))
line_list.append(Segment(begin=1, end=0))
exp_surf = SurfLine(line_list=line_list, label="test", point_ref=0.5 + 0.5j)

split_test.append(
    {
        "surf": surf,
        "exp_surf": exp_surf,
        "Z1": 0,
        "Z2": 2,
        "is_top": True,
        "is_join": True,
    }
)
# Cut Square bottom
line_list = list()
line_list.append(Segment(begin=-1j, end=0))
line_list.append(Segment(begin=0, end=1))
line_list.append(Segment(begin=1, end=-1j + 1))
line_list.append(Segment(begin=-1j + 1, end=-1j))
exp_surf = SurfLine(line_list=line_list, label="test", point_ref=0.5 - 0.5j)

split_test.append(
    {
        "surf": surf,
        "exp_surf": exp_surf,
        "Z1": 0,
        "Z2": 2,
        "is_top": False,
        "is_join": True,
    }
)


@pytest.mark.parametrize("test_dict", split_test)
def test_split_line(test_dict):

    res_surf = test_dict["surf"].split_line(
        Z1=test_dict["Z1"],
        Z2=test_dict["Z2"],
        is_top=test_dict["is_top"],
        is_join=test_dict["is_join"],
        label_join="",
    )

    assert res_surf == test_dict["exp_surf"], (
        "Differente surface:\nResult:\n"
        + str(res_surf)
        + "\nExpected:\n"
        + str(test_dict["exp_surf"])
    )
