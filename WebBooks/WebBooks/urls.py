from django.conf import settings
from django.contrib import admin
from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('admin/', admin.site.urls),
]
