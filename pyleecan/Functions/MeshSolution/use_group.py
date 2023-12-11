def use_group(func):
    """Decorator to extract the MeshSolution group name before calling the
    method

    Parameters
    ----------
    func : function
        MeshSolution method
    """

    def wrapper_use_group(self, *args, **kwargs):
        group_names = kwargs.get("group_names", None)
        if group_names is not None:
            kwargs["group_names"] = None
            meshsol_grp = self.get_group(group_names)
            return func(meshsol_grp, *args, **kwargs)

        return func(self, *args, **kwargs)

    return wrapper_use_group
