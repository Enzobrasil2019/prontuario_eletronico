from django.urls import path
from . import views
from .views import post_login
urlpatterns = [
    path(r'', views.post_login, name='post_login'),
]
