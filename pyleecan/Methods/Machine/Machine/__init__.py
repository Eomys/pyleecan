# -*- coding: utf-8 -*-

# List of all the direct variable translation matlab <=> python
trad_list = list()

trad_list.append(
    {"mat": "Input.Magnetics.type_machine", "py": "obj.type_machine", "type": int}
)
# Stator Global geometry
trad_list.append({"mat": "Input.Geometry.Lst1", "py": "obj.stator.L1", "type": float})
trad_list.append(
    {
        "mat": "Input.Geometry.type_skew_geoS",
        "py": "obj.stator.type_skew_geo",
        "type": int,
    }
)
trad_list.append(
    {"mat": "Input.Geometry.skew_rates", "py": "obj.stator.skew_angle", "type": float}
)
trad_list.append({"mat": "Input.Geometry.Kst1", "py": "obj.stator.Kf1", "type": float})
# Stator notches
trad_list.append(
    {"mat": "Input.Geometry.Nnotches", "py": "obj.stator.Nnotche", "type": int}
)
trad_list.append(
    {"mat": "Input.Geometry.Wnotches", "py": "obj.stator.Wnotche", "type": float}
)
trad_list.append(
    {"mat": "Input.Geometry.Hnotches", "py": "obj.stator.Hnotche", "type": float}
)
trad_list.append(
    {
        "mat": "Input.Geometry.type_shape_notches",
        "py": "obj.stator.type_shape_notche",
        "type": int,
    }
)
# thermics
trad_list.append({"mat": "Input.Thermics.Nrvds", "py": "obj.stator.Nrvd", "type": int})
trad_list.append(
    {"mat": "Input.Thermics.Wrvds", "py": "obj.stator.Wrvd", "type": float}
)
# Rotor global geometry
trad_list.append(
    {
        "mat": "Input.Geometry.is_inner_rotor",
        "py": "obj.rotor.is_internal",
        "type": bool,
    }
)
trad_list.append({"mat": "Input.Geometry.Lst2", "py": "obj.rotor.L1", "type": float})
trad_list.append(
    {
        "mat": "Input.Geometry.type_skew_geoR",
        "py": "obj.rotor.type_skew_geo",
        "type": float,
    }
)
trad_list.append(
    {"mat": "Input.Geometry.skew_rater", "py": "obj.rotor.skew_angle", "type": float}
)
trad_list.append({"mat": "Input.Geometry.Kst2", "py": "obj.rotor.Kf1", "type": float})
# Rotor notches
trad_list.append(
    {"mat": "Input.Geometry.Nnotcher", "py": "obj.rotor.Nnotche", "type": int}
)
trad_list.append(
    {"mat": "Input.Geometry.Wnotcher", "py": "obj.rotor.Wnotche", "type": float}
)
trad_list.append(
    {"mat": "Input.Geometry.Hnotcher", "py": "obj.rotor.Hnotche", "type": float}
)
trad_list.append(
    {
        "mat": "Input.Geometry.type_shape_notcher",
        "py": "obj.rotor.type_shape_notche",
        "type": int,
    }
)
# thermics
trad_list.append({"mat": "Input.Thermics.Nrvdr", "py": "obj.rotor.Nrvd", "type": int})
trad_list.append({"mat": "Input.Thermics.Wrvdr", "py": "obj.rotor.Wrvd", "type": float})
