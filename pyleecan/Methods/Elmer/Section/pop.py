from ..Section import ElmerSectionError


def pop(self, key):
    """
    Remove the item with the given key and return it.
    """
    if key not in self.keys():
        raise ElmerSectionError("Key doesn't exist.")

    value = self._statements.pop(key)
    comment = self._comments.pop(key)

    return (value, comment)
