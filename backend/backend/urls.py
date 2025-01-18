
from django.contrib import admin
from django.urls import path
from Base_App import views

urlpatterns = [
    path("", views.predict, name='predict'),
    path("msg/", views.msg, name='msg'),
]
