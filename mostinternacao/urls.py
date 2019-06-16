from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path(r'addinter/', views.post_form, name='post_form'),
    path(r'addalter/', views.post_alter, name='post_alter'),
    path(r'mostaltas/', views.post_altas, name='post_altas'),
]

