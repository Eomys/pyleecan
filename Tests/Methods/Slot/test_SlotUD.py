import pytest
from os.path import join
from pyleecan.Classes.SlotUD2 import SlotUD2
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

# For AlmostEqual
DELTA = 1e-6


class TestSlotUD_meth(object):
    """pytest for SlotUD methods"""

    def setup_method(self):
        self.Prius_Dxf = load(join(DATA_DIR, "Machine", "Toyota_Prius_DXF.json"))
        self.slot_dxf = self.Prius_Dxf.stator.slot
        self.Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
        self.slot = self.Prius.stator.slot

    def test_get_surface_X(self):
        """Check that the get_surface_X works when stator = false"""

        # 7 lines, one before active, one after
        assert len(self.slot_dxf.line_list) == 7
        assert self.slot_dxf.wind_begin_index == 1
        assert self.slot_dxf.wind_end_index == 6

        # Active Surface
        Dxf_act = self.slot_dxf.get_surface_active()
        assert Dxf_act.label == "Stator-0_Winding_R0-T0-S0"
        assert len(Dxf_act.get_lines()) == 6
        assert Dxf_act.is_inside(Dxf_act.point_ref)

        # Opening Surface
        Dxf_op = self.slot_dxf.get_surface_opening()
        assert len(Dxf_op) == 1
        assert Dxf_op[0].label == "Stator-0_SlotOpening_R0-T0-S0"
        assert len(Dxf_op[0].get_lines()) == 4
        assert Dxf_op[0].is_inside(Dxf_op[0].point_ref)

        # Complete surface
        Dxf_tot = self.slot_dxf.get_surface()
        assert len(Dxf_tot.get_lines()) == 8
        assert Dxf_tot.is_inside(Dxf_tot.point_ref)

        # Check computation
        Sa = Dxf_act.comp_surface()
        So = Dxf_op[0].comp_surface()
        St = Dxf_tot.comp_surface()
        assert Sa + So == pytest.approx(St, rel=0.1)
        assert Sa + So == pytest.approx(self.slot.comp_surface(), rel=0.1)

    def test_to_UD2(self):
        """Check that the slot can be converted to UD2"""
        slot_2 = self.slot_dxf.convert_to_SlotUD2()
        assert isinstance(slot_2, SlotUD2)
        assert len(slot_2.line_list) == 7
        assert len(slot_2.active_surf.line_list) == 6

        slot_2.parent = self.Prius.stator
        assert slot_2.comp_surface() == pytest.approx(self.slot.comp_surface(), rel=0.1)


if __name__ == "__main__":
    a = TestSlotUD_meth()
    a.setup_method()
    a.test_get_surface_X()
    a.test_to_UD2()
    print("Done")
