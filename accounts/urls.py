from django.urls import path
from . import views
from .views import UserList

urlpatterns = [
    path('users', views.getUser),
    path('users', views.createUser),
    path('users/<int:pk>', UserList.as_view()),
    ]