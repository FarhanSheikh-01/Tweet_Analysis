from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('backend\urls.py')),
    path("about", include('backend\urls.py')),
    path("services", include('backend\urls.py')),
]
