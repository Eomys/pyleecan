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
exp_top_surf = SurfLine(line_list=line_list, label="test", point_ref=0.5 + 0.5j)
# Cut Square bottom
line_list = list()
line_list.append(Segment(begin=-1j, end=0))
line_list.append(Segment(begin=0, end=1))
line_list.append(Segment(begin=1, end=-1j + 1))
line_list.append(Segment(begin=-1j + 1, end=-1j))
exp_bot_surf = SurfLine(line_list=line_list, label="test", point_ref=0.5 - 0.5j)

split_test.append(
    {
        "surf": surf,
        "exp_top_surf": exp_top_surf,
        "exp_bot_surf": exp_bot_surf,
        "Z1": 0,
        "Z2": 2,
        "is_join": True,
    }
)


@pytest.mark.parametrize("test_dict", split_test)
def test_split_line(test_dict):
    res_top_surf, res_bot_surf = test_dict["surf"].split_line(
        Z1=test_dict["Z1"],
        Z2=test_dict["Z2"],
        is_join=test_dict["is_join"],
    )

    assert res_top_surf == test_dict["exp_top_surf"], (
        "Differente Top surface:\nResult:\n"
        + str(res_top_surf)
        + "\nExpected:\n"
        + str(test_dict["exp_top_surf"])
    )
    assert res_bot_surf == test_dict["exp_bot_surf"], (
        "Differente Bot surface:\nResult:\n"
        + str(res_bot_surf)
        + "\nExpected:\n"
        + str(test_dict["exp_bot_surf"])
    )


if __name__ == "__main__":
    for test_dict in split_test:
        test_split_line(test_dict)
    print("Done")
