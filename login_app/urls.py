from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('wall', views.success),
    path('logout', views.logout),
    path('create_message', views.create_message),
    path('add_comment/<int:id>', views.add_comment),
    path('like/<int:id>', views.like),
]