from django.urls import path
from . import views



urlpatterns = [
    path('', views.post_list, name='post_list'),
    path(r'addamb/', views.post_form, name='post_form'),
    path(r'pac/<int:pk>/', views.post_detail, name='post_detail'),
    path(r'pac/<int:pk>/edit/', views.post_edit, name='post_edit'),
]