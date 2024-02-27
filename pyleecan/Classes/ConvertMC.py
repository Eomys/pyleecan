# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Converter/ConvertMC.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Converter/ConvertMC
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from .Convert import Convert

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Converter.ConvertMC.convert_to_P.convert_other_to_dict import (
        convert_other_to_dict,
    )
except ImportError as error:
    convert_other_to_dict = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_P.convert_slot_to_P import (
        convert_slot_to_P,
    )
except ImportError as error:
    convert_slot_to_P = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_P.convert_slot_rotor_to_P import (
        convert_slot_rotor_to_P,
    )
except ImportError as error:
    convert_slot_rotor_to_P = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_P.convert_machine_to_P import (
        convert_machine_to_P,
    )
except ImportError as error:
    convert_machine_to_P = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_P.convert_magnet_to_P import (
        convert_magnet_to_P,
    )
except ImportError as error:
    convert_magnet_to_P = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_P.convert_hole_to_P import (
        convert_hole_to_P,
    )
except ImportError as error:
    convert_hole_to_P = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_P.convert_pole_to_P import (
        convert_pole_to_P,
    )
except ImportError as error:
    convert_pole_to_P = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_P.convert_duct_to_P import (
        convert_duct_to_P,
    )
except ImportError as error:
    convert_duct_to_P = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_P.convert_notch_to_P import (
        convert_notch_to_P,
    )
except ImportError as error:
    convert_notch_to_P = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_P.convert_conductor_to_P import (
        convert_conductor_to_P,
    )
except ImportError as error:
    convert_conductor_to_P = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_P.convert_material_to_P import (
        convert_material_to_P,
    )
except ImportError as error:
    convert_material_to_P = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_P.convert_skew_to_P import (
        convert_skew_to_P,
    )
except ImportError as error:
    convert_skew_to_P = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_other.convert_slot_rotor_to_other import (
        convert_slot_rotor_to_other,
    )
except ImportError as error:
    convert_slot_rotor_to_other = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_other.init_other_unit import (
        init_other_unit,
    )
except ImportError as error:
    init_other_unit = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_other.convert_slot_to_other import (
        convert_slot_to_other,
    )
except ImportError as error:
    convert_slot_to_other = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_other.convert_machine_to_other import (
        convert_machine_to_other,
    )
except ImportError as error:
    convert_machine_to_other = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_other.convert_magnet_to_other import (
        convert_magnet_to_other,
    )
except ImportError as error:
    convert_magnet_to_other = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_other.convert_hole_to_other import (
        convert_hole_to_other,
    )
except ImportError as error:
    convert_hole_to_other = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_other.convert_duct_to_other import (
        convert_duct_to_other,
    )
except ImportError as error:
    convert_duct_to_other = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_other.convert_notch_to_other import (
        convert_notch_to_other,
    )
except ImportError as error:
    convert_notch_to_other = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_other.convert_pole_to_other import (
        convert_pole_to_other,
    )
except ImportError as error:
    convert_pole_to_other = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_other.convert_conductor_to_other import (
        convert_conductor_to_other,
    )
except ImportError as error:
    convert_conductor_to_other = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_other.convert_material_to_other import (
        convert_material_to_other,
    )
except ImportError as error:
    convert_material_to_other = error

try:
    from ..Methods.Converter.ConvertMC.convert_to_other.convert_skew_to_other import (
        convert_skew_to_other,
    )
except ImportError as error:
    convert_skew_to_other = error

try:
    from ..Methods.Converter.ConvertMC.Rules.add_rule_machine_dimension import (
        add_rule_machine_dimension,
    )
except ImportError as error:
    add_rule_machine_dimension = error

try:
    from ..Methods.Converter.ConvertMC.Rules.add_rule_machine_dimension_surface_magnet import (
        add_rule_machine_dimension_surface_magnet,
    )
except ImportError as error:
    add_rule_machine_dimension_surface_magnet = error

try:
    from ..Methods.Converter.ConvertMC.Rules.add_rule_machine_type import (
        add_rule_machine_type,
    )
except ImportError as error:
    add_rule_machine_type = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Slot.add_rule_slotW11 import (
        add_rule_slotW11,
    )
except ImportError as error:
    add_rule_slotW11 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Slot.add_rule_slotW29 import (
        add_rule_slotW29,
    )
except ImportError as error:
    add_rule_slotW29 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Slot.add_rule_slotW21 import (
        add_rule_slotW21,
    )
except ImportError as error:
    add_rule_slotW21 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Slot.add_rule_slotW14 import (
        add_rule_slotW14,
    )
except ImportError as error:
    add_rule_slotW14 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Slot.add_rule_slotW23 import (
        add_rule_slotW23,
    )
except ImportError as error:
    add_rule_slotW23 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Slot.rotor.add_rule_rotor_slotW30 import (
        add_rule_rotor_slotW30,
    )
except ImportError as error:
    add_rule_rotor_slotW30 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Slot.rotor.add_rule_rotor_slotW23 import (
        add_rule_rotor_slotW23,
    )
except ImportError as error:
    add_rule_rotor_slotW23 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Slot.rotor.add_rule_rotor_slotW11_2 import (
        add_rule_rotor_slotW11_2,
    )
except ImportError as error:
    add_rule_rotor_slotW11_2 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Slot.rotor.add_rule_rotor_slotW26 import (
        add_rule_rotor_slotW26,
    )
except ImportError as error:
    add_rule_rotor_slotW26 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Lamination.add_rule_ventilationCirc import (
        add_rule_ventilationCirc,
    )
except ImportError as error:
    add_rule_ventilationCirc = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Lamination.add_rule_ventilationPolar import (
        add_rule_ventilationPolar,
    )
except ImportError as error:
    add_rule_ventilationPolar = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Lamination.add_rule_ventilationTrap import (
        add_rule_ventilationTrap,
    )
except ImportError as error:
    add_rule_ventilationTrap = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Lamination.add_rule_notch_slotM19 import (
        add_rule_notch_slotM19,
    )
except ImportError as error:
    add_rule_notch_slotM19 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Lamination.add_rule_lamination import (
        add_rule_lamination,
    )
except ImportError as error:
    add_rule_lamination = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Rotor_Magnet.add_rule_slotM14 import (
        add_rule_slotM14,
    )
except ImportError as error:
    add_rule_slotM14 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Rotor_Magnet.add_rule_slotM13 import (
        add_rule_slotM13,
    )
except ImportError as error:
    add_rule_slotM13 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Rotor_Magnet.add_rule_slotM16 import (
        add_rule_slotM16,
    )
except ImportError as error:
    add_rule_slotM16 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Rotor_Magnet.add_rule_slotM11 import (
        add_rule_slotM11,
    )
except ImportError as error:
    add_rule_slotM11 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Rotor_Magnet.add_rule_slotM15 import (
        add_rule_slotM15,
    )
except ImportError as error:
    add_rule_slotM15 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Rotor_Magnet.add_rule_slotM12 import (
        add_rule_slotM12,
    )
except ImportError as error:
    add_rule_slotM12 = error

try:
    from ..Methods.Converter.ConvertMC.select_SIPMSM_machine_dimension import (
        select_SIPMSM_machine_dimension,
    )
except ImportError as error:
    select_SIPMSM_machine_dimension = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Hole.add_rule_holeM61 import (
        add_rule_holeM61,
    )
except ImportError as error:
    add_rule_holeM61 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Hole.add_rule_holeM57 import (
        add_rule_holeM57,
    )
except ImportError as error:
    add_rule_holeM57 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Hole.add_rule_holeM60 import (
        add_rule_holeM60,
    )
except ImportError as error:
    add_rule_holeM60 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Hole.add_rule_holeM63 import (
        add_rule_holeM63,
    )
except ImportError as error:
    add_rule_holeM63 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Hole.add_rule_holeM52 import (
        add_rule_holeM52,
    )
except ImportError as error:
    add_rule_holeM52 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Hole.add_rule_holeM62 import (
        add_rule_holeM62,
    )
except ImportError as error:
    add_rule_holeM62 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Pole.add_rule_parallel_tooth_slotW63 import (
        add_rule_parallel_tooth_slotW63,
    )
except ImportError as error:
    add_rule_parallel_tooth_slotW63 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Pole.add_rule_salient_pole_slotW62 import (
        add_rule_salient_pole_slotW62,
    )
except ImportError as error:
    add_rule_salient_pole_slotW62 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Pole.add_rule_parallel_slot_slotW29 import (
        add_rule_parallel_slot_slotW29,
    )
except ImportError as error:
    add_rule_parallel_slot_slotW29 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Winding.add_rule_winding import (
        add_rule_winding,
    )
except ImportError as error:
    add_rule_winding = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Winding.add_rule_condtype11 import (
        add_rule_condtype11,
    )
except ImportError as error:
    add_rule_condtype11 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Winding.add_rule_condtype12 import (
        add_rule_condtype12,
    )
except ImportError as error:
    add_rule_condtype12 = error

try:
    from ..Methods.Converter.ConvertMC.Rules.Winding.add_rule_rotor_bar import (
        add_rule_rotor_bar,
    )
except ImportError as error:
    add_rule_rotor_bar = error

try:
    from ..Methods.Converter.ConvertMC.Rules.add_rule_material_magnetics import (
        add_rule_material_magnetics,
    )
except ImportError as error:
    add_rule_material_magnetics = error

try:
    from ..Methods.Converter.ConvertMC.Rules.add_rule_material import add_rule_material
except ImportError as error:
    add_rule_material = error

try:
    from ..Methods.Converter.ConvertMC.Rules.add_rule_skew import add_rule_skew
except ImportError as error:
    add_rule_skew = error


from numpy import isnan
from ._check import InitUnKnowClassError


class ConvertMC(Convert):
    """convertorMC abstract"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Converter.ConvertMC.convert_to_P.convert_other_to_dict
    if isinstance(convert_other_to_dict, ImportError):
        convert_other_to_dict = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_other_to_dict: "
                    + str(convert_other_to_dict)
                )
            )
        )
    else:
        convert_other_to_dict = convert_other_to_dict
    # cf Methods.Converter.ConvertMC.convert_to_P.convert_slot_to_P
    if isinstance(convert_slot_to_P, ImportError):
        convert_slot_to_P = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_slot_to_P: "
                    + str(convert_slot_to_P)
                )
            )
        )
    else:
        convert_slot_to_P = convert_slot_to_P
    # cf Methods.Converter.ConvertMC.convert_to_P.convert_slot_rotor_to_P
    if isinstance(convert_slot_rotor_to_P, ImportError):
        convert_slot_rotor_to_P = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_slot_rotor_to_P: "
                    + str(convert_slot_rotor_to_P)
                )
            )
        )
    else:
        convert_slot_rotor_to_P = convert_slot_rotor_to_P
    # cf Methods.Converter.ConvertMC.convert_to_P.convert_machine_to_P
    if isinstance(convert_machine_to_P, ImportError):
        convert_machine_to_P = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_machine_to_P: "
                    + str(convert_machine_to_P)
                )
            )
        )
    else:
        convert_machine_to_P = convert_machine_to_P
    # cf Methods.Converter.ConvertMC.convert_to_P.convert_magnet_to_P
    if isinstance(convert_magnet_to_P, ImportError):
        convert_magnet_to_P = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_magnet_to_P: "
                    + str(convert_magnet_to_P)
                )
            )
        )
    else:
        convert_magnet_to_P = convert_magnet_to_P
    # cf Methods.Converter.ConvertMC.convert_to_P.convert_hole_to_P
    if isinstance(convert_hole_to_P, ImportError):
        convert_hole_to_P = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_hole_to_P: "
                    + str(convert_hole_to_P)
                )
            )
        )
    else:
        convert_hole_to_P = convert_hole_to_P
    # cf Methods.Converter.ConvertMC.convert_to_P.convert_pole_to_P
    if isinstance(convert_pole_to_P, ImportError):
        convert_pole_to_P = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_pole_to_P: "
                    + str(convert_pole_to_P)
                )
            )
        )
    else:
        convert_pole_to_P = convert_pole_to_P
    # cf Methods.Converter.ConvertMC.convert_to_P.convert_duct_to_P
    if isinstance(convert_duct_to_P, ImportError):
        convert_duct_to_P = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_duct_to_P: "
                    + str(convert_duct_to_P)
                )
            )
        )
    else:
        convert_duct_to_P = convert_duct_to_P
    # cf Methods.Converter.ConvertMC.convert_to_P.convert_notch_to_P
    if isinstance(convert_notch_to_P, ImportError):
        convert_notch_to_P = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_notch_to_P: "
                    + str(convert_notch_to_P)
                )
            )
        )
    else:
        convert_notch_to_P = convert_notch_to_P
    # cf Methods.Converter.ConvertMC.convert_to_P.convert_conductor_to_P
    if isinstance(convert_conductor_to_P, ImportError):
        convert_conductor_to_P = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_conductor_to_P: "
                    + str(convert_conductor_to_P)
                )
            )
        )
    else:
        convert_conductor_to_P = convert_conductor_to_P
    # cf Methods.Converter.ConvertMC.convert_to_P.convert_material_to_P
    if isinstance(convert_material_to_P, ImportError):
        convert_material_to_P = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_material_to_P: "
                    + str(convert_material_to_P)
                )
            )
        )
    else:
        convert_material_to_P = convert_material_to_P
    # cf Methods.Converter.ConvertMC.convert_to_P.convert_skew_to_P
    if isinstance(convert_skew_to_P, ImportError):
        convert_skew_to_P = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_skew_to_P: "
                    + str(convert_skew_to_P)
                )
            )
        )
    else:
        convert_skew_to_P = convert_skew_to_P
    # cf Methods.Converter.ConvertMC.convert_to_other.convert_slot_rotor_to_other
    if isinstance(convert_slot_rotor_to_other, ImportError):
        convert_slot_rotor_to_other = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_slot_rotor_to_other: "
                    + str(convert_slot_rotor_to_other)
                )
            )
        )
    else:
        convert_slot_rotor_to_other = convert_slot_rotor_to_other
    # cf Methods.Converter.ConvertMC.convert_to_other.init_other_unit
    if isinstance(init_other_unit, ImportError):
        init_other_unit = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method init_other_unit: "
                    + str(init_other_unit)
                )
            )
        )
    else:
        init_other_unit = init_other_unit
    # cf Methods.Converter.ConvertMC.convert_to_other.convert_slot_to_other
    if isinstance(convert_slot_to_other, ImportError):
        convert_slot_to_other = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_slot_to_other: "
                    + str(convert_slot_to_other)
                )
            )
        )
    else:
        convert_slot_to_other = convert_slot_to_other
    # cf Methods.Converter.ConvertMC.convert_to_other.convert_machine_to_other
    if isinstance(convert_machine_to_other, ImportError):
        convert_machine_to_other = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_machine_to_other: "
                    + str(convert_machine_to_other)
                )
            )
        )
    else:
        convert_machine_to_other = convert_machine_to_other
    # cf Methods.Converter.ConvertMC.convert_to_other.convert_magnet_to_other
    if isinstance(convert_magnet_to_other, ImportError):
        convert_magnet_to_other = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_magnet_to_other: "
                    + str(convert_magnet_to_other)
                )
            )
        )
    else:
        convert_magnet_to_other = convert_magnet_to_other
    # cf Methods.Converter.ConvertMC.convert_to_other.convert_hole_to_other
    if isinstance(convert_hole_to_other, ImportError):
        convert_hole_to_other = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_hole_to_other: "
                    + str(convert_hole_to_other)
                )
            )
        )
    else:
        convert_hole_to_other = convert_hole_to_other
    # cf Methods.Converter.ConvertMC.convert_to_other.convert_duct_to_other
    if isinstance(convert_duct_to_other, ImportError):
        convert_duct_to_other = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_duct_to_other: "
                    + str(convert_duct_to_other)
                )
            )
        )
    else:
        convert_duct_to_other = convert_duct_to_other
    # cf Methods.Converter.ConvertMC.convert_to_other.convert_notch_to_other
    if isinstance(convert_notch_to_other, ImportError):
        convert_notch_to_other = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_notch_to_other: "
                    + str(convert_notch_to_other)
                )
            )
        )
    else:
        convert_notch_to_other = convert_notch_to_other
    # cf Methods.Converter.ConvertMC.convert_to_other.convert_pole_to_other
    if isinstance(convert_pole_to_other, ImportError):
        convert_pole_to_other = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_pole_to_other: "
                    + str(convert_pole_to_other)
                )
            )
        )
    else:
        convert_pole_to_other = convert_pole_to_other
    # cf Methods.Converter.ConvertMC.convert_to_other.convert_conductor_to_other
    if isinstance(convert_conductor_to_other, ImportError):
        convert_conductor_to_other = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_conductor_to_other: "
                    + str(convert_conductor_to_other)
                )
            )
        )
    else:
        convert_conductor_to_other = convert_conductor_to_other
    # cf Methods.Converter.ConvertMC.convert_to_other.convert_material_to_other
    if isinstance(convert_material_to_other, ImportError):
        convert_material_to_other = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_material_to_other: "
                    + str(convert_material_to_other)
                )
            )
        )
    else:
        convert_material_to_other = convert_material_to_other
    # cf Methods.Converter.ConvertMC.convert_to_other.convert_skew_to_other
    if isinstance(convert_skew_to_other, ImportError):
        convert_skew_to_other = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method convert_skew_to_other: "
                    + str(convert_skew_to_other)
                )
            )
        )
    else:
        convert_skew_to_other = convert_skew_to_other
    # cf Methods.Converter.ConvertMC.Rules.add_rule_machine_dimension
    if isinstance(add_rule_machine_dimension, ImportError):
        add_rule_machine_dimension = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_machine_dimension: "
                    + str(add_rule_machine_dimension)
                )
            )
        )
    else:
        add_rule_machine_dimension = add_rule_machine_dimension
    # cf Methods.Converter.ConvertMC.Rules.add_rule_machine_dimension_surface_magnet
    if isinstance(add_rule_machine_dimension_surface_magnet, ImportError):
        add_rule_machine_dimension_surface_magnet = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_machine_dimension_surface_magnet: "
                    + str(add_rule_machine_dimension_surface_magnet)
                )
            )
        )
    else:
        add_rule_machine_dimension_surface_magnet = (
            add_rule_machine_dimension_surface_magnet
        )
    # cf Methods.Converter.ConvertMC.Rules.add_rule_machine_type
    if isinstance(add_rule_machine_type, ImportError):
        add_rule_machine_type = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_machine_type: "
                    + str(add_rule_machine_type)
                )
            )
        )
    else:
        add_rule_machine_type = add_rule_machine_type
    # cf Methods.Converter.ConvertMC.Rules.Slot.add_rule_slotW11
    if isinstance(add_rule_slotW11, ImportError):
        add_rule_slotW11 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_slotW11: "
                    + str(add_rule_slotW11)
                )
            )
        )
    else:
        add_rule_slotW11 = add_rule_slotW11
    # cf Methods.Converter.ConvertMC.Rules.Slot.add_rule_slotW29
    if isinstance(add_rule_slotW29, ImportError):
        add_rule_slotW29 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_slotW29: "
                    + str(add_rule_slotW29)
                )
            )
        )
    else:
        add_rule_slotW29 = add_rule_slotW29
    # cf Methods.Converter.ConvertMC.Rules.Slot.add_rule_slotW21
    if isinstance(add_rule_slotW21, ImportError):
        add_rule_slotW21 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_slotW21: "
                    + str(add_rule_slotW21)
                )
            )
        )
    else:
        add_rule_slotW21 = add_rule_slotW21
    # cf Methods.Converter.ConvertMC.Rules.Slot.add_rule_slotW14
    if isinstance(add_rule_slotW14, ImportError):
        add_rule_slotW14 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_slotW14: "
                    + str(add_rule_slotW14)
                )
            )
        )
    else:
        add_rule_slotW14 = add_rule_slotW14
    # cf Methods.Converter.ConvertMC.Rules.Slot.add_rule_slotW23
    if isinstance(add_rule_slotW23, ImportError):
        add_rule_slotW23 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_slotW23: "
                    + str(add_rule_slotW23)
                )
            )
        )
    else:
        add_rule_slotW23 = add_rule_slotW23
    # cf Methods.Converter.ConvertMC.Rules.Slot.rotor.add_rule_rotor_slotW30
    if isinstance(add_rule_rotor_slotW30, ImportError):
        add_rule_rotor_slotW30 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_rotor_slotW30: "
                    + str(add_rule_rotor_slotW30)
                )
            )
        )
    else:
        add_rule_rotor_slotW30 = add_rule_rotor_slotW30
    # cf Methods.Converter.ConvertMC.Rules.Slot.rotor.add_rule_rotor_slotW23
    if isinstance(add_rule_rotor_slotW23, ImportError):
        add_rule_rotor_slotW23 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_rotor_slotW23: "
                    + str(add_rule_rotor_slotW23)
                )
            )
        )
    else:
        add_rule_rotor_slotW23 = add_rule_rotor_slotW23
    # cf Methods.Converter.ConvertMC.Rules.Slot.rotor.add_rule_rotor_slotW11_2
    if isinstance(add_rule_rotor_slotW11_2, ImportError):
        add_rule_rotor_slotW11_2 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_rotor_slotW11_2: "
                    + str(add_rule_rotor_slotW11_2)
                )
            )
        )
    else:
        add_rule_rotor_slotW11_2 = add_rule_rotor_slotW11_2
    # cf Methods.Converter.ConvertMC.Rules.Slot.rotor.add_rule_rotor_slotW26
    if isinstance(add_rule_rotor_slotW26, ImportError):
        add_rule_rotor_slotW26 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_rotor_slotW26: "
                    + str(add_rule_rotor_slotW26)
                )
            )
        )
    else:
        add_rule_rotor_slotW26 = add_rule_rotor_slotW26
    # cf Methods.Converter.ConvertMC.Rules.Lamination.add_rule_ventilationCirc
    if isinstance(add_rule_ventilationCirc, ImportError):
        add_rule_ventilationCirc = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_ventilationCirc: "
                    + str(add_rule_ventilationCirc)
                )
            )
        )
    else:
        add_rule_ventilationCirc = add_rule_ventilationCirc
    # cf Methods.Converter.ConvertMC.Rules.Lamination.add_rule_ventilationPolar
    if isinstance(add_rule_ventilationPolar, ImportError):
        add_rule_ventilationPolar = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_ventilationPolar: "
                    + str(add_rule_ventilationPolar)
                )
            )
        )
    else:
        add_rule_ventilationPolar = add_rule_ventilationPolar
    # cf Methods.Converter.ConvertMC.Rules.Lamination.add_rule_ventilationTrap
    if isinstance(add_rule_ventilationTrap, ImportError):
        add_rule_ventilationTrap = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_ventilationTrap: "
                    + str(add_rule_ventilationTrap)
                )
            )
        )
    else:
        add_rule_ventilationTrap = add_rule_ventilationTrap
    # cf Methods.Converter.ConvertMC.Rules.Lamination.add_rule_notch_slotM19
    if isinstance(add_rule_notch_slotM19, ImportError):
        add_rule_notch_slotM19 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_notch_slotM19: "
                    + str(add_rule_notch_slotM19)
                )
            )
        )
    else:
        add_rule_notch_slotM19 = add_rule_notch_slotM19
    # cf Methods.Converter.ConvertMC.Rules.Lamination.add_rule_lamination
    if isinstance(add_rule_lamination, ImportError):
        add_rule_lamination = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_lamination: "
                    + str(add_rule_lamination)
                )
            )
        )
    else:
        add_rule_lamination = add_rule_lamination
    # cf Methods.Converter.ConvertMC.Rules.Rotor_Magnet.add_rule_slotM14
    if isinstance(add_rule_slotM14, ImportError):
        add_rule_slotM14 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_slotM14: "
                    + str(add_rule_slotM14)
                )
            )
        )
    else:
        add_rule_slotM14 = add_rule_slotM14
    # cf Methods.Converter.ConvertMC.Rules.Rotor_Magnet.add_rule_slotM13
    if isinstance(add_rule_slotM13, ImportError):
        add_rule_slotM13 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_slotM13: "
                    + str(add_rule_slotM13)
                )
            )
        )
    else:
        add_rule_slotM13 = add_rule_slotM13
    # cf Methods.Converter.ConvertMC.Rules.Rotor_Magnet.add_rule_slotM16
    if isinstance(add_rule_slotM16, ImportError):
        add_rule_slotM16 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_slotM16: "
                    + str(add_rule_slotM16)
                )
            )
        )
    else:
        add_rule_slotM16 = add_rule_slotM16
    # cf Methods.Converter.ConvertMC.Rules.Rotor_Magnet.add_rule_slotM11
    if isinstance(add_rule_slotM11, ImportError):
        add_rule_slotM11 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_slotM11: "
                    + str(add_rule_slotM11)
                )
            )
        )
    else:
        add_rule_slotM11 = add_rule_slotM11
    # cf Methods.Converter.ConvertMC.Rules.Rotor_Magnet.add_rule_slotM15
    if isinstance(add_rule_slotM15, ImportError):
        add_rule_slotM15 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_slotM15: "
                    + str(add_rule_slotM15)
                )
            )
        )
    else:
        add_rule_slotM15 = add_rule_slotM15
    # cf Methods.Converter.ConvertMC.Rules.Rotor_Magnet.add_rule_slotM12
    if isinstance(add_rule_slotM12, ImportError):
        add_rule_slotM12 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_slotM12: "
                    + str(add_rule_slotM12)
                )
            )
        )
    else:
        add_rule_slotM12 = add_rule_slotM12
    # cf Methods.Converter.ConvertMC.select_SIPMSM_machine_dimension
    if isinstance(select_SIPMSM_machine_dimension, ImportError):
        select_SIPMSM_machine_dimension = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method select_SIPMSM_machine_dimension: "
                    + str(select_SIPMSM_machine_dimension)
                )
            )
        )
    else:
        select_SIPMSM_machine_dimension = select_SIPMSM_machine_dimension
    # cf Methods.Converter.ConvertMC.Rules.Hole.add_rule_holeM61
    if isinstance(add_rule_holeM61, ImportError):
        add_rule_holeM61 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_holeM61: "
                    + str(add_rule_holeM61)
                )
            )
        )
    else:
        add_rule_holeM61 = add_rule_holeM61
    # cf Methods.Converter.ConvertMC.Rules.Hole.add_rule_holeM57
    if isinstance(add_rule_holeM57, ImportError):
        add_rule_holeM57 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_holeM57: "
                    + str(add_rule_holeM57)
                )
            )
        )
    else:
        add_rule_holeM57 = add_rule_holeM57
    # cf Methods.Converter.ConvertMC.Rules.Hole.add_rule_holeM60
    if isinstance(add_rule_holeM60, ImportError):
        add_rule_holeM60 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_holeM60: "
                    + str(add_rule_holeM60)
                )
            )
        )
    else:
        add_rule_holeM60 = add_rule_holeM60
    # cf Methods.Converter.ConvertMC.Rules.Hole.add_rule_holeM63
    if isinstance(add_rule_holeM63, ImportError):
        add_rule_holeM63 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_holeM63: "
                    + str(add_rule_holeM63)
                )
            )
        )
    else:
        add_rule_holeM63 = add_rule_holeM63
    # cf Methods.Converter.ConvertMC.Rules.Hole.add_rule_holeM52
    if isinstance(add_rule_holeM52, ImportError):
        add_rule_holeM52 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_holeM52: "
                    + str(add_rule_holeM52)
                )
            )
        )
    else:
        add_rule_holeM52 = add_rule_holeM52
    # cf Methods.Converter.ConvertMC.Rules.Hole.add_rule_holeM62
    if isinstance(add_rule_holeM62, ImportError):
        add_rule_holeM62 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_holeM62: "
                    + str(add_rule_holeM62)
                )
            )
        )
    else:
        add_rule_holeM62 = add_rule_holeM62
    # cf Methods.Converter.ConvertMC.Rules.Pole.add_rule_parallel_tooth_slotW63
    if isinstance(add_rule_parallel_tooth_slotW63, ImportError):
        add_rule_parallel_tooth_slotW63 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_parallel_tooth_slotW63: "
                    + str(add_rule_parallel_tooth_slotW63)
                )
            )
        )
    else:
        add_rule_parallel_tooth_slotW63 = add_rule_parallel_tooth_slotW63
    # cf Methods.Converter.ConvertMC.Rules.Pole.add_rule_salient_pole_slotW62
    if isinstance(add_rule_salient_pole_slotW62, ImportError):
        add_rule_salient_pole_slotW62 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_salient_pole_slotW62: "
                    + str(add_rule_salient_pole_slotW62)
                )
            )
        )
    else:
        add_rule_salient_pole_slotW62 = add_rule_salient_pole_slotW62
    # cf Methods.Converter.ConvertMC.Rules.Pole.add_rule_parallel_slot_slotW29
    if isinstance(add_rule_parallel_slot_slotW29, ImportError):
        add_rule_parallel_slot_slotW29 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_parallel_slot_slotW29: "
                    + str(add_rule_parallel_slot_slotW29)
                )
            )
        )
    else:
        add_rule_parallel_slot_slotW29 = add_rule_parallel_slot_slotW29
    # cf Methods.Converter.ConvertMC.Rules.Winding.add_rule_winding
    if isinstance(add_rule_winding, ImportError):
        add_rule_winding = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_winding: "
                    + str(add_rule_winding)
                )
            )
        )
    else:
        add_rule_winding = add_rule_winding
    # cf Methods.Converter.ConvertMC.Rules.Winding.add_rule_condtype11
    if isinstance(add_rule_condtype11, ImportError):
        add_rule_condtype11 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_condtype11: "
                    + str(add_rule_condtype11)
                )
            )
        )
    else:
        add_rule_condtype11 = add_rule_condtype11
    # cf Methods.Converter.ConvertMC.Rules.Winding.add_rule_condtype12
    if isinstance(add_rule_condtype12, ImportError):
        add_rule_condtype12 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_condtype12: "
                    + str(add_rule_condtype12)
                )
            )
        )
    else:
        add_rule_condtype12 = add_rule_condtype12
    # cf Methods.Converter.ConvertMC.Rules.Winding.add_rule_rotor_bar
    if isinstance(add_rule_rotor_bar, ImportError):
        add_rule_rotor_bar = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_rotor_bar: "
                    + str(add_rule_rotor_bar)
                )
            )
        )
    else:
        add_rule_rotor_bar = add_rule_rotor_bar
    # cf Methods.Converter.ConvertMC.Rules.add_rule_material_magnetics
    if isinstance(add_rule_material_magnetics, ImportError):
        add_rule_material_magnetics = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_material_magnetics: "
                    + str(add_rule_material_magnetics)
                )
            )
        )
    else:
        add_rule_material_magnetics = add_rule_material_magnetics
    # cf Methods.Converter.ConvertMC.Rules.add_rule_material
    if isinstance(add_rule_material, ImportError):
        add_rule_material = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_material: "
                    + str(add_rule_material)
                )
            )
        )
    else:
        add_rule_material = add_rule_material
    # cf Methods.Converter.ConvertMC.Rules.add_rule_skew
    if isinstance(add_rule_skew, ImportError):
        add_rule_skew = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ConvertMC method add_rule_skew: " + str(add_rule_skew)
                )
            )
        )
    else:
        add_rule_skew = add_rule_skew
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        other_unit_dict=-1,
        other_dict=-1,
        machine=None,
        rules_list=-1,
        is_P_to_other=False,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "other_unit_dict" in list(init_dict.keys()):
                other_unit_dict = init_dict["other_unit_dict"]
            if "other_dict" in list(init_dict.keys()):
                other_dict = init_dict["other_dict"]
            if "machine" in list(init_dict.keys()):
                machine = init_dict["machine"]
            if "rules_list" in list(init_dict.keys()):
                rules_list = init_dict["rules_list"]
            if "is_P_to_other" in list(init_dict.keys()):
                is_P_to_other = init_dict["is_P_to_other"]
        # Set the properties (value check and convertion are done in setter)
        # Call Convert init
        super(ConvertMC, self).__init__(
            other_unit_dict=other_unit_dict,
            other_dict=other_dict,
            machine=machine,
            rules_list=rules_list,
            is_P_to_other=is_P_to_other,
        )
        # The class is frozen (in Convert init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        ConvertMC_str = ""
        # Get the properties inherited from Convert
        ConvertMC_str += super(ConvertMC, self).__str__()
        return ConvertMC_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Convert
        if not super(ConvertMC, self).__eq__(other):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Convert
        diff_list.extend(
            super(ConvertMC, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Convert
        S += super(ConvertMC, self).__sizeof__()
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        # Get the properties inherited from Convert
        ConvertMC_dict = super(ConvertMC, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        ConvertMC_dict["__class__"] = "ConvertMC"
        return ConvertMC_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.other_unit_dict is None:
            other_unit_dict_val = None
        else:
            other_unit_dict_val = self.other_unit_dict.copy()
        if self.other_dict is None:
            other_dict_val = None
        else:
            other_dict_val = self.other_dict.copy()
        if self.machine is None:
            machine_val = None
        else:
            machine_val = self.machine.copy()
        if self.rules_list is None:
            rules_list_val = None
        else:
            rules_list_val = self.rules_list.copy()
        is_P_to_other_val = self.is_P_to_other
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            other_unit_dict=other_unit_dict_val,
            other_dict=other_dict_val,
            machine=machine_val,
            rules_list=rules_list_val,
            is_P_to_other=is_P_to_other_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Convert
        super(ConvertMC, self)._set_None()
