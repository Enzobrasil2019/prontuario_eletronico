from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.post_list, name='post_list'),
    path(r'mostmed', views.post_list, name='post_list'),
    path(r'addmed', views.post_form, name='post_form'),

]