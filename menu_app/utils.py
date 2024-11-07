
def get_parents(item):
    """
    Рекурсивно находит всех родителей элемента.

    Args:
        item (MenuItem): Элемент меню, для которого нужно найти родителей.

    Returns:
        list: Список родителей элемента в порядке от самого верхнего до самого нижнего.
    """
    parents = []
    while item.parent:
        parents.append(item.parent)
        item = item.parent
    return parents
