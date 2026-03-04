from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Создаём роутер и регистрируем ViewSet'ы
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

# URL-паттерны — роутер сам всё создаёт
urlpatterns = [
    path('', include(router.urls)),
]