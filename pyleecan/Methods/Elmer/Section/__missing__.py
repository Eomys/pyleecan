def __missing__(self, key):
    """method to implement self[key] for dict subclasses when key is not in the dict."""
    return self._statements.__missing__(key)
