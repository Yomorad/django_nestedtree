from django.shortcuts import render
from menu_app.models import MenuItem
from menu_app.utils import get_parents

def draw_menu(request, menu_name):
    """
    Генерирует меню для указанного имени меню и возвращает рендеринг HTML-шаблона.

    Args:
        request (HttpRequest): Объект запроса, содержащий информацию о текущем запросе.
        menu_name (str): Имя меню, по которому будет выполнен запрос к базе данных для получения элементов меню.

    Returns:
        HttpResponse: Ответ с отрисованным меню, в котором содержатся элементы меню,
                      текущий URL, активный элемент меню и его родительские элементы.
    """
    current_url = request.path
    menu_items = MenuItem.objects.filter(name=menu_name).prefetch_related('children')
    # Находим активный элемент по текущему URL
    active_item = MenuItem.objects.filter(url=current_url).first()
    # Получаем всех родителей активного элемента
    active_parents = get_parents(active_item) if active_item else []
    # Передаем список активных родителей для рендеринга
    return render(request, 'menu_app/menu.html', {
        'menu_items': menu_items,
        'current_url': current_url,
        'active_item': active_item,
        'active_parents': active_parents
    })