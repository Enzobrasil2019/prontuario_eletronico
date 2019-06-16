from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),

    path(r'addamb', views.post_form, name='post_form'),
]
