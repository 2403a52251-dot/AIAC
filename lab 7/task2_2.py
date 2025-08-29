def sort_list(data):
    """Consistently sort a list that may contain numbers and strings.

    - Numbers first (ascending)
    - Strings next (case-insensitive)
    """

    def key(item):
        if isinstance(item, (int, float)):
            return (0, float(item))
        if isinstance(item, str):
            return (1, item.lower())
        return (2, str(item))

    return sorted(data, key=key)


items = [3, "apple", 1, "banana", 2]
print(sort_list(items))


