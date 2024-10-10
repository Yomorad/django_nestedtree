from django.urls import path
from menu_app import views

app_name = 'menu_app'

urlpatterns = [
    path('<slug:slug>/', views.menu_tree, name = 'index'),
]
