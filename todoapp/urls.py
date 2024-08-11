from django.urls import path
from . import views

urlpatterns = [
    path('', views.custom_login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('delete/<int:list_id>/', views.delete, name='delete'),
    path('toggle/<int:list_id>/', views.toggle, name='toggle'),
    path('edit/<int:list_id>/', views.edit, name='edit'),
]