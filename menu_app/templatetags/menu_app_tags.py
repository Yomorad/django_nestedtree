from django import template
from menu_app.models import MenuItem
from django.utils.safestring import mark_safe
from django.urls import reverse
from menu_app.utils import get_parents

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path

    menu_items = MenuItem.objects.filter(name=menu_name).prefetch_related('children')

    active_item = MenuItem.objects.filter(url=current_url).first()
    active_parents = get_parents(active_item) if active_item else []

    return mark_safe(_render_menu(menu_items, current_url, active_item, active_parents))


def _render_menu(menu_items, current_url, active_item, active_parents):
    """Функция для рекурсивного рендеринга меню с учётом активных элементов."""
    menu_html = '<ul>'
    for item in menu_items:
        # Определяем активный или раскрытый элемент
        is_active = item == active_item
        is_expanded = item in active_parents
        active_class = ' class="active"' if is_active else ''
        expanded_class = ' class="expanded"' if is_expanded else ''

        menu_html += f'<li{expanded_class}>'
        if item.url:
            menu_html += f'<a href="{item.url}"{active_class}>{item.name}</a>'
        elif item.named_url:
            try:
                url = reverse(item.named_url)
                menu_html += f'<a href="{url}"{active_class}>{item.name}</a>'
            except:
                menu_html += f'<span{active_class}>{item.name}</span>'
        else:
            menu_html += f'<span{active_class}>{item.name}</span>'

        # Рекурсивно рендерим дочерние элементы, если есть
        if item.children.exists():
            menu_html += _render_menu(item.children.all(), current_url, active_item, active_parents)

        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html
