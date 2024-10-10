from django import template
from django.utils.http import urlencode
from menu_app.models import Menu

register = template.Library()

@register.simple_tag()
def tag_menu():
    return Menu.objects.all()