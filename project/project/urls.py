from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import ActorViewSet, MovieViewSet

routers = DefaultRouter()
routers.register(r'actors', ActorViewSet)
routers.register(r'movies', MovieViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routers.urls)),
]