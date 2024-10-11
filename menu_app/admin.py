from django.contrib import admin
from menu_app.models import  MenuItem

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'named_url', 'parent')
    search_fields = ('name', 'url', 'named_url')
    ordering = ('name', 'id')

admin.site.register(MenuItem, MenuAdmin)
