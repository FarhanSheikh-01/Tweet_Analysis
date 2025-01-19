
from django.contrib import admin
from django.urls import path
from Base_App import views

urlpatterns = [
    path("", views.msg, name='msg'),
]
