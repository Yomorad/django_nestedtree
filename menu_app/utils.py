
def get_parents(item):
    """Рекурсивно находим всех родителей элемента."""
    parents = []
    while item.parent:
        parents.append(item.parent)
        item = item.parent
    return parents
