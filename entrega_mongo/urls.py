from django.contrib import admin
from django.conf.urls import include, re_path
from django.db import router
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from coments.urls import api_urlpatterns

urlpatterns = [
    path("", include(api_urlpatterns)),
    path('admin/', admin.site.urls),
]
