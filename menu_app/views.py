from django.shortcuts import get_list_or_404, render

from menu_app.models import Menu

# Create your views here.

def menu_tree(request, slug = None):
    if slug == None:
        goods = Menu.objects.all()
    else:
        goods = get_list_or_404(Menu.objects.filter(slug=slug))

    context = {
        'slug_url': slug,
    }
    return render(request, 'menu_app/menu.html', context)