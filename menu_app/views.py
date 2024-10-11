from django.shortcuts import render
from menu_app.models import MenuItem
from menu_app.utils import get_parents

def draw_menu(request, menu_name):
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
