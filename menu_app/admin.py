from django.contrib import admin
from menu_app.models import Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'slug']