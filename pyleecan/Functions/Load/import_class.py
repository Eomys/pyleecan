from ...Classes._check import InitUnKnowClassError


def import_class(mod_name, class_name, prop_name=""):
    """Dynamical import of a class (for init_dict=class.as_dict())"""

    try:
        module = __import__(mod_name + "." + class_name, fromlist=[class_name])
        return getattr(module, class_name)
    except:
        if prop_name != "":
            raise InitUnKnowClassError(
                "Unknow class name "
                + class_name
                + " in init_dict for property "
                + prop_name
            )
        else:
            raise InitUnKnowClassError(
                "Unknow class name " + class_name + " when loading"
            )
