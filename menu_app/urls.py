from django.urls import path
from menu_app import views

app_name = 'menu_app'


urlpatterns = [
    path('<str:menu_name>/', views.draw_menu, name='draw_menu'),
]