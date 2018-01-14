from django.contrib import admin
from django.urls import path
from .views import posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', posts),
]
